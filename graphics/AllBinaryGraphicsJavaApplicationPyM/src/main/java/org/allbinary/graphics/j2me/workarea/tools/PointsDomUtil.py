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
# package org.allbinary.graphics.j2me.workarea.tools

from __future__ import annotations



class PointsDomUtil:
    instance: PointsDomUtil = None

    def _init_fields(self) -> None:
        self.LINES: str = "lines"
        self.POINTONE: str = "pointOne"
        self.POINTTWO: str = "pointTwo"
        self.ROTATEDPOINTONE: str = "rotatedPointOne"
        self.ROTATEDPOINTTWO: str = "rotatedPointTwo"
        self.LINE: str = "line"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PointsDomUtil:
        return PointsDomUtil.instance
    

    # throws Exception
    def toDom(self, canvasDom: CanvasDom, pointVector: BasicArrayList) -> Node:
        from org.allbinary.graphics.j2me.workarea.tools.PointsUtil import PointsUtil
        tempPointVector: BasicArrayList = PointsUtil.getInstance().doTransforms(pointVector, float(canvasDom.getAngle()), PointFactory.getInstance().createXY(canvasDom.getDimension().getWidth(), canvasDom.getDimension().getHeight()))
        document: Document = WorkAreaJPanel.getDocument()
        linesNode: Node = document.createElement(self.LINES)
        size2: int = tempPointVector.size()
        size: int = pointVector.size()
        firstPoint: GPoint = None
        rotatedFirstPoint: GPoint = None
        index: int = 0
        if index < size and index < size2:
            rotatedFirstPoint = tempPointVector.get(index)
            firstPoint = pointVector.get(index)
            index += 1
        while index < size and index < size2:
            lineNode: Node = document.createElement(self.LINE)
            rotatedSecondPoint: GPoint = tempPointVector.get(index)
            secondPoint: GPoint = pointVector.get(index)
            pointOneNode: Node = self.getPointNode(firstPoint, self.POINTONE)
            pointTwoNode: Node = self.getPointNode(secondPoint, self.POINTTWO)
            rotatedPointOneNode: Node = self.getPointNode(rotatedFirstPoint, self.ROTATEDPOINTONE)
            rotatedPointTwoNode: Node = self.getPointNode(rotatedSecondPoint, self.ROTATEDPOINTTWO)
            lineNode.appendChild(pointOneNode)
            lineNode.appendChild(pointTwoNode)
            lineNode.appendChild(rotatedPointOneNode)
            lineNode.appendChild(rotatedPointTwoNode)
            firstPoint = secondPoint
            rotatedFirstPoint = rotatedSecondPoint
            linesNode.appendChild(lineNode)
            index += 1
        return linesNode
    

    def getPointNode(self, point: GPoint, pointName: str) -> Node:
        document: Document = WorkAreaJPanel.getDocument()
        pointNode: Node = document.createElement(pointName)
        xNode: Node = document.createElement(PositionStrings.getInstance().X)
        xTextNode: Node = document.createTextNode(str(point.getX()))
        xNode.appendChild(xTextNode)
        yNode: Node = document.createElement(PositionStrings.getInstance().Y)
        yTextNode: Node = document.createTextNode(str(point.getY()))
        yNode.appendChild(yTextNode)
        pointNode.appendChild(xNode)
        pointNode.appendChild(yNode)
        return pointNode
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.j2me.workarea.WorkAreaJPanel import WorkAreaJPanel
from org.allbinary.graphics.j2me.workarea.canvas.CanvasDom import CanvasDom
from org.allbinary.math.PositionStrings import PositionStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.w3c.dom.Node import Node


PointsDomUtil.instance = PointsDomUtil()

