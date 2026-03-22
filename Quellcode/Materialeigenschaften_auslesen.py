# -*- coding: utf-8 -*-
import NXOpen
import os

def update_mass_properties(workPart):
    """Aktualisiert die Masseeigenschaften mit dem modernen MassCalculationBuilder (NX 1980+)."""
    theSession = NXOpen.Session.GetSession()
    
    # 1. Alle Körper im Part sammeln
    all_bodies = [body for body in workPart.Bodies]
    
    if not all_bodies:
        return # Nichts zu berechnen

    # 2. Den Builder erstellen (entspricht CreateCalculationBuilder in C#)
    # Wir übergeben die Liste der Körper
    mass_builder = workPart.PropertiesManager.MassCollection.CreateCalculationBuilder(all_bodies)
    
    try:
        # 3. Die Berechnung ausführen (Commit)
        mass_builder.Commit()
        
    finally:
        # 4. Den Builder zerstören (entspricht Destroy in C#)
        mass_builder.Destroy()

def main():
    theSession = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    
    if workPart is None:
        return

    # --- NEU: Vor dem Auslesen die Masse-Werte aktualisieren ---
    update_mass_properties(workPart)
    # -----------------------------------------------------------

    wanted_attributes = [
        "MassPropVolume",
        "MassPropMass",
        "MassPropArea",
        "Material"
    ]

    # Dynamischer Pfad (wie besprochen)
    filePath = workPart.FullPath.replace(".prt", "_selected_attributes.csv")

    values = {name: "N/A" for name in wanted_attributes}
    
    # Attribute abrufen (NX schreibt die Masse-Werte als Objekt-Attribute)
    for attr in workPart.GetUserAttributes():
        title = attr.TitleAlias if attr.TitleAlias else attr.Title
        
        if title in wanted_attributes:
            if attr.Type == NXOpen.NXObject.AttributeType.Real:
                values[title] = attr.RealValue
            elif attr.Type == NXOpen.NXObject.AttributeType.String:
                values[title] = attr.StringValue
            elif attr.Type == NXOpen.NXObject.AttributeType.Integer:
                values[title] = attr.IntegerValue

    # CSV Schreiben
    with open(filePath, "w") as f:
        # Header
        f.write("PartName;" + ";".join(wanted_attributes) + "\n")
        
        # Values
        row = [workPart.Leaf] # Nutzt den Dateinamen ohne Pfad
        for name in wanted_attributes:
            row.append(str(values[name]))
        
        f.write(";".join(row) + "\n")

if __name__ == '__main__':
    main()