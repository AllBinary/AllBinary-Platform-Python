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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


@java_inherited_overloads
class GameKeyEvent(AllBinaryEventObject):
    NONE: GameKeyEvent = None
    def _java_defaults(self):
        vars(self).setdefault("sourceId", 0)
        vars(self).setdefault("repeated", False)
        vars(self).setdefault("key", 0)
        vars(self).setdefault("gameActionKey", 0)
        vars(self).setdefault("originalKey", 0)

    def _init_fields(self) -> None:
        if "sourceId" not in vars(self): self.sourceId: int = 0
        if "repeated" not in vars(self): self.repeated: bool = False
        if "key" not in vars(self): self.key: int = 0
        if "gameActionKey" not in vars(self): self.gameActionKey: int = 0
        if "originalKey" not in vars(self): self.originalKey: int = 0
    

    @staticmethod
    def createEvent(anyType: object, sourceId: int, key: int) -> GameKeyEvent:
        return GameKeyEvent(anyType, sourceId, 0, 0, key, False)
    

    def __init__(self, anyType: object, sourceId: int, originalKey: int, gameActionKey: int, key: int, repeated: bool) -> None:
        __class__._java_defaults(self)
        super().__init__(anyType)
        __class__._init_fields(self)
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
        from org.allbinary.logic.string.StringMaker import StringMaker
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
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.string.StringMaker import StringMaker


def _GameKeyEvent_NONE() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return GameKeyEvent(NullUtil.getInstance().NULL_OBJECT, -1, -1, -1, -1, False)

lazy_static(GameKeyEvent, "NONE", _GameKeyEvent_NONE)

