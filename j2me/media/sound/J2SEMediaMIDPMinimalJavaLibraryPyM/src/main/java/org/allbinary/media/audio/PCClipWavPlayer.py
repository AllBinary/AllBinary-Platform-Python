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

import math
import threading
# from javax.sound.sampled.LineListener import LineListener
from org.allbinary.media.audio.BasicPlayer import BasicPlayer


class PCClipWavPlayer(BasicPlayer, LineListener):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.audioInputStream: AudioInputStream = None
        self.clip: Clip = None
    

    def __init__(self, inputStream: InputStream) -> None:
        from org.allbinary.media.audio.NullAudioFormat import NullAudioFormat
        from org.allbinary.media.audio.NullClip import NullClip
        super().__init__()
        self._init_fields()
        audioInputStream: AudioInputStream = AudioInputStream(ByteArrayInputStream(NullUtil.getInstance().NULL_BYTE_ARRAY), NullAudioFormat.NULL_AUDIO_FORMAT, 0)
        clip: Clip = NullClip()
        try:
            audioInputStream = AudioSystem.getAudioInputStream(inputStream)
            clip = self.create(audioInputStream)
            if clip is None:
                self.logUtil.put("Clip was null", self, self.commonStrings.CONSTRUCTOR, Exception())
                raise RuntimeError()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
        self.audioInputStream = audioInputStream
        self.clip = clip
    

    def close(self) -> None:
        MusicThreadPool.getInstance().runTask((ARunnable()  # Java anonymous class body:
#             
# 
#             def run(self) -> None:
#                 try:
#                     self.close2()
#                 except Exception as e:
#                     PreLogUtil.putOE(self.commonStrings.EXCEPTION, self, self.commonStrings.PROCESS, e)
))
    

    # throws Exception
    def close2(self) -> None:
        self.clip.drain()
        self.clip.flush()
        self.clip.close()
    

    def getContentType(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    # throws MediaException
    def start(self) -> None:
        with self._lock:
            return self._start_unlocked()

    def _start_unlocked(self) -> None:
        MusicThreadPool.getInstance().runTask((ARunnable()  # Java anonymous class body:
#             
# 
#             def run(self) -> None:
#                 try:
#                     self.start2()
#                 except Exception as e:
#                     PreLogUtil.putOE(self.commonStrings.EXCEPTION, self, self.commonStrings.PROCESS, e)
))
    

    # throws Exception
    def start2(self) -> None:
        self.clip.setFramePosition(0)
        self.clip.loop(self.getLoopCount())
        self.clip.start()
        super().start()
    

    # throws Exception
    def create(self, audioInputStream: AudioInputStream) -> Clip:
        clip: Clip = AudioSystem.getClip()
        clip.addLineListener(self)
        clip.open(audioInputStream)
        return clip
    

    # throws MediaException
    def stop(self) -> None:
        with self._lock:
            return self._stop_unlocked()

    def _stop_unlocked(self) -> None:
        MusicThreadPool.getInstance().runTask((ARunnable()  # Java anonymous class body:
#             
# 
#             def run(self) -> None:
#                 try:
#                     self.stop2()
#                 except Exception as e:
#                     PreLogUtil.putOE(self.commonStrings.EXCEPTION, self, self.commonStrings.PROCESS, e)
))
    

    # throws Exception
    def stop2(self) -> None:
        self.clip.stop()
        super().stop()
    

    def getControl(self, controlType: str) -> Control:
        from org.allbinary.media.audio.NullControl import NullControl
        return NullControl()
    

    def getControls(self) -> list[Control]:
        return [None] * (0)
    

    def setVolume(self, leftVolume: int, rightVolume: int) -> None:
        self.setVolumeF((float(leftVolume)) / 100.0)
    

    def getVolume(self) -> float:
        masterGainFloatControl: FloatControl = self.clip.getControl(FloatControl.Type.MASTER_GAIN)
        return float(math.pow(10.0, masterGainFloatControl.getValue() / 20.0))
    

    def setVolumeF(self, volume: float) -> None:
        if volume < 0.0 or volume > 1.0:
            raise ValueError("Volume: " + str(volume))
        masterGainFloatControl: FloatControl = self.clip.getControl(FloatControl.Type.MASTER_GAIN)
        masterGainFloatControl.setValue(20.0 * float(math.log10(volume)))
    

    def getDuration(self) -> int:
        return self.clip.getMicrosecondLength() / 1000
    

    def update(self, event: LineEvent) -> None:
        if event.getType().equals(LineEvent.Type.STOP):
            size: int = self.listenersList.size()
            for index in range(0, size):
                listener: PlayerListener = self.listenersList.get(size)
                listener.playerUpdate(self, PlayerListener.END_OF_MEDIA, None)
from org.allbinary.thread.ARunnable import ARunnable
# from java.io.ByteArrayInputStream import ByteArrayInputStream
# from java.io.InputStream import InputStream
# from javax.microedition.media.Control import Control
# from javax.microedition.media.MediaException import MediaException
# from javax.microedition.media.PlayerListener import PlayerListener
# from javax.sound.sampled.AudioInputStream import AudioInputStream
# from javax.sound.sampled.AudioSystem import AudioSystem
# from javax.sound.sampled.Clip import Clip
# from javax.sound.sampled.FloatControl import FloatControl
# from javax.sound.sampled.LineEvent import LineEvent
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.thread.MusicThreadPool import MusicThreadPool


