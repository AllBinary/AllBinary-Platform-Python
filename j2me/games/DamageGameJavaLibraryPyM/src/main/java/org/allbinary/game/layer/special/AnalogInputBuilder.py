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



class AnalogInputBuilder:
    instance: AnalogInputBuilder = None
    

    @staticmethod
    def getInstance() -> AnalogInputBuilder:
        return AnalogInputBuilder.instance
    

    def disable(self, inputProcessorArray: list[GameInputProcessor], collidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer) -> None:
        from org.allbinary.game.layer.special.SpecialUpGameInputProcessor import SpecialUpGameInputProcessor
        from org.allbinary.game.layer.special.SpecialDownGameInputProcessor import SpecialDownGameInputProcessor
        from org.allbinary.game.layer.special.SpecialRightGameInputProcessor import SpecialRightGameInputProcessor
        from org.allbinary.game.layer.special.SpecialLeftGameInputProcessor import SpecialLeftGameInputProcessor
        from org.allbinary.game.layer.special.Special1GameInputProcessor import Special1GameInputProcessor
        from org.allbinary.game.layer.special.Special3GameInputProcessor import Special3GameInputProcessor
        inputProcessorArray[Canvas.UP] = SpecialUpGameInputProcessor(collidableDestroyableDamageableLayer)
        inputProcessorArray[Canvas.DOWN] = SpecialDownGameInputProcessor(collidableDestroyableDamageableLayer)
        inputProcessorArray[Canvas.RIGHT] = SpecialRightGameInputProcessor(collidableDestroyableDamageableLayer)
        inputProcessorArray[Canvas.LEFT] = SpecialLeftGameInputProcessor(collidableDestroyableDamageableLayer)
        inputProcessorArray[Canvas.KEY_NUM0] = Special1GameInputProcessor(collidableDestroyableDamageableLayer)
        inputProcessorArray[Canvas.KEY_NUM5] = Special3GameInputProcessor(collidableDestroyableDamageableLayer)
    

    def enable(self, inputProcessorArray: list[GameInputProcessor], collidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer) -> None:
        from org.allbinary.game.layer.special.SpecialAnalogUpGameInputProcessor import SpecialAnalogUpGameInputProcessor
        from org.allbinary.game.layer.special.SpecialAnalogDownGameInputProcessor import SpecialAnalogDownGameInputProcessor
        from org.allbinary.game.layer.special.SpecialAnalogRightGameInputProcessor import SpecialAnalogRightGameInputProcessor
        from org.allbinary.game.layer.special.SpecialAnalogLeftGameInputProcessor import SpecialAnalogLeftGameInputProcessor
        from org.allbinary.game.layer.special.SpecialAnalogLeftTriggerGameInputProcessor import SpecialAnalogLeftTriggerGameInputProcessor
        from org.allbinary.game.layer.special.SpecialAnalogRightTriggerGameInputProcessor import SpecialAnalogRightTriggerGameInputProcessor
        inputProcessorArray[Canvas.UP] = SpecialAnalogUpGameInputProcessor(collidableDestroyableDamageableLayer)
        inputProcessorArray[Canvas.DOWN] = SpecialAnalogDownGameInputProcessor(collidableDestroyableDamageableLayer)
        inputProcessorArray[Canvas.RIGHT] = SpecialAnalogRightGameInputProcessor(collidableDestroyableDamageableLayer)
        inputProcessorArray[Canvas.LEFT] = SpecialAnalogLeftGameInputProcessor(collidableDestroyableDamageableLayer)
        inputProcessorArray[Canvas.KEY_NUM0] = SpecialAnalogLeftTriggerGameInputProcessor(collidableDestroyableDamageableLayer)
        inputProcessorArray[Canvas.KEY_NUM5] = SpecialAnalogRightTriggerGameInputProcessor(collidableDestroyableDamageableLayer)
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.game.input.GameInputProcessor import GameInputProcessor


AnalogInputBuilder.instance = AnalogInputBuilder()

