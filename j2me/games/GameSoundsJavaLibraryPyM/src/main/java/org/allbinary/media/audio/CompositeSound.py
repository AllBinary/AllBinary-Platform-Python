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

from org.allbinary.media.audio.Sound import Sound


class CompositeSound(Sound):
    

    def __init__(self, resource: str) -> None:
        super().__init__(resource)
    

    # throws Exception
    def init(self) -> None:
        from org.allbinary.media.audio.PlayerComposite import PlayerComposite
        from org.allbinary.media.audio.AllBinaryMediaManager import AllBinaryMediaManager
        self.setPlayerP(PlayerComposite(AllBinaryMediaManager.createPlayer(self.getResource()), 570))


