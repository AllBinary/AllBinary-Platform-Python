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

# from javax.microedition.lcdui.Gauge import Gauge


class GameConfigurationGauge(Gauge):
    

    def __init__(self, gameConfiguration: GameConfiguration) -> None:
        super().__init__(gameConfiguration.getName(), gameConfiguration.isModifiable(), int(gameConfiguration.getMaxValue()) - int(gameConfiguration.getMinValue()), int(gameConfiguration.getValue()) - int(gameConfiguration.getMinValue()))


