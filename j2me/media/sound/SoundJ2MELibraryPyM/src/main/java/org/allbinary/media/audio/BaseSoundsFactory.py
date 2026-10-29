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

from org.allbinary.media.audio.SoundsFactoryInterface import SoundsFactoryInterface


class BaseSoundsFactory(SoundsFactoryInterface):

    def _init_fields(self) -> None:
        self.initialized: bool = False

    def __init__(self) -> None:
        self._init_fields()
    

    def init(self) -> None:
        pass
    

    # throws Exception
    def getSoundInterfaceArray(self) -> list[Sound]:
        return [None] * (0)
    

    def setInitialized(self, initialized: bool) -> None:
        self.initialized = initialized
    

    def isInitialized(self) -> bool:
        return self.initialized


