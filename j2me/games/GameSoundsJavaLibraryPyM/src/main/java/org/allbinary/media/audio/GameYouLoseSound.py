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

from org.allbinary.media.audio.CompositeSound import CompositeSound


#Use 8hz16bitmono for most J2ME
class GameYouLoseSound(CompositeSound):
    soundInterface: Sound = None
    

    def __init__(self) -> None:
        super().__init__("resource:/wav/youlose.wav")
    

    @staticmethod
    def getInstance() -> Sound:
        return GameYouLoseSound.soundInterface


GameYouLoseSound.soundInterface = GameYouLoseSound()

