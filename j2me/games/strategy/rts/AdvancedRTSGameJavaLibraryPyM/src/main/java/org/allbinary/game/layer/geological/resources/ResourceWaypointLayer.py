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
# package org.allbinary.game.layer.geological.resources

from __future__ import annotations

from org.allbinary.game.layer.waypoint.WaypointLayer import WaypointLayer


class ResourceWaypointLayer(WaypointLayer):
    

    def __init__(self, remoteInfo: RemoteInfo, parentLayer: PathFindingLayerInterface, groupInterface: list[Group], rootName: str, name: str, animationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, proceduralAnimationInterfaceFactoryInterface: ProceduralAnimationInterfaceFactoryInterface, rectangle: Rectangle, x: int, y: int) -> None:
        super().__init__(remoteInfo, parentLayer, groupInterface, rootName, name, animationInterfaceFactoryInterface, proceduralAnimationInterfaceFactoryInterface, rectangle, x, y)
    

    def createHudPaintable(self) -> SelectionHudPaintable:
        from org.allbinary.game.layer.geological.resources.GeologicalResourceInfoHudPaintableSingleton import GeologicalResourceInfoHudPaintableSingleton
        rtsLayerHudPaintable: GeologicalResourceInfoHudPaintable = GeologicalResourceInfoHudPaintableSingleton.getInstance()
        rtsLayerHudPaintable.setBasicColorP(self.allBinaryGameLayerManagerP.getForegroundBasicColor())
        rtsLayerHudPaintable.setRtsLayer(self)
        return rtsLayerHudPaintable
    

    def getHudPaintable(self) -> SelectionHudPaintable:
        from org.allbinary.game.layer.geological.resources.GeologicalResourceInfoHudPaintableSingleton import GeologicalResourceInfoHudPaintableSingleton
        rtsLayerHudPaintable: GeologicalResourceInfoHudPaintable = GeologicalResourceInfoHudPaintableSingleton.getInstance()
        return rtsLayerHudPaintable
from org.allbinary.game.layer.SelectionHudPaintable import SelectionHudPaintable
from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface
from org.allbinary.animation.ProceduralAnimationInterfaceFactoryInterface import ProceduralAnimationInterfaceFactoryInterface
from org.allbinary.game.identification.Group import Group
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo


