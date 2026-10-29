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
# package org.allbinary.game.ag.layer.pickup.points

from __future__ import annotations



class PointsResources:
    SINGLETON: PointsResources = None

    def _init_fields(self) -> None:
        self.RESOURCE: str = "points_drop_20_by_20.png"
        self.RESOURCE_2: str = "points_2_drop_20_by_20.png"
        self.RESOURCE_3: str = "points_3_drop_20_by_20.png"
        self.RESOURCE_4: str = "points_4_drop_20_by_20.png"
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PointsResources:
        return PointsResources.SINGLETON


PointsResources.SINGLETON = PointsResources()

