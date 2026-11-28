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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.media.graphics.geography.pathfinding.PathFinderGraphVisitorFactoryBase import PathFinderGraphVisitorFactoryBase


@java_inherited_overloads
class SimplePathFinderGraphVisitorFactory(PathFinderGraphVisitorFactoryBase):
    def _java_defaults(self):
        vars(self).setdefault("edgeMinimum", 0)
        vars(self).setdefault("minPathWeight", 0)
        vars(self).setdefault("maxPathWeight", 0)

    def _init_fields(self) -> None:
        if "edgeMinimum" not in vars(self): self.edgeMinimum: int = 0
        if "minPathWeight" not in vars(self): self.minPathWeight: int = 0
        if "maxPathWeight" not in vars(self): self.maxPathWeight: int = 0
    

    def __init__(self, edgeMinimum: int, minPathWeight: int, maxPathWeight: int) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.edgeMinimum = edgeMinimum
        self.minPathWeight = minPathWeight
        self.maxPathWeight = maxPathWeight
    

    def getInstance(self, geographicMapInterface: BasicGeographicMap) -> PathFinderGraphVisitorBase:
        from org.allbinary.game.media.graphics.geography.map.racetrack.BasePathFinderGraphVisitor import BasePathFinderGraphVisitor
        from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
        from org.allbinary.media.graphics.geography.pathfinding.PathFinderGraphVisitorBase import PathFinderGraphVisitorBase
        return BasePathFinderGraphVisitor(geographicMapInterface, self.edgeMinimum, self.minPathWeight, self.maxPathWeight)
# from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
# from org.allbinary.media.graphics.geography.pathfinding.PathFinderGraphVisitorBase import PathFinderGraphVisitorBase


