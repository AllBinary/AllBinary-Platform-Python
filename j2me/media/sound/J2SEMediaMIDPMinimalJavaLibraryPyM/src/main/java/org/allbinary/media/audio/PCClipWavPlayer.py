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
from java.lang.JavaRuntimeStatic import java_equals
from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_divide
import threading
from java.lang.JavaRuntimeStatic import java_bases
from javax.sound.sampled.LineListener import LineListener
from org.allbinary.media.audio.BasicPlayer import BasicPlayer


@java_inherited_overloads
class PCClipWavPlayer(*java_bases(BasicPlayer, LineListener)):
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("audioInputStream", None)
        vars(self).setdefault("clip", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "audioInputStream" not in vars(self): self.audioInputStream: AudioInputStream = None
        if "clip" not in vars(self): self.clip: Clip = None
    

    def __init__(self, inputStream: InputStream) -> None:
        __class__._java_defaults(self)
        from org.allbinary.media.audio.NullAudioFormat import NullAudioFormat
        from org.allbinary.media.audio.NullClip import NullClip
        from java.io.ByteArrayInputStream import ByteArrayInputStream
        from java.io.InputStream import InputStream
        from javax.sound.sampled.AudioInputStream import AudioInputStream
        from javax.sound.sampled.AudioSystem import AudioSystem
        from javax.sound.sampled.Clip import Clip
        from org.allbinary.logic.NullUtil import NullUtil
        super().__init__()
        __class__._init_fields(self)
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
        from org.allbinary.thread.ARunnable import ARunnable
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.thread.MusicThreadPool import MusicThreadPool
        _java_listener_owner = self
        class _JavaListenerN66744(ARunnable):
            
            

            def run(self) -> None:
                from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
                try:
                    (self if hasattr(self, "close2") else _java_listener_owner).close2()
                except Exception as e:
                    PreLogUtil.putOE((self if hasattr(self, "commonStrings") else _java_listener_owner).commonStrings.EXCEPTION, self, (self if hasattr(self, "commonStrings") else _java_listener_owner).commonStrings.PROCESS, e)
        MusicThreadPool.getInstance().runTask(_JavaListenerN66744()
            )
    

    # throws Exception
    def close2(self) -> None:
        self.clip.drain()
        self.clip.flush()
        self.clip.close()
    

    def getContentType(self) -> str:
        from org.allbinary.logic.string.StringUtil import StringUtil
        return StringUtil.getInstance().EMPTY_STRING
    

    # throws MediaException
    def start(self) -> None:
        with self._lock:
            return __class__.__dict__["_start_unlocked"].__get__(self, __class__)()

    def _start_unlocked(self) -> None:
        from org.allbinary.thread.ARunnable import ARunnable
        from javax.microedition.media.MediaException import MediaException
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.thread.MusicThreadPool import MusicThreadPool
        _java_listener_owner = self
        class _JavaListenerN67156(ARunnable):
            
            

            def run(self) -> None:
                from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
                try:
                    (self if hasattr(self, "start2") else _java_listener_owner).start2()
                except Exception as e:
                    PreLogUtil.putOE((self if hasattr(self, "commonStrings") else _java_listener_owner).commonStrings.EXCEPTION, self, (self if hasattr(self, "commonStrings") else _java_listener_owner).commonStrings.PROCESS, e)
        MusicThreadPool.getInstance().runTask(_JavaListenerN67156()
            )
    

    # throws Exception
    def start2(self) -> None:
        self.clip.setFramePosition(0)
        self.clip.loop(self.getLoopCount())
        self.clip.start()
        java_super_call(super(), "start")
    

    # throws Exception
    def create(self, audioInputStream: AudioInputStream) -> Clip:
        from javax.sound.sampled.AudioInputStream import AudioInputStream
        from javax.sound.sampled.AudioSystem import AudioSystem
        from javax.sound.sampled.Clip import Clip
        clip: Clip = AudioSystem.getClip()
        clip.addLineListener(self)
        clip.open(audioInputStream)
        return clip
    

    # throws MediaException
    def stop(self) -> None:
        with self._lock:
            return __class__.__dict__["_stop_unlocked"].__get__(self, __class__)()

    def _stop_unlocked(self) -> None:
        from org.allbinary.thread.ARunnable import ARunnable
        from javax.microedition.media.MediaException import MediaException
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.thread.MusicThreadPool import MusicThreadPool
        _java_listener_owner = self
        class _JavaListenerN67738(ARunnable):
            
            

            def run(self) -> None:
                from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
                try:
                    (self if hasattr(self, "stop2") else _java_listener_owner).stop2()
                except Exception as e:
                    PreLogUtil.putOE((self if hasattr(self, "commonStrings") else _java_listener_owner).commonStrings.EXCEPTION, self, (self if hasattr(self, "commonStrings") else _java_listener_owner).commonStrings.PROCESS, e)
        MusicThreadPool.getInstance().runTask(_JavaListenerN67738()
            )
    

    # throws Exception
    def stop2(self) -> None:
        self.clip.stop()
        java_super_call(super(), "stop")
    

    def getControl(self, controlType: str) -> Control:
        from org.allbinary.media.audio.NullControl import NullControl
        from javax.microedition.media.Control import Control
        return NullControl()
    

    def getControls(self) -> list[Control]:
        from javax.microedition.media.Control import Control
        return [None] * (0)
    

    def setVolume(self, leftVolume: int, rightVolume: int) -> None:
        self.setVolumeF((float(leftVolume)) / 100.0)
    

    def getVolume(self) -> float:
        from javax.sound.sampled.FloatControl import FloatControl
        masterGainFloatControl: FloatControl = self.clip.getControl(FloatControl.Type.MASTER_GAIN)
        return float(math.pow(10.0, masterGainFloatControl.getValue() / 20.0))
    

    def setVolumeF(self, volume: float) -> None:
        from javax.sound.sampled.FloatControl import FloatControl
        if volume < 0.0 or volume > 1.0:
            raise ValueError("Volume: " + str(volume))
        masterGainFloatControl: FloatControl = self.clip.getControl(FloatControl.Type.MASTER_GAIN)
        masterGainFloatControl.setValue(20.0 * float(math.log10(volume)))
    

    def getDuration(self) -> int:
        return java_divide(self.clip.getMicrosecondLength(), 1000)
            
    

    def update(self, event: LineEvent) -> None:
        from javax.microedition.media.PlayerListener import PlayerListener
        from javax.sound.sampled.LineEvent import LineEvent
        if java_equals(event.getType(), LineEvent.Type.STOP):
            size: int = self.listenersList.size()
            for index in range(0, size):
                listener: PlayerListener = self.listenersList.get(size)
                listener.playerUpdate(self, PlayerListener.END_OF_MEDIA, None)
# from org.allbinary.thread.ARunnable import ARunnable
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
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.thread.MusicThreadPool import MusicThreadPool


