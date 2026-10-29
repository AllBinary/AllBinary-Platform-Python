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
# package org.allbinary.graphics.form.item

from __future__ import annotations



class CommandTextItemArrayFactory:

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListD()
        self.visitorInterface: Visitor = None
    

    def __init__(self, visitorInterface: Visitor) -> None:
        self._init_fields()
        self.visitorInterface = visitorInterface
    

    def getInstance(self, vector: object, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> list[ABCustomItem]:
        from org.allbinary.graphics.form.item.CommandTextItem import CommandTextItem
        vectorUtil: VectorUtil = VectorUtil.getInstance()
        size: int = vectorUtil.getSize(vector)
        self.list_.clear()
        textItem: CommandTextItem = None
        priorityLimit: int = 7
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        isLargeEnoughDisplayForBigMenu: bool = (displayInfo.isPortrait() and displayInfo.getLastHeight() >= ScreenInfo.getInstance().MEDIUM_WIDTH) or (not displayInfo.isPortrait() and displayInfo.getLastWidth() >= ScreenInfo.getInstance().MEDIUM_WIDTH)
        if not isLargeEnoughDisplayForBigMenu and size > 3:
            priorityLimit = 3
        command: Command = None
        for index in range(0, size):
            command = vectorUtil.elementAt(vector, index)
            if command.getPriority() < priorityLimit:
                aBoolean: bool = self.visitorInterface.visit(command)
                if aBoolean:
                    textItem = CommandTextItem(command, ImageItem.LAYOUT_DEFAULT, StringUtil.getInstance().EMPTY_STRING, backgroundBasicColor, foregroundBasicColor)
                    self.list_.add(textItem)
        textItemArray: list[ABCustomItem] = [None] * (self.list_.size())
        size2: int = len(textItemArray)
        for index in range(0, size2):
            textItemArray[index] = self.list_.objectArray[index]
        return textItemArray
# from javax.microedition.lcdui.Command import Command
# from javax.microedition.lcdui.ImageItem import ImageItem
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.form.ScreenInfo import ScreenInfo
from org.allbinary.logic.VectorUtil import VectorUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.util.visitor.Visitor import Visitor
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


