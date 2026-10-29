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


#NotDeviceSpecificMIDP2JavaLibrary
class AllBinaryMediaManager:
    THIS: str = "AllBinaryMediaManagerNoMIPD2"
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
        ProgressCanvasFactory.getInstance().addNormalPortion(50, "Media Manager")
        Sounds(soundsFactoryInterface).init()
    

    # throws Exception
    @staticmethod
    def shutdown(soundsFactoryInterface: SoundsFactoryInterface) -> None:
        from org.allbinary.media.audio.Sounds import Sounds
        from org.allbinary.media.audio.Sounds import Sounds
        Sounds(soundsFactoryInterface).stopAll()
        Sounds(soundsFactoryInterface).closeAll()
        TsUtil.getInstance().gc()
    

    # throws Exception
    @staticmethod
    def createPlayer(resource: str) -> Player:
        from org.allbinary.media.audio.NoPlayer import NoPlayer
        if Features.getInstance().isFeature(GameFeatureFactory.getInstance().SOUND):
            if TsUtil.getInstance().compareTo(resource, Manager.TONE_DEVICE_LOCATOR) == 0:
                return Manager.createPlayer(resource)
            else:
                inputStream: InputStream = ResourceUtil.getInstance().getResourceAsStream(resource)
                return Manager.createPlayer(inputStream, AudioContentTypeDataFactory.getInstance().MIME_AUDIO_WAV.getName())
        else:
            return NoPlayer.NO_PLAYER
    

    # throws MediaException
    @staticmethod
    def playTone(frequency: int, time: int, volume: int) -> None:
        with AllBinaryMediaManager._lock:
            return AllBinaryMediaManager._playTone_unlocked(frequency, time, volume)

    @staticmethod
    def _playTone_unlocked(frequency: int, time: int, volume: int) -> None:
        if Features.getInstance().isFeature(GameFeatureFactory.getInstance().SOUND):
            Manager.playTone(frequency, time, volume)
# from java.io.InputStream import InputStream
# from javax.microedition.media.Manager import Manager
# from javax.microedition.media.MediaException import MediaException
# from javax.microedition.media.Player import Player
from org.allbinary.TsUtil import TsUtil
from org.allbinary.audio.AudioContentTypeDataFactory import AudioContentTypeDataFactory
from org.allbinary.data.resource.ResourceUtil import ResourceUtil
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.GameFeatureFactory import GameFeatureFactory
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


