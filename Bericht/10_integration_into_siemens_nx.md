## 9 Execution and Integration in Siemens NX

This section describes how the developed scripts are integrated and executed within the Siemens NX environment.

The mechanisms described here apply globally to the entire project and are not repeated in individual function descriptions.

---

## 9.1 Execution Methods in Siemens NX

There are multiple ways to execute the NX launcher script inside Siemens NX.

### Option 1: Journal Playback

The script can be executed using the **Journal Playback** functionality.

Steps:

- Open *Journal Playback* in NX
- Select the NX launcher script
- Execute the script

This is the simplest method and is recommended for development and testing.

---

### Option 2: Custom User Command

The script can also be integrated as a **custom NX command**.

- A user-defined command is created in NX
- The NX launcher script is assigned as the execution action
- The command can be added to toolbars or menus

This approach is recommended for productive workflows.

---

## 9.2 File Path Dependencies

Scripts in Siemens NX are referenced via **absolute or relative file paths**.

Important considerations:

- If scripts are moved or renamed, paths must be updated
- The NX launcher script must be able to locate:
  - the external script
  - the temporary STEP file

Incorrect paths will prevent execution.

---

## 9.3 External Script Execution

The NX launcher automatically executes the external script:

- Don't change path of the downloaded scripts
- No manual interaction is required
- Communication is handled via:
  - file system (STEP file)
  - return codes
  - stdout / stderr logging

---

## 9.4 UI Styler Integration (Optional)

If a graphical interface is created using **NX UI Styler**, additional integration is possible.

### Requirements

- `.cs` file (UI logic)
- `.dllx` file (compiled UI definition)

### Important Notes

- The `.cs` file contains a reference to the `.dllx` file
- This path must be updated before first execution
- Both files must remain linked

---

### Execution Options for UI Styler

UI Styler scripts can be executed via:

- **Journal Replay**
- **Custom NX Command**

This allows seamless integration into NX workflows.

---

## 9.5 Workflow Overview

The following diagram illustrates the interaction between:

- NX launcher script
- External AAS processing script
- Optional UI layer

![Technical flowchart of the AASX-to-NX import workflow](bilder/Workflow_functions.svg)