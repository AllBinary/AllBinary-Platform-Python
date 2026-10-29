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

import threading


class GameKeyEventHandler:
    instance: GameKeyEventHandler = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.pressGameKeyEventHandler: PressGameKeyEventHandler = PressGameKeyEventHandler.getInstance()
        self.upGameKeyEventHandler: UpGameKeyEventHandler = UpGameKeyEventHandler.getInstance()
        self.downGameKeyEventHandler: DownGameKeyEventHandler = DownGameKeyEventHandler.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GameKeyEventHandler:
        return GameKeyEventHandler.instance
    

    def removeAllListeners(self) -> None:
        with self._lock:
            return self._removeAllListeners_unlocked()

    def _removeAllListeners_unlocked(self) -> None:
        self.pressGameKeyEventHandler.removeAllListeners()
        self.upGameKeyEventHandler.removeAllListeners()
        self.downGameKeyEventHandler.removeAllListeners()
    

    def addListenerForPlayer(self, eventListenerInterface: EventListenerInterface, playerInputId: int) -> None:
        self.logUtil.putF(str(eventListenerInterface), self, self.commonStrings.ADD_LISTENER)
        self.pressGameKeyEventHandler.addListenerSingleThreaded(eventListenerInterface)
        self.upGameKeyEventHandler.getInstanceForPlayer(playerInputId).addListenerSingleThreaded(eventListenerInterface)
        self.downGameKeyEventHandler.getInstanceForPlayer(playerInputId).addListenerSingleThreaded(eventListenerInterface)
    

    def addListener(self, eventListenerInterface: EventListenerInterface) -> None:
        self.logUtil.putF(str(eventListenerInterface), self, self.commonStrings.ADD_LISTENER)
        self.pressGameKeyEventHandler.addListenerSingleThreaded(eventListenerInterface)
        self.upGameKeyEventHandler.addListenerSingleThreaded(eventListenerInterface)
        self.downGameKeyEventHandler.addListenerSingleThreaded(eventListenerInterface)
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        self.logUtil.putF(str(eventListenerInterface), self, self.commonStrings.REMOVE_LISTENER)
        self.pressGameKeyEventHandler.removeListenerSingleThreaded(eventListenerInterface)
        self.upGameKeyEventHandler.removeListenerSingleThreaded(eventListenerInterface)
        self.downGameKeyEventHandler.removeListenerSingleThreaded(eventListenerInterface)
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.game.input.event.PressGameKeyEventHandler import PressGameKeyEventHandler
from org.allbinary.game.input.event.UpGameKeyEventHandler import UpGameKeyEventHandler
from org.allbinary.game.input.event.DownGameKeyEventHandler import DownGameKeyEventHandler


GameKeyEventHandler.instance = GameKeyEventHandler()

