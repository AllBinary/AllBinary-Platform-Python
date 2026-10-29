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

from org.allbinary.layer.AllBinaryLayerCircularPool import AllBinaryLayerCircularPool


class PointsLayerCircularStaticPool(AllBinaryLayerCircularPool):
    

    def __init__(self, allbinaryLayerFactoryInterface: AllBinaryLayerFactoryInterface, total: int) -> None:
        super().__init__()
        super().initAllBinaryLayerCircularPool(allbinaryLayerFactoryInterface, total)
    

    # throws Exception
    def visit(self, sourceLayerInterface: AllBinaryLayer) -> None:
        pointsLayer: PointsLayer = self.getNextInstance()
        scoreableInterface: ScoreableInterface = sourceLayerInterface
        pointsLayer.visit(scoreableInterface)
from org.allbinary.game.score.ScoreableInterface import ScoreableInterface
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerFactoryInterface import AllBinaryLayerFactoryInterface


