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

from org.allbinary.media.audio.BaseSoundsFactory import BaseSoundsFactory


class EarlySoundsFactory(BaseSoundsFactory):
    instance: EarlySoundsFactory = None

    def __init__(self) -> None:
        super().__init__()
    

    # throws Exception
    def getSoundInterfaceArray(self) -> list[Sound]:
        from org.allbinary.media.audio.SelectSound import SelectSound
        from org.allbinary.media.audio.ErrorSound import ErrorSound
        soundInterfaceArray: list[Sound] = [None] * (2)
        index: int = 0
        soundInterfaceArray[((index := index + 1) - 1)] = SelectSound.getInstance()
        soundInterfaceArray[((index := index + 1) - 1)] = ErrorSound.getInstance()
        return soundInterfaceArray
    

    @staticmethod
    def getInstance() -> EarlySoundsFactory:
        return EarlySoundsFactory.instance


EarlySoundsFactory.instance = EarlySoundsFactory()

