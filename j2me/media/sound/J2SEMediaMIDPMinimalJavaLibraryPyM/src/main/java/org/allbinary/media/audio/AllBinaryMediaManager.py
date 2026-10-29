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


#J2SEMediaMIDPMinimalJavaLibrary
class AllBinaryMediaManager:
    THIS: str = "AllBinaryMediaManagerPC"
    CREATE_PLAYER: str = "createPlayer"
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
        from org.allbinary.media.audio.PCClipWavPlayer import PCClipWavPlayer
        from org.allbinary.media.audio.NoPlayer import NoPlayer
        if resource.startswith(Manager.TONE_DEVICE_LOCATOR):
            return AllBinaryMediaManager.createPlayerFromInputStream(ByteArrayInputStream(NullUtil.getInstance().NULL_BYTE_ARRAY), AudioContentTypeDataFactory.getInstance().MIME_AUDIO_TONE.getName())
        elif Features.getInstance().isFeature(GameFeatureFactory.getInstance().SOUND):
            try:
                inputStream: InputStream = ResourceUtil.getInstance().getResourceAsStream(resource)
                bufferedInputStream: BufferedInputStream = BufferedInputStream(inputStream)
                return PCClipWavPlayer(bufferedInputStream)
            except Exception as e:
                logUtil: LogUtil = LogUtil.getInstance()
                commonString: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonString.EXCEPTION, AllBinaryMediaManager.THIS, AllBinaryMediaManager.CREATE_PLAYER, e)
                return NoPlayer.NO_PLAYER
        else:
            return NoPlayer.NO_PLAYER
    

    # throws IOException, MediaException
    @staticmethod
    def createPlayerFromInputStream(stream: InputStream, type_: str) -> Player:
        raise MediaException("No Impl")
    

    # throws MediaException
    @staticmethod
    def playTone(frequency: int, time: int, volume: int) -> None:
        with AllBinaryMediaManager._lock:
            return AllBinaryMediaManager._playTone_unlocked(frequency, time, volume)

    @staticmethod
    def _playTone_unlocked(frequency: int, time: int, volume: int) -> None:
        raise MediaException("No Impl")
    

    @staticmethod
    def isInitialized() -> bool:
        return True
# from java.io.BufferedInputStream import BufferedInputStream
# from java.io.ByteArrayInputStream import ByteArrayInputStream
# from java.io.IOException import IOException
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
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


