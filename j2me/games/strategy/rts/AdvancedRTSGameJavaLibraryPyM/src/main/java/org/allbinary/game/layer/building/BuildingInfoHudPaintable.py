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

from org.allbinary.game.layer.SelectionHudPaintable import SelectionHudPaintable


class BuildingInfoHudPaintable(SelectionHudPaintable):
    instance: BuildingInfoHudPaintable = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.HEALTH: str = "Health:"
        self.productivityHud: NumberStringHud = None
        self.efficiencyHud: NumberStringHud = None
        self.healthHud: NumberStringHud = None
        self.maxHealthHud: NumberStringHud = None
        self.rtsLayer: PathFindingLayerInterface = NullPathFindingLayer.NULL_PATH_FINDING_LAYER
        self.currentHealth: int = 0
    

    @staticmethod
    def getInstance() -> BuildingInfoHudPaintable:
        return BuildingInfoHudPaintable.instance
    

    def __init__(self) -> None:
        from org.allbinary.game.layer.building.ProductivityNumberStringHud import ProductivityNumberStringHud
        from org.allbinary.game.layer.building.EfficiencyNumberStringHud import EfficiencyNumberStringHud
        from org.allbinary.game.layer.building.HEALTH import HEALTH
        from org.allbinary.game.layer.building.HealthNumberStringHud import HealthNumberStringHud
        from org.allbinary.game.layer.building.MaxHealthNumberStringHud import MaxHealthNumberStringHud
        super().__init__()
        self._init_fields()
        numberStringHudFactory: NumberStringHudFactory = NumberStringHudFactory.getInstance()
        productivityHud: NumberStringHud = numberStringHudFactory.NULL_NUMBER_STRING_HUD
        efficiencyHud: NumberStringHud = numberStringHudFactory.NULL_NUMBER_STRING_HUD
        healthHud: NumberStringHud = numberStringHudFactory.NULL_NUMBER_STRING_HUD
        maxHealthHud: NumberStringHud = numberStringHudFactory.NULL_NUMBER_STRING_HUD
        try:
            index: int = 0
            basicHudFactory: BasicHudFactory = BasicHudFactory.getInstance()
            basicColor: BasicColor = self.getBasicColorP()
            textX: int = self.textX
            y: int = self.y
            firstIndex: int = index
            class ProductivityNumberStringHud(NumberStringHud):
                

                def __init__(self) -> None:
                    super().__init__("Productivity:", 999, self.basicHudFactory.ABSOLUTE, self.basicHudFactory.HORIZONTAL, 0, self.basicColor)
                

                def updateMeasurement(self, graphics: Graphics) -> None:
                    font: Font = graphics.getFont()
                    self.updateMaxWidth = self.textX
                    self.updateMaxHeight = self.y + ((self.firstIndex + 1) * font.getHeight())
                    super().updateMeasurement(graphics)
            productivityHud = ProductivityNumberStringHud()
            index += 1
            secondIndex: int = index
            class EfficiencyNumberStringHud(NumberStringHud):
                

                def __init__(self) -> None:
                    super().__init__("Efficiency:", 999, self.basicHudFactory.ABSOLUTE, self.basicHudFactory.HORIZONTAL, 0, self.basicColor)
                

                def updateMeasurement(self, graphics: Graphics) -> None:
                    super().updateMeasurement(graphics)
                    font: Font = graphics.getFont()
                    self.updateMaxWidth = self.textX
                    self.updateMaxHeight = self.y + ((self.secondIndex + 1) * font.getHeight())
            efficiencyHud = EfficiencyNumberStringHud()
            index += 1
            HEALTH: str = self.HEALTH
            thirdIndex: int = index
            class HealthNumberStringHud(NumberStringHud):
                

                def __init__(self) -> None:
                    super().__init__(self.HEALTH, 99999, self.basicHudFactory.ABSOLUTE, self.basicHudFactory.HORIZONTAL, 0, self.basicColor)
                

                def updateMeasurement(self, graphics: Graphics) -> None:
                    font: Font = graphics.getFont()
                    self.updateMaxWidth = self.textX
                    self.updateMaxHeight = self.y + ((self.thirdIndex + 1) * font.getHeight())
                    super().updateMeasurement(graphics)
            totalLength: int = len(HEALTH) + 1
            healthHud = HealthNumberStringHud()
            fourthIndex: int = index
            class MaxHealthNumberStringHud(NumberStringHud):
                

                def __init__(self) -> None:
                    super().__init__("/ ", 99999, self.basicHudFactory.ABSOLUTE, self.basicHudFactory.HORIZONTAL, 0, self.basicColor)
                

                def updateMeasurement(self, graphics: Graphics) -> None:
                    super().updateMeasurement(graphics)
                    font: Font = graphics.getFont()
                    self.updateMaxWidth = self.textX + (self.totalLength * font.getHeight())
                    self.updateMaxHeight = self.y + ((self.fourthIndex + 1) * font.getHeight())
            maxHealthHud = MaxHealthNumberStringHud()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.CONSTRUCTOR, e)
        self.productivityHud = productivityHud
        self.efficiencyHud = efficiencyHud
        self.healthHud = healthHud
        self.maxHealthHud = maxHealthHud
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        totalLength: int = len(self.HEALTH) + MathUtil.getInstance().getTotalDigits(self.currentHealth)
        self.maxHealthHud.setX(self.textX + MyFontProcessor.defaultStringWidth(font, totalLength))
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        super().setBasicColorP(basicColor)
        self.productivityHud.setBasicColorP(basicColor)
        self.efficiencyHud.setBasicColorP(basicColor)
        self.healthHud.setBasicColorP(basicColor)
        self.maxHealthHud.setBasicColorP(basicColor)
    

    def paint(self, graphics: Graphics) -> None:
        super().paint(graphics)
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
        self.efficiencyHud.set(buildingLayer.getEfficiency() / 100)
        self.currentHealth = buildingLayer.getHealthInterface().getHealth()
        self.healthHud.set(self.currentHealth)
        self.myFontProcessor = self.updateMyFontProcessor
        self.maxHealthHud.set(buildingLayer.getHealthInterface().getMaxHealth())
    

    def setRtsLayer(self, rtsLayer: PathFindingLayerInterface) -> None:
        self.rtsLayer = rtsLayer
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.ag.layer.hud.basic.NumberStringHud import NumberStringHud
from org.allbinary.game.ag.layer.hud.basic.NumberStringHudFactory import NumberStringHudFactory
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.logic.math.MathUtil import MathUtil


BuildingInfoHudPaintable.instance = BuildingInfoHudPaintable()

