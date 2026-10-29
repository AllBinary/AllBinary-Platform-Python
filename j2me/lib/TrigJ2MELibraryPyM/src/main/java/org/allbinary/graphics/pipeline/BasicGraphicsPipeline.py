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



class BasicGraphicsPipeline:

    def _init_fields(self) -> None:
        self.pointBasicArrayList: BasicArrayList = None
        self.noDecimalTrigTable: NoDecimalTrigTable = NoDecimalTrigTable.getInstance()
    

    def __init__(self, points: BasicArrayList) -> None:
        self._init_fields()
        self.pointBasicArrayList = points
    

    def setInitMatrix(self, points: BasicArrayList) -> None:
        self.pointBasicArrayList = points
    

    def createMatrix(self) -> None:
        pass
    

    # throws Exception
    def translate(self, x: int, y: int) -> None:
        newBasicArrayList: BasicArrayList = BasicArrayListD()
        size: int = self.pointBasicArrayList.size()
        pointFactory: PointFactory = PointFactory.getInstance()
        secondPoint: GPoint = None
        for index in range(0, size):
            secondPoint = self.pointBasicArrayList.objectArray[index]
            if secondPoint.getX() != 1000:
                newBasicArrayList.add(pointFactory.createXY(secondPoint.getX() + x, secondPoint.getY() + y))
            else:
                newBasicArrayList.add(secondPoint)
        self.pointBasicArrayList = newBasicArrayList
    

    # throws Exception
    def rotateToAngle(self, angle: Angle) -> None:
        self.rotate(int(angle.getValue()))
    

    # throws Exception
    def rotate(self, angle: int) -> None:
        newBasicArrayList: BasicArrayList = BasicArrayListD()
        secondPoint: GPoint = None
        y: int = 0
        secondX: int = 0
        secondY: int = 0
        point: GPoint = None
        pointFactory: PointFactory = PointFactory.getInstance()
        size: int = self.pointBasicArrayList.size()
        sin: int = 0
        cos: int = 0
        for index in range(0, size):
            secondPoint = self.pointBasicArrayList.objectArray[index]
            if secondPoint.getX() != 1000:
                sin = self.noDecimalTrigTable.sin(angle)
                cos = self.noDecimalTrigTable.cos(angle)
                y = secondPoint.getY() * sin
                secondX = (secondPoint.getX() * cos) - y
                secondY = (secondPoint.getX() * sin) + (secondPoint.getY() * cos)
                point = pointFactory.createXY(int(secondX / 10000), int(secondY / 10000))
                newBasicArrayList.add(point)
            else:
                newBasicArrayList.add(secondPoint)
        self.pointBasicArrayList = newBasicArrayList
    

    # throws Exception
    def mirror(self, width: int) -> None:
        pointFactory: PointFactory = PointFactory.getInstance()
        halfWidth: int = (width >> 1)
        newBasicArrayList: BasicArrayList = BasicArrayListD()
        secondPoint: GPoint = None
        newX: int = 0
        point: GPoint = None
        size: int = self.pointBasicArrayList.size()
        for index in range(0, size):
            secondPoint = self.pointBasicArrayList.objectArray[index]
            if secondPoint.getX() != 1000:
                newX = 0
                if secondPoint.getX() > halfWidth:
                    newX = halfWidth - (secondPoint.getX() - halfWidth)
                else:
                    newX = halfWidth + (halfWidth - secondPoint.getX())
                point = pointFactory.createXY(newX, secondPoint.getY())
                newBasicArrayList.add(point)
            else:
                newBasicArrayList.add(secondPoint)
        self.pointBasicArrayList = newBasicArrayList
    

    def getMatrix(self) -> BasicArrayList:
        return self.pointBasicArrayList
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.math.Angle import Angle
from org.allbinary.math.NoDecimalTrigTable import NoDecimalTrigTable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


