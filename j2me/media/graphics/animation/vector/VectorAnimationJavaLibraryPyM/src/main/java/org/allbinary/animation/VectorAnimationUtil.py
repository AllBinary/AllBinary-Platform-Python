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



class VectorAnimationUtil:
    instance: VectorAnimationUtil = None
    

    @staticmethod
    def getInstance() -> VectorAnimationUtil:
        return VectorAnimationUtil.instance
    

    def __init__(self) -> None:
        pass
    

    def toAnimationArrayFromListOfPointListWithPointsPerFrame(self, vector: BasicArrayList, pointsPerFrame: int) -> list[list[list[int]]]:
        size: int = vector.size()
        points: list[list[list[int]]] = [[[0] * (2) for _ in range(pointsPerFrame)] for _ in range(size)]
        nextBasicArrayList: BasicArrayList = None
        framePoints: list[list[int]] = None
        for index in range(0, size):
            nextBasicArrayList = vector.objectArray[index]
            framePoints = self.toFrameArrayFromPointBasicArrayList(nextBasicArrayList)
            for pointIndex in range(0, len(framePoints)):
                points[index][pointIndex][0] = framePoints[pointIndex][0]
                points[index][pointIndex][1] = framePoints[pointIndex][1]
        return points
    

    def toAnimationArrayFromListOfPointList(self, vector: BasicArrayList) -> list[list[list[int]]]:
        size: int = vector.size()
        points: list[list[list[int]]] = [[[0] * (0) for _ in range(0)] for _ in range(size)]
        nextBasicArrayList: BasicArrayList = None
        framePoints: list[list[int]] = None
        for index in range(0, size):
            nextBasicArrayList = vector.objectArray[index]
            framePoints = self.toFrameArrayFromPointBasicArrayList(nextBasicArrayList)
            points[index] = [[0] * (2) for _ in range(len(framePoints))]
            for pointIndex in range(0, len(framePoints)):
                points[index][pointIndex][0] = framePoints[pointIndex][0]
                points[index][pointIndex][1] = framePoints[pointIndex][1]
        return points
    

    def toFrameArrayFromPointBasicArrayList(self, list_: BasicArrayList) -> list[list[int]]:
        points: list[list[int]] = [[0] * (2) for _ in range(list_.size())]
        size: int = list_.size()
        for index in range(0, size):
            nextPoint: GPoint = list_.objectArray[index]
            points[index][0] = nextPoint.getX()
            points[index][1] = nextPoint.getY()
        return points
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.util.BasicArrayList import BasicArrayList


VectorAnimationUtil.instance = VectorAnimationUtil()

