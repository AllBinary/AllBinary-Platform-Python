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
# package org.allbinary.animation

from __future__ import annotations



class VectorRotationGenerator:
    instance: VectorRotationGenerator = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.vectorAnimationUtil: VectorAnimationUtil = VectorAnimationUtil.getInstance()
        self.angleFactory: AngleFactory = AngleFactory.getInstance()
    

    @staticmethod
    def getInstance() -> VectorRotationGenerator:
        return VectorRotationGenerator.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, vectorRotationInfo: VectorInfo) -> list[list[list[int]]]:
        return self.getInstanceFrames(vectorRotationInfo.getWidth(), vectorRotationInfo.getHeight(), vectorRotationInfo.getPoints(), vectorRotationInfo.getTotalFrames())
    

    def getInstanceFrames(self, width: int, height: int, points: list[list[int]], frames: int) -> list[list[list[int]]]:
        try:
            totalAngle: int = self.angleFactory.TOTAL_ANGLE
            angleIncrement: int = int(totalAngle / frames)
            pointsBasicArrayList: BasicArrayList = BasicArrayListS(int(totalAngle / angleIncrement))
            pointBasicArrayList: BasicArrayList = BasicArrayListS(len(points))
            pointFactory: PointFactory = PointFactory.getInstance()
            size: int = len(points)
            for index in range(0, size):
                pointBasicArrayList.add(pointFactory.createXY(points[index][0], points[index][1]))
            index: int = 0
            while index < totalAngle:
                pointsBasicArrayList.add(self.getListAtAngle(width, height, pointBasicArrayList, self.angleFactory.getAt(index)))
                index += angleIncrement
            newPoints: list[list[list[int]]] = self.vectorAnimationUtil.toAnimationArrayFromListOfPointListWithPointsPerFrame(pointsBasicArrayList, pointBasicArrayList.size())
            return newPoints
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            return NullUtil.getInstance().NULL_INT_ARRAY_ARRAY_ARRAY
    

    # throws Exception
    def getListAtAngle(self, width: int, height: int, pointBasicArrayList: BasicArrayList, angle: Angle) -> BasicArrayList:
        graphicsPipe: BasicGraphicsPipeline = BasicGraphicsPipeline(pointBasicArrayList)
        graphicsPipe.createMatrix()
        graphicsPipe.translate(-(width >> 1), -(height >> 1))
        graphicsPipe.rotateToAngle(angle)
        graphicsPipe.translate((width >> 1), (height >> 1))
        return graphicsPipe.getMatrix()
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.pipeline.BasicGraphicsPipeline import BasicGraphicsPipeline
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.math.Angle import Angle
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListS import BasicArrayListS
from org.allbinary.vector.VectorInfo import VectorInfo
from org.allbinary.animation.VectorAnimationUtil import VectorAnimationUtil


VectorRotationGenerator.instance = VectorRotationGenerator()

