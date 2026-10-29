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



#1.4.2
class PathFinderGraphVisitorBase:
    

    # throws Exception
    def visit(self, graph: object, startPathFindingNodeList: BasicArrayList, endPathFindingNodeList: BasicArrayList) -> None:
        raise RuntimeError()
    

    # throws Exception
    def fixPath(self, startPathFindingNodeList: BasicArrayList, endPathFindingNodeList: BasicArrayList, pathList: BasicArrayList) -> None:
        raise RuntimeError()
    

    def isValid(self, graphPath: object) -> bool:
        raise RuntimeError()
    

    def getInvalidReason(self, graphPath: object) -> str:
        raise RuntimeError()
from org.allbinary.util.BasicArrayList import BasicArrayList


