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



class PathFindingNodeCostInfoData:
    instance: PathFindingNodeCostInfoData = None

    def _init_fields(self) -> None:
        self.MAX_TOTAL_COST: int = 2147483647
        self.MAX_NODE_COST: int = 2147483647 / 10000
    

    @staticmethod
    def getInstance() -> PathFindingNodeCostInfoData:
        return PathFindingNodeCostInfoData.instance
    

    def __init__(self) -> None:
        self._init_fields()


PathFindingNodeCostInfoData.instance = PathFindingNodeCostInfoData()

