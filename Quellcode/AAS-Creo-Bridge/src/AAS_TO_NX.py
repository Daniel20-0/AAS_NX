from pathlib import Path
import sys
import os
import tkinter as tk
from tkinter import filedialog, simpledialog

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

    root.destroy()

    if not file_path:
        print("Keine Datei ausgewählt")
        return None

    return Path(file_path)


def ask_part_name():
    root = tk.Tk()
    root.withdraw()

    part_name = simpledialog.askstring(
        "Teilname eingeben",
        "Bitte Teilnamen eingeben (z. B. GPLE60-3S):"
    )

    root.destroy()

    if not part_name or not part_name.strip():
        print("Kein Teilname eingegeben")
        return None

    return part_name.strip()


def get_stem_from_filepath(filepath: str) -> str:
    # Wandelt z. B. '/aasx/files/GPLE60-3S.stp' in 'GPLE60-3S' um.
    return Path(filepath).stem


def extract_step_from_aasx_by_name(aasx_path: Path, wanted_name: str):
    # Sucht in der AASX nach einer STEP-Datei, deren Dateiname
    # (ohne Endung) dem gewünschten Namen entspricht, und speichert sie temporär.
    print("Importiere AASX...")
    result = import_aasx(aasx_path)

    print("Gefundene AAS:", result.shells)

    wanted_name_lower = wanted_name.lower()

    for aas_id in result.shells:
        models = get_models_from_aas(result, aas_id)

        for model in models:
            for meta in model.metadata:
                # Nur STEP-Dateien betrachten
                if "step" not in meta.file_format.format_name.lower():
                    continue

                # Dateinamen ohne Endung aus dem Pfad ableiten
                current_name = get_stem_from_filepath(meta.filepath)

                print(f"Prüfe: {meta.filepath} -> {current_name}")

                if current_name.lower() == wanted_name_lower:
                    print("Passende STEP gefunden:", meta.filepath)

                    if TEMP_STEP.exists():
                        TEMP_STEP.unlink()

                    with open(TEMP_STEP, "wb") as f:
                        result.file_store.write_file(meta.filepath, f)

                    print("STEP wird geschrieben nach:", TEMP_STEP)
                    return str(TEMP_STEP)

    return None


def main():
    aasx_file = select_aasx_file()
    if aasx_file is None:
        print("Keine Datei ausgewählt -> externer Prozess wird beendet")
        sys.exit(1)

    print("Gewählte Datei:", aasx_file)

    part_name = ask_part_name()
    if part_name is None:
        print("Kein Teilname eingegeben -> externer Prozess wird beendet")
        sys.exit(1)

    print("Gesuchter Teilname:", part_name)

    step_file = extract_step_from_aasx_by_name(aasx_file, part_name)

    if step_file:
        print("STEP Datei erstellt:", step_file)
        sys.exit(0)
    else:
        print(f"Keine STEP Datei mit Namen '{part_name}' gefunden")
        sys.exit(2)


if __name__ == "__main__":
    main()
