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
# package org.allbinary.animation.vector

from __future__ import annotations



class VectorCenterGenerator:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.minX: int = 2147483647
        self.minY: int = 2147483647
        self.maxX: int = -2147483648
        self.maxY: int = -2147483648
        self.dx: int = 0
        self.dy: int = 0
        self.width: int = 0
        self.height: int = 0
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def calculate(self, hashMap: dict) -> None:
        graphicItemArray: list[object] = hashMap.keySet().toArray()
        size: int = len(graphicItemArray)
        for index in range(0, size):
            item: GraphicItemInterface = hashMap.get(graphicItemArray[index])
            if item.getName() == LinesGraphicItem.getStaticName():
                self.getInstance(item.getPointsInterface().getPoints())
        self.logUtil.putF("minX: " + str(self.minX) + " minY: " + str(self.minY) + " maxX: " + str(self.maxX) + " maxY: " + str(self.maxY), self, self.commonStrings.GET_INSTANCE)
        self.setWidth(self.maxX - self.minX)
        self.setHeight(self.maxY - self.minY)
        max: int = self.getWidth()
        if self.getHeight() > max:
            max = self.getHeight()
        middle: int = int(max / 2)
        commonLabels: CommonLabels = CommonLabels.getInstance()
        s: str = str(StringMaker().append(commonLabels.WIDTH_LABEL).appendint(self.getWidth()).append(commonLabels.HEIGHT_LABEL).appendint(self.getHeight()).append(" max: ").appendint(max).append(" middle: ").appendint(middle))
        self.logUtil.putF(s, self, self.commonStrings.GET_INSTANCE)
        currentMiddleX: int = self.minX + int(self.getWidth() / 2)
        currentMiddleY: int = self.minY + int(self.getHeight() / 2)
        self.dx = middle - currentMiddleX
        self.dy = middle - currentMiddleY
    

    # throws Exception
    def transform(self, hashMap: dict) -> None:
        self.calculate(hashMap)
        self.logUtil.putF(str(StringMaker().append(" dx: ").appendint(self.dx).append(" dy: ").appendint(self.dy)), self, self.commonStrings.GET_INSTANCE)
        graphicItemArray: list[object] = hashMap.keySet().toArray()
        size: int = len(graphicItemArray)
        for index in range(0, size):
            item: GraphicItemInterface = hashMap.get(graphicItemArray[index])
            list_: BasicArrayList = VectorCenterGenerator.translate(item.getPointsInterface().getPoints(), self.dx, self.dy)
            newPoints: Points = Points()
            newPoints.addPoints(list_)
            item.setPointsInterface(newPoints)
    

    # throws Exception
    def getInstance(self, pointVector: BasicArrayList) -> None:
        try:
            size: int = pointVector.size()
            for index in range(0, size):
                point: GPoint = pointVector.get(index)
                if point.getX() < self.minX:
                    self.minX = point.getX()
                if point.getX() > self.maxX:
                    self.maxX = point.getX()
                if point.getY() < self.minY:
                    self.minY = point.getY()
                if point.getY() > self.maxY:
                    self.maxY = point.getY()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.GET_INSTANCE, e)
            raise e
    

    # throws Exception
    @staticmethod
    def translate(list_: BasicArrayList, x: int, y: int) -> BasicArrayList:
        graphicsPipe: BasicGraphicsPipeline = BasicGraphicsPipeline(list_)
        graphicsPipe.createMatrix()
        graphicsPipe.translate(x, y)
        return graphicsPipe.getMatrix()
    

    def getWidth(self) -> int:
        return self.width
    

    def setWidth(self, width: int) -> None:
        self.width = width
    

    def getHeight(self) -> int:
        return self.height
    

    def setHeight(self, height: int) -> None:
        self.height = height
# from java.util.HashMap import HashMap
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
from org.allbinary.graphics.j2me.workarea.tools.LinesGraphicItem import LinesGraphicItem
from org.allbinary.graphics.j2me.workarea.tools.Points import Points
from org.allbinary.graphics.pipeline.BasicGraphicsPipeline import BasicGraphicsPipeline
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList


