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
        part_name = r"C:\Users\chris\AAS-Creo-Bridge\StartPart.prt"

        if os.path.exists(part_name):
            lw.WriteLine("StartPart existiert bereits -> öffne vorhandenes Part")
            part_load_status = None
            try:
                base_part, part_load_status = session.Parts.OpenBaseDisplay(part_name)
            finally:
                if part_load_status:
                    part_load_status.Dispose()
        else:
            lw.WriteLine("Kein aktives Part vorhanden -> erstelle neues Part")
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

        lw.WriteLine("Importiere STEP -> PRT: " + step_path)
        importer.Commit()
        lw.WriteLine("STEP Import abgeschlossen: " + prt_path)

        return prt_path

    except Exception as ex:
        lw.WriteLine("Fehler während STEP Import:")
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
        lw.WriteLine("PRT geöffnet: " + part_path)
        return opened_part
    except Exception as ex:
        lw.WriteLine("Fehler beim Öffnen der PRT:")
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

        lw.WriteLine(f"Komponente eingefügt: {component_name} | X={x}, Y={y}, Z={z}")
        return component

    except Exception as ex:
        lw.WriteLine("Fehler beim Einfügen der Komponente:")
        lw.WriteLine(str(ex))
        return None


def import_step_into_nx_as_component(step_path, x=0.0, y=0.0, z=0.0, axis="X", angle_deg=0.0, component_name=None):
    session = NXOpen.Session.GetSession()
    lw = session.ListingWindow

    target_part = ensure_work_part()

    prt_path = import_step_to_prt(step_path)
    if not prt_path:
        lw.WriteLine("PRT wurde nicht erzeugt.")
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

    lw.WriteLine("NX Launcher gestartet")

    python_exe = r"C:\Users\chris\AppData\Local\Programs\Python\Python311\python.exe"
    script_path = r"C:\Users\chris\Documents\EntwicklungsPorjekt_AAS_Master\Entwicklungsprojekt_AAS\AAS_NX\Quellcode\AAS-Creo-Bridge\src\AAS_TO_NX.py"

    step_path_1 = Path(r"C:\Users\chris\AAS-Creo-Bridge\temp_model.step")
    step_path_2 = Path(r"C:\Users\chris\AAS-Creo-Bridge\temp_model.step")

    try:
        lw.WriteLine("Starte externes Skript...")
        lw.WriteLine(script_path)

        # Alte STEP-Datei vor dem Start löschen,
        # damit kein vorhandener Altbestand importiert wird.
        if step_path_1.exists():
            lw.WriteLine("Vorhandene STEP-Datei gefunden -> wird gelöscht")
            step_path_1.unlink()

        result = subprocess.run(
            [python_exe, script_path],
            capture_output=True,
            text=True
        )

        lw.WriteLine("Externes Skript beendet")
        lw.WriteLine("Return Code: " + str(result.returncode))

        if result.stdout:
            lw.WriteLine(result.stdout)

        if result.stderr:
            lw.WriteLine(result.stderr)

        if result.returncode != 0:
            lw.WriteLine("Externes Skript wurde abgebrochen oder ist fehlgeschlagen -> kein Import")
            return

        if not step_path_1.exists():
            lw.WriteLine("STEP Datei wurde nicht neu erzeugt -> kein Import")
            return

        lw.WriteLine("STEP Datei gefunden -> starte Import als Komponente")

        ensure_work_part()
        sleep(1)

        import_step_into_nx_as_component(
            str(step_path_1),
            x=0.0,
            y=0.0,
            z=0.0,
            component_name="Teil_1"
        )

        import_step_into_nx_as_component(
            str(step_path_2),
            x=150.0,
            y=0.0,
            z=0.0,
            component_name="Teil_2"
        )

    except Exception as e:
        lw.WriteLine("Fehler:")
        lw.WriteLine(str(e))


if __name__ == "__main__":
    main()
