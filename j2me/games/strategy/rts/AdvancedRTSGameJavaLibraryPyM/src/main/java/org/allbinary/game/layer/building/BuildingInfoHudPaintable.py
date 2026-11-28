# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
#  
# By agreeing to this license you and any business entity you represent are 
# legally bound to the AllBinary Open License Version 1 legal agreement. 
#  
# You may obtain the AllBinary Open License Version 1 legal agreement from 
# AllBinary or the root directory of AllBinary's AllBinary Platform repository. 
#  
# Created By: Travis Berthelot 
#   
# Generated Code Do Not Modify
# package org.allbinary.game.layer.building

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_divide
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.ag.layer.hud.basic.NumberStringHud import NumberStringHud
from org.allbinary.game.layer.SelectionHudPaintable import SelectionHudPaintable


@java_inherited_overloads
class BuildingInfoHudPaintable(SelectionHudPaintable):
    instance: BuildingInfoHudPaintable = None
    @java_inherited_overloads
    class BuildingNumberHud(NumberStringHud):
        def _java_defaults(self):
            vars(self).setdefault("baseTextX", 0)
            vars(self).setdefault("baseY", 0)
            vars(self).setdefault("row", 0)
            vars(self).setdefault("prefixLength", 0)
            vars(self).setdefault("positionBeforeMeasurement", False)

        def _init_fields(self) -> None:
            if "baseTextX" not in vars(self): self.baseTextX: int = 0
            if "baseY" not in vars(self): self.baseY: int = 0
            if "row" not in vars(self): self.row: int = 0
            if "prefixLength" not in vars(self): self.prefixLength: int = 0
            if "positionBeforeMeasurement" not in vars(self): self.positionBeforeMeasurement: bool = False
        

        def __init__(self, label: str, maximum: int, basicHudFactory: BasicHudFactory, basicColor: BasicColor, baseTextX: int, baseY: int, row: int, prefixLength: int, positionBeforeMeasurement: bool) -> None:
            __class__._java_defaults(self)
            from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
            from org.allbinary.graphics.color.BasicColor import BasicColor
            super().__init__(label, maximum, basicHudFactory.ABSOLUTE, basicHudFactory.HORIZONTAL, 0, basicColor)
            __class__._init_fields(self)
            self.baseTextX = baseTextX
            self.baseY = baseY
            self.row = row
            self.prefixLength = prefixLength
            self.positionBeforeMeasurement = positionBeforeMeasurement
        

        def updateMeasurement(self, graphics: Graphics) -> None:
            from javax.microedition.lcdui.Font import Font
            from javax.microedition.lcdui.Graphics import Graphics
            if not (self.positionBeforeMeasurement):
                java_super_call(super(), "updateMeasurement", graphics)
            font: Font = graphics.getFont()
            self.updateMaxWidth = self.baseTextX + self.prefixLength * font.getHeight()
            self.updateMaxHeight = self.baseY + self.row * font.getHeight()
            if self.positionBeforeMeasurement:
                java_super_call(super(), "updateMeasurement", graphics)
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("HEALTH", None)
        vars(self).setdefault("productivityHud", None)
        vars(self).setdefault("efficiencyHud", None)
        vars(self).setdefault("healthHud", None)
        vars(self).setdefault("maxHealthHud", None)
        vars(self).setdefault("rtsLayer", None)
        vars(self).setdefault("currentHealth", 0)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.HEALTH: str = "Health:"
        if "productivityHud" not in vars(self): self.productivityHud: NumberStringHud = None
        if "efficiencyHud" not in vars(self): self.efficiencyHud: NumberStringHud = None
        if "healthHud" not in vars(self): self.healthHud: NumberStringHud = None
        if "maxHealthHud" not in vars(self): self.maxHealthHud: NumberStringHud = None
        self.rtsLayer: PathFindingLayerInterface = NullPathFindingLayer.NULL_PATH_FINDING_LAYER
        self.currentHealth: int = 0
    

    @staticmethod
    def getInstance() -> BuildingInfoHudPaintable:
        return BuildingInfoHudPaintable.instance
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.ag.layer.hud.basic.NumberStringHudFactory import NumberStringHudFactory
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__()
        __class__._init_fields(self)
        numberStringHudFactory: NumberStringHudFactory = NumberStringHudFactory.getInstance()
        productivityHud: NumberStringHud = numberStringHudFactory.NULL_NUMBER_STRING_HUD
        efficiencyHud: NumberStringHud = numberStringHudFactory.NULL_NUMBER_STRING_HUD
        healthHud: NumberStringHud = numberStringHudFactory.NULL_NUMBER_STRING_HUD
        maxHealthHud: NumberStringHud = numberStringHudFactory.NULL_NUMBER_STRING_HUD
        try:
            basicHudFactory: BasicHudFactory = BasicHudFactory.getInstance()
            basicColor: BasicColor = self.getBasicColorP()
            textX: int = self.textX
            y: int = self.y
            productivityHud = BuildingInfoHudPaintable.BuildingNumberHud("Productivity:", 999, basicHudFactory, basicColor, textX, y, 1, 0, True)
            efficiencyHud = BuildingInfoHudPaintable.BuildingNumberHud("Efficiency:", 999, basicHudFactory, basicColor, textX, y, 2, 0, False)
            healthHud = BuildingInfoHudPaintable.BuildingNumberHud(self.HEALTH, 99999, basicHudFactory, basicColor, textX, y, 3, 0, True)
            maxHealthHud = BuildingInfoHudPaintable.BuildingNumberHud("/ ", 99999, basicHudFactory, basicColor, textX, y, 3, len(self.HEALTH) + 1, False)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.CONSTRUCTOR, e)
        self.productivityHud = productivityHud
        self.efficiencyHud = efficiencyHud
        self.healthHud = healthHud
        self.maxHealthHud = maxHealthHud
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
        from org.allbinary.logic.math.MathUtil import MathUtil
        font: Font = graphics.getFont()
        totalLength: int = len(self.HEALTH) + MathUtil.getInstance().getTotalDigits(self.currentHealth)
        self.maxHealthHud.setX(self.textX + MyFontProcessor.defaultStringWidth(font, totalLength))
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        java_super_call(super(), "setBasicColorP", basicColor)
        self.productivityHud.setBasicColorP(basicColor)
        self.efficiencyHud.setBasicColorP(basicColor)
        self.healthHud.setBasicColorP(basicColor)
        self.maxHealthHud.setBasicColorP(basicColor)
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        java_super_call(super(), "paint", graphics)
        self.myFontProcessor.process(graphics)
        self.productivityHud.paint(graphics)
        self.efficiencyHud.paint(graphics)
        self.healthHud.paint(graphics)
        self.maxHealthHud.paint(graphics)
        self.getAnimationInterface().paintXY(graphics, self.imageX, self.y)
    

    def updateSelectionInfo(self) -> None:
        buildingLayer: BuildingLayer = self.rtsLayer
        self.setName(buildingLayer.getName())
        self.setAnimationInterface(buildingLayer.getVerticleBuildAnimationInterface())
        self.productivityHud.set(buildingLayer.getProductivity())
        self.efficiencyHud.set(java_divide(buildingLayer.getEfficiency(), 100)
            )
        self.currentHealth = buildingLayer.getHealthInterface().getHealth()
        self.healthHud.set(self.currentHealth)
        self.myFontProcessor = self.updateMyFontProcessor
        self.maxHealthHud.set(buildingLayer.getHealthInterface().getMaxHealth())
    

    def setRtsLayer(self, rtsLayer: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        self.rtsLayer = rtsLayer
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.game.ag.layer.hud.basic.NumberStringHudFactory import NumberStringHudFactory
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
# from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer
# from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
# from org.allbinary.logic.math.MathUtil import MathUtil


def _BuildingInfoHudPaintable_instance() -> object:
    return BuildingInfoHudPaintable()

lazy_static(BuildingInfoHudPaintable, "instance", _BuildingInfoHudPaintable_instance)

