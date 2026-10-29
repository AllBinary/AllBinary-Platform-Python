# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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
# package org.allbinary.game.layer.waypoint

from __future__ import annotations

from org.allbinary.game.layer.AdvancedRTSGameLayer import AdvancedRTSGameLayer


class WaypointLayer(AdvancedRTSGameLayer):
    

    def __init__(self, remoteInfo: RemoteInfo, parentLayer: PathFindingLayerInterface, groupInterface: list[Group], rootName: str, name: str, animationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, proceduralAnimationInterfaceFactoryInterface: ProceduralAnimationInterfaceFactoryInterface, rectangle: Rectangle, x: int, y: int) -> None:
        from org.allbinary.game.layer.waypoint.CollidableWaypointBehavior import CollidableWaypointBehavior
        from org.allbinary.game.layer.waypoint.Waypoint import Waypoint
        super().__init__(remoteInfo, parentLayer, AdvancedRTSProperties.createProperties(), groupInterface, rootName, name, Health(1000), NullRTSFormInputFactory.getInstance(), animationInterfaceFactoryInterface, animationInterfaceFactoryInterface, animationInterfaceFactoryInterface, animationInterfaceFactoryInterface, animationInterfaceFactoryInterface, proceduralAnimationInterfaceFactoryInterface, rectangle, x, y, TileLayerPositionIntoViewPosition())
        self.setCollidableInferface(CollidableWaypointBehavior(True))
        self.getWaypointBehavior().setWaypoint(Waypoint(self, AttackSound.getInstance()))
        self.setAnimationInterface(self.indexedButShouldBeRotationAnimationInterface)
    

    def construct(self, rtsPlayerLayerInterface: RTSPlayerLayerInterface) -> None:
        self.percentCompleteP = 100
        self.initVisibility(rtsPlayerLayerInterface)
    

    def paint(self, graphics: Graphics) -> None:
        if self.isVisible():
            super().paint(graphics)
    

    def processTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        try:
            self.indexedButShouldBeRotationAnimationInterface.nextFrame()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "processTick", e)
    

    def damage(self, damage: int, damageType: int) -> None:
        pass
    

    # throws Exception
    def getDamage(self, damageType: int) -> int:
        return 0
    

    # throws Exception
    def setDestroyed(self, destroyed: bool) -> None:
        from org.allbinary.game.layer.waypoint.WaypointCellPositionHistory import WaypointCellPositionHistory
        super().setDestroyed(destroyed)
        if self.isDestroyed():
            WaypointCellPositionHistory.getInstance().removeLayer(self)
    

    def getType(self) -> int:
        return WaypointLayer.getStaticType()
    

    @staticmethod
    def getStaticType() -> int:
        return 4
    

    def isSelfUpgradeable(self) -> bool:
        return False
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface
from org.allbinary.animation.ProceduralAnimationInterfaceFactoryInterface import ProceduralAnimationInterfaceFactoryInterface
from org.allbinary.game.health.Health import Health
from org.allbinary.game.identification.Group import Group
from org.allbinary.game.input.form.NullRTSFormInputFactory import NullRTSFormInputFactory
from org.allbinary.game.layer.AdvancedRTSProperties import AdvancedRTSProperties
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
from org.allbinary.game.view.TileLayerPositionIntoViewPosition import TileLayerPositionIntoViewPosition
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.game.layer.RTSPlayerLayerInterface import RTSPlayerLayerInterface
from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
from org.allbinary.media.audio.AttackSound import AttackSound


