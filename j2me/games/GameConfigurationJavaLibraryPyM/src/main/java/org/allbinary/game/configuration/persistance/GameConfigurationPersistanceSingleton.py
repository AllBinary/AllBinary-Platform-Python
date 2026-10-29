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
# package org.allbinary.game.configuration.persistance

from __future__ import annotations

from org.allbinary.game.configuration.persistance.KeyValuePersistance import KeyValuePersistance


class GameConfigurationPersistanceSingleton(KeyValuePersistance):
    GAME_PERSISTANCE: GameConfigurationPersistanceSingleton = None
    

    @staticmethod
    def getInstance() -> GameConfigurationPersistanceSingleton:
        return GameConfigurationPersistanceSingleton.GAME_PERSISTANCE
    

    def __init__(self) -> None:
        from org.allbinary.game.configuration.persistance.GamePersistanceStrings import GamePersistanceStrings
        super().__init__(GamePersistanceStrings.getInstance().SAVED_GAME_CONFIGURATION_RECORD_ID)


GameConfigurationPersistanceSingleton.GAME_PERSISTANCE = GameConfigurationPersistanceSingleton()

