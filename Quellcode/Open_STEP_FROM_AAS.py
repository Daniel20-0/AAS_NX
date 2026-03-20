import sys
import subprocess
import os
from time import sleep
import NXOpen


def ensure_work_part():
    # Ensures that an active NX part exists.
    # If no part is currently open, a new one is created.
    # If an old file with the same name exists, it will be deleted first.

    session = NXOpen.Session.GetSession()
    lw = session.ListingWindow

    if session.Parts.Work is None:

        part_name = r"C:\Users\chris\AAS-Creo-Bridge\StartPart.prt"

        if os.path.exists(part_name):
            try:
                os.remove(part_name)
            except:
                lw.WriteLine("Altes Part konnte nicht gelöscht werden")

        lw.WriteLine("Kein aktives Part vorhanden → erstelle neues Part")

        session.Parts.NewDisplay(
            part_name,
            NXOpen.Part.Units.Millimeters
        )

def import_step_into_nx(step_path):
    # Imports a STEP file into NX and converts it into an NX part (.prt).
    # Includes geometry such as curves, surfaces, solids, and PMI data.
    # Configures the importer and executes the import process.
    session = NXOpen.Session.GetSession()
    lw = session.ListingWindow

    importer = session.DexManager.CreateStep242Importer()

    try:

        importer.Optimize = True
        importer.SimplifyGeometry = False
        importer.Messages = NXOpen.Step242Importer.MessageEnum.Error

        importer.SetMode(NXOpen.BaseImporter.Mode.NativeFileSystem)

        importer.InputFile = step_path
        importer.OutputFile = step_path.replace(".step", ".prt").replace(".stp", ".prt")

        importer.ObjectTypes.Curves = True
        importer.ObjectTypes.Surfaces = True
        importer.ObjectTypes.Solids = True
        importer.ObjectTypes.PmiData = True

        importer.FileOpenFlag = False
        importer.ProcessHoldFlag = True

        lw.WriteLine("Importiere: " + step_path)

        importer.Commit()

        lw.WriteLine("STEP Import abgeschlossen")

    except Exception as ex:
        lw.WriteLine("Fehler während STEP Import:")
        lw.WriteLine(str(ex))


def main():
    # Main function of the script.
    # Runs an external Python script to generate a STEP file.
    # Checks whether the STEP file was created successfully.
    # Ensures a working NX part exists and then imports the STEP file.

    session = NXOpen.Session.GetSession()
    lw = session.ListingWindow
    lw.Open()

    lw.WriteLine("NX Launcher gestartet")

    python_exe = r"C:\Users\chris\AppData\Local\Programs\Python\Python311\python.exe"
    script_path = r"C:\Users\chris\AAS-Creo-Bridge\src\AAS_TO_NX.py" # Path to the external script that generates the STEP file
    step_path = r"C:\Users\chris\AAS-Creo-Bridge\temp_model.step"

    try:

        lw.WriteLine("Starte externes Skript...")
        lw.WriteLine(script_path)

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

        if not os.path.exists(step_path):
            lw.WriteLine("STEP Datei wurde nicht erzeugt!")
            return

        lw.WriteLine("STEP Datei gefunden -> starte Import")

        ensure_work_part()

        sleep(1)

        import_step_into_nx(step_path)

    except Exception as e:
        lw.WriteLine("Fehler:")
        lw.WriteLine(str(e))


if __name__ == "__main__":
    main()