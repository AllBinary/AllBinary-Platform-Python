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
# package org.allbinary.game.configuration

from __future__ import annotations



class GameSpeed:
    instance: GameSpeed = None
    

    def getSpeed(self) -> int:
        from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
        speedGameConfiguration: GameConfiguration = GameConfigurationCentral.getInstance().SPEED
        return (int(speedGameConfiguration.getMaxValue()) - int(speedGameConfiguration.getValue()) + 1)
    

    def getDelay(self) -> int:
        from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
        speedGameConfiguration: GameConfiguration = GameConfigurationCentral.getInstance().SPEED
        return 19 * (int(speedGameConfiguration.getMaxValue()) - int(speedGameConfiguration.getValue()))
    

    @staticmethod
    def getInstance() -> GameSpeed:
        return GameSpeed.instance


GameSpeed.instance = GameSpeed()

