from pathlib import Path
import sys
import os
import tkinter as tk
from tkinter import filedialog, simpledialog

from aas_adapter import importer
from aas_adapter import extractor


# Defines the temporary file path where the extracted STEP file will be stored
BASE_DIR = Path(__file__).resolve().parent.parent

TEMP_STEP = BASE_DIR / "temp_model.step"


def select_aasx_file():
    # Opens a file dialog to let the user select an AASX file
    # Returns the selected file path as a Path object
    # If no file is selected, returns None
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select AASX File",
        filetypes=[("AASX files", "*.aasx"), ("All files", "*.*")]
    )

    root.destroy()

    if not file_path:
        print("No file selected")
        return None

    return Path(file_path)


def ask_part_name():
    root = tk.Tk()
    root.withdraw()

    part_name = simpledialog.askstring(
        "Enter Part Name",
        "Please enter the part name (e.g., GPLE60-3S):"
    )

    root.destroy()

    if not part_name or not part_name.strip():
        print("No part name entered")
        return None

    return part_name.strip()


def get_stem_from_filepath(filepath: str) -> str:
    # Converts e.g. '/aasx/files/GPLE60-3S.stp' into 'GPLE60-3S'
    return Path(filepath).stem


def extract_step_from_aasx_by_name(aasx_path: Path, wanted_name: str):
    # Searches the AASX for a STEP file whose filename
    # (without extension) matches the desired name, and saves it temporarily.
    print("Importing AASX...")
    result = importer.import_aasx(aasx_path)

    print("Found AAS:", result.shells)

    wanted_name_lower = wanted_name.lower()

    for aas_id in result.shells:
        models = extractor.get_models_from_aas(result, aas_id)

        for model in models:
            for meta in model.metadata:
                # Only consider STEP files
                if "step" not in meta.file_format.format_name.lower():
                    continue

                # Derive the filename without extension from the path.
                current_name = get_stem_from_filepath(meta.filepath)

                print(f"Prüfe: {meta.filepath} -> {current_name}")

                if current_name.lower() == wanted_name_lower:
                    print("Found matching STEP file:", meta.filepath)

                    if TEMP_STEP.exists():
                        TEMP_STEP.unlink()

                    with open(TEMP_STEP, "wb") as f:
                        result.file_store.write_file(meta.filepath, f)

                    print("STEP file written to:", TEMP_STEP)
                    return str(TEMP_STEP)

    return None


def main():
    aasx_file = select_aasx_file()
    if aasx_file is None:
        print("No file selected -> external process will be terminated")
        sys.exit(1)

    print("Selected file:", aasx_file)

    part_name = ask_part_name()
    if part_name is None:
        print("No part name entered -> external process will be terminated")
        sys.exit(1)

    print("Searched part name:", part_name)

    step_file = extract_step_from_aasx_by_name(aasx_file, part_name)

    if step_file:
        print("STEP file created:", step_file)
        sys.exit(0)
    else:
        print(f"No STEP file with name '{part_name}' found")
        sys.exit(2)


if __name__ == "__main__":
    main()
