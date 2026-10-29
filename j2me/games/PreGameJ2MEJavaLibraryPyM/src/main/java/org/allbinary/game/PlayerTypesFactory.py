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



class PlayerTypesFactory:
    SINGLETON: PlayerTypesFactory = None

    def _init_fields(self) -> None:
        self.PLAYER_TYPE_ONE: PlayerType = PlayerType("Player Type One", 0)
        self.PLAYER_TYPE_TWO: PlayerType = PlayerType("Player Type Two", 1)
        self.PLAYER_TYPE_THREE: PlayerType = PlayerType("Player Type Three", 2)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PlayerTypesFactory:
        return PlayerTypesFactory.SINGLETON
from org.allbinary.game.PlayerType import PlayerType


PlayerTypesFactory.SINGLETON = PlayerTypesFactory()

