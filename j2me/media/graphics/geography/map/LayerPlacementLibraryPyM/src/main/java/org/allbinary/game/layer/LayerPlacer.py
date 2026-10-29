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



class LayerPlacer:

    def _init_fields(self) -> None:
        self.enumerationUtil: EnumerationUtil = EnumerationUtil.getInstance()
        self.layerInterfaceVisitor: LayerInterfaceVisitor = None
        self.dimension: GPoint = None
    

    def __init__(self, layerInterfaceVisitor: LayerInterfaceVisitor, dimension: GPoint) -> None:
        self._init_fields()
        self.layerInterfaceVisitor = layerInterfaceVisitor
        self.dimension = dimension
    

    # throws Exception
    def processList(self, list_: BasicArrayList) -> None:
        size: int = list_.size()
        layerPlacementInterface: LayerPlacementInterface = None
        for index in range(0, size):
            layerPlacementInterface = list_.objectArray[index]
            self.process(layerPlacementInterface)
    

    # throws Exception
    def process(self, layerPlacementInterface: LayerPlacementInterface) -> None:
        relativePoint: GPoint = self.getPoint(layerPlacementInterface)
        layerInterfaceFactory: LayerInterfaceFactory = LayerInterfaceFactory.getInstance()
        hashtable: ABHashtable[object, object] = layerPlacementInterface.getInstance()
        enumeration: Enumeration = hashtable.keys()
        point: GPoint = None
        layerHashtable: ABHashtable[object, object] = None
        x: int = 0
        y: int = 0
        z: int = 0
        layerInterface: AllBinaryLayer = None
        while self.enumerationUtil.hasMoreElements(enumeration):
            point = self.enumerationUtil.nextElement(enumeration)
            layerHashtable = hashtable.get(point)
            x = point.getX() + relativePoint.getX()
            y = point.getY() + relativePoint.getY()
            z = point.getZ() + relativePoint.getZ()
            layerInterface = layerInterfaceFactory.getNexInstance(layerHashtable, x, y, z)
            self.layerInterfaceVisitor.visit(layerInterface)
    

    # throws Exception
    def getPoint(self, layerPlacementInterface: LayerPlacementInterface) -> GPoint:
        from org.allbinary.game.layer.LayerPlacementTypeFactory import LayerPlacementTypeFactory
        from org.allbinary.game.layer.LayerPlacementTypeFactory import LayerPlacementTypeFactory
        pointFactory: PointFactory = PointFactory.getInstance()
        layerPlacementType: LayerPlacementType = layerPlacementInterface.getLayerType()
        if layerPlacementType == LayerPlacementTypeFactory.getInstance().MAP:
            width: int = layerPlacementInterface.getWidth()
            height: int = layerPlacementInterface.getHeight()
            x: int = ((self.dimension.getX() - width) / 2)
            y: int = ((self.dimension.getY() - height) / 2)
            return pointFactory.createXY(x, y)
        elif layerPlacementType == LayerPlacementTypeFactory.getInstance().UP:
            width: int = layerPlacementInterface.getWidth()
            height: int = layerPlacementInterface.getHeight()
            x: int = ((self.dimension.getX() - width) / 2)
            y: int = -height
            return pointFactory.createXY(x, y)
        else:
            raise Exception("PlacementType Not Recognized")
# from java.util.Enumeration import Enumeration
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.LayerInterfaceFactory import LayerInterfaceFactory
from org.allbinary.layer.LayerInterfaceVisitor import LayerInterfaceVisitor
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.EnumerationUtil import EnumerationUtil


