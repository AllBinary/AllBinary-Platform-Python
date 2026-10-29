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
# package org.allbinary.game.ag.layer.pickup

from __future__ import annotations

from org.allbinary.game.layer.pickup.PickupLayer import PickupLayer
from org.allbinary.game.tick.TickableInterface import TickableInterface


class FallingPickupLayer(PickupLayer, TickableInterface):
    NAME: str = "FallingPickupLayer"
    

    def __init__(self, remoteInfo: RemoteInfo) -> None:
        super().__init__(FallingPickupLayer.NAME, remoteInfo, 0, CountedPickedUpLayerInterfaceFactory.NULL_COUNTED_PICKUP_LAYER_FACTORY, NullAnimationFactory.getFactoryInstance().getInstance(0), Rectangle(PointFactory.getInstance().ZERO_ZERO, 0, 0), ViewPosition.getInstanceD())
    

    def processTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        self.setPosition(self.x, self.y + 1, self.z)
    

    def implmentsTickableInterface(self) -> bool:
        return True
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.game.layer.pickup.CountedPickedUpLayerInterfaceFactory import CountedPickedUpLayerInterfaceFactory
from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.view.ViewPosition import ViewPosition


