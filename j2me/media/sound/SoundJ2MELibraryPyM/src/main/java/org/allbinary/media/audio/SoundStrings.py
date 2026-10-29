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



class SoundStrings:
    instance: SoundStrings = None

    def _init_fields(self) -> None:
        self.STOP_ALL: str = "stopAll"
        self.CLOSE_ALL: str = "closeAll"
        self.SOUND: str = " Sound: "
        self.INIT_SOUND: str = "Initializing Sound: "
        self.STOPPING_SOUND: str = "Stopping Sound: "
        self.CLOSING_SOUND: str = "Closing Sound: "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> SoundStrings:
        return SoundStrings.instance


SoundStrings.instance = SoundStrings()

