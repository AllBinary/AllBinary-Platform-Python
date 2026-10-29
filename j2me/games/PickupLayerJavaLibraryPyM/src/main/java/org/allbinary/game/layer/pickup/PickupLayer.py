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

from org.allbinary.game.multiplayer.layer.MultiPlayerGameLayer import MultiPlayerGameLayer
from org.allbinary.game.layer.pickup.PickedUpLayerInterface import PickedUpLayerInterface
from org.allbinary.game.layer.pickup.PickupableInterface import PickupableInterface


class PickupLayer(MultiPlayerGameLayer, PickedUpLayerInterface, PickupableInterface):

    def _init_fields(self) -> None:
        self.pickedUpLayerInterfaceFactoryInterface: PickedUpLayerInterfaceFactoryInterface = CountedPickedUpLayerInterfaceFactory.NULL_COUNTED_PICKUP_LAYER_FACTORY
        self.destroyed: bool = False
        self.animationInterface: Animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
    

    def __init__(self, name: str, remoteInfo: RemoteInfo, total: int, pickedUpLayerInterfaceFactoryInterface: PickedUpLayerInterfaceFactoryInterface, animationInterface: Animation, rectangle: Rectangle, viewPosition: ViewPositionBase) -> None:
        super().__init__(remoteInfo, BasicGroupFactory.getInstance().NONE_ARRAY, name, rectangle, viewPosition)
        self._init_fields()
        self.setCollidableInferface(CollidableAlwaysPickupNeverCollideBehaviorFactory.getInstance().createBehavior())
        self.setLayerWidth(10)
        self.setLayerHeight(10)
        self.init(pickedUpLayerInterfaceFactoryInterface, animationInterface)
    

    def init(self, pickedUpLayerInterfaceFactoryInterface: PickedUpLayerInterfaceFactoryInterface, animationInterface: Animation) -> None:
        self.pickedUpLayerInterfaceFactoryInterface = pickedUpLayerInterfaceFactoryInterface
        self.animationInterface = animationInterface
        self.setDestroyed(False)
    

    def initXYZ(self, x: int, y: int, z: int) -> None:
        self.setPosition(x, y, z)
    

    def paint(self, graphics: Graphics) -> None:
        viewPosition: ViewPositionBase = self.getViewPosition()
        viewX: int = viewPosition.getX()
        viewY: int = viewPosition.getY()
        self.animationInterface.paintXY(graphics, viewX, viewY)
    

    def paintThreed(self, graphics: Graphics) -> None:
        viewPosition: ViewPositionBase = self.getViewPosition()
        viewX: int = viewPosition.getX()
        viewY: int = viewPosition.getY()
        self.animationInterface.paintThreedXYZ(graphics, viewX, viewY, 3)
    

    def getPickedUpLayerInterfaceFactoryInterface(self) -> PickedUpLayerInterfaceFactoryInterface:
        return self.pickedUpLayerInterfaceFactoryInterface
    

    def setPickedUp(self) -> None:
        self.setDestroyed(True)
    

    def isDestroyed(self) -> bool:
        return self.destroyed
    

    def setDestroyed(self, destroyed: bool) -> None:
        self.destroyed = destroyed
        if self.isDestroyed():
            DestroyedLayerProcessor.getInstance().add(self)
    

    def damage(self, damage: int, damageType: int) -> None:
        pass
    

    def getDamage(self, damageType: int) -> int:
        return 0
    

    # throws Exception
    def set(self, gl: GL) -> None:
        openGLSurfaceChangedInterface: OpenGLSurfaceChangedInterface = self.animationInterface
        openGLSurfaceChangedInterface.set(gl)
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.game.collision.CollidableAlwaysPickupNeverCollideBehaviorFactory import CollidableAlwaysPickupNeverCollideBehaviorFactory
from org.allbinary.game.combat.destroy.DestroyedLayerProcessor import DestroyedLayerProcessor
from org.allbinary.game.identification.BasicGroupFactory import BasicGroupFactory
from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.image.opengles.OpenGLSurfaceChangedInterface import OpenGLSurfaceChangedInterface
from org.allbinary.view.ViewPositionBase import ViewPositionBase
from org.allbinary.game.layer.pickup.CountedPickedUpLayerInterfaceFactory import CountedPickedUpLayerInterfaceFactory


