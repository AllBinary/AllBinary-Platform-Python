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
# package org.allbinary.game.input.event

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class GameKeyEvent(AllBinaryEventObject):
    NONE: GameKeyEvent = None

    def _init_fields(self) -> None:
        self.sourceId: int = None
        self.repeated: bool = False
        self.key: int = None
        self.gameActionKey: int = 0
        self.originalKey: int = 0
    

    @staticmethod
    def createEvent(anyType: object, sourceId: int, key: int) -> GameKeyEvent:
        return GameKeyEvent(anyType, sourceId, 0, 0, key, False)
    

    def __init__(self, anyType: object, sourceId: int, originalKey: int, gameActionKey: int, key: int, repeated: bool) -> None:
        super().__init__(anyType)
        self._init_fields()
        self.sourceId = sourceId
        self.setOriginalKey(originalKey)
        self.key = key
        self.setGameActionKey(gameActionKey)
        self.setRepeatEvents(repeated)
    

    def init(self, anyType: object) -> None:
        self.setSource(anyType)
    

    def setRepeatEvents(self, repeated: bool) -> None:
        self.repeated = repeated
    

    def hasRepeatEvents(self) -> bool:
        return self.repeated
    

    def getKey(self) -> int:
        return self.key
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("\nKey: ")
        stringBuffer.appendint(self.getKey())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def getOriginalKey(self) -> int:
        return self.originalKey
    

    def setOriginalKey(self, originalKey: int) -> None:
        self.originalKey = originalKey
    

    def getGameActionKey(self) -> int:
        return self.gameActionKey
    

    def setGameActionKey(self, gameActionKey: int) -> None:
        self.gameActionKey = gameActionKey
    

    def getSourceId(self) -> int:
        return self.sourceId
from org.allbinary.logic.string.StringMaker import StringMaker


GameKeyEvent.NONE = GameKeyEvent(NullUtil.getInstance().NULL_OBJECT, -1, -1, -1, -1, False)

