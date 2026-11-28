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

from java.lang.JavaRuntimeStatic import java_divide
from java.lang.JavaRuntimeStatic import lazy_static


class VectorRotationGenerator:
    instance: VectorRotationGenerator = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.math.AngleFactory import AngleFactory
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.vectorAnimationUtil: VectorAnimationUtil = VectorAnimationUtil.getInstance()
        self.angleFactory: AngleFactory = AngleFactory.getInstance()
    

    @staticmethod
    def getInstance_j0() -> VectorRotationGenerator:
        return VectorRotationGenerator.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def getInstance_j1(self, vectorRotationInfo: VectorInfo) -> list[list[list[int]]]:
        from org.allbinary.vector.VectorInfo import VectorInfo
        return self.getInstanceFrames(vectorRotationInfo.getWidth(), vectorRotationInfo.getHeight(), vectorRotationInfo.getPoints(), vectorRotationInfo.getTotalFrames())

    def getInstance(self=None, *args):
        if self is None and not args: return __class__.getInstance_j0()
        implementation = __class__.__dict__.get("getInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getInstance(*args)
    

    def getInstanceFrames(self, width: int, height: int, points: list[list[int]], frames: int) -> list[list[list[int]]]:
        from org.allbinary.graphics.PointFactory import PointFactory
        from org.allbinary.logic.NullUtil import NullUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListS import BasicArrayListS
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
        from org.allbinary.graphics.pipeline.BasicGraphicsPipeline import BasicGraphicsPipeline
        from org.allbinary.math.Angle import Angle
        from org.allbinary.util.BasicArrayList import BasicArrayList
        graphicsPipe: BasicGraphicsPipeline = BasicGraphicsPipeline(pointBasicArrayList)
        graphicsPipe.createMatrix()
        graphicsPipe.translate(-int(width) >> (int(1) & 31), -int(height) >> (int(1) & 31))
        graphicsPipe.rotateToAngle(angle)
        graphicsPipe.translate((int(width) >> (int(1) & 31)), (int(height) >> (int(1) & 31)))
        return graphicsPipe.getMatrix()
# from org.allbinary.graphics.PointFactory import PointFactory
# from org.allbinary.graphics.pipeline.BasicGraphicsPipeline import BasicGraphicsPipeline
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.math.Angle import Angle
# from org.allbinary.math.AngleFactory import AngleFactory
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListS import BasicArrayListS
# from org.allbinary.vector.VectorInfo import VectorInfo
from org.allbinary.animation.VectorAnimationUtil import VectorAnimationUtil


def _VectorRotationGenerator_instance() -> object:
    return VectorRotationGenerator()

lazy_static(VectorRotationGenerator, "instance", _VectorRotationGenerator_instance)

