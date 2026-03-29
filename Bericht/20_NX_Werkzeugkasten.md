## Toolbox in NX

The connection of the CAD system Siemens NX to the AAS enables a continuous, bidirectional flow of information. This transforms the static 3D model into an integral component of the Digital Twin. Using the NX Open API, a wide variety of functions can be implemented, expanding the functional scope for AAS use cases almost limitlessly.

The following core functions and workflows are made possible by this integration:

### 1. Automated import of CAD data from the AAS
* **AASX extraction:** CAD models (such as STEP files) referenced within an AASX container can be specifically searched for, extracted, and saved in a temporary directory using external Python scripts.
* **Automatic loading in NX:** A launcher script executed in NX picks up this data and automatically imports it into the work environment via the NX Step Importer.
* **Assemblies and single parts:** Complex assembly structures as well as individual parts can be loaded. *Note on positioning: Via the NX Open API, exact transformation matrices (coordinates) can be passed to the imported bodies during loading or within the assembly.*

### 2. Assignment of a unique Asset ID (Digital Thread)
* **ID linking:** To uniquely assign a CAD part to a specific AAS instance, a unique ID can be assigned to the model directly in NX.
* **Attribution:** This assignment is done by writing metadata into the part attributes (e.g., creating the attribute `PART_ID`). If the part is exported later, this ID is retained as meta-information within the model and can be read by Industry 4.0 systems.

### 3. Data export for Bills of Materials (BOM) and AAS synchronization
* **Reading properties:** Specific physical mass properties of an NX part (such as volume, mass, and surface area) can be automatically read out using a Python script.
* **BOM creation:** These extracted CAD attributes can be exported (e.g., as a CSV file). This data forms the basis for detailed bills of materials (such as an R-BOM for recycling scenarios), which can then be linked directly into the structure of the AASX file.

### 4. UI customization and user interaction
* **NX Block UI Styler:** Native graphical user interfaces (dialog boxes) can be created directly in NX. For example, the user can enter IDs via a convenient text field while validation checks run in the background (e.g., whether an active part is open).
* **Seamless integration:** The NX user interface can be customized by adding scripts as interactive buttons directly to the NX menu bar (ribbon). This ensures a high level of user-friendliness.
* **Limitless extensibility:** Since NX can act both as a launcher for external Python scripts and execute internal C#/Python logic, there are virtually no technical limitations for automation and data linking with the Digital Twin.