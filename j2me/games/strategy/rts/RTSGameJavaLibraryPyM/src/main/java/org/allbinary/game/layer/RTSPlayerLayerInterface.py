# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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
# package org.allbinary.game.layer

from __future__ import annotations

from org.allbinary.game.ag.layer.hud.basic.notification.GameNotificationHudCompositeInterface import GameNotificationHudCompositeInterface
from org.allbinary.game.input.BuildMenuCompositeInterface import BuildMenuCompositeInterface
from org.allbinary.game.combat.destroy.event.DestroyedEventListenerInterface import DestroyedEventListenerInterface
from org.allbinary.game.input.PlayerGameInputCompositeInterface import PlayerGameInputCompositeInterface
from org.allbinary.game.tick.TickableInterface import TickableInterface
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface


# Java interface
class RTSPlayerLayerInterface(GameNotificationHudCompositeInterface, BuildMenuCompositeInterface, PlayerGameInputCompositeInterface, DestroyedEventListenerInterface, TickableInterface, PathFindingLayerInterface):
    

    def getCapital(self) -> Capital:
        raise NotImplementedError()
    

    def getRTSFormInput(self) -> RTSFormInput:
        raise NotImplementedError()
    

    def add(self, sound: Sound) -> None:
        raise NotImplementedError()
    

    def getPlayerOwnedRTSLayers(self) -> PlayerOwnedRTSLayers:
        raise NotImplementedError()
    

    def implmentsArtificialIntelligenceCompositeInterface(self) -> bool:
        raise NotImplementedError()
from org.allbinary.game.input.form.RTSFormInput import RTSFormInput
from org.allbinary.game.layer.capital.Capital import Capital
from org.allbinary.media.audio.Sound import Sound


