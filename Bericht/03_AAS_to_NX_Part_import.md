# 4 Function Descriptions

The following sections describe the implementation of the core features.

## 4.1 NX AASX to STEP Import Tool

This project contains a Python-based workflow for importing CAD geometry from an **AASX file (Asset Administration Shell package)** into **Siemens NX**.

The solution consists of two scripts:

- **NX launcher script**  
  Executes inside Siemens NX via the **NX Open Python API**
- **External AAS script**  
  Extracts a STEP file from an AASX package

The workflow connects an AAS with a CAD system by extracting a referenced STEP model and importing it into NX as a native `.prt` component.

---

## 4.2 Overview

The tool enables a semi-automated workflow to extract and load CAD data from an AASX container into Siemens NX.

### 4.2.1 Key Features

- Interactive execution from Siemens NX
- Launch of an external Python extraction script via `subprocess`
- Automatic detection or creation of an active NX work part
- Conversion from **STEP** to **NX PRT**
- Insertion of imported `.prt` files as assembly components
- Support for multiple component instances
- Logging and error output via the NX Listing Window

---

## 4.3 Basic Functionality

The current implementation performs the following workflow:

1. The NX launcher script starts inside Siemens NX
2. The launcher executes the external script `AAS_TO_NX.py`
3. The external script handles:
   - AASX file selection
   - STEP model identification
   - STEP extraction
4. The NX launcher checks whether the STEP file was created
5. The STEP file is converted into a native NX `.prt` file
6. The resulting `.prt` file is inserted into the active assembly as a component
7. A second component instance can be added at another position

---

## 4.4 Project Structure

The solution consists of two scripts:

- **NX launcher script**
- **External extraction script**: `AAS_TO_NX.py`

---

# 4.5 NX Launcher Script

The NX launcher script is responsible for the NX-side import workflow.

It currently includes the following main tasks:

- Ensure that a valid work part exists
- Launch the external extraction script
- Convert STEP to NX PRT
- Insert the imported geometry as assembly components
- Write status and error information to the NX Listing Window

---

## `main()`

Entry point of the NX launcher script.

### Responsibilities

- Opens the NX Listing Window
- Resolves the path to the external script
- Deletes an old STEP file before starting the extraction
- Executes the external script via `subprocess.run(...)`
- Evaluates return code, stdout, and stderr
- Verifies whether the extracted STEP file exists
- Ensures that an NX work part is available
- Imports the STEP file as one or more assembly components

### Notes

- The launcher currently checks for `temp_model.step` in  
  `AAS-Creo-Bridge/temp_model.step`
- It also tries to place a second instance using  
  `temp_model.step` in the launcher base directory
- The code currently validates only the first STEP path before import

---

## `ensure_work_part()`

Ensures that an active NX work part exists.

###  Behavior

- Checks whether `session.Parts.Work` is available
- If no work part exists:
  - Looks for `StartPart.prt` in the launcher directory
  - Opens it if it already exists
  - Otherwise creates a new part in millimeter units

### Purpose

This prevents NX Open operations from failing due to a missing active work part.

---

## `identity_matrix()`

Creates and returns an identity rotation matrix of type `NXOpen.Matrix3x3`.

### Purpose

Used as the default orientation matrix when inserting components.

---

## `rotation_matrix_x(angle_deg)`

Creates a rotation matrix for a rotation about the **X axis**.

### Input

- `angle_deg`: rotation angle in degrees

---

## `rotation_matrix_y(angle_deg)`

Creates a rotation matrix for a rotation about the **Y axis**.

### Input

- `angle_deg`: rotation angle in degrees

---

## `rotation_matrix_z(angle_deg)`

Creates a rotation matrix for a rotation about the **Z axis**.

### Input

- `angle_deg`: rotation angle in degrees

---

## `get_rotation_matrix(axis="X", angle_deg=0.0)`

Returns a rotation matrix depending on the selected axis.

### Supported axes

- `X`
- `Y`
- `Z`

If the axis is invalid, the function returns the identity matrix.

### Note

This helper function exists in the code, but the current component insertion logic does **not yet apply** the computed rotation matrix.  
`add_prt_as_component()` currently uses `identity_matrix()` directly.

---

## `import_step_to_prt(step_path)`

Converts a STEP file into a native NX `.prt` file.

### Behavior

- Creates an NX `Step242Importer`
- Uses native file system import mode
- Imports the file into a **new part**
- Enables import of:
  - Curves
  - Surfaces
  - Solids
  - PMI data
- Writes the output `.prt` file next to the STEP file

### Returns

- Path to the generated `.prt` file on success
- `None` on failure

---

## `open_part(part_path)`

Opens an NX part file using `session.Parts.OpenBaseDisplay(...)`.

### Behavior

- Opens the specified `.prt` file
- Logs success or failure in the NX Listing Window

### Returns

- The opened part object on success
- `None` on failure

### Note

This function is currently available in the launcher code but is not used by `main()`.

---

## add_prt_as_component


Adds a `.prt` file as a component to the target assembly.

### Behavior

- Creates a placement point from `x`, `y`, `z`
- Uses the NX `ComponentAssembly.AddComponent(...)` API
- Assigns the given component name
- Inserts the part as `"Entire Part"`

### Returns

- The created component on success
- `None` on failure

### Important Note

Although the function signature includes:

- `axis`
- `angle_deg`

the current implementation does **not** apply rotational placement.  
The component orientation is currently always the identity matrix.

---

## import_step_into_nx_as_component


Central import helper for NX-side processing.

### Process

1. Ensure an active work part exists
2. Convert STEP to PRT
3. Derive a default component name from the `.prt` filename if needed
4. Insert the `.prt` file as a component into the assembly

### Returns

- The created NX component on success
- `None` on failure

---

## Multiple Component Placement

The NX launcher currently supports inserting multiple instances of the imported model.

### Current Example in Code

- `Part_1` at `(0.0, 0.0, 0.0)`
- `Part_2` at `(150.0, 0.0, 0.0)`

This allows simple assembly population with repeated geometry.

### Note

The second import currently references a different STEP path:

- `AAS-Creo-Bridge/temp_model.step`
- `temp_model.step` in the base directory

This behavior should be kept in mind when testing the workflow.

---

# External Script: `AAS_TO_NX.py`

The external script is responsible for extracting a STEP file from the selected AASX package.

Its functionality remains unchanged.

---

## `main()`

Entry point of the external extraction script.

### Process

1. Opens a file selection dialog
2. User selects an `.aasx` file
3. The AASX content is analyzed
4. A matching STEP file is extracted
5. The STEP file is written to a temporary location

---

## `select_aasx_file()`

Opens a file dialog using Tkinter.

### Behavior

- Allows the user to select an `.aasx` file
- Aborts the process if no file is selected

---

## `ask_part_name()`

Prompts the user to enter a specific part name.

### Behavior

- Uses a Tkinter input dialog
- Validates that the input is not empty
- Defines which STEP model should be extracted from the AASX package

---

## `extract_step_from_aasx_by_name()`

Performs a targeted extraction of a STEP model from the AASX package.

### Process

1. Open and parse the AASX file
2. Iterate over available AAS shells
3. Inspect referenced files and metadata
4. Identify STEP files
5. Compare the file name with the user-defined part name
6. Extract the matching STEP file
7. Save it to a temporary location
8. Return the resulting STEP path

### Returns

- STEP file path if a matching file is found
- `None` if no matching STEP file exists

---

## 4.6 Installation and Execution in NX

1. Ensure Python is installed and available
2. Ensure the NX Open Python API is available
3. Place both scripts in the expected project structure
4. Open Siemens NX
5. Execute the NX launcher script

The launcher then starts the extraction and import workflow automatically.

---

## 4.7 Troubleshooting

### No file selected

Possible cause:

- The AASX file selection dialog was cancelled

---

### No matching STEP file found

Possible causes:

- No STEP file matches the entered part name
- Naming mismatch between AASX file content and user input

---

### External script failed

The launcher reports the external return code and any stdout/stderr output in the NX Listing Window.

Possible causes:

- Missing Python environment
- Invalid script path
- Runtime error in the external script

---

### STEP file was not created

Possible causes:

- Extraction failed
- Output path mismatch
- File was written to a different temporary location than expected

---

### Import into NX failed

Possible causes:

- STEP to PRT conversion failed
- NX importer configuration issue
- Invalid or inaccessible file path
- Component insertion failure in the current assembly

---

## 4.8 Possible Improvements

- Apply the computed rotation matrix during component placement
- Validate both STEP paths before inserting multiple instances
- Use a consistent temporary output path
- Let the user select from available STEP models instead of entering a name manually
- Support import of multiple different components from one AASX package
- Add automatic placement using metadata
- Add configurable paths instead of fixed relative paths
- Write logs to a file in addition to the NX Listing Window