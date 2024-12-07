import bpy

from .globals import *
from .color_functions import *


# PCOY CLASSES

# 2000-2009

class PMS2000(bpy.types.Operator):
    """Pantone 15-4020"""
    bl_label = "Cerulean Blue"
    bl_idname = 'color.pms_2000'
    def execute(self, context):
        set_base_color(0x9BB7D4, self.bl_label)
        return {'FINISHED'}

class PMS2001(bpy.types.Operator):
    """Pantone 17-2031"""
    bl_label = "Fuschia Rose"
    bl_idname = 'color.pms_2001'
    def execute(self, context):
        set_base_color(0xC74375, self.bl_label)
        return {'FINISHED'}

class PMS2002(bpy.types.Operator):
    """Pantone 19-1664"""
    bl_label = "True Red"
    bl_idname = 'color.pms_2002'
    def execute(self, context):
        set_base_color(0xBF1932, self.bl_label)
        return {'FINISHED'}

class PMS2003(bpy.types.Operator):
    """Pantone 14-4811"""
    bl_label = "Aqua Sky"
    bl_idname = 'color.pms_2003'
    def execute(self, context):
        set_base_color(0x7BC4C4, self.bl_label)
        return {'FINISHED'}

class PMS2004(bpy.types.Operator):
    """Pantone 17-1456"""
    bl_label = "Tigerlily"
    bl_idname = 'color.pms_2004'
    def execute(self, context):
        set_base_color(0xE2583E, self.bl_label)
        return {'FINISHED'}

class PMS2005(bpy.types.Operator):
    """Pantone 15-5217"""
    bl_label = "Blue Turquoise"
    bl_idname = 'color.pms_2005'
    def execute(self, context):
        set_base_color(0x53B0AE, self.bl_label)
        return {'FINISHED'}

class PMS2006(bpy.types.Operator):
    """Pantone 13-1106"""
    bl_label = "Sand Dollar"
    bl_idname = 'color.pms_2006'
    def execute(self, context):
        set_base_color(0xDECDBE, self.bl_label)
        return {'FINISHED'}

class PMS2007(bpy.types.Operator):
    """Pantone 19-1557"""
    bl_label = "Chili Pepper"
    bl_idname = 'color.pms_2007'
    def execute(self, context):
        set_base_color(0x9B1B30, self.bl_label)
        return {'FINISHED'}

class PMS2008(bpy.types.Operator):
    """Pantone 18-3943"""
    bl_label = "Blue Iris"
    bl_idname = 'color.pms_2008'
    def execute(self, context):
        set_base_color(0x5A5B9F, self.bl_label)
        return {'FINISHED'}

class PMS2009(bpy.types.Operator):
    """Pantone 14-0848"""
    bl_label = "Mimosa"
    bl_idname = 'color.pms_2009'
    def execute(self, context):
        set_base_color(0xF0C05A, self.bl_label)
        return {'FINISHED'}

# 2010-2019

class PMS2010(bpy.types.Operator):
    """Pantone 15-5519"""
    bl_label = "Turquoise"
    bl_idname = 'color.pms_2010'
    def execute(self, context):
        set_base_color(0x45B5AA, self.bl_label)
        return {'FINISHED'}

class PMS2011(bpy.types.Operator):
    """Pantone 18-2120"""
    bl_label = "Honeysuckle"
    bl_idname = 'color.pms_2011'
    def execute(self, context):
        set_base_color(0xD94F70, self.bl_label)
        return {'FINISHED'}

class PMS2012(bpy.types.Operator):
    """Pantone 17-1463"""
    bl_label = "Tangerine"
    bl_idname = 'color.pms_2012'
    def execute(self, context):
        set_base_color(0xDD4124, self.bl_label)
        return {'FINISHED'}

class PMS2013(bpy.types.Operator):
    """Pantone 17-5641"""
    bl_label = "Emerald"
    bl_idname = 'color.pms_2013'
    def execute(self, context):
        set_base_color(0x009473, self.bl_label)
        return {'FINISHED'}

class PMS2014(bpy.types.Operator):
    """Pantone 18-3224"""
    bl_label = "Radiant Orchid"
    bl_idname = 'color.pms_2014'
    def execute(self, context):
        set_base_color(0xB163A3, self.bl_label)
        return {'FINISHED'}

class PMS2015(bpy.types.Operator):
    """Pantone 18-1438"""
    bl_label = "Marsala"
    bl_idname = 'color.pms_2015'
    def execute(self, context):
        set_base_color(0x955251, self.bl_label)
        return {'FINISHED'}

class PMS2016A(bpy.types.Operator):
    """Pantone 13-1520"""
    bl_label = "Rose Quartz"
    bl_idname = 'color.pms_2016_a'
    def execute(self, context):
        set_base_color(0xF7CAC9, self.bl_label)
        return {'FINISHED'}

class PMS2016B(bpy.types.Operator):
    """Pantone 15-3919"""
    bl_label = "Serenity"
    bl_idname = 'color.pms_2016_b'
    def execute(self, context):
        set_base_color(0x92A8D1, self.bl_label)
        return {'FINISHED'}

class PMS2017(bpy.types.Operator):
    """Pantone 15-0343"""
    bl_label = "Greenery"
    bl_idname = 'color.pms_2017'
    def execute(self, context):
        set_base_color(0x88B04B, self.bl_label)
        return {'FINISHED'}

class PMS2018(bpy.types.Operator):
    """Pantone 18-3838"""
    bl_label = "Ultra Violet"
    bl_idname = 'color.pms_2018'
    def execute(self, context):
        set_base_color(0x5F4B8B, self.bl_label)
        return {'FINISHED'}

class PMS2019(bpy.types.Operator):
    """Pantone 16-1546 TCX"""
    bl_label = "Living Coral"
    bl_idname = 'color.pms_2019'
    def execute(self, context):
        set_base_color(0xFF6F61, self.bl_label)
        return {'FINISHED'}

# 2020-2029

class PMS2020(bpy.types.Operator):
    """Pantone 19-4052"""
    bl_label = "Classic Blue"
    bl_idname = 'color.pms_2020'
    def execute(self, context):
        set_base_color(0x0F4C81, self.bl_label)
        return {'FINISHED'}

class PMS2021A(bpy.types.Operator):
    """Pantone 17-5104"""
    bl_label = "Ultimate Gray"
    bl_idname = 'color.pms_2021_a'
    def execute(self, context):
        set_base_color(0x949597, self.bl_label)
        return {'FINISHED'}

class PMS2021B(bpy.types.Operator):
    """Pantone 13-0647"""
    bl_label = "Illuminating"
    bl_idname = 'color.pms_2021_b'
    def execute(self, context):
        set_base_color(0xF5DF4D, self.bl_label)
        return {'FINISHED'}

class PMS2022(bpy.types.Operator):
    """Pantone 17-3938"""
    bl_label = "Very Peri"
    bl_idname = 'color.pms_2022'
    def execute(self, context):
        set_base_color(0x6567aa, self.bl_label)
        return {'FINISHED'}

class PMS2023(bpy.types.Operator):
    """Pantone 18-1750"""
    bl_label = "Viva Magenta"
    bl_idname = 'color.pms_2023'
    def execute(self, context):
        set_base_color(0xBB2649, self.bl_label)
        return {'FINISHED'}

class PMS2024(bpy.types.Operator):
    """Pantone 13-1023"""
    bl_label = "Peach Fuzz"
    bl_idname = 'color.pms_2024'
    def execute(self, context):
        set_base_color(0xfebe98, self.bl_label)
        return {'FINISHED'}

class PMS2025(bpy.types.Operator):
    """Pantone 17-1230"""
    bl_label = "Mocha Mousse"
    bl_idname = 'color.pms_2025'
    def execute(self, context):
        set_base_color(0xA47764, self.bl_label)
        return {'FINISHED'}

# EXTRAS & APOCRYPHA

class PMSPrince(bpy.types.Operator):
    """Custom Color selected by Pantone"""
    bl_label = "Prince"
    bl_idname = 'color.pms_prince'
    def execute(self, context):
        set_base_color(0x493452, self.bl_label)
        return {'FINISHED'}

class PMSConan(bpy.types.Operator):
    """Custom Color selected by Pantone"""
    bl_label = "Team Coco"
    bl_idname = 'color.pms_conan'
    def execute(self, context):
        set_base_color(0xFE7A0B, self.bl_label)
        return {'FINISHED'}

class PMSBCoral(bpy.types.Operator):
    """Pantone P-115-1-U (Community reaction to 2019 Living Coral)"""
    bl_label = "Bleached Coral"
    bl_idname = 'color.pms_bcoral'
    def execute(self, context):
        set_base_color(0xF4F7FC, self.bl_label)
        return {'FINISHED'}

class PMSSDCoral(bpy.types.Operator):
    """(Community reaction to 2019 Living Coral)"""
    bl_label = "Dead Coral"
    bl_idname = 'color.pms_dcoral'
    def execute(self, context):
        set_base_color(0xA7997E, self.bl_label)
        return {'FINISHED'}

class PMSUnignorable(bpy.types.Operator):
    """Custom Color selected by Pantone"""
    bl_label = "UW Unignorable"
    bl_idname = 'color.pms_uwign'
    def execute(self, context):
        set_base_color(0xFC502E, self.bl_label)
        return {'FINISHED'}

class PMS383(bpy.types.Operator):
    """Pantone 383"""
    bl_label = "Nice Green"
    bl_idname = 'color.pms_383'
    def execute(self, context):
        set_base_color(0xD0DF68, self.bl_label)
        return {'FINISHED'}

class PMS448C(bpy.types.Operator):
    """Pantone 448 C"""
    bl_label = "Ugliest Color in the World"
    bl_idname = 'color.pms_448c'
    def execute(self, context):
        set_base_color(0x4A412A, self.bl_label)
        return {'FINISHED'}

class PMSFreedomBlue(bpy.types.Operator):
    """Pantone Freedom Blue for Ukraine"""
    bl_label = "Freedom Blue"
    bl_idname = 'color.pms_freedom_blue'
    def execute(self, context):
        set_base_color(0x005eb8, self.bl_label)
        return {'FINISHED'}

class PMSEnergizingYellow(bpy.types.Operator):
    """Pantone Energizing Yellow for Ukraine"""
    bl_label = "Energizing Yellow"
    bl_idname = 'color.pms_energizing_yellow'
    def execute(self, context):
        set_base_color(0xffd101, self.bl_label)
        return {'FINISHED'}

# SS2022 NY

class PMS12_4401(bpy.types.Operator):
    """Pantone 12_4401"""
    bl_label = "Spun Sugar"
    bl_idname = 'color.pms_12_4401'
    def execute(self, context):
        set_base_color(0xc0e3ee, self.bl_label)
        return {'FINISHED'}

class PMS13_1513(bpy.types.Operator):
    """Pantone 13_1513"""
    bl_label = "Gossamer Pink"
    bl_idname = 'color.pms_13_1513'
    def execute(self, context):
        set_base_color(0xfcd3ce, self.bl_label)
        return {'FINISHED'}

class PMS18_2042(bpy.types.Operator):
    """Pantone 18_2042"""
    bl_label = "Innuendo"
    bl_idname = 'color.pms_18_2042'
    def execute(self, context):
        set_base_color(0xd14b75, self.bl_label)
        return {'FINISHED'}

class PMS19_4151(bpy.types.Operator):
    """Pantone 19_4151"""
    bl_label = "Skydiver"
    bl_idname = 'color.pms_19_4151'
    def execute(self, context):
        set_base_color(0x006dab, self.bl_label)
        return {'FINISHED'}

class PMS14_0850(bpy.types.Operator):
    """Pantone 14_0850"""
    bl_label = "Daffodil"
    bl_idname = 'color.pms_14_0850'
    def execute(self, context):
        set_base_color(0xfeca60, self.bl_label)
        return {'FINISHED'}

class PMS16_4118(bpy.types.Operator):
    """Pantone 16_4118"""
    bl_label = "Glacier Lake"
    bl_idname = 'color.pms_16_4118'
    def execute(self, context):
        set_base_color(0x93b0c6, self.bl_label)
        return {'FINISHED'}

class PMS18_4728(bpy.types.Operator):
    """Pantone 18_4728"""
    bl_label = "Harbor Blue"
    bl_idname = 'color.pms_18_4728'
    def execute(self, context):
        set_base_color(0x007781, self.bl_label)
        return {'FINISHED'}

class PMS18_1019(bpy.types.Operator):
    """Pantone 18_1019"""
    bl_label = "Coca Mocha"
    bl_idname = 'color.pms_18_1019'
    def execute(self, context):
        set_base_color(0x987d6a, self.bl_label)
        return {'FINISHED'}

class PMS18_3324(bpy.types.Operator):
    """Pantone 18_3324"""
    bl_label = "Dahlia"
    bl_idname = 'color.pms_18_3324'
    def execute(self, context):
        set_base_color(0x985696, self.bl_label)
        return {'FINISHED'}

class PMS18_1564(bpy.types.Operator):
    """Pantone 18_1564"""
    bl_label = "Poinciana"
    bl_idname = 'color.pms_18_1564'
    def execute(self, context):
        set_base_color(0xd64a2c, self.bl_label)
        return {'FINISHED'}

# PMS SS2022 LONDON

class PMS14_5713(bpy.types.Operator):
    """Pantone 14_5713"""
    bl_label = "Cascade"
    bl_idname = 'color.pms_14_5713'
    def execute(self, context):
        set_base_color(0x87cbbf, self.bl_label)
        return {'FINISHED'}

class PMS16_1349(bpy.types.Operator):
    """Pantone 16_1349"""
    bl_label = "Coral Rose"
    bl_idname = 'color.pms_16_1349'
    def execute(self, context):
        set_base_color(0xf78c5f, self.bl_label)
        return {'FINISHED'}

class PMS18_4143(bpy.types.Operator):
    """Pantone 18_4143"""
    bl_label = "Super Sonic"
    bl_idname = 'color.pms_18_4143'
    def execute(self, context):
        set_base_color(0x3c88c4, self.bl_label)
        return {'FINISHED'}

class PMS12_0825(bpy.types.Operator):
    """Pantone 12_0825"""
    bl_label = "Popcorn"
    bl_idname = 'color.pms_12_0825'
    def execute(self, context):
        set_base_color(0xfae39e, self.bl_label)
        return {'FINISHED'}

class PMS13_2004(bpy.types.Operator):
    """Pantone 13_2004"""
    bl_label = "Potpourri"
    bl_idname = 'color.pms_13_2004'
    def execute(self, context):
        set_base_color(0xecd4d4, self.bl_label)
        return {'FINISHED'}

class PMS17_1928(bpy.types.Operator):
    """Pantone 17_1928"""
    bl_label = "Bubblegum"
    bl_idname = 'color.pms_17_1928'
    def execute(self, context):
        set_base_color(0xef8a9e, self.bl_label)
        return {'FINISHED'}

class PMS18_1160(bpy.types.Operator):
    """Pantone 18_1160"""
    bl_label = "Sudan Brown"
    bl_idname = 'color.pms_18_1160'
    def execute(self, context):
        set_base_color(0xbb7f35, self.bl_label)
        return {'FINISHED'}

class PMS15_0549(bpy.types.Operator):
    """Pantone 15_0549"""
    bl_label = "Fragile Sprou"
    bl_idname = 'color.pms_15_0549'
    def execute(self, context):
        set_base_color(0xc5c637, self.bl_label)
        return {'FINISHED'}

class PMS14_3612(bpy.types.Operator):
    """Pantone 14_3612"""
    bl_label = "Orchid Bloom"
    bl_idname = 'color.pms_14_3612'
    def execute(self, context):
        set_base_color(0xd0bdd8, self.bl_label)
        return {'FINISHED'}

class PMS18_1307(bpy.types.Operator):
    """Pantone 18_1307"""
    bl_label = "Coffee Quartz"
    bl_idname = 'color.pms_18_1307'
    def execute(self, context):
        set_base_color(0x7d6963, self.bl_label)
        return {'FINISHED'}


# PCOY PANEL
class PMSPanel(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel"
    bl_label = "Pantone Color of the Year"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'QMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout


# 2000-09 PANEL
class PMSPanel2000(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_2000"
    bl_label = "    2000-09"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'PMS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 0.5
        scol.label(text="2000")
        scol.label(text="2001")
        scol.label(text="2002")
        scol.label(text="2003")
        scol.label(text="2004")
        scol.label(text="2005")
        scol.label(text="2006")
        scol.label(text="2007")
        scol.label(text="2008")
        scol.label(text="2009")

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["pcoy_2000"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2001"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2002"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2003"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2004"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2005"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2006"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2007"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2008"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2009"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 2.0
        scol.operator("color.pms_2000", text="Cerulean Blue")
        scol.operator("color.pms_2001", text="Fuschia Rose")
        scol.operator("color.pms_2002", text="True Red")
        scol.operator("color.pms_2003", text="Aqua Sky")
        scol.operator("color.pms_2004", text="Tigerlily")
        scol.operator("color.pms_2005", text="Blue Turquoise")
        scol.operator("color.pms_2006", text="Sand Dollar")
        scol.operator("color.pms_2007", text="Chili Pepper")
        scol.operator("color.pms_2008", text="Blue Iris")
        scol.operator("color.pms_2009", text="Mimosa")


# 2010-19 PANEL
class PMSPanel2010(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_2010"
    bl_label = "    2010-19"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'PMS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 0.5
        scol.label(text="2010")
        scol.label(text="2011")
        scol.label(text="2012")
        scol.label(text="2013")
        scol.label(text="2014")
        scol.label(text="2015")
        scol.label(text="2016")
        scol.label(text="2016")
        scol.label(text="2017")
        scol.label(text="2018")
        scol.label(text="2019")

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["pcoy_2010"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2011"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2012"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2013"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2014"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2015"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2016a"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2016b"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2017"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2018"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2019"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 2.0
        scol.operator("color.pms_2010", text="Turquoise")
        scol.operator("color.pms_2011", text="Honeysuckle")
        scol.operator("color.pms_2012", text="Tangerine")
        scol.operator("color.pms_2013", text="Emerald")
        scol.operator("color.pms_2014", text="Radiant Orchid")
        scol.operator("color.pms_2015", text="Marsala")
        scol.operator("color.pms_2016_a", text="Rose Quartz")
        scol.operator("color.pms_2016_b", text="Serenity")
        scol.operator("color.pms_2017", text="Greenery")
        scol.operator("color.pms_2018", text="Ultra Violet")
        scol.operator("color.pms_2019", text="Living Coral")


# 2020+ PANEL
class PMSPanel2020(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_2020"
    bl_label = "    2020-29"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'PMS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 0.5
        scol.label(text="2020")
        scol.label(text="2021")
        scol.label(text="2021")
        scol.label(text="2022")
        scol.label(text="2023")
        scol.label(text="2024")
        scol.label(text="2025")

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["pcoy_2020"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2021a"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2021b"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2022"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2023"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2024"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2025"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 2.0
        scol.operator("color.pms_2020", text="Classic Blue")
        scol.operator("color.pms_2021_a", text="Ultimate Gray")
        scol.operator("color.pms_2021_b", text="Illuminating")
        scol.operator("color.pms_2022", text="Very Peri")
        scol.operator("color.pms_2023", text="Viva Magenta")
        scol.operator("color.pms_2024", text="Peach Fuzz")
        scol.operator("color.pms_2025", text="Mocha Mousse")


# SS2022 NY PANEL
class PMSPanelSS2022London(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_SS2022London"
    bl_label = "    SS2022 London"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'PMS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["pms_14_5713"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_16_1349"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_18_4143"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_12_0825"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_13_2004"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_17_1928"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_18_1160"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_15_0549"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_14_3612"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_18_1307"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.pms_14_5713", text="Cascade")
        scol.operator("color.pms_16_1349", text="Coral Rose")
        scol.operator("color.pms_18_4143", text="Super Sonic")
        scol.operator("color.pms_12_0825", text="Popcorn")
        scol.operator("color.pms_13_2004", text="Potpourri")
        scol.operator("color.pms_17_1928", text="Bubblegum")
        scol.operator("color.pms_18_1160", text="Sudan Brown")
        scol.operator("color.pms_15_0549", text="Fragile Sprou")
        scol.operator("color.pms_14_3612", text="Orchid Bloom")
        scol.operator("color.pms_18_1307", text="Coffee Quartz")


# SS2022 NY PANEL
class PMSPanelSS2022NY(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_SS2022NY"
    bl_label = "    SS2022 New York"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'PMS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["pms_12_4401"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_13_1513"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_18_2042"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_19_4151"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_14_0850"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_16_4118"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_18_4728"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_18_1019"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_18_3324"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_18_1564"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.pms_12_4401", text="Spun Sugar")
        scol.operator("color.pms_13_1513", text="Gossamer Pink")
        scol.operator("color.pms_18_2042", text="Innuendo")
        scol.operator("color.pms_19_4151", text="Skydiver")
        scol.operator("color.pms_14_0850", text="Daffodil")
        scol.operator("color.pms_16_4118", text="Glacier Lake")
        scol.operator("color.pms_18_4728", text="Harbor Blue")
        scol.operator("color.pms_18_1019", text="Coca Mocha")
        scol.operator("color.pms_18_3324", text="Dahlia")
        scol.operator("color.pms_18_1564", text="Poinciana")


# Extras & Apocrypha PANEL
class PMSPanelExtras(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_Extras"
    bl_label = "    Extras & Apocrypha"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'PMS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["pcoy_2020b"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2043"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_prince"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_conan"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_uw"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_383"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_448"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_freedom_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_energizing_yellow"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.pms_bcoral", text="2020 Bleached Coral")
        scol.operator("color.pms_dcoral", text="2043 Dead Coral")
        scol.operator("color.pms_prince", text="Prince")
        scol.operator("color.pms_conan", text="Team Coco Orange")
        scol.operator("color.pms_uwign", text="United Way Unignorable")
        scol.operator("color.pms_383", text="A Nice Green")
        scol.operator("color.pms_448c", text="Ugliest Color in the World (Official)")
        scol.operator("color.pms_freedom_blue", text="Freedom Blue")
        scol.operator("color.pms_energizing_yellow", text="Energizing Yellow")


array_pcoy = [
    PMSPanel,
    PMSPanel2000,
    PMSPanel2010,
    PMSPanel2020,
    PMSPanelSS2022London,
    PMSPanelSS2022NY,
    PMSPanelExtras,
    PMS2000,
    PMS2001,
    PMS2002,
    PMS2003,
    PMS2004,
    PMS2005,
    PMS2006,
    PMS2007,
    PMS2008,
    PMS2009,
    PMS2010,
    PMS2011,
    PMS2012,
    PMS2013,
    PMS2014,
    PMS2015,
    PMS2016A,
    PMS2016B,
    PMS2017,
    PMS2018,
    PMS2019,
    PMS2020,
    PMS2021A,
    PMS2021B,
    PMS2022,
    PMS2023,
    PMS2024,
    PMS2025,
    PMSPrince,
    PMSConan,
    PMSBCoral,
    PMSSDCoral,
    PMSUnignorable,
    PMS383,
    PMS448C,
    PMSFreedomBlue,
    PMSEnergizingYellow,
    PMS12_4401,
    PMS13_1513,
    PMS18_2042,
    PMS19_4151,
    PMS14_0850,
    PMS16_4118,
    PMS18_4728,
    PMS18_1019,
    PMS18_3324,
    PMS18_1564,
    PMS14_5713,
    PMS16_1349,
    PMS18_4143,
    PMS12_0825,
    PMS13_2004,
    PMS17_1928,
    PMS18_1160,
    PMS15_0549,
    PMS14_3612,
    PMS18_1307,
]
