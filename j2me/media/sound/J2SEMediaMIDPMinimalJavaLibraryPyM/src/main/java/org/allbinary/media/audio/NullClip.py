# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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

# from javax.sound.sampled.BooleanControl import BooleanControl
# from javax.sound.sampled.Clip import Clip
# from javax.sound.sampled.Control.Type import Type
from org.allbinary.media.audio.NullJ2SEControl import NullJ2SEControl


class NullClip(Clip):
    NULL_CONTROL: NullJ2SEControl = NullJ2SEControl(BooleanControl.Type.MUTE)
    

    # throws LineUnavailableException
    def open(self, format: AudioFormat, data: list[int], offset: int, bufferSize: int) -> None:
        pass
    

    # throws LineUnavailableException, IOException
    # Java overloaded method: Python keeps the last definition
    def open(self, stream: AudioInputStream) -> None:
        pass
    

    def getFrameLength(self) -> int:
        return 0
    

    def getMicrosecondLength(self) -> int:
        return 0
    

    def setFramePosition(self, frames: int) -> None:
        pass
    

    def setMicrosecondPosition(self, microseconds: int) -> None:
        pass
    

    def setLoopPoints(self, start: int, end: int) -> None:
        pass
    

    def loop(self, count: int) -> None:
        pass
    

    def drain(self) -> None:
        pass
    

    def flush(self) -> None:
        pass
    

    def start(self) -> None:
        pass
    

    def stop(self) -> None:
        pass
    

    def isRunning(self) -> bool:
        return False
    

    def isActive(self) -> bool:
        return False
    

    def getFormat(self) -> AudioFormat:
        from org.allbinary.media.audio.NullAudioFormat import NullAudioFormat
        return NullAudioFormat.NULL_AUDIO_FORMAT
    

    def getBufferSize(self) -> int:
        return 0
    

    def available(self) -> int:
        return 0
    

    def getFramePosition(self) -> int:
        return 0
    

    def getLongFramePosition(self) -> int:
        return 0
    

    def getMicrosecondPosition(self) -> int:
        return 0
    

    def getLevel(self) -> float:
        return 0.0
    

    def getLineInfo(self) -> Info:
        from org.allbinary.media.audio.NullAudioFormat import NullAudioFormat
        return Info(type(self), NullAudioFormat.NULL_AUDIO_FORMAT)
    

    # throws LineUnavailableException
    # Java overloaded method: Python keeps the last definition
    def open(self) -> None:
        pass
    

    def close(self) -> None:
        pass
    

    def isOpen(self) -> bool:
        return False
    

    def getControls(self) -> list[Control]:
        return [None] * (0)
    

    def isControlSupported(self, control: Type) -> bool:
        return False
    

    def getControl(self, control: Type) -> Control:
        return NullClip.NULL_CONTROL
    

    def addLineListener(self, listener: LineListener) -> None:
        pass
    

    def removeLineListener(self, listener: LineListener) -> None:
        pass
# from java.io.IOException import IOException
# from javax.sound.sampled.AudioFormat import AudioFormat
# from javax.sound.sampled.AudioInputStream import AudioInputStream
# from javax.sound.sampled.Control import Control
# from javax.sound.sampled.Line.Info import Info
# from javax.sound.sampled.LineListener import LineListener
# from javax.sound.sampled.LineUnavailableException import LineUnavailableException


