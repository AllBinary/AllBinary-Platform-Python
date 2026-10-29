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
# package org.allbinary.media.audio.music

from __future__ import annotations



class MusicManagerFactory:
    

    @staticmethod
    def createMusicManager(soundList: BasicArrayList) -> MusicManager:
        from org.allbinary.media.audio.music.MusicManager import MusicManager
        return MusicManager(MusicService, soundList)
from org.allbinary.util.BasicArrayList import BasicArrayList


