# 03 NX AASX to STEP Import Tool
This project includes a Python script that is executed via the **NX Open Python API**.
The tool is used to select an **AASX file (Asset Administration Shell)**, automatically extract a contained **STEP model**, and then import it into **Siemens NX**.

The application thus connects an **Asset Administration Shell (AAS)** with a CAD system by directly opening a STEP model referenced within the AAS in NX.
---

## Überblick

The **NX Part Loader** provides a simplified workflow for quickly locating and opening parts.

Features:

- Automatically checks for an existing work part
- Creates a new part if none exists
- Dialog-based file name input
- Recursive search for `.prt` files
- Automatically opens the first matching file found
- Displays errors via the NX MessageBox

---

# Basic functionality (importing a STEP model from an AASX file)

To integrate digital twins or Industry 4.0 models into CAD systems, CAD data must be extracted from the Asset Administration Shell and loaded into the CAD environment.

This script automates this workflow:

1. **Start of the NX script**

The user starts the script directly in Siemens NX.
The script acts as a launcher and starts an external Python script.

2. **Selection of an AASX file**

The external script opens a file selection dialog.
The user selects an .aasx file.

3. **Extraction of the STEP model**

The external script searches the AAS for referenced models and extracts a contained STEP file.

4. **Temporary storage**

The STEP file is stored temporarily.

5. **Import into Siemens NX**

The NX script detects the generated STEP file and automatically imports it into NX.

---

# Code structure and individual functions

The code consists of two scripts:

- **NX launcher script** (performs the import in NX)
- **External AAS script** (extracts the STEP model from the AASX)

---

# NX launcher script

This script is executed directly in Siemens NX and controls the entire workflow.

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

## `import_step_into_nx()`

This function handles the import of the STEP file into NX.

For this purpose, the NX Step242Importer is used.

Importer configuration:

- Geometry optimization is enabled
- Curves, surfaces, and solids are imported
- PMI data is also included
- Import is performed directly from the file system

The import is then executed automatically.
---
# External script (AAS_TO_NX.py)

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

## `extract_step_from_aasx()`

This function searches the AASX file for contained CAD models.

Process:

1. Import of the AASX file
2. Search for Asset Administration Shells
3. Iteration through the models
4. Checking file formats
5. Detection of a STEP file
6. Extraction of the STEP file from the file store
7. Writing the file to the temporary directory

---

# Installation & execution in NX

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

# Configuration

Currently, several paths are hardcoded in the code.

Examples:

script_path = C:\Users\chris\AAS-Creo-Bridge\src\AAS_TO_NX.py

step_path = C:\Users\chris\AAS-Creo-Bridge\temp_model.step

---

# Troubleshooting (Error handling)

## STEP file is not created
Possible causes:

- The AASX file does not contain a STEP model
- The model format is not STEP
- Access to the file store has failed

---

## External script does not start

Possible causes:

- Incorrect Python path
- Wrong script path
- Missing Python dependencies

---

## Import into NX fails

Possible causes:

- STEP file is corrupted
- NX Step Importer not initialized correctly
- No work part available

# Possible improvements

Currently, the script searches for all STP files within the AASX file. If multiple STP files are present, this can lead to issues. The script should be extended to select the correct STP file from the AASX based on a specific identifier or naming convention.
