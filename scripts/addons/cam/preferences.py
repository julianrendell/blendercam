"""Fabex 'preferences.py'

Class to store all Addon preferences.
"""

from bpy.props import (
    BoolProperty,
    EnumProperty,
    IntProperty,
    StringProperty,
)
from bpy.types import (
    AddonPreferences,
)


class CamAddonPreferences(AddonPreferences):
    # this must match the addon name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __package__

    op_preset_update: BoolProperty(
        name="Have the Operation Presets Been Updated",
        default=False,
    )

    experimental: BoolProperty(
        name="Show Experimental Features",
        default=False,
    )

    default_interface_level: EnumProperty(
        name="Interface Level in New File",
        description="Choose visible options",
        items=[
            ("0", "Basic", "Only show Essential Options"),
            ("1", "Advanced", "Show Advanced Options"),
            ("2", "Complete", "Show All Options"),
            ("3", "Experimental", "Show Experimental Options"),
        ],
        default="3",
    )

    default_machine_preset: StringProperty(
        name="Machine Preset in New File",
        description="So that machine preset choice persists between files",
        default="",
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Use Experimental Features when you want to help development of Fabex:")
        layout.prop(self, "experimental")
