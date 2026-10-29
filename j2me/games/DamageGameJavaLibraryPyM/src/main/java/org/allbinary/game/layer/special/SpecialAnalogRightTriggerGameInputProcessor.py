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
# package org.allbinary.game.layer.special

from __future__ import annotations

from org.allbinary.game.layer.special.SpecialGameInputProcessor import SpecialGameInputProcessor


class SpecialAnalogRightTriggerGameInputProcessor(SpecialGameInputProcessor):
    

    def __init__(self, collidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer) -> None:
        super().__init__(collidableDestroyableDamageableLayer)
    

    # throws Exception
    def processAnalog(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent, yAnalogValue: int) -> None:
        self.collidableDestroyableDamageableLayer.rightTrigger(allbinaryLayerManager, gameKeyEvent, yAnalogValue)
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


