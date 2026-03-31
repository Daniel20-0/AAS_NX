#==============================================================================
#   WARNING!!  This file is overwritten by the Block UI Styler while generating
#   the automation code. Any modifications to this file will be lost after
#   generating the code again.
#==============================================================================

import os
import NXOpen
import NXOpen.BlockStyler
import NXOpen.Assemblies

class Add_Attributes:
    theSession = None
    theUI = None

    # ------------------------------------------------------------------------------
    # Bit Option for Property: SnapPointTypesEnabled
    # ------------------------------------------------------------------------------
    SnapPointTypesEnabled_UserDefined = 1 << 0
    SnapPointTypesEnabled_Inferred = 1 << 1
    SnapPointTypesEnabled_ScreenPosition = 1 << 2
    SnapPointTypesEnabled_EndPoint = 1 << 3
    SnapPointTypesEnabled_MidPoint = 1 << 4
    SnapPointTypesEnabled_ControlPoint = 1 << 5
    SnapPointTypesEnabled_Intersection = 1 << 6
    SnapPointTypesEnabled_ArcCenter = 1 << 7
    SnapPointTypesEnabled_QuadrantPoint = 1 << 8
    SnapPointTypesEnabled_ExistingPoint = 1 << 9
    SnapPointTypesEnabled_PointonCurve = 1 << 10
    SnapPointTypesEnabled_PointonSurface = 1 << 11
    SnapPointTypesEnabled_PointConstructor = 1 << 12
    SnapPointTypesEnabled_TwocurveIntersection = 1 << 13
    SnapPointTypesEnabled_TangentPoint = 1 << 14
    SnapPointTypesEnabled_Poles = 1 << 15
    SnapPointTypesEnabled_BoundedGridPoint = 1 << 16
    SnapPointTypesEnabled_FacetVertexPoint = 1 << 17
    SnapPointTypesEnabled_DefiningPoint = 1 << 18

    # ------------------------------------------------------------------------------
    # Bit Option for Property: SnapPointTypesOnByDefault
    # ------------------------------------------------------------------------------
    SnapPointTypesOnByDefault_EndPoint = 1 << 3
    SnapPointTypesOnByDefault_MidPoint = 1 << 4
    SnapPointTypesOnByDefault_ControlPoint = 1 << 5
    SnapPointTypesOnByDefault_Intersection = 1 << 6
    SnapPointTypesOnByDefault_ArcCenter = 1 << 7
    SnapPointTypesOnByDefault_QuadrantPoint = 1 << 8
    SnapPointTypesOnByDefault_ExistingPoint = 1 << 9
    SnapPointTypesOnByDefault_PointonCurve = 1 << 10
    SnapPointTypesOnByDefault_PointonSurface = 1 << 11
    SnapPointTypesOnByDefault_PointConstructor = 1 << 12
    SnapPointTypesOnByDefault_BoundedGridPoint = 1 << 16
    SnapPointTypesOnByDefault_FacetVertexPoint = 1 << 17

    def __init__(self):
        try:
            self.theSession = NXOpen.Session.GetSession()
            self.theUI = NXOpen.UI.GetUI()

            script_dir = os.path.dirname(os.path.abspath(__file__))
            self.theDlxFileName = os.path.join(script_dir, "NX Add Attributes Tool.dlx")

            self.theDialog = self.theUI.CreateDialog(self.theDlxFileName)
            self.theDialog.AddApplyHandler(self.apply_cb)
            self.theDialog.AddOkHandler(self.ok_cb)
            self.theDialog.AddUpdateHandler(self.update_cb)
            self.theDialog.AddInitializeHandler(self.initialize_cb)
            self.theDialog.AddDialogShownHandler(self.dialogShown_cb)
        except Exception as ex:
            raise ex

    def Show(self):
        try:
            self.theDialog.Show()
        except Exception as ex:
            self.theUI.NXMessageBox.Show(
                "Block Styler",
                NXOpen.NXMessageBox.DialogType.Error,
                str(ex)
            )

    def Dispose(self):
        if self.theDialog is not None:
            self.theDialog.Dispose()
            self.theDialog = None

    def initialize_cb(self):
        try:
            self.selection0 = self.theDialog.TopBlock.FindBlock("selection0")
            self.string0 = self.theDialog.TopBlock.FindBlock("string0")
            self.string01 = self.theDialog.TopBlock.FindBlock("string01")
        except Exception as ex:
            self.theUI.NXMessageBox.Show(
                "Block Styler",
                NXOpen.NXMessageBox.DialogType.Error,
                str(ex)
            )

    def dialogShown_cb(self):
        try:
            pass
        except Exception as ex:
            self.theUI.NXMessageBox.Show(
                "Block Styler",
                NXOpen.NXMessageBox.DialogType.Error,
                str(ex)
            )

    def apply_cb(self):
        errorCode = 0
        props_selection = None
        props_name = None
        props_value = None

        try:
            props_selection = self.GetBlockProperties("selection0")
            props_name = self.GetBlockProperties("string0")
            props_value = self.GetBlockProperties("string01")

            attr_name = props_name.GetString("Value")
            attr_value = props_value.GetString("Value")

            if attr_name is None or attr_name.strip() == "":
                raise Exception("Der Attributname darf nicht leer sein.")

            selected_objects = props_selection.GetTaggedObjectVector("SelectedObjects")

            if selected_objects is None or len(selected_objects) == 0:
                raise Exception("Bitte ein Bauteil oder eine Komponente auswählen.")

            target_obj = selected_objects[0]

            # Write the attribute directly to the selected object
            target_obj.SetUserAttribute(
                attr_name,
                -1,
                attr_value,
                NXOpen.Update.Option.Now
            )

        except Exception as ex:
            errorCode = 1
            self.theUI.NXMessageBox.Show(
                "Block Styler",
                NXOpen.NXMessageBox.DialogType.Error,
                str(ex)
            )
        finally:
            if props_selection is not None:
                props_selection.Dispose()
            if props_name is not None:
                props_name.Dispose()
            if props_value is not None:
                props_value.Dispose()

        return errorCode

    def update_cb(self, block):
        try:
            if block == self.selection0:
                pass
            elif block == self.string0:
                pass
            elif block == self.string01:
                pass
        except Exception as ex:
            self.theUI.NXMessageBox.Show(
                "Block Styler",
                NXOpen.NXMessageBox.DialogType.Error,
                str(ex)
            )

        return 0

    def ok_cb(self):
        errorCode = 0
        try:
            errorCode = self.apply_cb()
        except Exception as ex:
            errorCode = 1
            self.theUI.NXMessageBox.Show(
                "Block Styler",
                NXOpen.NXMessageBox.DialogType.Error,
                str(ex)
            )

        return errorCode

    def GetBlockProperties(self, blockID):
        try:
            return self.theDialog.GetBlockProperties(blockID)
        except Exception as ex:
            self.theUI.NXMessageBox.Show(
                "Block Styler",
                NXOpen.NXMessageBox.DialogType.Error,
                str(ex)
            )

        return None


def main():
    theAdd_Attributes = None
    try:
        theAdd_Attributes = Add_Attributes()
        theAdd_Attributes.Show()
    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show(
            "Block Styler",
            NXOpen.NXMessageBox.DialogType.Error,
            str(ex)
        )
    finally:
        if theAdd_Attributes is not None:
            theAdd_Attributes.Dispose()
            theAdd_Attributes = None


if __name__ == '__main__':
    main()