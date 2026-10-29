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

from org.allbinary.layer.AllBinaryLayerFactoryInterface import AllBinaryLayerFactoryInterface


class PointsLayerFactory(AllBinaryLayerFactoryInterface):

    def _init_fields(self) -> None:
        self.points: int = None
    

    def __init__(self, points: int) -> None:
        self._init_fields()
        self.points = points
    

    # throws Exception
    def getInstance(self) -> AllBinaryLayer:
        from org.allbinary.game.ag.layer.pickup.points.PointsLayer import PointsLayer
        return PointsLayer(self.points)
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


