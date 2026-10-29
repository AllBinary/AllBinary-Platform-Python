# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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

from org.allbinary.game.layer.VehicleLayerInterface import VehicleLayerInterface


class NullVehicleLayer(VehicleLayerInterface):
    NULL_VEHICLE_LAYER: NullVehicleLayer = None
    

    def getName(self) -> str:
        raise RuntimeError()
    

    def getGroupInterface(self) -> list[Group]:
        raise RuntimeError()
    

    def setPosition(self, x: int, y: int, z: int) -> None:
        raise RuntimeError()
    

    def getHeight(self) -> int:
        raise RuntimeError()
    

    def getWidth(self) -> int:
        raise RuntimeError()
    

    def getHalfHeight(self) -> int:
        raise RuntimeError()
    

    def getHalfWidth(self) -> int:
        raise RuntimeError()
    

    def getXP(self) -> int:
        raise RuntimeError()
    

    def getYP(self) -> int:
        raise RuntimeError()
    

    def getZP(self) -> int:
        raise RuntimeError()
    

    def getX2(self) -> int:
        raise RuntimeError()
    

    def getY2(self) -> int:
        raise RuntimeError()
    

    def getZ2(self) -> int:
        raise RuntimeError()
    

    def isVisible(self) -> bool:
        raise RuntimeError()
    

    def moveDXYZ(self, dx: int, dy: int, dz: int) -> None:
        raise RuntimeError()
    

    def setVisible(self, visible: bool) -> None:
        raise RuntimeError()
    

    def implmentsTickableInterface(self) -> bool:
        raise RuntimeError()
    

    def implmentsCollidableInterface(self) -> bool:
        raise RuntimeError()
    

    def implmentsGameInputInterface(self) -> bool:
        raise RuntimeError()
    

    def implmentsArtificialIntelligenceCompositeInterface(self) -> bool:
        raise RuntimeError()
    

    def getType(self) -> int:
        raise RuntimeError()
    

    def getVehicleProperties(self) -> VehicleProperties:
        raise RuntimeError()
    

    def getGameKeyEventList(self) -> BasicArrayList:
        raise RuntimeError()
    

    def getSpeedBasicDecimal(self) -> BasicDecimal:
        raise RuntimeError()
    

    def isReadyForExplosion(self) -> bool:
        raise RuntimeError()
    

    def getRotationAnimationInterface(self) -> RotationAnimation:
        raise RuntimeError()
    

    def setRotationAnimationInterface(self, animationInterface: RotationAnimation) -> None:
        raise RuntimeError()
    

    def isDestroyed(self) -> bool:
        raise RuntimeError()
    

    def isFinish(self) -> bool:
        raise RuntimeError()
    

    def getFinalPosition(self) -> int:
        raise RuntimeError()
    

    # throws Exception
    def handleFinish(self) -> None:
        raise RuntimeError()
    

    def getGeographicMapCellPositionTracking(self) -> GeographicMapCellPositionTracking:
        raise RuntimeError()
    

    def getGeographicMapCellHistoryArray(self) -> list[GeographicMapCellHistory]:
        raise RuntimeError()
    

    def setGeographicMapCellHistoryArray(self, geographicMapCellHistory: list[GeographicMapCellHistory]) -> None:
        raise RuntimeError()
    

    def paint(self, graphics: Graphics) -> None:
        pass
    

    def paintThreed(self, graphics: Graphics) -> None:
        pass
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.RotationAnimation import RotationAnimation
from org.allbinary.game.identification.Group import Group
from org.allbinary.logic.math.BasicDecimal import BasicDecimal
from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionTracking import GeographicMapCellPositionTracking
from org.allbinary.util.BasicArrayList import BasicArrayList


NullVehicleLayer.NULL_VEHICLE_LAYER = NullVehicleLayer()

