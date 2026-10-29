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
# package org.allbinary.graphics.pipeline

from __future__ import annotations

import math
from org.allbinary.graphics.pipeline.BasicGraphicsPipeline import BasicGraphicsPipeline


class GraphicsPipeline(BasicGraphicsPipeline):
    

    def __init__(self, points: BasicArrayList) -> None:
        super().__init__(points)
    

    # throws Exception
    def rotateTheta(self, aTheta: float) -> None:
        newVector: BasicArrayList = BasicArrayListD()
        size: int = self.pointBasicArrayList.size()
        for index in range(0, size):
            secondPoint: GPoint = self.pointBasicArrayList.get(index)
            secondX: float = (secondPoint.getX() * math.cos(aTheta)) - (secondPoint.getY() * math.sin(aTheta))
            secondY: float = (secondPoint.getX() * math.sin(aTheta)) + (secondPoint.getY() * math.cos(aTheta))
            point: GPoint = PointFactory.getInstance().createXY((int(secondX)), (int(secondY)))
            newVector.add(point)
        self.pointBasicArrayList = newVector
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


