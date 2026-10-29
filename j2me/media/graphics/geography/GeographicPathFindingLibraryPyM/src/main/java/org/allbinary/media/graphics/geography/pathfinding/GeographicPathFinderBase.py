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



class GeographicPathFinderBase:
    NULL_GEOGRAPHIC_PATH_FINDER_BASE: GeographicPathFinderBase = None

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def searchTotalPath(self, startPathFindingNodeList: BasicArrayList, endPathFindingNodeList: BasicArrayList, totalPaths: int) -> BasicArrayList:
        raise RuntimeError()
    

    # throws Exception
    def searchTotalPathN(self, startPathFindingNodeList: BasicArrayList, endPathFindingNodeList: BasicArrayList, totalPaths: int, multipassState: MultipassState) -> BasicArrayList:
        raise RuntimeError()
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList


GeographicPathFinderBase.NULL_GEOGRAPHIC_PATH_FINDER_BASE = GeographicPathFinderBase()

