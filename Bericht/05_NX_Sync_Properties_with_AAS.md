# 6 NX Add Attributes Tool  
This project includes a Siemens NX Open application (Python) created using the NX Block UI Styler. For detailed instructions and technical background on working with this tool, please refer to the official Siemens manual **"NX Open Programmer's Guide"**, specifically the chapters on the **"Block UI Styler Introduction"** (for dialog creation and callbacks).

The tool enables designers to assign **custom user-defined attributes** (name + value) to the active NX part via a simple graphical user interface.

---

## 6.1 Basic functionality (Adding custom attributes to an NX part)

In many engineering workflows, additional metadata must be attached to a CAD model (e.g., IDs, descriptions, classifications). This script provides a flexible way to assign such attributes:

1. **User input:**  
   The user starts the script in NX. A dialog box (defined by the `.dlx` file) opens with two input fields:
   - Attribute name (Label/Title)
   - Attribute value

2. **Validation:**  
   The tool checks:
   - Whether a part is currently open and active (Work Part)
   - Whether a valid attribute name has been entered (not empty)

3. **Attribute assignment:**  
   The entered attribute is written directly into the part metadata using the NX Open API.  
   The attribute is created or overwritten dynamically based on the user input.

This allows flexible enrichment of NX parts with metadata for downstream processes such as PLM integration, export, or digital twin applications.

---

## 6.3 Code structure and the individual functions

The code is based on the standard template of the NX Block UI Styler. Below is a detailed description of the key functions in `Add_Attributes.py`:

### `main()`
The entry point of the application.  
An instance of the `Add_Attributes` class is created, and the dialog is displayed using the `Show()` method. After execution, resources are properly released via `Dispose()`.

---

### `__init__()`
*(Constructor)*  
Initializes the NX session and UI, loads the `.dlx` dialog file, and registers all callback functions:
- Apply
- OK
- Update
- Initialize
- DialogShown

---

### `initialize_cb()`
*(Initialize Callback)*  
Executed when the dialog is loaded.  
This function connects the UI elements (defined in the `.dlx` file) with the Python variables:
- `string0` → Attribute name
- `string01` → Attribute value  

These references allow access to user input later in the process.

---

### `dialogShown_cb()`
*(Dialog Shown Callback)*  
Executed just before the dialog is displayed.  
Currently not used, but can be extended to:
- Set default values
- Pre-fill fields
- Configure dynamic UI behavior

---

### `apply_cb()`
*(Apply Callback)*  
This is the **core function** of the application and is triggered when the user clicks **"Apply"**:

* **Read values:**  
  Retrieves the input from both text fields:
  - Attribute name (`string0`)
  - Attribute value (`string01`)

* **Validation checks:**
  - Ensures a Work Part exists
  - Ensures the attribute name is not empty

* **Write operation:**  
  The attribute is written to the active part using:
  ```python
  workPart.SetUserAttribute(...)
* **Error handling:**  
  If any issue occurs, an error message is displayed via the NX Message Box.

---

### `update_cb(block)`
*(Update Callback)*  
Triggered whenever a UI element changes.  
Currently not used, but can be extended for:
- Live validation
- Dynamic UI updates
- Enabling/disabling fields

---

### `ok_cb()`
*(OK Callback)*  
Executed when the user clicks the **"OK"** button.  
Internally calls `apply_cb()` to perform the attribute assignment and then closes the dialog.

---

### `GetBlockProperties(blockID)`
Helper function to access the properties of UI elements (blocks).  
Used to retrieve values from the dialog input fields.

---

### `Dispose()`
Ensures proper cleanup of the dialog and frees NX resources after execution.

---

## The User Interface (`Add_Attributes.dlx`)

The included XML file (`.dlx`) defines the visual structure of the dialog:

* Two input fields:
  - **Attribute Name** (`string0`)
  - **Attribute Value** (`string01`)
* Standard NX dialog buttons:
  - Apply
  - OK
  - Cancel

The UI is intentionally minimalistic to allow fast and flexible attribute entry.

---

## 6.4 Installation & Execution in NX

1. Download the files `Add_Attributes.py` and `Add_Attributes.dlx`
2. Ensure both files are located in the same directory  
   *(or in a configured NX application directory, e.g. `$UGII_USER_DIR/application`)*
3. Open a part in Siemens NX
4. Run the script via:
   - **Menu:** File → Execute → NX Open → Python
   - Or integrate it into the NX Ribbon

---

## 6.7 Troubleshooting

* **Dialog cannot be found:**  
  Ensure that the `.dlx` file is located in the same directory as the Python script. The script automatically resolves the path based on its own location.

* **Error: "No active work part found":**  
  No part is currently active. Open a part or set an existing part as the Work Part.

* **Error: "Attribute name cannot be empty":**  
  The first input field must contain a valid attribute name.