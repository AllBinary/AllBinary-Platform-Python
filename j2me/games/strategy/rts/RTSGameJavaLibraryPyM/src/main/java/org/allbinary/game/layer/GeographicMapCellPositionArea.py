# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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

from org.allbinary.game.layer.GeographicMapCellPositionAreaBase import GeographicMapCellPositionAreaBase


class GeographicMapCellPositionArea(GeographicMapCellPositionAreaBase):

    def _init_fields(self) -> None:
        self.cellPositionsUtil: CellPositionsUtil = CellPositionsUtil.getInstance()
        self.layerCoveringCellPositionsUtil: LayerCoveringCellPositionsUtil = LayerCoveringCellPositionsUtil.getInstance()
        self.reusableOccupyingGeographicMapCellPositionList: BasicArrayList = BasicArrayListS(4)
        self.reusableSurroundingGeographicMapCellPositionList: BasicArrayList = BasicArrayListS(12)
        self.surroundingCircularIndexUtil: CircularIndexUtil = CircularIndexUtil.createInstance(0)
        self.layerInterface: AllBinaryLayer = None
        self.LIST: BasicArrayList = BasicArrayListUtil.getInstance().getImmutableInstance()
        self.occupyingGeographicMapCellPositionList: BasicArrayList = self.LIST
        self.surroundingGeographicMapCellPositionList: BasicArrayList = self.LIST
    

    def __init__(self, layerInterface: AllBinaryLayer) -> None:
        super().__init__()
        self._init_fields()
        self.layerInterface = layerInterface
    

    # throws Exception
    def update(self, geographicMapInterface: BasicGeographicMap) -> None:
        self.occupyingGeographicMapCellPositionList = self.layerCoveringCellPositionsUtil.getAllXY(geographicMapInterface, self.layerInterface, self.layerInterface.getXP(), self.layerInterface.getYP(), self.reusableOccupyingGeographicMapCellPositionList)
        self.surroundingGeographicMapCellPositionList = self.cellPositionsUtil.getAllSurrounding(geographicMapInterface, self.occupyingGeographicMapCellPositionList, self.reusableSurroundingGeographicMapCellPositionList)
        self.surroundingCircularIndexUtil.setSize(self.surroundingGeographicMapCellPositionList.size())
    

    def getOccupyingGeographicMapCellPositionList(self) -> BasicArrayList:
        return self.occupyingGeographicMapCellPositionList
    

    def getSurroundingGeographicMapCellPositionList(self) -> BasicArrayList:
        return self.surroundingGeographicMapCellPositionList
    

    def getNextSurroundingGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        geographicMapCellPosition: GeographicMapCellPosition = self.surroundingGeographicMapCellPositionList.get(self.surroundingCircularIndexUtil.getIndex())
        self.surroundingCircularIndexUtil.next()
        return geographicMapCellPosition
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
from org.allbinary.game.layer.geographic.map.LayerCoveringCellPositionsUtil import LayerCoveringCellPositionsUtil
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.CellPositionsUtil import CellPositionsUtil
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.util.BasicArrayListS import BasicArrayListS
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


