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
# from javax.microedition.media.Controllable import Controllable
# from javax.microedition.media.Player import Player


#BasicPlayerMIDP2
class PlayerComposite(Controllable, Player):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.player: Player = None
        self.timeElapsedHelper: TimeDelayHelper = TimeDelayHelper(0)
        self.gameTickTimeDelayHelper: GameTickTimeDelayHelper = GameTickTimeDelayHelperFactory.getInstance()
    

    def __init__(self, player: Player, repeatTime: int) -> None:
        self._init_fields()
        self.player = player
        self.timeElapsedHelper.delay = repeatTime
    

    def addPlayerListener(self, playerListener: PlayerListener) -> None:
        with self._lock:
            return self._addPlayerListener_unlocked(playerListener)

    def _addPlayerListener_unlocked(self, playerListener: PlayerListener) -> None:
        self.player.addPlayerListener(playerListener)
    

    def removePlayerListener(self, playerListener: PlayerListener) -> None:
        self.player.removePlayerListener(playerListener)
    

    def close(self) -> None:
        self.player.close()
    

    def deallocate(self) -> None:
        self.player.deallocate()
    

    def getContentType(self) -> str:
        return self.player.getContentType()
    

    def getDuration(self) -> int:
        return self.player.getDuration()
    

    def getMediaTime(self) -> int:
        return self.player.getMediaTime()
    

    def getTimeBase(self) -> TimeBase:
        return (self.player).getTimeBase()
    

    # throws MediaException
    def setTimeBase(self, timeBase: TimeBase) -> None:
        with self._lock:
            return self._setTimeBase_unlocked(timeBase)

    def _setTimeBase_unlocked(self, timeBase: TimeBase) -> None:
        (self.player).setTimeBase(timeBase)
    

    def prefetch(self) -> None:
        try:
            self.player.prefetch()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "prefetch", e)
    

    def realize(self) -> None:
        try:
            self.player.realize()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "realize", e)
    

    def getState(self) -> int:
        return self.player.getState()
    

    def setLoopCount(self, count: int) -> None:
        self.player.setLoopCount(count)
    

    def setMediaTime(self, now: int) -> int:
        try:
            return self.player.setMediaTime(now)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "setMediaTime", e)
            return -1
    

    def start(self) -> None:
        try:
            if self.timeElapsedHelper.isTime(self.gameTickTimeDelayHelper.startTime):
                self.player.start()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.START_METHOD_NAME, e)
    

    def stop(self) -> None:
        try:
            self.player.stop()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "stop", e)
    

    def getControl(self, controlType: str) -> Control:
        return self.player.getControl(controlType)
    

    def getControls(self) -> list[Control]:
        raise RuntimeError()
    

    def setVolume(self, leftVolume: int, rightVolume: int) -> None:
        controllable2: Controllable2 = (self.player)
        controllable2.setVolume(leftVolume, rightVolume)
    

    def getPlayerP(self) -> Player:
        return self.player
# from javax.microedition.media.Control import Control
# from javax.microedition.media.MediaException import MediaException
# from javax.microedition.media.PlayerListener import PlayerListener
# from javax.microedition.media.TimeBase import TimeBase
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.time.GameTickTimeDelayHelper import GameTickTimeDelayHelper
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


