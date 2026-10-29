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
# package org.allbinary.media.graphics.geography.pathfinding

from __future__ import annotations



# Java interface
class PathGeneratorInterface:
    

    # throws Exception
    def createList(self, geographicMapInterface: BasicGeographicMap, geographicMapCellHistory: GeographicMapCellHistory, pathFindingInfo: PathFindingInfo, totalPaths: int) -> BasicArrayList:
        raise NotImplementedError()
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
from org.allbinary.util.BasicArrayList import BasicArrayList


