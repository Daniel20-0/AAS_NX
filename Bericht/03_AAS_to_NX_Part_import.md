# NX AASX to STEP Import Tool

This project contains a Python script that is executed via the **NX Open Python API**.  
The tool is used to select an **AASX file (Asset Administration Shell)**, automatically extract a contained **STEP model** from it, and then import it into **Siemens NX**.

The application thus connects an **Asset Administration Shell (AAS)** with a CAD system by directly opening a STEP model referenced within the AAS in NX.

---

## Overview

The tool enables a semi-automated workflow to extract and load CAD data from an Asset Administration Shell (AASX) into Siemens NX.

Key Features:

- Interactive selection of an AASX file
- User-defined selection of a specific STEP model via part name
- Targeted extraction of STEP files instead of generic search
- Automatic conversion from STEP → NX PRT format
- Automatic insertion of components into an assembly
- Support for positioning multiple instances of the same model
- Logging and error output via NX Listing Window

---

## Basic functionality

The workflow has been extended to allow **targeted selection of CAD models** and **structured import into NX assemblies**.

### Process:

1. **Start of the NX script**

   The user launches the NX script inside Siemens NX.

2. **Execution of external AAS script**

   The NX script starts the external Python script via subprocess.

3. **Selection of AASX file**

   A file dialog is opened, allowing the user to select an `.aasx` file.

4. **Input of part name**

   The user is prompted to enter a specific part name  
   (e.g., `GPLE60-3S`).

5. **Targeted STEP extraction**

   The script:
   - Parses the AASX file
   - Searches for STEP models
   - Compares filenames with the user input
   - Extracts only the matching STEP file

6. **Temporary storage**

   The STEP file is stored locally.

7. **Import into NX**

   The NX script:
   - Converts the STEP file into a `.prt` file
   - Inserts it as a component into the current assembly
   - Optionally inserts multiple instances with positioning

---

## Code structure and individual functions

The code consists of two scripts:

- **NX launcher script** (performs the import in NX)
- **External AAS script** (extracts the STEP model from the AASX)

---

## NX launcher script

The NX script has been extended to support:

- STEP → PRT conversion
- Component-based assembly building
- Multiple component placement

---

## `main()`

The entry point of the NX script.

Functions:

- Opens the NX Listing Window to display status messages
- Starts the external Python script via subprocess
- Checks whether the STEP file was created
- Ensures that an active NX part exists
- Imports the STEP file into NX

---

## `ensure_work_part()`

This function ensures that an active NX part exists.

If no work part is available:

- a new part is created
- any existing old part is deleted
- the new part is set as the work part

This prevents NXOpen functions from being executed without a valid target part.

---

## `import_step_to_prt()`

This function converts a STEP file into an NX `.prt` file.

Features:

- Uses NX Step242Importer
- Creates a new NX-native part file
- Enables:
  - Solids
  - Surfaces
  - Curves
  - PMI data
- Outputs a `.prt` file in the same directory

This replaces direct STEP import into the work part.

---

## `add_prt_as_component()`

This function inserts a `.prt` file into the current assembly.

Features:

- Adds part as a component
- Supports positioning via:
  - X, Y, Z coordinates
- Assigns a component name
- Uses NX ComponentAssembly API

---

## `import_step_into_nx_as_component()`

This is the central import function.

Process:

1. Ensure active work part exists
2. Convert STEP → PRT
3. Insert PRT as component into assembly
4. Apply position and naming

This replaces the old direct STEP import.

---

## Multiple component placement

The script supports inserting multiple instances of the same STEP model:

Example:

- Component 1 at (0, 0, 0)
- Component 2 at (150, 0, 0)

This enables simple assembly creation directly from AAS data.

---

## External script (AAS_TO_NX.py)

This script extracts a STEP model from an AASX file.

---

## `main()`

The entry point of the external script.

Process:

1. Opens a file selection dialog
2. The user selects an .aasx file
3. The file is analyzed
4. A STEP model is extracted
5. The STEP file is saved locally

---

## `select_aasx_file()`

This function opens a file dialog using Tkinter.

The user can select an .aasx file.

If no file is selected, the process is terminated.

---

## `extract_step_from_aasx_by_name()`

This function performs a **targeted search** for a STEP file inside the AASX.

Process:

1. Import AASX file
2. Iterate through all AAS shells
3. Extract models from each AAS
4. Check metadata for STEP format
5. Extract filename (without extension)
6. Compare with user-defined part name
7. If match is found:
   - Extract file from file store
   - Save to temporary location
8. Return path to STEP file

If no matching STEP file is found:
- Function returns `None`

## `ask_part_name()`

This function prompts the user to enter a part name.

- Uses Tkinter dialog
- Input is validated (no empty values)
- Defines which STEP model should be extracted

This replaces the previous "take first STEP file" logic.

---

## Installation & execution in NX

1. Ensure that Python is installed.
2. Ensure that the NX Python API is available.
3. Place both scripts in your project directory.

Required scripts:

- NX launcher script:
  AAS_TO_NX.py

4. Open Siemens NX.
5. Start the NX script

The script will then automatically start the complete workflow.

---

## Configuration

Currently, several paths are hardcoded in the code.

Examples:

script_path = C:\Users\chris\AAS-Creo-Bridge\src\AAS_TO_NX.py

step_path = C:\Users\chris\AAS-Creo-Bridge\temp_model.step

---

## Troubleshooting

### STEP file not found

Possible causes:

- No STEP file matches the entered part name
- Naming mismatch between AASX and user input

---

### External script aborted

Return codes:

- `1` → No file selected
- `2` → No matching STEP found

---

### Import into NX fails

Possible causes:

- STEP → PRT conversion failed
- NX importer configuration issue
- File system access problem

## Possible improvements

- Selection of part names from dropdown instead of manual input
- Preview of available STEP models inside AASX
- Support for multiple different components from one AASX
- Automatic placement based on metadata (position/orientation)
- Configurable paths instead of hardcoded values
- Logging to file instead of only NX Listing Window
