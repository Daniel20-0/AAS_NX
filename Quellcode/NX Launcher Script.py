import sys
import subprocess
import os
from time import sleep
import math
from pathlib import Path
import NXOpen


def ensure_work_part():
    session = NXOpen.Session.GetSession()
    lw = session.ListingWindow

    if session.Parts.Work is None:
        BASE_DIR = Path(__file__).resolve().parent
        part_name = str(BASE_DIR / "StartPart.prt")

        if os.path.exists(part_name):
            lw.WriteLine("Start part already exists → opening existing part")
            part_load_status = None
            try:
                base_part, part_load_status = session.Parts.OpenBaseDisplay(part_name)
            finally:
                if part_load_status:
                    part_load_status.Dispose()
        else:
            lw.WriteLine("No active part available → creating new part")
            session.Parts.NewDisplay(
                part_name,
                NXOpen.Part.Units.Millimeters
            )

    return session.Parts.Work


def identity_matrix():
    m = NXOpen.Matrix3x3()
    m.Xx = 1.0; m.Xy = 0.0; m.Xz = 0.0
    m.Yx = 0.0; m.Yy = 1.0; m.Yz = 0.0
    m.Zx = 0.0; m.Zy = 0.0; m.Zz = 1.0
    return m


def rotation_matrix_x(angle_deg):
    a = math.radians(angle_deg)
    c = math.cos(a)
    s = math.sin(a)

    m = NXOpen.Matrix3x3()
    m.Xx = 1.0; m.Xy = 0.0; m.Xz = 0.0
    m.Yx = 0.0; m.Yy = c;   m.Yz = -s
    m.Zx = 0.0; m.Zy = s;   m.Zz = c
    return m


def rotation_matrix_y(angle_deg):
    a = math.radians(angle_deg)
    c = math.cos(a)
    s = math.sin(a)

    m = NXOpen.Matrix3x3()
    m.Xx = c;   m.Xy = 0.0; m.Xz = s
    m.Yx = 0.0; m.Yy = 1.0; m.Yz = 0.0
    m.Zx = -s;  m.Zy = 0.0; m.Zz = c
    return m


def rotation_matrix_z(angle_deg):
    a = math.radians(angle_deg)
    c = math.cos(a)
    s = math.sin(a)

    m = NXOpen.Matrix3x3()
    m.Xx = c;   m.Xy = -s;  m.Xz = 0.0
    m.Yx = s;   m.Yy = c;   m.Yz = 0.0
    m.Zx = 0.0; m.Zy = 0.0; m.Zz = 1.0
    return m


def get_rotation_matrix(axis="X", angle_deg=0.0):
    axis = axis.upper()
    if axis == "X":
        return rotation_matrix_x(angle_deg)
    if axis == "Y":
        return rotation_matrix_y(angle_deg)
    if axis == "Z":
        return rotation_matrix_z(angle_deg)
    return identity_matrix()


def import_step_to_prt(step_path):
    session = NXOpen.Session.GetSession()
    lw = session.ListingWindow
    importer = session.DexManager.CreateStep242Importer()

    try:
        prt_path = step_path.replace(".step", ".prt").replace(".stp", ".prt")

        importer.Optimize = True
        importer.SimplifyGeometry = False
        importer.Messages = NXOpen.Step242Importer.MessageEnum.Error
        importer.SetMode(NXOpen.BaseImporter.Mode.NativeFileSystem)

        importer.InputFile = step_path
        importer.OutputFile = prt_path
        importer.ImportTo = NXOpen.Step242Importer.ImportToOption.NewPart

        importer.ObjectTypes.Curves = True
        importer.ObjectTypes.Surfaces = True
        importer.ObjectTypes.Solids = True
        importer.ObjectTypes.PmiData = True

        importer.FileOpenFlag = False
        importer.ProcessHoldFlag = True

        lw.WriteLine("Importing STEP -> PRT: " + step_path)
        importer.Commit()
        lw.WriteLine("STEP Import completed: " + prt_path)

        return prt_path

    except Exception as ex:
        lw.WriteLine("Error during STEP Import:")
        lw.WriteLine(str(ex))
        return None

    finally:
        try:
            importer.Destroy()
        except:
            pass


def open_part(part_path):
    session = NXOpen.Session.GetSession()
    lw = session.ListingWindow

    part_load_status = NXOpen.PartLoadStatus()
    opened_part = None

    try:
        opened_part, part_load_status = session.Parts.OpenBaseDisplay(part_path)
        lw.WriteLine("PRT opened: " + part_path)
        return opened_part
    except Exception as ex:
        lw.WriteLine("Error while opening PRT:")
        lw.WriteLine(str(ex))
        return None
    finally:
        try:
            if part_load_status is not None:
                part_load_status.Dispose()
        except:
            pass


def add_prt_as_component(target_part, prt_path, component_name, x=0.0, y=0.0, z=0.0, axis="X", angle_deg=0.0):
    session = NXOpen.Session.GetSession()
    lw = session.ListingWindow

    base_point = NXOpen.Point3d(x, y, z)
    orientation = identity_matrix()

    try:
        component, load_status = target_part.ComponentAssembly.AddComponent(
            prt_path,
            "Entire Part",
            component_name,
            base_point,
            orientation,
            -1
        )

        try:
            if load_status:
                load_status.Dispose()
        except:
            pass

        lw.WriteLine(f"Component added: {component_name} | X={x}, Y={y}, Z={z}")
        return component

    except Exception as ex:
        lw.WriteLine("Error while adding component:")
        lw.WriteLine(str(ex))
        return None


def import_step_into_nx_as_component(step_path, x=0.0, y=0.0, z=0.0, axis="X", angle_deg=0.0, component_name=None):
    session = NXOpen.Session.GetSession()
    lw = session.ListingWindow

    target_part = ensure_work_part()

    prt_path = import_step_to_prt(step_path)
    if not prt_path:
        lw.WriteLine("PRT was not created.")
        return None

    if component_name is None:
        component_name = os.path.splitext(os.path.basename(prt_path))[0]

    return add_prt_as_component(
        target_part,
        prt_path,
        component_name,
        x,
        y,
        z,
        axis,
        angle_deg
    )


def main():
    session = NXOpen.Session.GetSession()
    lw = session.ListingWindow
    lw.Open()
    current_dir = Path(__file__).resolve().parent

    script_path = current_dir / "AAS-Creo-Bridge" / "src" / "AAS_TO_NX.py"
    lw.WriteLine("NX Launcher started")

    python_exe = "python"
   
    BASE_DIR = Path(__file__).resolve().parent

    step_path_1 = BASE_DIR / "AAS-Creo-Bridge" / "temp_model.step"
    step_path_2 = BASE_DIR / "temp_model.step"

    try:
        lw.WriteLine("Starte externes Skript...")
        lw.WriteLine(str(script_path))

        # Delete the old STEP file before starting
        # so that no existing old data is imported.
        if step_path_1.exists():
            lw.WriteLine("Existing STEP file found -> will be deleted")
            step_path_1.unlink()

        result = subprocess.run(
            [python_exe, str(script_path)],
            capture_output=True,
            text=True
        )

        lw.WriteLine("External script completed")
        lw.WriteLine("Return Code: " + str(result.returncode))

        if result.stdout:
            lw.WriteLine(result.stdout)

        if result.stderr:
            lw.WriteLine(result.stderr)

        if result.returncode != 0:
            lw.WriteLine("External script was cancelled or failed -> no import")
            return

        if not step_path_1.exists():
            lw.WriteLine("STEP file was not created -> no import")
            return

        lw.WriteLine("STEP file found -> starting import as component")

        ensure_work_part()
        sleep(1)

        import_step_into_nx_as_component(
            str(step_path_1),
            x=0.0,
            y=0.0,
            z=0.0,
            component_name="Part_1"
        )

        import_step_into_nx_as_component(
            str(step_path_2),
            x=150.0,
            y=0.0,
            z=0.0,
            component_name="Part_2"
        )

    except Exception as e:
        lw.WriteLine("Error:")
        lw.WriteLine(str(e))


if __name__ == "__main__":
    main()
