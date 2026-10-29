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
# package org.allbinary.game

from __future__ import annotations



class GameInfoData:
    instance: GameInfoData = None

    def _init_fields(self) -> None:
        self.GAME_TYPE: str = "GAME_TYPE"
        self.GAME_MODE: str = "GAME_MODE"
        self.PLAYER_TYPE: str = "PLAYER_TYPE"
        self.HIGHEST_LEVEL: str = "HIGHEST_LEVEL"
        self.CURRENT_LEVEL: str = "CURRENT_LEVEL"
        self.SOFTWARE_INFORMATION: str = "SOFTWARE_INFORMATION"
    

    @staticmethod
    def getInstance() -> GameInfoData:
        return GameInfoData.instance
    

    def __init__(self) -> None:
        self._init_fields()


GameInfoData.instance = GameInfoData()

