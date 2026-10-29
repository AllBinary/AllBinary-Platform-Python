#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
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
# package org.allbinary.game.part

from __future__ import annotations

from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface


class CountedLayersHudPaintable(PaintableInterface, UpdateMyFontInterface):
    XXStringWidth: int = 0

    def _init_fields(self) -> None:
        self.displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.partInterfaceArray: list[PartInterface] = None
        self.countedTotalStringColor: int = None
        self.countedPartsBorder: int = None
        self.startIndex: int = None
        self.dropSize: int = None
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.height: int = 0
    

    def __init__(self, partInterfaceArray: list[PartInterface], dropSize: int, startIndex: int, countedTotalStringColor: int, countedPartsBorder: int) -> None:
        self._init_fields()
        self.partInterfaceArray = partInterfaceArray
        self.startIndex = startIndex
        self.countedTotalStringColor = countedTotalStringColor
        self.countedPartsBorder = countedPartsBorder
        self.dropSize = dropSize
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.height = font.getHeight()
        if self.dropSize > font.getHeight():
            self.height = self.dropSize
        if CountedLayersHudPaintable.XXStringWidth == 0:
            XXString: str = "XX"
            CountedLayersHudPaintable.XXStringWidth = font.stringWidth(XXString)
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        lastWidth: int = self.displayInfoSingleton.getLastWidth()
        widthEdge: int = lastWidth - self.dropSize
        size: int = len(self.partInterfaceArray)
        count: int = 0
        y: int = 0
        countedLayerInterfaceFactory: CountedLayerInterfaceFactoryPart = None
        pickedUpLayerInterfaceFactoryInterface: PickedUpLayerInterfaceFactoryInterface = None
        layerInterface: AllBinaryLayer = None
        charArray: list[str] = None
        for index in range(self.startIndex, size):
            countedLayerInterfaceFactory = self.partInterfaceArray[index]
            if countedLayerInterfaceFactory.getTotal() > 0:
                pickedUpLayerInterfaceFactoryInterface = countedLayerInterfaceFactory.getCountedPickedUpLayerInterfaceFactory()
                layerInterface = pickedUpLayerInterfaceFactoryInterface.getIconLayer()
                y = 40 + (count * self.height)
                layerInterface.setPosition(widthEdge, y, layerInterface.getZP())
                layerInterface.paint(graphics)
                graphics.setColor(self.countedTotalStringColor)
                countedLayerInterfaceFactory.paint(graphics)
                charArray = countedLayerInterfaceFactory.getTotalString()
                graphics.drawChars(charArray, 0, len(charArray), widthEdge - countedLayerInterfaceFactory.getXOffset(), y, 0)
                count += 1
        if count > 0:
            graphics.setColor(self.countedPartsBorder)
            graphics.drawRect(lastWidth - (CountedLayersHudPaintable.XXStringWidth + self.dropSize), 40, CountedLayersHudPaintable.XXStringWidth + self.dropSize, (count * self.height) + 3)
    

    def paintThreed(self, graphics: Graphics) -> None:
        pass
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.layer.pickup.PickedUpLayerInterfaceFactoryInterface import PickedUpLayerInterfaceFactoryInterface
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


