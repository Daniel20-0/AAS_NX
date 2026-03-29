# Prerequisites

Before setup, make sure to download the required scripts from this repository.

For the successful setup and execution of the integration between Siemens NX and the AAS, the following system requirements must be met:

### Software & Licenses
- **Siemens NX:** Local installation (e.g., version 2021).
- **NX License:** Enterprise or NX Open license for executing and compiling scripts and external programs.
- **AASX Package Explorer:** Tool for viewing and validating the AAS.
### Development Environment & Languages
- **Python:** Standalone installation (version 3.11 or higher) for adapters, because the Python version in NX 2021 is only version 3.8 and does not include the lxml library.
- **IDE:** Visual Studio (e.g., for C#) or Visual Studio Code (for Python) to customize the scripts.

### System Rights & Configuration
- **Administrator Rights:** Local Windows admin rights (for installations via `pip` and setting environment variables).
- **NX Role:** An advanced user role (e.g., "Advanced") to unlock the developer tab in the NX user interface.