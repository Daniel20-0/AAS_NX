# 01 Introduction HKA: Integration of Digital Twins (AAS) and CAD (Siemens NX)

Within the scope of this development project, the informational and conceptual bridge between the Asset Administration Shell (AAS) and the CAD system Siemens NX is built. 

> "The Asset Administration Shell is the standardized digital representation of an asset. It structures all relevant data and properties of a physical or logical object throughout its entire lifecycle, thus forming the technical foundation for the Digital Twin in Industry 4.0." [1]

The goal is to enable working with Digital Twins across system boundaries and to ensure continuous data utilization throughout the entire product lifecycle. 

Methodologically, the project is divided into two consecutive phases:

## Phase 1: Fundamentals and Application Scenarios in the Product Lifecycle

In the first phase of the project, the theoretical fundamentals of the AAS were developed, and the specific added value and application scenarios offered by connecting a CAD system to the administration shell were evaluated. 

A practical example of a **dishwasher** serves to illustrate the concepts. Along its product lifecycle, highly varying requirements arise in each phase regarding the provision, updating, and structuring of data from the Digital Twin. 

The considered lifecycle encompasses the following six phases:

1.  Development (CAD & Engineering)
2.  Parts Procurement
3.  **Production (Manufacturing)**
4.  Sales
5.  Service / After-Sales
6.  **Recycling (End-of-Life)**

*As shown in the following diagram, these phases form a continuous cycle. Within the scope of this project, the **Production** and **Recycling** phases, in particular, were elaborated in depth. The detailed elaboration of these use cases is the subject of the following chapters.*

![Product lifecycle of a dishwasher](bilder/Eng_AAS_CAD_Lifecycle.drawio.svg)

## Phase 2: Technical Implementation and Interface Functions

Based on the conceptual preliminary work of the first phase, the focus of the second project phase was on the technical implementation. Here, the central core functions required for practical work with AASX data packages and the CAD program Siemens NX were identified and developed. 

---

> **Documentation Note ("Living Document"):**
> Since research and work on this repository will continue in the future, this documentation is designed directly as the structure for the GitHub repository (`README.md` and linked Markdown files). Redundant, separately maintained documentation was deliberately avoided. This ensures that code changes and documentation always remain synchronous, transparently versioned, and accessible in a central location for future developers.

---

## 3. Scenario: Production (Manufacturing)

### 3.1 Detailed description of the scenario
Lena Müller works as a production planner and assembly manager in final assembly. She is responsible for the correct execution of the assembly processes as well as for the quality assurance of the assembled modules. Lena checks the tightening torques of the individual screw connections and assembles the corresponding sheet metal components. In doing so, she ensures that all assembly specifications are strictly adhered to in order to guarantee the functionality, safety, and quality of the product. 

The relevant assembly information is provided to Lena digitally. An assembly drawing, linked to the respective physical asset via the Asset Administration Shell (AAS), is stored in the CAD model. Using a digital device (e.g., an industrial tablet or HMI), Lena can access this information in context.

### 3.2 Process flow description

* **Product / Asset Identification:** Lena identifies the product to be assembled using a serial number or a QR code.
* **Calling up the AAS:** The corresponding Asset Administration Shell is loaded via the manufacturing system.
* **Accessing assembly information:** The AAS points to the linked CAD model and the corresponding assembly drawing.
* **Display of assembly steps:** The individual assembly steps are presented sequentially, including the required tools.
* **Checking tightening torques:** The target torques for each screw connection are displayed and verified with the torque tool in use.
* **Assembly of sheet metal components:** Lena assembles the sheet metal components according to the drawing and the defined process steps.
* **Documentation and feedback:** The completed assembly and the verified torques are documented in the system and, if necessary, reported back to higher-level systems.

### 3.3 Required files and resources
* **CAD models** (e.g., STEP, JT, native CAD formats)
* **Assembly drawings** (2D/3D, e.g., PDF or directly in CAD)
* **Torque specifications** (e.g., tables or metadata)
* **Asset Administration Shell** (AAS model in JSON or XML format)
* **Digital devices** (tablet, industrial PC, HMI)
* **Torque tools** (ideally with a digital interface)
* **MES/PLM systems** for data management

### 3.4 Technical implementation

#### 3.4.1 Implementation in the Asset Administration Shell (AAS)
The Asset Administration Shell serves as a central data hub for assembly- and quality-relevant information. Technically, the implementation is carried out via clearly defined `SubmodelElements` that standardize assembly knowledge, CAD references, and torque specifications.

**Assembly and torque data**
* **Submodel "AssemblyInformation":** Contains the complete description of the assembly steps as structured `SubmodelElements` (e.g., `Operation`, `Sequence`, `StepNumber`).
* **Tightening torques:** Each screw connection is described by a `Property` element:
    * `FastenerID`
    * `TorqueNominal` (e.g., 12 Nm)
    * `TorqueTolerance` (e.g., ±10%)
    * `ToolType` (e.g., electronic torque wrench)

> **Example:** The screw connection of the side panel has the attribute `TorqueNominal = 12 Nm`, `TorqueTolerance = ±1.2 Nm`.

#### 3.4.2 Implementation in the CAD environment
The CAD environment (viewer or assembly frontend at Lena's workstation) acts as a visual and interactive interface between the worker and the digital product twin.

* Each component and screw connection in the CAD model is linked to the `InstanceId` of the corresponding AAS component.
* If Lena clicks on a screw in the 3D model, the **target torque**, **tolerance**, and **tool type** are loaded directly from the AAS and displayed.

**Feedback and reporting channel (As-Planned vs. As-Built)**
Lena can report deviations directly in the CAD interface, e.g.:
* Screw is inaccessible
* Component does not fit stress-free
* Torque cannot be achieved structurally

These reports are stored as an `Event` or `Annotation` directly in the AAS and are made available to engineering and production planning.

---

## 6. Scenario: Recycling (End-of-Life)

### 6.1 Detailed description of the scenario
In 2026, the linear economy ("take, make, dispose") was legally ended by the *Ecodesign for Sustainable Products Regulation* (ESPR). Every dishwasher sold in the EU must now have a Digital Product Passport (DPP), which is technically implemented as an Asset Administration Shell (AAS). 

Markus Mustermann, a specialized employee in a certified dismantling center, faces a challenge: A modern dishwasher consists of over 150 different materials, including valuable stainless steel, copper-bearing motors, electronics with rare earths, and problematic bitumen insulation mats.

Without the AAS, the dishwasher would be a "black box" for Markus. He would have to shred it, which severely degrades material purity. Thanks to the AAS, Markus becomes an Urban Miner: He accesses the digital twin, which tells him not only what is installed but also how to separate it non-destructively to maximize recycling yields.

### 6.2 Process flow description
The workflow is divided into five phases:

1.  **Capture & Initialization:** Markus scans the QR code lasered onto the housing frame. The AAS opens the corresponding model for this.
2.  **Status & Safety Analysis:** Before Markus uses any tools, the system checks the "Safety" submodel. It displays whether capacitors need to be discharged or if chemical residues (e.g., rinse aid remnants) are present in the hoses.
3.  **Virtual Exploration:** Markus receives the dismantling drawings in the AAS and disassembles the machine based on them. He is shown which part is made of which material. At the end, he enters how much mass of each material he has separated by type.
4.  **Guided Dismantling:** Markus follows the steps stored in the AAS. The system dictates:
    * *Step 1:* Loosen the Torx screws (T15) on the back panel.
    * *Step 2:* Disconnect the wiring harness.
    * *Step 3:* Remove the insulation.

### 6.3 Required files and resources
The following items are required for the implementation:

* **The AASX container file:** Contains the logical structure and all references.
* **Identification:** Unique ID.
* **Digital Product Passport (DPP):** Contains the legally required ESPR data (carbon footprint, recyclate content).
* **Bill of Materials (R-BOM):** The hierarchical list as well as properties for recycling all components.
* **TechnicalProperties:** Material data sheets per component, provided by the respective manufacturers and merged into the dishwasher's AAS.
* **CAD resources:** Dismantling drawings and 3D model for disassembly.

### 6.4 Technical implementation

#### 6.4.1 Implementation in the Asset Administration Shell (AAS)
The AAS serves as a data hub. All installed components have their properties stored by the respective manufacturers, and these are assembled into a dishwasher.

* **Material Identification:** Every component in the dishwasher receives a `Property` element with the material ID.
    * *Example:* The cladding elements receive the attribute `Material: V2A (Stainless Steel)`.
* **API Interface:** The AAS provides a REST API through which the recycling software makes queries (e.g., `GET /submodels/MaterialComposition/submodel-elements/CopperWeight`).

#### 6.4.2 Implementation in the CAD environment
The CAD environment serves as the central data source for creating the Asset Administration Shell (AAS). The process is structured as follows:

* **Provision of documents:** Dismantling drawings in PDF format are generated directly from the CAD system and made available to the AAS.
* **Material flow analysis:** An automated list is generated that records all components, including their volumes and materials. From this, the exact masses of the different raw materials can be derived. 
* **Target-actual comparison in the recycling process:** As part of the recycling process, this data is calculated for each dishwasher variant and stored in the AAS as target values.
* **Proof of obligation:** After dismantling, the recycler is obliged to enter the actually recovered masses of the different materials as actual values into the AAS.
* **Feedback loop to the manufacturer:** This data is fed back to the manufacturer. This gives the manufacturer seamless proof of the percentage to which the machine was sorted and dismantled.
* **Visualization:** Given high system complexity, an additional 3D model can be provided to the recycler.
* **Additional visualization:** The system calculates the recycling priority based on the stored material properties. Components containing pollutants are displayed flashing red.

### 6.5 Regulations and Legal Guidelines (Additional Requirements)

1.  **ESPR (Ecodesign for Sustainable Products Regulation)**
    * **Standard tools & dismantlability:** The existing Regulation (EU) 2019/2022 for dishwashers already stipulates that certain parts (such as pumps or motors) must be replaceable with "commonly available tools" and without causing permanent damage to the appliance.
    * **Dismantling time:** The new ESPR (Regulation (EU) 2024/1781) allows the EU to set explicit performance requirements in product-specific "delegated acts". For the revision of the dishwasher rules (planned from 2026), discussions are underway to include dismantling time as a metric for recyclability. [2], [3]
2.  **EU Battery Regulation (2023/1542)**
    * **Removability:** From February 18, 2027, portable batteries must be designed so that they can be easily removed and replaced by the end user or qualified personnel.
    * **Battery passport:** While the full "battery passport" primarily applies to industrial (>2 kWh) and traction batteries, information on chemical composition and safe removal for small batteries must be stored in the Digital Product Passport (DPP) of the main device (here, the dishwasher's AAS). [4]
3.  **WEEE Directive (Waste Electrical and Electronic Equipment)**
    * WEEE regulates the handling of electronic waste after use. 
    * **Collection and recovery targets:** For large appliances (Category 1), which include dishwashers, the directive prescribes a recovery target of 85% and a target for preparation for reuse and recycling of 80%. 
    * **Role of the AAS:** The AAS is the tool to guarantee "material hygiene". These high targets can only be achieved economically through single-origin separation (e.g., grade 1.4301 stainless steel instead of mixed scrap). [5]
4.  **Substances of Concern (REACH & SCIP)**
    * **Information obligation:** Since January 2021, manufacturers must submit information on Substances of Very High Concern (SVHC) to the ECHA SCIP database if the concentration exceeds 0.1%.
    * **AAS Integration:** The AAS serves as an interface to make this complex chemical data directly visualizable for Markus Mustermann at his workstation (e.g., warning label for bitumen mats or flame retardants in circuit boards), without him having to search manually in databases. [6], [7]

---