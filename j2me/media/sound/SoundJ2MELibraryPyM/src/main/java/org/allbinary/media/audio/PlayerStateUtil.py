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



class PlayerStateUtil:
    instance: PlayerStateUtil = None

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.UNREALIZED: str = "UNREALIZED"
        self.REALIZED: str = "REALIZED"
        self.PREFETCHED: str = "PREFETCHED"
        self.STARTED: str = "STARTED"
        self.CLOSED: str = "CLOSED"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PlayerStateUtil:
        return PlayerStateUtil.instance
    

    def convert(self, state: int) -> str:
        if state == Player.UNREALIZED:
            return self.UNREALIZED
        elif state == Player.REALIZED:
            return self.REALIZED
        elif state == Player.PREFETCHED:
            return self.PREFETCHED
        elif state == Player.STARTED:
            return self.STARTED
        elif state == Player.CLOSED:
            return self.CLOSED
        return self.commonStrings.UNKNOWN
# from javax.microedition.media.Player import Player
from org.allbinary.string.CommonStrings import CommonStrings


PlayerStateUtil.instance = PlayerStateUtil()

