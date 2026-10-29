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
# package org.allbinary.game.layer.pickup

from __future__ import annotations

from org.allbinary.game.layer.pickup.PickupLayer import PickupLayer


class RaceTrackPickupLayer(PickupLayer):
    NAME: str = "RaceTrackPickupLayer"

    def _init_fields(self) -> None:
        self.viewPositionEventHandler: ViewPositionEventHandler = ViewPositionEventHandler.getInstance()
    

    def __init__(self) -> None:
        from org.allbinary.game.layer.pickup.CountedPickedUpLayerInterfaceFactory import CountedPickedUpLayerInterfaceFactory
        super().__init__(RaceTrackPickupLayer.NAME, RemoteInfo.REMOTE_INFO, 0, CountedPickedUpLayerInterfaceFactory.NULL_COUNTED_PICKUP_LAYER_FACTORY, NullAnimationFactory.getFactoryInstance().getInstance(0), Rectangle(PointFactory.getInstance().ZERO_ZERO, 0, 0), TileLayerPositionIntoViewPosition())
        self._init_fields()
    

    def setTiledLayer(self, tiledLayer: AllBinaryTiledLayer) -> None:
        viewPosition: TileLayerPositionIntoViewPosition = self.getViewPosition()
        viewPosition.setTiledLayer(tiledLayer)
        self.viewPositionEventHandler.addListener(self)
    

    def setDestroyed(self, destroyed: bool) -> None:
        super().setDestroyed(destroyed)
        if self.isDestroyed():
            self.viewPositionEventHandler.removeListener(self)
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.game.identification.BasicGroupFactory import BasicGroupFactory
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
from org.allbinary.game.view.TileLayerPositionIntoViewPosition import TileLayerPositionIntoViewPosition
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.view.ViewPosition import ViewPosition
from org.allbinary.view.event.ViewPositionEventHandler import ViewPositionEventHandler


