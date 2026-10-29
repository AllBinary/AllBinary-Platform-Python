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
# package org.allbinary.vector

from __future__ import annotations



class PointsUtil:
    instance: PointsUtil = None
    

    @staticmethod
    def getInstance() -> PointsUtil:
        return PointsUtil.instance
    

    def adjustXY(self, points: list[list[list[int]]], x: int, y: int) -> list[list[list[int]]]:
        size: int = len(points)
        newPoints: list[list[list[int]]] = [[[0] * (0) for _ in range(0)] for _ in range(size)]
        for index in range(0, size):
            size2: int = len(points[index])
            newPoints[index] = [[0] * (2) for _ in range(size2)]
            for index2 in range(0, size2):
                if points[index][index2][0] != 1000:
                    newPoints[index][index2][0] = points[index][index2][0] + x
                    newPoints[index][index2][1] = points[index][index2][1] + y
                else:
                    newPoints[index][index2][0] = 1000
                    newPoints[index][index2][1] = 1000
        return newPoints
    

    def adjust(self, points: list[list[int]], both: int) -> list[list[int]]:
        return self.adjust(points, both, both)
    

    # Java overloaded method: Python keeps the last definition
    def adjust(self, points: list[list[int]], x: int, y: int) -> list[list[int]]:
        newPoints: list[list[int]] = [[0] * (2) for _ in range(len(points))]
        for index2 in range(0, len(points)):
            if points[index2][0] != 1000:
                newPoints[index2][0] = points[index2][0] + x
                newPoints[index2][1] = points[index2][1] + y
            else:
                newPoints[index2][0] = 1000
                newPoints[index2][1] = 1000
        return newPoints


PointsUtil.instance = PointsUtil()

