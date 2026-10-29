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



# Java interface
class GeographicMapCellPositionAreaInterface:
    

    def getNextSurroundingGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        raise NotImplementedError()
    

    def getOccupyingGeographicMapCellPositionList(self) -> BasicArrayList:
        raise NotImplementedError()
    

    def getSurroundingGeographicMapCellPositionList(self) -> BasicArrayList:
        raise NotImplementedError()
    

    # throws Exception
    def update(self, geographicMapInterface: BasicGeographicMap) -> None:
        raise NotImplementedError()
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.util.BasicArrayList import BasicArrayList


