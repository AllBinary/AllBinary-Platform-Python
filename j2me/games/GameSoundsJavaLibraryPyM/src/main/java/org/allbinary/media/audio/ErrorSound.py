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

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.media.audio.CompositeSound import CompositeSound


class ErrorSound(CompositeSound):
    soundInterface: Sound = None
    

    def __init__(self) -> None:
        super().__init__("resource:/wav/error.wav")
    

    @staticmethod
    def getInstance() -> Sound:
        return ErrorSound.soundInterface


def _ErrorSound_soundInterface() -> object:
    return ErrorSound()

lazy_static(ErrorSound, "soundInterface", _ErrorSound_soundInterface)

