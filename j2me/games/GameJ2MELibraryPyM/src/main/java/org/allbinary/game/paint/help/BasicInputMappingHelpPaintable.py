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


class BasicInputMappingHelpPaintable(HelpPaintable):

    def _init_fields(self) -> None:
        self.gameInputMappingArray: list[GameInputMapping] = None
        self.NONE: GameKey = GameKeyFactory.getInstance().NONE
    

    def __init__(self, gameInputMappingArray: list[GameInputMapping], basicColor: BasicColor) -> None:
        super().__init__("Help Screen", BasicColorFactory.getInstance().BLACK, basicColor)
        self._init_fields()
        self.gameInputMappingArray = gameInputMappingArray
        self.update(self.NONE, self.NONE)
    

    def update(self, selectedGameKey: GameKey, selectedInput: Input) -> None:
        gameKeyMapping: PersistentInputMapping = PlatformInputMappingFactory.getInstance().getPersistentInputMappingInstance()
        EQUAL: str = " = "
        stringMaker: StringMaker = StringMaker()
        size: int = len(self.gameInputMappingArray)
        keyInfo: list[str] = [None] * (size)
        gameInputMapping: GameInputMapping = None
        gameKey: GameKey = None
        list_: BasicArrayList = None
        for index in range(0, size):
            gameInputMapping = self.gameInputMappingArray[index]
            gameKey = gameInputMapping.getGameKey()
            list_ = gameKeyMapping.getInputMapping().getMappedInput(gameKey)
            stringMaker.delete(0, stringMaker.length())
            keyInfo[index] = str(stringMaker.append(gameInputMapping.getName()).append(EQUAL).append(self.get(list_)))
        super().setInputInfoP(keyInfo)
    

    def get(self, keyList: BasicArrayList) -> str:
        commonSeps: CommonSeps = CommonSeps.getInstance()
        stringBuffer: StringMaker = StringMaker()
        AND: str = "and "
        key: Input = None
        size: int = keyList.size()
        for index in range(0, size):
            key = keyList.objectArray[index]
            stringBuffer.append(key.getName())
            if index + 1 < keyList.size():
                if keyList.size() == 2:
                    stringBuffer.append(commonSeps.SPACE).append(AND)
                else:
                    if index + 2 == keyList.size():
                        stringBuffer.append(commonSeps.COMMA_SEP)
                        stringBuffer.append(AND)
                    else:
                        stringBuffer.append(commonSeps.COMMA_SEP)
        return str(stringBuffer)
from org.allbinary.game.input.GameKey import GameKey
from org.allbinary.game.input.GameKeyFactory import GameKeyFactory
from org.allbinary.game.input.Input import Input
from org.allbinary.game.input.PlatformInputMappingFactory import PlatformInputMappingFactory
from org.allbinary.game.input.mapping.GameInputMapping import GameInputMapping
from org.allbinary.game.input.mapping.PersistentInputMapping import PersistentInputMapping
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.util.BasicArrayList import BasicArrayList


