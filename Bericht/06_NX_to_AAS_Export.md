# 06 Attribute Export Skript

This Python script uses the NXOpen Python API to read specific attributes of an open NX part and export them into a CSV file.

The CSV file contains selected mass properties of a part, e.g.:

- Volume
- Mass
- Surface area
- Material

The file is automatically saved in the same directory as the NX part.

---
# Basic Functionality

The script executes the following process:

1. Establish a connection to the current NX session 
2. Access the active work part 
3. Define the attributes to be read
4. Iterate over all attributes of the part 
5. Extract the required values
6. Write the data to a CSV file

---

# Code Structure and Functions


## main()

The entry point of the script.

Functions:

- Initialize Session: Access the current `NXOpen.Session`.
- Get Active Part: Access the `workPart` (abort if none is open).
- Determine Script Directory: Use `Path(__file__)` to get the folder where the script is stored.
- Define Target Attributes: Specify required keys (e.g., `MassPropMass`, `Material`).
- Update Mass Properties: Use `MassCalculationBuilder` to ensure geometry data is up-to-date.
- Collect Attribute Values: Iterate through all part attributes and filter by defined keys.
- Define CSV Path: Combine the script directory with the part name for the export file.
- Export to CSV: Write the filtered values into a `.csv` file located in the script's folder.

## Definition of the required attributes

The following attributes are exported:

wanted_attributes = [
    "MassPropVolume",
    "MassPropMass",
    "MassPropArea",
    "Material"
]

These attributes correspond to mass properties of an NX part.

| Attribut        | Description                |
|-----------------|--------------------------|
| MassPropVolume  | Volume of the part     |
| MassPropMass    | Mass of the part     |
| MassPropArea    | Surface area of the part |
| Material        | Material of the part |

## Creation of the export file path

The file path of the CSV file is generated automatically

---

## Installation & Execution in NX

Ensure that Siemens NX with the NX Open Python API is installed. Save the script in an NX script directory or a project folder. Open a part in Siemens NX. Execute the script via the following menu:
- File → Execute → NX Open
- Select the Python script
- After execution, a CSV file is automatically generated

---

## Troubleshooting (Fehlerbehebung)
No CSV file is generated
Possible causes:
- No active work part is available
- The part does not contain the required attributes
- Missing write permissions in the target directory (CSV File already open)

Attributes are not found
Possible causes:

- Attributes have different names
- Attributes are not stored as user attributes
- Alias and title differ