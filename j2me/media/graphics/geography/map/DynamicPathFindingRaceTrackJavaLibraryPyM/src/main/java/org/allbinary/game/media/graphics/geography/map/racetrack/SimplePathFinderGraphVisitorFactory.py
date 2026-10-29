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
# package org.allbinary.game.media.graphics.geography.map.racetrack

from __future__ import annotations

from org.allbinary.media.graphics.geography.pathfinding.PathFinderGraphVisitorFactoryBase import PathFinderGraphVisitorFactoryBase


class SimplePathFinderGraphVisitorFactory(PathFinderGraphVisitorFactoryBase):

    def _init_fields(self) -> None:
        self.edgeMinimum: int = None
        self.minPathWeight: int = None
        self.maxPathWeight: int = None
    

    def __init__(self, edgeMinimum: int, minPathWeight: int, maxPathWeight: int) -> None:
        super().__init__()
        self._init_fields()
        self.edgeMinimum = edgeMinimum
        self.minPathWeight = minPathWeight
        self.maxPathWeight = maxPathWeight
    

    def getInstance(self, geographicMapInterface: BasicGeographicMap) -> PathFinderGraphVisitorBase:
        from org.allbinary.game.media.graphics.geography.map.racetrack.BasePathFinderGraphVisitor import BasePathFinderGraphVisitor
        return BasePathFinderGraphVisitor(geographicMapInterface, self.edgeMinimum, self.minPathWeight, self.maxPathWeight)
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.pathfinding.PathFinderGraphVisitorBase import PathFinderGraphVisitorBase


