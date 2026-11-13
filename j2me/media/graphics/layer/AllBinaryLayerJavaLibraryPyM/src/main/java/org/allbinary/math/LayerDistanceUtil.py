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
# package org.allbinary.math

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class LayerDistanceUtil:
    instance: LayerDistanceUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.math.MathUtil import MathUtil
        self.mathUtil: MathUtil = MathUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> LayerDistanceUtil:
        return LayerDistanceUtil.instance
    

    def getDistance(self, layerInterface: AllBinaryLayer, layerInterface2: AllBinaryLayer) -> int:
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        dx: int = (layerInterface.getXP() + layerInterface.getHalfWidth()) - (layerInterface2.getXP() + layerInterface2.getHalfWidth())
        dy: int = (layerInterface.getYP() + layerInterface.getHalfHeight()) - (layerInterface2.getYP() + layerInterface2.getHalfHeight())
        return int(self.mathUtil.sqrt((dx * dx) + (dy * dy)))
    

    def getDistance3D(self, layerInterface: AllBinaryLayer, layerInterface2: AllBinaryLayer) -> int:
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        dx: int = (layerInterface.getXP() + layerInterface.getHalfWidth()) - (layerInterface2.getXP() + layerInterface2.getHalfWidth())
        dy: int = (layerInterface.getYP() + layerInterface.getHalfHeight()) - (layerInterface2.getYP() + layerInterface2.getHalfHeight())
        dz: int = (layerInterface.getZP() + layerInterface.getHalfDepth()) - (layerInterface2.getZP() + layerInterface2.getHalfDepth())
        return int(self.mathUtil.sqrt((dx * dx) + (dy * dy) + (dz * dz)))
    

    def getDistanceAt(self, layerInterface: AllBinaryLayer, point: GPoint) -> int:
        from org.allbinary.graphics.GPoint import GPoint
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        dx: int = layerInterface.getXP() - point.getX()
        dy: int = layerInterface.getYP() - point.getY()
        return int(self.mathUtil.sqrt((dx * dx) + (dy * dy)))
# from org.allbinary.graphics.GPoint import GPoint
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.logic.math.MathUtil import MathUtil


def _LayerDistanceUtil_instance() -> object:
    return LayerDistanceUtil()

lazy_static(LayerDistanceUtil, "instance", _LayerDistanceUtil_instance)

