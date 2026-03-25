# -*- coding: utf-8 -*-
import NXOpen
import NXOpen.Assemblies
import os
import csv

def update_mass_properties(part):
    """Aktualisiert die Masseeigenschaften eines Parts robust."""
    if part is None:
        return

    solid_bodies = [body for body in part.Bodies if body.IsSolidBody]

    if not solid_bodies:
        return

    theSession = NXOpen.Session.GetSession()

    mark_id = theSession.SetUndoMark(
        NXOpen.Session.MarkVisibility.Invisible,
        "Update Mass Properties"
    )

    mass_builder = part.PropertiesManager.MassCollection.CreateCalculationBuilder(solid_bodies)

    try:
        mass_builder.Commit()
        theSession.UpdateManager.DoUpdate(mark_id)
    finally:
        mass_builder.Destroy()


def nx_attr_to_python_value(attr):
    """Wandelt ein NX-Attribut robust in einen Python-String/Wert um."""
    try:
        if attr.Type == NXOpen.NXObject.AttributeType.String:
            return attr.StringValue
        elif attr.Type == NXOpen.NXObject.AttributeType.Integer:
            return attr.IntegerValue
        elif attr.Type == NXOpen.NXObject.AttributeType.Real:
            return attr.RealValue
        elif attr.Type == NXOpen.NXObject.AttributeType.Boolean:
            return attr.BooleanValue
        else:
            return "N/A"
    except:
        return "N/A"


def get_all_user_attributes(nx_object):
    """Liest alle Benutzerattribute eines NX-Objekts in ein Dictionary."""
    values = {}

    if nx_object is None:
        return values

    try:
        for attr in nx_object.GetUserAttributes():
            title = attr.TitleAlias if attr.TitleAlias else attr.Title
            values[title] = nx_attr_to_python_value(attr)
    except:
        pass

    return values


def get_standard_attribute_values(part, wanted_attributes):
    """Liest Standardwerte: Masse direkt messen, Rest aus Attributen."""
    values = {name: "N/A" for name in wanted_attributes}

    # Massenwerte direkt berechnen statt als Attribute auszulesen
    mass_values = get_mass_values(part)
    for key, value in mass_values.items():
        if key in values:
            values[key] = value

    # Andere Standardattribute wie Material weiter normal auslesen
    for attr in part.GetUserAttributes():
        title = attr.TitleAlias if attr.TitleAlias else attr.Title

        if title in wanted_attributes and title not in ["MassPropVolume", "MassPropMass", "MassPropArea"]:
            values[title] = nx_attr_to_python_value(attr)

    return values


def get_leaf_components(component):
    """Liefert rekursiv alle Blatt-Komponenten."""
    children = component.GetChildren()

    if not children:
        return [component]

    result = []
    for child in children:
        result.extend(get_leaf_components(child))
    return result

def get_mass_values(part):
    """Liest Masse, Volumen und Fläche direkt per MeasureManager aus."""
    solid_bodies = [body for body in part.Bodies if body.IsSolidBody]

    result = {
        "MassPropVolume": "N/A",
        "MassPropMass": "N/A",
        "MassPropArea": "N/A"
    }

    if not solid_bodies:
        return result

    unit_collection = part.UnitCollection

    area_unit = unit_collection.GetBase("Area")
    volume_unit = unit_collection.GetBase("Volume")
    mass_unit = unit_collection.GetBase("Mass")
    length_unit = unit_collection.GetBase("Length")
    weight_unit = unit_collection.GetBase("Force")

    mass_units = [area_unit, volume_unit, mass_unit, length_unit, weight_unit]

    measure_bodies = None
    try:
        measure_bodies = part.MeasureManager.NewMassProperties(mass_units, 0.99, solid_bodies)

        result["MassPropArea"] = measure_bodies.Area
        result["MassPropVolume"] = measure_bodies.Volume
        result["MassPropMass"] = measure_bodies.Mass
    finally:
        if measure_bodies is not None:
            measure_bodies.Dispose()

    return result

def get_component_part(component):
    """Ermittelt das Part-Objekt einer Komponente robust."""
    proto = component.Prototype

    if isinstance(proto, NXOpen.Part):
        return proto

    try:
        return proto.OwningPart
    except:
        return None


def main():
    theSession = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work

    if workPart is None:
        return

    wanted_attributes = [
        "MassPropVolume",
        "MassPropMass",
        "MassPropArea",
        "Material"
    ]

    script_dir = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(script_dir, workPart.Leaf + "_selected_attributes.csv")

    rows = []
    custom_attribute_names = set()

    root_component = workPart.ComponentAssembly.RootComponent

    if root_component is None:
        # Einzelteil
        update_mass_properties(workPart)

        standard_values = get_standard_attribute_values(workPart, wanted_attributes)
        all_attrs = get_all_user_attributes(workPart)

        # Standardattribute aus benutzerdefiniertem Satz entfernen,
        # damit sie nicht doppelt in der CSV auftauchen
        for name in wanted_attributes:
            if name in all_attrs:
                del all_attrs[name]

        custom_attribute_names.update(all_attrs.keys())

        row_data = {
            "Komponente": workPart.Leaf
        }

        for name in wanted_attributes:
            row_data[name] = standard_values[name]

        for name, value in all_attrs.items():
            row_data[name] = value

        rows.append(row_data)

    else:
        # Baugruppe: jede Blatt-Komponente als eigene Zeile
        leaf_components = get_leaf_components(root_component)

        for comp in leaf_components:
            comp_part = get_component_part(comp)

            if comp_part is None:
                continue

            update_mass_properties(comp_part)

            # Standardattribute vom Part
            standard_values = get_standard_attribute_values(comp_part, wanted_attributes)

            # Alle Part-Attribute
            part_attrs = get_all_user_attributes(comp_part)

            # Alle Komponenten-Attribute (Instanzattribute)
            comp_attrs = get_all_user_attributes(comp)

            # Standardattribute aus Part-Attributen entfernen
            for name in wanted_attributes:
                if name in part_attrs:
                    del part_attrs[name]
                if name in comp_attrs:
                    del comp_attrs[name]

            # Zusammenführen:
            # erst Part-Attribute, dann Komponenten-Attribute überschreiben ggf. gleiche Namen
            merged_custom_attrs = {}
            merged_custom_attrs.update(part_attrs)
            merged_custom_attrs.update(comp_attrs)

            custom_attribute_names.update(merged_custom_attrs.keys())

            row_data = {
                "Komponente": comp.DisplayName
            }

            for name in wanted_attributes:
                row_data[name] = standard_values[name]

            for name, value in merged_custom_attrs.items():
                row_data[name] = value

            rows.append(row_data)

    # Sortierte benutzerdefinierte Attributnamen für sauberen CSV-Header
    custom_attribute_names = sorted(custom_attribute_names)

    with open(filePath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")

        header = ["Komponente"] + wanted_attributes + custom_attribute_names
        writer.writerow(header)

        for row_data in rows:
            row = []
            for col in header:
                row.append(str(row_data.get(col, "N/A")))
            writer.writerow(row)


if __name__ == '__main__':
    main()