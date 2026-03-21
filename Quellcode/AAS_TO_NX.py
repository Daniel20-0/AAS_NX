from pathlib import Path
import sys
import os
import tkinter as tk
from tkinter import filedialog

from aas_creo_bridge.adapters.aasx.aasx_importer import import_aasx
from aas_creo_bridge.adapters.aasx.get_models import get_models_from_aas


# Defines the temporary file path where the extracted STEP file will be stored
TEMP_STEP = Path(r"C:\Users\chris\AAS-Creo-Bridge\temp_model.step")


def select_aasx_file():
    # Opens a file dialog to let the user select an AASX file
    # Returns the selected file path as a Path object
    # If no file is selected, returns None
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="AASX Datei auswählen",
        filetypes=[("AASX files", "*.aasx"), ("Alle Dateien", "*.*")]
    )

    if not file_path:
        print("Keine Datei ausgewählt")
        return None

    return Path(file_path)


def extract_step_from_aasx(aasx_path):
    # Imports the given AASX file and searches for embedded STEP files
    # Iterates through all AAS shells, models, and metadata entries
    # When a STEP file is found, it is extracted and written to a temporary location
    # Returns the path to the extracted STEP file or None if no STEP file is found

    print("Importiere AASX...")

    result = import_aasx(aasx_path)

    print("Gefundene AAS:", result.shells)

    for aas_id in result.shells:

        models = get_models_from_aas(result, aas_id)

        for model in models:
            for meta in model.metadata:

                if "step" in meta.file_format.format_name.lower():

                    print("STEP gefunden:", meta.filepath)

                    step_path = TEMP_STEP

                    if step_path.exists():
                        step_path.unlink()

                    with open(step_path, "wb") as f:
                        result.file_store.write_file(meta.filepath, f)

                    print("STEP wird geschrieben nach:", step_path)

                    return str(step_path)

    return None


def main():
    # Main function of the script
    # Prompts the user to select an AASX file
    # Calls the extraction function to retrieve a STEP file
    # Outputs whether a STEP file was successfully created or not
    aasx_file = select_aasx_file()

    if aasx_file is None:
        return

    print("Gewählte Datei:", aasx_file)

    step_file = extract_step_from_aasx(aasx_file)

    if step_file:
        print("STEP Datei erstellt:", step_file)
    else:
        print("Keine STEP Datei gefunden")


if __name__ == "__main__":
    main()