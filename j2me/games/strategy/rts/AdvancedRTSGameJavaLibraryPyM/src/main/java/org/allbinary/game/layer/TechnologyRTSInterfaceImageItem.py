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
# package org.allbinary.game.layer

from __future__ import annotations

from org.allbinary.graphics.form.item.ABCustomImageItem import ABCustomImageItem
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface


class TechnologyRTSInterfaceImageItem(ABCustomImageItem, UpdateMyFontInterface):

    def _init_fields(self) -> None:
        self.rtsInterface: RTSInterface = None
        self.primitiveLongUtil: PrimitiveLongUtil = PrimitiveLongUtil.createPowerOfTen(10000)
        self.LEVEL: str = "Level"
        self.COST: str = "Cost"
        self.DOLLAR: str = "$"
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.costString: list[str] = CharArrayFactory.getInstance().getZeroCharArray()
        self.costLength: int = 0
        self.levelString: list[str] = CharArrayFactory.getInstance().getZeroCharArray()
        self.levelLength: int = 0
        self.adjustedCostLabelY: int = 0
        self.adjustedCostX: int = 0
        self.adjustedCostY: int = 0
        self.adjustedLevelX: int = 0
        self.adjustedLevelY: int = 0
    

    def __init__(self, label: str, img: Image, layout: int, altText: str, basicColor: BasicColor, rtsInterface: RTSInterface) -> None:
        super().__init__(label, img, layout, altText, basicColor, 0)
        self._init_fields()
        self.rtsInterface = rtsInterface
        self.update()
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        fontHeight: int = font.getHeight()
        imageHeight: int = 0
        image: Image = self.getImage()
        if image != NullImage.NULL_IMAGE:
            imageHeight = image.getHeight()
        self.adjustedCostLabelY = -self.yOffset + imageHeight - (3 * fontHeight)
        self.adjustedCostY = -self.yOffset + imageHeight - (2 * fontHeight)
        self.adjustedCostX = 2 + (len(self.DOLLAR) * (fontHeight - 1))
        self.adjustedLevelY = -self.yOffset + imageHeight - fontHeight
        self.adjustedLevelX = 2 + (len(self.LEVEL) * (fontHeight - 1))
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def getRtsInterface(self) -> RTSInterface:
        return self.rtsInterface
    

    def update(self) -> None:
        self.costString = self.primitiveLongUtil.getCharArray(self.getRtsInterface().getUpgradeCost())
        self.levelString = self.primitiveLongUtil.getCharArray(self.getRtsInterface().getLevel())
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.myFontProcessor.process(graphics)
        super().paintXY(graphics, x, y)
        xa: int = x + 2
        graphics.drawString(self.COST, xa, y + self.adjustedCostLabelY, 0)
        graphics.drawString(self.DOLLAR, xa, y + self.adjustedCostY, 0)
        graphics.drawChars(self.costString, 0, self.costLength, x + self.adjustedCostX, y + self.adjustedCostY, 0)
        graphics.drawString(self.LEVEL, xa, y + self.adjustedLevelY, 0)
        graphics.drawChars(self.levelString, 0, self.levelLength, x + self.adjustedLevelX, y + self.adjustedLevelY, 0)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.logic.java.character.CharArrayFactory import CharArrayFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil


