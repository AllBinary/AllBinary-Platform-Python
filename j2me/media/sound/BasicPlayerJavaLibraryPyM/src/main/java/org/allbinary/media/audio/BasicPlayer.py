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
# package org.allbinary.media.audio

from __future__ import annotations

import threading
# from javax.microedition.media.Player import Player
from org.allbinary.media.audio.Controllable2 import Controllable2


#BasicPlayerJavaLibrary
class BasicPlayer(Player, Controllable2):
    CONTROL_TYPE: str = "ToneControl"
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.listenersList: BasicArrayList = BasicArrayListD()
        self.stateP: int = 0
        self.loopCountP: int = 0
    

    def __init__(self) -> None:
        self._init_fields()
        self.setLoopCount(0)
        self.setState(Player.UNREALIZED)
    

    def getContentType(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    def getControl(self, controlType: str) -> Control:
        from org.allbinary.media.audio.NullControl import NullControl
        return NullControl()
    

    def getControls(self) -> list[Control]:
        return [None] * (0)
    

    def close(self) -> None:
        pass
    

    def addPlayerListener(self, playerListener: PlayerListener) -> None:
        with self._lock:
            return self._addPlayerListener_unlocked(playerListener)

    def _addPlayerListener_unlocked(self, playerListener: PlayerListener) -> None:
        if not self.listenersList.contains(playerListener):
            self.listenersList.add(playerListener)
    

    def removePlayerListener(self, playerListener: PlayerListener) -> None:
        self.listenersList.remove(playerListener)
    

    def getState(self) -> int:
        return self.stateP
    

    def setState(self, state: int) -> None:
        with self._lock:
            return self._setState_unlocked(state)

    def _setState_unlocked(self, state: int) -> None:
        self.stateP = state
    

    def getDuration(self) -> int:
        return 0
    

    def getMediaTime(self) -> int:
        return 0
    

    def deallocate(self) -> None:
        pass
    

    # throws MediaException
    def prefetch(self) -> None:
        pass
    

    # throws MediaException
    def realize(self) -> None:
        pass
    

    def setLoopCount(self, count: int) -> None:
        with self._lock:
            return self._setLoopCount_unlocked(count)

    def _setLoopCount_unlocked(self, count: int) -> None:
        self.loopCountP = count
    

    def getLoopCount(self) -> int:
        return self.loopCountP
    

    # throws MediaException
    def setMediaTime(self, now: int) -> int:
        with self._lock:
            return self._setMediaTime_unlocked(now)

    def _setMediaTime_unlocked(self, now: int) -> int:
        return 0
    

    # throws MediaException
    def start(self) -> None:
        with self._lock:
            return self._start_unlocked()

    def _start_unlocked(self) -> None:
        self.setState(Player.STARTED)
    

    # throws MediaException
    def stop(self) -> None:
        with self._lock:
            return self._stop_unlocked()

    def _stop_unlocked(self) -> None:
        self.setState(Player.PREFETCHED)
    

    def setVolume(self, leftVolume: int, rightVolume: int) -> None:
        pass
# from javax.microedition.media.Control import Control
# from javax.microedition.media.MediaException import MediaException
# from javax.microedition.media.PlayerListener import PlayerListener
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


