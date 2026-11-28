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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.game.layer.pickup.PickupLayer import PickupLayer


@java_inherited_overloads
class RaceTrackPickupLayer(PickupLayer):
    NAME: str = "RaceTrackPickupLayer"
    def _java_defaults(self):
        vars(self).setdefault("viewPositionEventHandler", None)

    def _init_fields(self) -> None:
        from org.allbinary.view.event.ViewPositionEventHandler import ViewPositionEventHandler
        self.viewPositionEventHandler: ViewPositionEventHandler = ViewPositionEventHandler.getInstance()
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.layer.pickup.CountedPickedUpLayerInterfaceFactory import CountedPickedUpLayerInterfaceFactory
        from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
        from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
        from org.allbinary.game.view.TileLayerPositionIntoViewPosition import TileLayerPositionIntoViewPosition
        from org.allbinary.graphics.PointFactory import PointFactory
        from org.allbinary.graphics.Rectangle import Rectangle
        super().__init__(RaceTrackPickupLayer.NAME, RemoteInfo.REMOTE_INFO, 0, CountedPickedUpLayerInterfaceFactory.NULL_COUNTED_PICKUP_LAYER_FACTORY, NullAnimationFactory.getFactoryInstance().getInstance(0), Rectangle(PointFactory.getInstance().ZERO_ZERO, 0, 0), TileLayerPositionIntoViewPosition())
        __class__._init_fields(self)
    

    def setTiledLayer(self, tiledLayer: AllBinaryTiledLayer) -> None:
        from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
        from org.allbinary.game.view.TileLayerPositionIntoViewPosition import TileLayerPositionIntoViewPosition
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        viewPosition: TileLayerPositionIntoViewPosition = self.getViewPosition()
        viewPosition.setTiledLayer(tiledLayer)
        self.viewPositionEventHandler.addListener(self)
    

    def setDestroyed(self, destroyed: bool) -> None:
        java_super_call(super(), "setDestroyed", destroyed)
        if java_predicate(self, "isDestroyed"):
            self.viewPositionEventHandler.removeListener(self)
# from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
# from org.allbinary.game.identification.BasicGroupFactory import BasicGroupFactory
# from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
# from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
# from org.allbinary.game.view.TileLayerPositionIntoViewPosition import TileLayerPositionIntoViewPosition
# from org.allbinary.graphics.PointFactory import PointFactory
# from org.allbinary.graphics.Rectangle import Rectangle
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.view.ViewPosition import ViewPosition
# from org.allbinary.view.event.ViewPositionEventHandler import ViewPositionEventHandler


