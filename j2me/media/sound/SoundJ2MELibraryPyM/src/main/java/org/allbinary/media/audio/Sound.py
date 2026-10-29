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

from org.allbinary.media.audio.SoundInterface import SoundInterface


class Sound(SoundInterface, object):

    def _init_fields(self) -> None:
        self.resource: str = None
        self.player: Player = NoPlayer.NO_PLAYER
    

    def __init__(self, resource: str) -> None:
        self._init_fields()
        self.resource = resource
    

    def getResource(self) -> str:
        return self.resource
    

    def getPlayerP(self) -> Player:
        return self.player
    

    def setPlayerP(self, player: Player) -> None:
        self.player = player
    

    # throws Exception
    def init(self) -> None:
        pass
    

    def getDuration(self) -> int:
        return -1
    

    def run(self) -> None:
        try:
            self.player.start()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            PreLogUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN)
# from javax.microedition.media.Player import Player
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.media.audio.NoPlayer import NoPlayer


