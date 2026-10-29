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
# package org.allbinary.game.multiplayer.layer

from __future__ import annotations

from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.game.multiplayer.layer.MultiPlayerGameLayerInterface import MultiPlayerGameLayerInterface


class MultiPlayerGameLayer(CollidableDestroyableDamageableLayer, MultiPlayerGameLayerInterface):
    

    def __init__(self, remoteInfo: RemoteInfo, groupInterface: list[Group], name: str, layerInfo: Rectangle, viewPosition: ViewPositionBase) -> None:
        super().__init__(groupInterface, name, layerInfo, viewPosition)
    

    def getMultiplayerBehavior(self) -> MultiplayerBehavior:
        from org.allbinary.game.multiplayer.layer.MultiplayerBehavior import MultiplayerBehavior
        return MultiplayerBehavior.NULL_MULTIPLAYER_BEHAVIOR
    

    def setPingInfo(self, show: bool) -> None:
        pass
    

    def setFiring(self, firing: int) -> None:
        pass
    

    def getFiring(self) -> int:
        return 0
from org.allbinary.game.identification.Group import Group
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.view.ViewPositionBase import ViewPositionBase


