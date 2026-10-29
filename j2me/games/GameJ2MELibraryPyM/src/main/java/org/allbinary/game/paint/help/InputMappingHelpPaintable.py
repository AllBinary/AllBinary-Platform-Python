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
# package org.allbinary.game.paint.help

from __future__ import annotations

from org.allbinary.game.paint.help.HelpPaintable import HelpPaintable


class InputMappingHelpPaintable(HelpPaintable):
    AND: str = " and "
    SEP: str = ", "
    MORE_THAN_TWO_IN_LIST_AND: str = ", and "
    class UpdateMyFontProperties:

        def _init_fields(self) -> None:
            self.actionStringArray: list[str] = StringUtil.getInstance().getArrayInstance()
            self.keymappingBeginWidthArray: list[int] = NullUtil.getInstance().NULL_INT_ARRAY
            self.actionStringDeltaXArray: list[int] = NullUtil.getInstance().NULL_INT_ARRAY
            self.inputDeltaXArray: list[list[int]] = NullUtil.getInstance().NULL_INT_ARRAY_ARRAY
            self.sepArray: list[list[str]] = [[None] * (0) for _ in range(0)]
            self.sepWidthArray: list[list[int]] = NullUtil.getInstance().NULL_INT_ARRAY_ARRAY
            self.charHeight: int = 0

        def __init__(self) -> None:
            self._init_fields()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        self.NONE: GameKey = GameKeyFactory.getInstance().NONE
        self.EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
        self.gameInputMappingArray: list[GameInputMapping] = None
        self.keyMappingArray: list[BasicArrayList] = [None] * (0)
        self.actionBasicColor: list[BasicColor] = [None] * (0)
        self.inputBasicColorArray: list[list[BasicColor]] = [[None] * (0) for _ in range(0)]
        self.selectedBasicColor: BasicColor = None
        self.updateMyFontProperties: UpdateMyFontProperties = UpdateMyFontProperties()
    

    def __init__(self, gameInputMappingArray: list[GameInputMapping], backgroundBasicColor: BasicColor, basicColor: BasicColor) -> None:
        super().__init__("Input Mapping", backgroundBasicColor, basicColor)
        self._init_fields()
        self.gameInputMappingArray = gameInputMappingArray
        self.update(self.NONE, self.NONE)
        if backgroundBasicColor == self.basicColorFactory.WHITE or basicColor == self.basicColorFactory.WHITE:
            self.selectedBasicColor = self.basicColorFactory.RED
        else:
            self.selectedBasicColor = self.basicColorFactory.WHITE
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from org.allbinary.game.paint.help.UpdateMyFontProperties import UpdateMyFontProperties
        font: Font = graphics.getFont()
        updateMyFontProperties: UpdateMyFontProperties = UpdateMyFontProperties()
        updateMyFontProperties.charHeight = font.getHeight()
        stringMaker: StringMaker = StringMaker()
        inputInfo: list[str] = self.inputInfo
        size: int = len(inputInfo)
        updateMyFontProperties.actionStringArray = [None] * (size)
        updateMyFontProperties.keymappingBeginWidthArray = [0] * (size)
        updateMyFontProperties.actionStringDeltaXArray = [0] * (size)
        updateMyFontProperties.inputDeltaXArray = [[0] * (0) for _ in range(size)]
        updateMyFontProperties.sepArray = [[None] * (0) for _ in range(size)]
        updateMyFontProperties.sepWidthArray = [[0] * (0) for _ in range(size)]
        list_: BasicArrayList = None
        keyMappings: str = None
        actionString: str = None
        input: Input = None
        size2: int = 0
        for index in range(0, size):
            list_ = self.keyMappingArray[index]
            keyMappings = self.get(list_)
            stringMaker.delete(0, stringMaker.length())
            actionString = str(stringMaker.append(inputInfo[index]).append(self.commonSeps.COLON).append(self.commonSeps.SPACE).append(self.commonSeps.SPACE))
            updateMyFontProperties.actionStringArray[index] = actionString
            stringMaker.delete(0, stringMaker.length())
            updateMyFontProperties.keymappingBeginWidthArray[index] = (font.stringWidth(str(stringMaker.append(updateMyFontProperties.actionStringArray[index]).append(keyMappings))) >> 1)
            updateMyFontProperties.actionStringDeltaXArray[index] = font.stringWidth(actionString)
            size2 = list_.size()
            updateMyFontProperties.inputDeltaXArray[index] = [0] * (size2)
            updateMyFontProperties.sepArray[index] = [None] * (size2)
            updateMyFontProperties.sepWidthArray[index] = [0] * (size2)
            for index2 in range(0, size2):
                input = list_.objectArray[index2]
                updateMyFontProperties.inputDeltaXArray[index][index2] = font.stringWidth(input.getName())
                updateMyFontProperties.sepArray[index][index2] = self.EMPTY_STRING
                if index2 + 1 < list_.size():
                    if list_.size() == 2:
                        updateMyFontProperties.sepArray[index][index2] = InputMappingHelpPaintable.AND
                    else:
                        if index2 + 2 == list_.size():
                            updateMyFontProperties.sepArray[index][index2] = InputMappingHelpPaintable.MORE_THAN_TWO_IN_LIST_AND
                        else:
                            updateMyFontProperties.sepArray[index][index2] = InputMappingHelpPaintable.SEP
                if updateMyFontProperties.sepArray[index][index2] != self.EMPTY_STRING:
                    updateMyFontProperties.sepWidthArray[index][index2] = font.stringWidth(updateMyFontProperties.sepArray[index][index2])
        self.updateMyFontProperties = updateMyFontProperties
        super().updateMeasurement(graphics)
    

    def update(self, selectedGameKey: GameKey, selectedInput: Input) -> None:
        stringMaker: StringMaker = StringMaker()
        self.logUtil.putF(str(stringMaker.append(CommonLabels.getInstance().START_LABEL).append("selected GameKey: ").append(self.stringUtil.toString(selectedGameKey)).append(" Input: ").append(self.stringUtil.toString(selectedInput))), self, self.commonStrings.UPDATE)
        gameKeyMapping: PersistentInputMapping = PlatformInputMappingFactory.getInstance().getPersistentInputMappingInstance()
        size: int = len(self.gameInputMappingArray)
        keyInfo: list[str] = [None] * (size)
        keyMappingArray: list[BasicArrayList] = [None] * (size)
        actionBasicColor: list[BasicColor] = [None] * (size)
        inputBasicColorArray: list[list[BasicColor]] = [None] * (size)
        gameInputMapping: GameInputMapping = None
        gameKey: GameKey = None
        list_: BasicArrayList = None
        for index in range(0, size):
            gameInputMapping = self.gameInputMappingArray[index]
            gameKey = gameInputMapping.getGameKey()
            list_ = gameKeyMapping.getInputMapping().getMappedInput(gameKey)
            size2: int = list_.size()
            inputBasicColorArray[index] = [None] * (size2)
            for index2 in range(0, size2):
                inputBasicColorArray[index][index2] = self.basicColor
            if gameKey == selectedGameKey:
                stringMaker.delete(0, stringMaker.length())
                self.logUtil.putF(str(stringMaker.append("Found: selected GameKey: ").append(self.stringUtil.toString(selectedGameKey))), self, self.commonStrings.UPDATE)
                actionBasicColor[index] = self.selectedBasicColor
                indexOfSelectedInput: int = list_.indexOf(selectedInput)
                if indexOfSelectedInput >= 0:
                    stringMaker.delete(0, stringMaker.length())
                    self.logUtil.putF(str(stringMaker.append("Found: selected Input: ").append(self.stringUtil.toString(selectedInput))), self, self.commonStrings.UPDATE)
                    inputBasicColorArray[index][indexOfSelectedInput] = self.selectedBasicColor
            else:
                actionBasicColor[index] = self.basicColor
            keyInfo[index] = gameInputMapping.getName()
            keyMappingArray[index] = list_
        self.keyMappingArray = keyMappingArray
        self.actionBasicColor = actionBasicColor
        self.inputBasicColorArray = inputBasicColorArray
        super().setInputInfoP(keyInfo)
        self.myFontProcessor = self.updateMyFontProcessor
    

    def get(self, keyList: BasicArrayList) -> str:
        stringBuffer: StringMaker = StringMaker()
        key: Input = None
        size: int = keyList.size()
        for index in range(0, size):
            key = keyList.objectArray[index]
            stringBuffer.append(key.getName())
            if index + 1 < keyList.size():
                if keyList.size() == 2:
                    stringBuffer.append(InputMappingHelpPaintable.AND)
                else:
                    if index + 2 == keyList.size():
                        stringBuffer.append(InputMappingHelpPaintable.MORE_THAN_TWO_IN_LIST_AND)
                    else:
                        stringBuffer.append(InputMappingHelpPaintable.SEP)
        return str(stringBuffer)
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        halfWidth: int = self.displayInfo.getLastHalfWidth()
        graphics.setColor(int(self.basicColor))
        graphics.drawString(self.title, halfWidth - self.titleBeginWidth, self.updateMyFontProperties.charHeight, self.anchor)
        inputInfo: list[str] = self.inputInfo
        size: int = len(inputInfo)
        y: int = 0
        deltaX: int = 0
        size2: int = 0
        actionString: str = None
        input: Input = None
        list_: BasicArrayList = None
        sep: str = None
        beginWidth: int = 0
        for index in range(0, size):
            y = (index + 3) * self.updateMyFontProperties.charHeight
            deltaX = 0
            list_ = self.keyMappingArray[index]
            size2 = list_.size()
            beginWidth = self.updateMyFontProperties.keymappingBeginWidthArray[index]
            graphics.setColor(int(self.actionBasicColor[index]))
            actionString = self.updateMyFontProperties.actionStringArray[index]
            graphics.drawString(actionString, halfWidth - beginWidth + deltaX, y, self.anchor)
            deltaX += self.updateMyFontProperties.actionStringDeltaXArray[index]
            for index2 in range(0, size2):
                input = list_.objectArray[index2]
                graphics.setColor(int(self.inputBasicColorArray[index][index2]))
                graphics.drawString(input.getName(), halfWidth - beginWidth + deltaX, y, self.anchor)
                deltaX += self.updateMyFontProperties.inputDeltaXArray[index][index2]
                sep = self.updateMyFontProperties.sepArray[index][index2]
                graphics.setColor(int(self.basicColor))
                graphics.drawString(sep, halfWidth - beginWidth + deltaX, y, self.anchor)
                deltaX += self.updateMyFontProperties.sepWidthArray[index][index2]
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.input.GameKey import GameKey
from org.allbinary.game.input.GameKeyFactory import GameKeyFactory
from org.allbinary.game.input.Input import Input
from org.allbinary.game.input.PlatformInputMappingFactory import PlatformInputMappingFactory
from org.allbinary.game.input.mapping.GameInputMapping import GameInputMapping
from org.allbinary.game.input.mapping.PersistentInputMapping import PersistentInputMapping
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.game.paint.help.UpdateMyFontProperties import UpdateMyFontProperties


