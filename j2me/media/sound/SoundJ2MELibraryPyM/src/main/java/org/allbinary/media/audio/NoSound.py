# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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

from org.allbinary.media.audio.Sound import Sound


class NoSound(Sound):
    instance: NoSound = None
    

    @staticmethod
    def getInstance() -> NoSound:
        return NoSound.instance
    

    def __init__(self) -> None:
        from org.allbinary.media.audio.NoPlayer import NoPlayer
        super().__init__(StringUtil.getInstance().EMPTY_STRING)
        self.setPlayerP(NoPlayer.NO_PLAYER)
from org.allbinary.logic.string.StringUtil import StringUtil


NoSound.instance = NoSound()

