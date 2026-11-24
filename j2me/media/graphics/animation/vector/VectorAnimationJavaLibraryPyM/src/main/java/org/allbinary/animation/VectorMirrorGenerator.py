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

from java.lang.JavaRuntimeStatic import lazy_static


class VectorMirrorGenerator:
    instance: VectorMirrorGenerator = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.vectorAnimationUtil: VectorAnimationUtil = VectorAnimationUtil.getInstance()
    

    @staticmethod
    def getInstance_j0() -> VectorMirrorGenerator:
        return VectorMirrorGenerator.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j2_1(self, points: list[list[list[int]]], width: int) -> list[list[list[int]]]:
        from org.allbinary.graphics.PointFactory import PointFactory
        from org.allbinary.logic.NullUtil import NullUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListS import BasicArrayListS
        try:
            pointFactory: PointFactory = PointFactory.getInstance()
            pointBasicArrayList: BasicArrayList = None
            nextPoints: list[list[int]] = None
            size2: int = 0
            size: int = len(points)
            pointsBasicArrayList: BasicArrayList = BasicArrayListS(size)
            for frame in range(0, size):
                nextPoints = points[frame]
                size2 = len(nextPoints)
                pointBasicArrayList = BasicArrayListS(size2)
                for index in range(0, size2):
                    pointBasicArrayList.add(pointFactory.createXY(nextPoints[index][0], nextPoints[index][1]))
                pointsBasicArrayList.add(pointBasicArrayList)
            for index in range(0, len(points)):
                pointsBasicArrayList.add(self.getInstance(pointsBasicArrayList.objectArray[index], width))
            newPoints: list[list[list[int]]] = self.vectorAnimationUtil.toAnimationArrayFromListOfPointList(pointsBasicArrayList)
            return newPoints
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            return NullUtil.getInstance().NULL_INT_ARRAY_ARRAY_ARRAY
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j2_2(self, pointBasicArrayList: BasicArrayList, width: int) -> BasicArrayList:
        from org.allbinary.graphics.pipeline.BasicGraphicsPipeline import BasicGraphicsPipeline
        from org.allbinary.util.BasicArrayList import BasicArrayList
        graphicsPipe: BasicGraphicsPipeline = BasicGraphicsPipeline(pointBasicArrayList)
        graphicsPipe.createMatrix()
        graphicsPipe.mirror(width)
        return graphicsPipe.getMatrix()

    def getInstance(self, *args):
        if len(args) == 2 and True and (args[0] is None or isinstance(args[0], list)) and isinstance(args[1], int) and not isinstance(args[1], bool):
            return self.getInstance_j2_1(*args)
        if len(args) == 2:
            return self.getInstance_j2_2(*args)
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from org.allbinary.graphics.PointFactory import PointFactory
# from org.allbinary.graphics.pipeline.BasicGraphicsPipeline import BasicGraphicsPipeline
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListS import BasicArrayListS
from org.allbinary.animation.VectorAnimationUtil import VectorAnimationUtil


def _VectorMirrorGenerator_instance() -> object:
    return VectorMirrorGenerator()

lazy_static(VectorMirrorGenerator, "instance", _VectorMirrorGenerator_instance)

