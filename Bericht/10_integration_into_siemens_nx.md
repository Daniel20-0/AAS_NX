## Integration of the developed scripts into the Siemens NX CAD environment

---

## Integration of Python Scripts in Siemens NX

There are multiple ways to integrate and execute Python scripts in Siemens NX.

### Option 1: Execution via Journal

One approach is to execute the script using the **Journal playback functionality**.

Steps:
- Add the *Journal Playback* command in NX
- Select the desired Python script
- Execute the script directly within the NX environment

---

### Option 2: User-defined command

Another approach is to create a **custom user command** in NX.

- A new user command is defined
- The Python script is assigned as the corresponding action
- The script can then be executed like a native NX command

---

### Important note

It is important to note that scripts are referenced via **file paths** in Siemens NX.

- If the script is moved or renamed,
- the corresponding path in NX must be updated

Otherwise, the script can no longer be executed.

---

## Integration of C# based UI Styler Scripts

Scripts created with the **NX UI Styler** can also be executed via the **Journal Replay** functionality.

However, there are some important aspects to consider:

- UI Styler-based scripts require both a `.cs` file and a corresponding `.dllx` file.
- These files must be correctly linked to each other.
- The `.cs` file contains a file path reference to the associated `.dllx` file.
- This path must be updated before the first execution to ensure correct functionality.

---

### Additional Integration Option

UI Styler scripts can also be integrated as a **custom user command**:

- The `.cs` script is assigned as the execution action.
- The command can then be added to the NX user interface (e.g., toolbar or menu).

This allows seamless integration into regular NX workflows.

---

## Workflow Diagram

The following flowchart presents the internal process flow of the interaction between a UI Styler-based interface and a Python script.

The UI Styler component is exemplified by the `add_PartID` function, whereas the Python-based backend logic is represented by the `NX AASX to STEP Import Tool` function.

![Technical flowchart of the AASX-to-NX import workflow](bilder/Workflow_functions.svg)