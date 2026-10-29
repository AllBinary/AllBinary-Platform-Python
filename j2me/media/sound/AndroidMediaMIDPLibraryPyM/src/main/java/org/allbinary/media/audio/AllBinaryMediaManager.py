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


#AndroidMediaMIDPLibrary
class AllBinaryMediaManager:
    THIS: str = "AllBinaryMediaManagerAndroid"
    mostUsedTotal: int = 0
    _lock = threading.RLock()
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def isMuted() -> bool:
        return False
    

    @staticmethod
    def setMuted(aMuted: bool) -> None:
        pass
    

    @staticmethod
    def update() -> bool:
        return True
    

    # throws Exception
    @staticmethod
    def init(soundsFactoryInterface: SoundsFactoryInterface) -> None:
        from org.allbinary.media.audio.Sounds import Sounds
        logUtil: LogUtil = LogUtil.getInstance()
        commonString: CommonStrings = CommonStrings.getInstance()
        logUtil.putF(commonString.START, AllBinaryMediaManager.THIS, commonString.INIT)
        AllBinaryMediaManager.shutdown(soundsFactoryInterface)
        ProgressCanvasFactory.getInstance().addNormalPortion(50, "Media Manager")
        TsUtil.getInstance().gc()
        Sounds(soundsFactoryInterface).init()
        logUtil.putF(commonString.END, AllBinaryMediaManager.THIS, commonString.INIT)
    

    # throws Exception
    @staticmethod
    def shutdown(soundsFactoryInterface: SoundsFactoryInterface) -> None:
        from org.allbinary.media.audio.Sounds import Sounds
        from org.allbinary.media.audio.MediaPlayerUtil import MediaPlayerUtil
        from org.allbinary.media.audio.Sounds import Sounds
        logUtil: LogUtil = LogUtil.getInstance()
        commonString: CommonStrings = CommonStrings.getInstance()
        logUtil.putF(commonString.START, AllBinaryMediaManager.THIS, "shutdown")
        if soundsFactoryInterface.isInitialized():
            Sounds(soundsFactoryInterface).stopAll()
            soundInterfaceArray: list[Sound] = soundsFactoryInterface.getSoundInterfaceArray()
            player: Player = None
            player2: Player = None
            androidMediaPlayerWrapper: AndroidMediaPlayerWrapper = None
            for i in range(0, len(soundInterfaceArray)):
                if soundInterfaceArray[i] is not None:
                    player = soundInterfaceArray[i].getPlayerP()
                    if player is not None:
                        player2 = (player).getPlayerP()
                        if isinstance(player2, AndroidMediaPlayerWrapper):
                            androidMediaPlayerWrapper = player2
                            MediaPlayerUtil.getInstance().waitForMediaPlayer(androidMediaPlayerWrapper.getMediaPlayer())
                        else:
                            raise Exception("Unknown Property Player: " + type(player).__module__ + "." + type(player).__qualname__)
            Sounds(soundsFactoryInterface).closeAll()
            TsUtil.getInstance().gc()
            soundsFactoryInterface.setInitialized(False)
            AllBinaryMediaManager.mostUsedTotal = 0
        logUtil.putF(commonString.START, AllBinaryMediaManager.THIS, "shutdown")
    

    # throws Exception
    @staticmethod
    def createPlayer(resource: str) -> Player:
        from org.allbinary.media.audio.NoPlayer import NoPlayer
        from org.allbinary.media.audio.AndroidMediaPlayerWrapper import AndroidMediaPlayerWrapper
        from org.allbinary.media.audio.NoPlayer import NoPlayer
        AllBinaryMediaManager.mostUsedTotal += 1
        logUtil: LogUtil = LogUtil.getInstance()
        if Features.getInstance().isFeature(GameFeatureFactory.getInstance().SOUND):
            try:
                return AndroidMediaPlayerWrapper(resource)
            except Exception as e:
                logUtil.put("Could not create AndroidMediaPlayerWrapper using NoPlayer at " + str(CommonLabels.getInstance().TOTAL_LABEL) + str(AllBinaryMediaManager.mostUsedTotal), AllBinaryMediaManager.THIS, "createPlayer", e)
                return NoPlayer.NO_PLAYER
        else:
            return NoPlayer.NO_PLAYER
    

    # throws IOException, MediaException
    @staticmethod
    def createPlayerFromInputStream(stream: InputStream, type_: str) -> Player:
        raise MediaException("No Input Stream Player")
    

    # throws MediaException
    @staticmethod
    def playTone(frequency: int, time: int, volume: int) -> None:
        with AllBinaryMediaManager._lock:
            return AllBinaryMediaManager._playTone_unlocked(frequency, time, volume)

    @staticmethod
    def _playTone_unlocked(frequency: int, time: int, volume: int) -> None:
        raise MediaException("No Tone Player")
    

    @staticmethod
    def isInitialized() -> bool:
        return True
# from java.io.IOException import IOException
# from java.io.InputStream import InputStream
# from javax.microedition.media.MediaException import MediaException
# from javax.microedition.media.Player import Player
from org.allbinary.TsUtil import TsUtil
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.GameFeatureFactory import GameFeatureFactory
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
from org.allbinary.logic.ABSystemWrapper import ABSystemWrapper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings


