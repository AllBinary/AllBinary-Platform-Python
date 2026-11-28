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
# package org.allbinary.game.input

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.game.input.event.GameKeyEventListenerInterface import GameKeyEventListenerInterface
from org.allbinary.game.input.GameInput import GameInput


@java_inherited_overloads
class PlayerGameInput(*java_bases(GameInput, GameKeyEventListenerInterface)):
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("gameInputStrings", None)
        vars(self).setdefault("playerInputId", 0)

    def _init_fields(self) -> None:
        self.gameInputStrings: GameInputStrings = GameInputStrings.getInstance()
        if "playerInputId" not in vars(self): self.playerInputId: int = 0
    

    def __init__(self, gameKeyEventList: BasicArrayList, removalGameKeyEventList: BasicArrayList, playerInputId: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.util.BasicArrayList import BasicArrayList
        super().__init__(gameKeyEventList, removalGameKeyEventList)
        __class__._init_fields(self)
        self.playerInputId = playerInputId
    

    def onPressGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return __class__.__dict__["_onPressGameKeyEvent_unlocked"].__get__(self, __class__)(gameKeyEvent)

    def _onPressGameKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        self.add(gameKeyEvent)
        self.addForRemoval(gameKeyEvent)
    

    def onDownGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return __class__.__dict__["_onDownGameKeyEvent_unlocked"].__get__(self, __class__)(gameKeyEvent)

    def _onDownGameKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        self.add(gameKeyEvent)
    

    def onDownKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return __class__.__dict__["_onDownKeyEvent_unlocked"].__get__(self, __class__)(gameKeyEvent)

    def _onDownKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        self.add(gameKeyEvent)
        self.addForRemoval(gameKeyEvent)
    

    def onDownKey(self, gameKeyEvent: int) -> None:
        with self._lock:
            return __class__.__dict__["_onDownKey_unlocked"].__get__(self, __class__)(gameKeyEvent)

    def _onDownKey_unlocked(self, gameKeyEvent: int) -> None:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonLabels import CommonLabels
        PreLogUtil.put(str(StringMaker().append(CommonLabels.getInstance().START_LABEL).append(str(gameKeyEvent))), self, self.gameInputStrings.ON_DOWN_GAME_KEY)
    

    def onUpGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return __class__.__dict__["_onUpGameKeyEvent_unlocked"].__get__(self, __class__)(gameKeyEvent)

    def _onUpGameKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        self.addForRemoval(gameKeyEvent)
    

    def onUpKeyEvent(self, gameKeyEvent: int) -> None:
        with self._lock:
            return __class__.__dict__["_onUpKeyEvent_unlocked"].__get__(self, __class__)(gameKeyEvent)

    def _onUpKeyEvent_unlocked(self, gameKeyEvent: int) -> None:
        pass
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventStrings import EventStrings
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def getPlayerInputId(self) -> int:
        return self.playerInputId
# from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
# from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
# from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.logic.util.event.EventStrings import EventStrings
# from org.allbinary.string.CommonLabels import CommonLabels
# from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.game.input.GameInputStrings import GameInputStrings


