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
from java.lang.JavaRuntimeStatic import java_bases
from javax.microedition.media.Player import Player
from org.allbinary.media.audio.Controllable2 import Controllable2


#BasicPlayerJavaLibrary
class BasicPlayer(*java_bases(Player, Controllable2)):
    CONTROL_TYPE: str = "ToneControl"
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.listenersList: BasicArrayList = BasicArrayListD()
        if "stateP" not in vars(self): self.stateP: int = 0
        if "loopCountP" not in vars(self): self.loopCountP: int = 0
    

    def __init__(self) -> None:
        __class__._init_fields(self)
        self.setLoopCount(0)
        self.setState(Player.UNREALIZED)
    

    def getContentType(self) -> str:
        from org.allbinary.logic.string.StringUtil import StringUtil
        return StringUtil.getInstance().EMPTY_STRING
    

    def getControl(self, controlType: str) -> Control:
        from org.allbinary.media.audio.NullControl import NullControl
        from javax.microedition.media.Control import Control
        return NullControl()
    

    def getControls(self) -> list[Control]:
        from javax.microedition.media.Control import Control
        return [None] * (0)
    

    def close(self) -> None:
        pass
    

    def addPlayerListener(self, playerListener: PlayerListener) -> None:
        with self._lock:
            return __class__.__dict__["_addPlayerListener_unlocked"].__get__(self, __class__)(playerListener)

    def _addPlayerListener_unlocked(self, playerListener: PlayerListener) -> None:
        from javax.microedition.media.PlayerListener import PlayerListener
        if not (self.listenersList.contains(playerListener)):
            self.listenersList.add(playerListener)
    

    def removePlayerListener(self, playerListener: PlayerListener) -> None:
        from javax.microedition.media.PlayerListener import PlayerListener
        self.listenersList.remove(playerListener)
    

    def getState(self) -> int:
        return self.stateP
    

    def setState(self, state: int) -> None:
        with self._lock:
            return __class__.__dict__["_setState_unlocked"].__get__(self, __class__)(state)

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
        from javax.microedition.media.MediaException import MediaException
        pass
    

    # throws MediaException
    def realize(self) -> None:
        from javax.microedition.media.MediaException import MediaException
        pass
    

    def setLoopCount(self, count: int) -> None:
        with self._lock:
            return __class__.__dict__["_setLoopCount_unlocked"].__get__(self, __class__)(count)

    def _setLoopCount_unlocked(self, count: int) -> None:
        self.loopCountP = count
    

    def getLoopCount(self) -> int:
        return self.loopCountP
    

    # throws MediaException
    def setMediaTime(self, now: int) -> int:
        with self._lock:
            return __class__.__dict__["_setMediaTime_unlocked"].__get__(self, __class__)(now)

    def _setMediaTime_unlocked(self, now: int) -> int:
        from javax.microedition.media.MediaException import MediaException
        return 0
    

    # throws MediaException
    def start(self) -> None:
        with self._lock:
            return __class__.__dict__["_start_unlocked"].__get__(self, __class__)()

    def _start_unlocked(self) -> None:
        from javax.microedition.media.MediaException import MediaException
        self.setState(Player.STARTED)
    

    # throws MediaException
    def stop(self) -> None:
        with self._lock:
            return __class__.__dict__["_stop_unlocked"].__get__(self, __class__)()

    def _stop_unlocked(self) -> None:
        from javax.microedition.media.MediaException import MediaException
        self.setState(Player.PREFETCHED)
    

    def setVolume(self, leftVolume: int, rightVolume: int) -> None:
        pass
# from javax.microedition.media.Control import Control
# from javax.microedition.media.MediaException import MediaException
# from javax.microedition.media.PlayerListener import PlayerListener
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


