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
# package org.allbinary.graphics.form

from __future__ import annotations

from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.form.ScrollCurrentSelectionForm import ScrollCurrentSelectionForm


class CommandCurrentSelectionForm(ScrollCurrentSelectionForm, UpdateMyFontInterface):

    def _init_fields(self) -> None:
        self.selectedAnimationArray: list[Animation] = [None] * (16)
        self.unSelectedAnimationArray: list[Animation] = [None] * (16)
    

    def __init__(self, title: str, items: list[ABCustomItem], border: int, moveForSmallScreen: bool, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        from org.allbinary.graphics.form.ItemPaintableFactory import ItemPaintableFactory
        super().__init__(title, items, ItemPaintableFactory.getInstance(), border, -3, moveForSmallScreen, backgroundBasicColor, foregroundBasicColor)
        self._init_fields()
        self.initAnimations()
        self.addAll(items)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        self.updateAll(graphics, self.getAllitems())
        super().updateMeasurement(graphics)
    

    def initAnimations(self) -> None:
        nullAnimation: Animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
        index = len(self.selectedAnimationArray)
        while (index := index - 1) >= 0:
            self.selectedAnimationArray[index] = nullAnimation
        index = len(self.unSelectedAnimationArray)
        while (index := index - 1) >= 0:
            self.unSelectedAnimationArray[index] = nullAnimation
    

    def addAll(self, items: list[ABCustomItem]) -> None:
        index = len(items)
        while (index := index - 1) >= 0:
            self.addAt(index, items[index])
    

    def addAt(self, index: int, item: ABCustomItem) -> None:
        basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        buttonColor: BasicColor = basicColorFactory.TRANSPARENT_GREY
        selectedButtonColor: BasicColor = basicColorFactory.TRANSPARENT_RED
        width: int = item.getMinimumWidth()
        height: int = item.getMinimumHeight()
        adjustedBorder: int = 3
        offset: int = -(self.halfBorder + adjustedBorder)
        rectWidth: int = width + self.border - adjustedBorder
        rectHeight: int = height + self.border - adjustedBorder
        if J2MEUtil.isJ2ME() or J2MEUtil.isHTML():
            self.selectedAnimationArray[index] = RectangleAdjustedAnimation(rectWidth, rectHeight, offset, offset, selectedButtonColor)
        else:
            self.selectedAnimationArray[index] = RectangleFilledAdjustedAnimation(rectWidth, rectHeight, offset, offset, selectedButtonColor)
        adjustedBorder = 4
        if J2MEUtil.isJ2ME() or J2MEUtil.isHTML():
            self.unSelectedAnimationArray[index] = RectangleAdjustedAnimation(rectWidth, rectHeight, offset, offset, buttonColor)
        else:
            self.unSelectedAnimationArray[index] = RectangleFilledAdjustedAnimation(rectWidth, rectHeight, offset, offset, buttonColor)
    

    def updateAll(self, graphics: Graphics, items: list[ABCustomItem]) -> None:
        index = len(items)
        while (index := index - 1) >= 0:
            items[index].preMeasurement(graphics)
            self.updateAt(index, items[index])
    

    def updateAt(self, index: int, item: ABCustomItem) -> None:
        basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        buttonColor: BasicColor = basicColorFactory.TRANSPARENT_GREY
        selectedButtonColor: BasicColor = basicColorFactory.TRANSPARENT_RED
        width: int = item.getMinimumWidth()
        height: int = item.getMinimumHeight()
        adjustedBorder: int = 3
        offset: int = -(self.halfBorder + adjustedBorder)
        rectWidth: int = width + self.border - adjustedBorder
        rectHeight: int = height + self.border - adjustedBorder
        if J2MEUtil.isJ2ME() or J2MEUtil.isHTML():
            rectangleAdjustedAnimation: RectangleAdjustedAnimation = self.selectedAnimationArray[index]
            rectangleAdjustedAnimation.setWidth(rectWidth)
            rectangleAdjustedAnimation.setHeight(rectHeight)
            rectangleAdjustedAnimation.setOffsetX(offset)
            rectangleAdjustedAnimation.setOffsetY(offset)
            rectangleAdjustedAnimation.setBasicColorP(selectedButtonColor)
        else:
            rectangleAdjustedAnimation: RectangleFilledAdjustedAnimation = self.selectedAnimationArray[index]
            rectangleAdjustedAnimation.setWidth(rectWidth)
            rectangleAdjustedAnimation.setHeight(rectHeight)
            rectangleAdjustedAnimation.setOffsetX(offset)
            rectangleAdjustedAnimation.setOffsetY(offset)
            rectangleAdjustedAnimation.setBasicColorP(selectedButtonColor)
        adjustedBorder = 4
        if J2MEUtil.isJ2ME() or J2MEUtil.isHTML():
            rectangleAdjustedAnimation: RectangleAdjustedAnimation = self.unSelectedAnimationArray[index]
            rectangleAdjustedAnimation.setWidth(rectWidth)
            rectangleAdjustedAnimation.setHeight(rectHeight)
            rectangleAdjustedAnimation.setOffsetX(offset)
            rectangleAdjustedAnimation.setOffsetY(offset)
            rectangleAdjustedAnimation.setBasicColorP(buttonColor)
        else:
            rectangleAdjustedAnimation: RectangleFilledAdjustedAnimation = self.unSelectedAnimationArray[index]
            rectangleAdjustedAnimation.setWidth(rectWidth)
            rectangleAdjustedAnimation.setHeight(rectHeight)
            rectangleAdjustedAnimation.setOffsetX(offset)
            rectangleAdjustedAnimation.setOffsetY(offset)
            rectangleAdjustedAnimation.setBasicColorP(buttonColor)
    

    def getSelectedCommand(self) -> Command:
        index: int = super().getSelectedIndex()
        commandTextItem: CommandTextItem = self.get(index)
        return commandTextItem.getCommand()
    

    def append(self, item: ABCustomItem) -> int:
        result: int = super().append(item)
        self.addAt(result, item)
        return result
    

    def delete(self, itemNum: int) -> None:
        super().delete(itemNum)
    

    def deleteAll(self) -> None:
        self.initAnimations()
        super().deleteAll()
    

    def insert(self, itemNum: int, item: ABCustomItem) -> None:
        super().insert(itemNum, item)
    

    def set(self, itemNum: int, item: ABCustomItem) -> None:
        super().set(itemNum, item)
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        super().paint(graphics)
    

    # throws Exception
    def paintItem(self, graphics: Graphics, index: int, item: ABCustomItem, x: int, y: int) -> int:
        self.selectedAnimationArray[index].paintXY(graphics, x, y)
        return super().paintItem(graphics, index, item, x, y)
    

    # throws Exception
    def paintUnselectedItem(self, graphics: Graphics, index: int, item: ABCustomItem, x: int, y: int) -> int:
        self.unSelectedAnimationArray[index].paintXY(graphics, x, y)
        return super().paintUnselectedItem(graphics, index, item, x, y)
# from javax.microedition.lcdui.Command import Command
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.J2MEUtil import J2MEUtil
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.animation.vector.RectangleAdjustedAnimation import RectangleAdjustedAnimation
from org.allbinary.animation.vector.RectangleFilledAdjustedAnimation import RectangleFilledAdjustedAnimation
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.form.item.CommandTextItem import CommandTextItem
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem


