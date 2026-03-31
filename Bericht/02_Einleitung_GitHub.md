# 2 Introduction GitHub

# AAS-CAD Integration: Connection between Asset Administration Shell and CAD

Introductory document for our AAS-CAD Integration project. 

In this project, we are working on enabling the Asset Administration Shell (AAS) – the standardized digital twin – to communicate directly with our CAD systems. The goal is to enable bidirectional data exchange and to provide concrete code examples and workflows for this purpose.

## 2.1 What exactly is this about?

The current state of the art is: 3D models reside in CAD, and the digital twin lives completely isolated from it in its own software environment. However, if we want to implement use cases like intelligent recycling or seamless material tracking, these two worlds must talk to each other. This repository collects scripts and plug-ins to build exactly this bridge.

---
 <div style="page-break-after: always;"></div>

## 2.2 Core Features Overview

We focus on four fundamental functions to establish the interaction between AAS and CAD. In the table, you will find direct links to the respective explanations and implementations for Siemens NX and PTC Creo, as well as the current development status for Autodesk Fusion 360.

| # | Feature | Implementation in Siemens NX | Implementation in PTC Creo | Implementation in Autodesk Fusion 360 |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Import of 3D data from the AAS** <br>*(Loading the model from the digital twin into CAD)* | [NX Part Loader](03_AAS_to_NX_Part_import.md) | [Creo Doc](CREO_DATEINAME.md) | 🚧 Work in Progress |
| **2** | **Assignment of an Asset ID to a part** <br>*(The fundamental link between the 3D model and the AAS instance)* | [NX Asset-ID assign](04_NX_PartID_to_AAS.md) | [Creo Doc](CREO_DATEINAME.md) | 🚧 Work in Progress |
| **3** | **Synchronize properties** <br>*(Exchanging material data, metadata, etc.)* | [NX Sync Properties with AAS](05_NX_Sync_Properties_with_AAS.md) | [Creo Doc](CREO_DATEINAME.md) | 🚧 Work in Progress |
| **4** | **Data export from CAD** <br>*(currently as CSV)* | [NX to AAS Export](06_NX_to_AAS_Export.md) | [Creo Doc](CREO_DATEINAME.md) | 🚧 Work in Progress |

## 2.3 Detailed Description of the Features

How exactly these four functions work in detail and how they are solved on the system side can be found directly in the linked documents from the table above. There you will find detailed explanations and code examples for Siemens NX and PTC Creo.

---

## 2.4 Contributing
We always welcome support. If you want to contribute your own scripts, have a solution for another CAD system like SolidWorks, or find bugs, feel free to create a Pull Request.

## 2.5 License

The core project "Connecting CAD to Digital Twins" is licensed under the **Apache License 2.0**. Detailed information can be found in the [LICENSE.md](LICENSE.md) file.

> **Important note regarding Siemens NX (UI-Styler):** > This project contains UI code generated with the **Siemens NX 2021 UI-Styler** and manually adapted. To compile or run this code, proprietary NX Open libraries (DLLs) are required, which are **not** part of this repository. The rights to these libraries and to the basic framework of the generated code remain with Siemens AG. Please observe the corresponding license terms (EULA) of your Siemens NX installation.

Further legal notices are listed in the [NOTICE.md](NOTICE.md) file.