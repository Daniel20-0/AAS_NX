# -*- coding: utf-8 -*-
import NXOpen
import os

def main():

    theSession = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work

    wanted_attributes = [
        "MassPropVolume",
        "MassPropMass",
        "MassPropArea",
        "Material"
    ]

    filePath = workPart.FullPath.replace(".prt", "_selected_attributes.csv")

    # Dictionary vorbereiten
    values = {name: "" for name in wanted_attributes}

    # Alle Attribute durchgehen
    attrs = workPart.GetUserAttributes()

    for attr in attrs:

        title = attr.TitleAlias if attr.TitleAlias else attr.Title

        if title in wanted_attributes:

            if attr.Type == NXOpen.NXObject.AttributeType.Real:
                values[title] = attr.RealValue
            elif attr.Type == NXOpen.NXObject.AttributeType.String:
                values[title] = attr.StringValue
            elif attr.Type == NXOpen.NXObject.AttributeType.Integer:
                values[title] = attr.IntegerValue

    with open(filePath, "w") as f:

        # Kopfzeile
        header = "PartName;"
        for name in wanted_attributes:
            header += name + ";"
        f.write(header.rstrip(";") + "\n")

        # Werte
        row = workPart.Name + ";"
        for name in wanted_attributes:
            row += str(values[name]) + ";"

        f.write(row.rstrip(";") + "\n")

if __name__ == '__main__':
    main()