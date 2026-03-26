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
3. Check whether the active part is a standalone part or an assembly
4. Define the standard attributes to be exported
5. Update the mass properties of each relevant part
6. Read mass, volume, and area directly via NX measurement functions
7. Read additional standard attributes, such as material, from part attributes
8. Collect all custom user attributes from the part
9. In assemblies, additionally collect instance-specific attributes from each leaf component
10. Merge part attributes and component attributes, with component attributes overriding identical names if necessary
11. Remove standard attributes from the custom attribute set to avoid duplicate CSV columns
12. Create one CSV row per standalone part or per leaf component in an assembly
13. Build a sorted CSV header containing standard and custom attributes
14. Write the extracted data to a CSV file

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

## Sync other Properties



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