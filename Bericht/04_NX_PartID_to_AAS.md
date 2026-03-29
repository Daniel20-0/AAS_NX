# NX addPartID for AAS
This project includes a Siemens NX Open application (C#) created using the NX Block UI Styler. For detailed instructions and technical background on working with this tool, please refer to the official Siemens manual **"NX Open Programmer's Guide"**, specifically the chapters on the **"Block UI Styler Introduction"** (for dialog creation and callbacks).

The tool enables designers to assign a unique ID (Part ID) to an active NX part via a simple graphical user interface. This ID is stored as a part attribute (`PART_ID`) and is used to link the 3D model with the AAS for digital twins.

---

## Basic functionality (Adding the Part ID for the AAS)

To make a 3D model usable in Industry 4.0 scenarios, it must be uniquely identifiable. This script addresses this requirement by providing a defined workflow in NX:

1. **User input:** The user starts the script in NX. A dialog box (defined by the `.dlx` file) opens, in which the desired ID for the AAS is entered.

2. **Validation:** The tool verifies whether an ID has been entered and whether a part is opened and active (Work Part) in NX.

3. **Attribute assignment:** The entered string is written directly into the part metadata via the NX Open API. The attribute **`PART_ID`** is created or overwritten.

Once the part is saved and, for example, exported as a STEP file (including metadata), the AAS can read this `PART_ID` and associate the part with a digital twin.

--- 

## Technical workflow diagram

The following SVG file shows a **flowchart** that describes the technical functionality of the implemented process.

![Technical flowchart of the AASX-to-NX import workflow](bilder/Workflow_ADD_ID.drawio.svg)

---

## Code structure and the individual functions

The code is based on the standard template of the NX Block UI Styler. Below is a detailed description of the key functions in `add_PartID.cs`:

### `Main()`
The entry point of the application. A new instance of the `add_PartID` class is created, and the dialog is displayed on the user’s screen via the `Show()` method. 

### `initialize_cb()`
*(Initialize Callback)*
This method is executed immediately when the dialog is loaded. It establishes the connection between the C# logic and the graphical user interface (the `.dlx` file). Here, the input field (block type: String) is located in the UI and assigned to the variable `string0`, so it can be accessed later in the process.

### `apply_cb()`
*(Apply Callback)*
This function is triggered when the user clicks **"Apply"**:

* **Read values:** Retrieves the text from the input field (`string0.Value`).
* **Validation checks (If-Statements):**
  * Checks whether the field is empty. If so, an informational message is displayed and the process is stopped.
  * Checks whether an active work part (`workPart`) exists. Without a part, no attribute can be assigned.
* **Write operation:** The command `workPart.SetAttribute("PART_ID", eingegebeneID);` writes the actual attribute to the NX part.
* **Session Undo:** Creates a visible undo step ("Part ID set"), to keep the NX session clean.

### `ok_cb()`
*(OK Callback)*
Executed when the user clicks the "OK" button. This function internally calls `apply_cb()`, thereby performing the attribute assignment and then closing the dialog window.

### `GetUnloadOption()`
Defines how the program is handled in NX memory after execution. Here, `Session.LibraryUnloadOption.Immediately` is set. This means that memory is released immediately after the script has been executed. This prevents memory leaks during an NX session.

---

## The User Interface (`add_PartID.dlx`)

The included XML file (`.dlx`) defines the visual appearance of the NX dialog. It includes:
* The window title: **"Add Part ID"**
* A group (`group0`) for visual structuring
* The essential text input field (`string0`) labeled **"Enter Part ID"**.

---

## Installation & Execution in NX

1. Download the files `add_PartID.cs` and `add_PartID.dlx`
2. Ensure that both files are located in the same directory or placed according to the NX environment variables (e.g., in the `application` folder under `UGII_USER_DIR`)
3. Open a part in Siemens NX.
4. Execute the C# file via (File -> Execute -> NX Open) or integrate it as a button into your NX user interface (Ribbon).

---

## Troubleshooting

* **Error during startup (dialog cannot be found):** By default, the C# script automatically locates the `add_PartID.dlx` file within the same directory where the script is stored. There is no need to manually adjust the path in the code, as long as the .cs file and the .dlx file remain in the same folder. Alternatively, the `.dlx file` can be placed in a standardized NX directory `($UGII_USER_DIR/application/)` for automatic detection by NX.".
* **Message "No active part available":** The script was executed without a part being open, or the displayed part is not the "Work Part". Set the part as the Work Part by right-clicking it in the Assembly Navigator and try again.