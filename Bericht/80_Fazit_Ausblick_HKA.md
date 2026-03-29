## 11 Conclusion and Outlook

### 11.1 Conclusion

This project has successfully built a functioning bridge between the standardized AAS and the CAD system Siemens NX. In doing so, it has shown that a direct, bidirectional connection between both worlds is essential. Data must flow seamlessly throughout the entire product lifecycle – whether it is generated in CAD and transferred to the AAS, or vice versa. A clear practical example of this is the automated calculation of the material weights of an assembly in CAD, which are then made directly available for processes in the AAS.

However, there were some hurdles to overcome at the beginning of the project. One challenge was the licensing model of Siemens NX: the "NX Open" functions, which are absolutely necessary for interface programming, are missing in the free student version.

Nevertheless, we were able to successfully implement the essential tools for automated data exchange within the scope of the project:

* **Import of 3D data from the AAS:** A tool specifically extracts STEP models from AASX containers, converts them into native NX PRT files, and automatically inserts them into NX, including the option for positioning.
* **Assignment of an Asset ID to a part ("addPartID"):** Using an integrated user interface, designers can assign a unique Asset ID (`PART_ID`) to their models directly in NX. This linking of the 3D model with its AAS instance is a fundamental prerequisite for Industry 4.0.
* **Synchronize properties & Data export from CAD:** A Python script automatically reads physical properties (volume, mass, material) from NX and exports them as a CSV file – the ideal basis for recycling bills of materials (R-BOMs).
* **Seamless UI integration:** All developed functions were integrated as buttons directly into the NX menu bar (ribbon). They do not disrupt the normal design workflow and are highly intuitive to use.


### 11.2 Outlook

The created interfaces form a solid foundation. To completely close the data loop, the following further developments are recommended for future projects:

* **Web-based search function:** The goal is to use an Asset ID in the browser to directly download the appropriate AASX file, automatically find the contained CAD model, and seamlessly open it in NX.
* **Direct AASX export:** The current workaround using CSV files should be eliminated. In the future, material and geometry data from the CAD system should be written directly into the standardized AASX format so that it can be used in the AAS without intermediate steps.

Once this bidirectional workflow is fully established in Siemens NX, our methodology can serve as a blueprint. The concepts developed here can then be easily transferred to other CAD systems to achieve true, cross-system interoperability.