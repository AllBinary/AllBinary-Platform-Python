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
# package org.allbinary.media.graphics.geography.pathfinding

from __future__ import annotations



class PathFindingNode:

    def _init_fields(self) -> None:
        self.parent: object = NullUtil.getInstance().NULL_OBJECT
        self.geographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
    

    def __init__(self, parent: object, geographicMapCellPosition: GeographicMapCellPosition) -> None:
        self._init_fields()
        self.parent = parent
        self.setGeographicMapCellPositionP(geographicMapCellPosition)
        if self.geographicMapCellPosition == SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
            raise Exception("No GeographicMapCellPosition")
    

    def getParentP(self) -> PathFindingNode:
        return self.parent
    

    def setGeographicMapCellPositionP(self, geographicMapCellPosition: GeographicMapCellPosition) -> None:
        self.geographicMapCellPosition = geographicMapCellPosition
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(type(self).__module__ + "." + type(self).__qualname__)
        stringBuffer.append(CommonLabels.getInstance().COLON_SEP)
        stringBuffer.append(" Path: ")
        stringBuffer.append(str(self.geographicMapCellPosition))
        pathFindingNode: PathFindingNode = self.getParentP()
        while pathFindingNode is not None:
            stringBuffer.append(str(pathFindingNode.geographicMapCellPosition))
            stringBuffer.append(CommonSeps.getInstance().SPACE)
            pathFindingNode = pathFindingNode.getParentP()
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
from org.allbinary.string.CommonLabels import CommonLabels


