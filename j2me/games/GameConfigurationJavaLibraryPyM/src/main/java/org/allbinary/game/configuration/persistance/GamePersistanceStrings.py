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
# package org.allbinary.game.configuration.persistance

from __future__ import annotations



class GamePersistanceStrings:
    instance: GamePersistanceStrings = None

    def _init_fields(self) -> None:
        self.SAVED_GAME_RECORD_ID: str = "_SG"
        self.SAVED_GAME_CONFIGURATION_RECORD_ID: str = "_SGC"
        self.DEFAULT_INPUT_MAPPING_RECORD_ID: str = "_DIM"
        self.SAVED_INPUT_CONFIGURATION_RECORD_ID: str = "_SIC"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GamePersistanceStrings:
        return GamePersistanceStrings.instance


GamePersistanceStrings.instance = GamePersistanceStrings()

