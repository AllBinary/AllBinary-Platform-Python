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
# package org.allbinary.game.layer

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.layer.LayerInterface import LayerInterface
from org.allbinary.game.layer.VehiclePropertiesCompositeInterface import VehiclePropertiesCompositeInterface


# Java interface
@java_inherited_overloads
class VehicleLayerInterface(*java_bases(LayerInterface, VehiclePropertiesCompositeInterface)):
    

    def getGameKeyEventList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise NotImplementedError()
    

    def getSpeedBasicDecimal(self) -> BasicDecimal:
        from org.allbinary.logic.math.BasicDecimal import BasicDecimal
        raise NotImplementedError()
    

    def isReadyForExplosion(self) -> bool:
        raise NotImplementedError()
    

    def getRotationAnimationInterface(self) -> RotationAnimation:
        from org.allbinary.animation.RotationAnimation import RotationAnimation
        raise NotImplementedError()
    

    def setRotationAnimationInterface(self, animationInterface: RotationAnimation) -> None:
        from org.allbinary.animation.RotationAnimation import RotationAnimation
        raise NotImplementedError()
    

    def isDestroyed(self) -> bool:
        raise NotImplementedError()
    

    def isFinish(self) -> bool:
        raise NotImplementedError()
    

    def getFinalPosition(self) -> int:
        raise NotImplementedError()
    

    # throws Exception
    def handleFinish(self) -> None:
        raise NotImplementedError()
    

    def getGeographicMapCellPositionTracking(self) -> GeographicMapCellPositionTracking:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionTracking import GeographicMapCellPositionTracking
        raise NotImplementedError()
    

    def getGeographicMapCellHistoryArray(self) -> list[GeographicMapCellHistory]:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
        raise NotImplementedError()
    

    def setGeographicMapCellHistoryArray(self, geographicMapCellHistory: list[GeographicMapCellHistory]) -> None:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
        raise NotImplementedError()
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.animation.RotationAnimation import RotationAnimation
# from org.allbinary.logic.math.BasicDecimal import BasicDecimal
# from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
# from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionTracking import GeographicMapCellPositionTracking


