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

import math
import threading
from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface


class LinesGraphicItem(GraphicItemInterface):
    RECT: str = "rect"
    ARC: str = "arc"
    STRING: str = "string"
    CHAR: str = "char"
    IMAGE: str = "image"
    item: int = 0
    NAME: str = "Line Tool"
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.gameInputStrings: GameInputStrings = GameInputStrings.getInstance()
        self.treeNode: DefaultMutableTreeNode = None
        self.pointTreeNodeVector: BasicArrayList = None
        self.currentMousePoint: GPoint = None
        self.fulcrumPoint: GPoint = None
        self.active: bool = False
        self.theta: float = 0.0
        self.color: Color = Color(int(BasicColorFactory.getInstance().WHITE))
        self.points: Points = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.Points import Points
        self._init_fields()
        self.points = Points()
        try:
            self.init()
            self.active = True
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
    

    def _constructor1(self, linesNode: Node) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.Points import Points
        from org.allbinary.graphics.j2me.workarea.tools.PointsDomUtil import PointsDomUtil
        from org.allbinary.graphics.j2me.workarea.tools.PointsDomUtil import PointsDomUtil
        self._init_fields()
        self.points = Points()
        self.init()
        self.active = False
        lineNodes: BasicArrayList = DomHelper.getInstance().getWithoutTextNodes(linesNode.getChildNodes())
        numberOfLines: int = lineNodes.size()
        for index in range(0, numberOfLines):
            lineNode: Node = lineNodes.get(index)
            pointNodes: BasicArrayList = DomHelper.getInstance().getWithoutTextNodes(lineNode.getChildNodes())
            pointOneNode: Node = DomHelper.getInstance().searchNodeList(PointsDomUtil.getInstance().POINTONE, pointNodes)
            self.addPoint(pointOneNode.getChildNodes())
            if index == numberOfLines - 1:
                pointTwoNode: Node = DomHelper.getInstance().searchNodeList(PointsDomUtil.getInstance().POINTTWO, pointNodes)
                self.addPoint(pointTwoNode.getChildNodes())
        if numberOfLines == 0:
            raise Exception("Lines node does not contain a line")
    

    # throws Exception
    def init(self) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.PointsDomUtil import PointsDomUtil
        self.treeNode = DefaultMutableTreeNode(PointsDomUtil.getInstance().LINES + LinesGraphicItem.item)
        LinesGraphicItem.item += 1
        self.points.init()
        self.pointTreeNodeVector = BasicArrayListD()
        self.fulcrumPoint = PointFactory.getInstance().createXY(0, 0)
    

    # throws Exception
    def translate(self, x: int, y: int) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.Points import Points
        StatusFactory.getInstance().setStatus("Translating: " + str(self.points.getPoints()))
        basicGraphicsPipeline: BasicGraphicsPipeline = BasicGraphicsPipeline(self.points.getPoints())
        basicGraphicsPipeline.translate(x, y)
        self.points = Points()
        self.points.addPoints(basicGraphicsPipeline.getMatrix())
    

    def setRotate(self, theta: float) -> None:
        while theta > 2 * Math.PI:
            theta -= 2 * Math.PI
        while theta < 0.0:
            theta += 2 * Math.PI
        self.theta = theta
    

    def addRotate(self, theta: float) -> None:
        self.setRotate(self.theta + theta)
    

    def setAngle(self, angle: float) -> None:
        self.setRotate(math.radians(angle))
    

    def addAngle(self, angle: float) -> None:
        self.setRotate(self.theta + math.radians(angle))
    

    def getTreeNode(self) -> MutableTreeNode:
        return self.treeNode
    

    def getName(self) -> str:
        return LinesGraphicItem.NAME
    

    @staticmethod
    def getStaticName() -> str:
        return LinesGraphicItem.NAME
    

    # throws Exception
    def addPoint(self, pointNodes: NodeList) -> None:
        with self._lock:
            return self._addPoint_unlocked(pointNodes)

    def _addPoint_unlocked(self, pointNodes: NodeList) -> None:
        list_: BasicArrayList = DomHelper.getInstance().getWithoutTextNodes(pointNodes)
        xNode: Node = DomHelper.getInstance().searchNodeList(PositionStrings.getInstance().X, list_)
        xTextNode: Node = xNode.getFirstChild()
        xInteger: int = int(xTextNode.getNodeValue())
        yNode: Node = DomHelper.getInstance().searchNodeList(PositionStrings.getInstance().Y, list_)
        yTextNode: Node = yNode.getFirstChild()
        yInteger: int = int(yTextNode.getNodeValue())
        point: GPoint = PointFactory.getInstance().createXY(int(xInteger), int(yInteger))
        self.addPoint(point)
    

    # Java overloaded method: Python keeps the last definition
    def addPoint(self, point: GPoint) -> None:
        with self._lock:
            return self._addPoint_unlocked(point)

    def _addPoint_unlocked(self, point: GPoint) -> None:
        self.points.getPoints().add(point)
        self.logUtil.putF(str(point), self, "addPoint")
        self.pointTreeNodeVector.add(DefaultMutableTreeNode(str(point)))
        self.treeNode.add(self.pointTreeNodeVector.get(self.pointTreeNodeVector.size() - 1))
    

    def removePoint(self) -> GPoint:
        with self._lock:
            return self._removePoint_unlocked()

    def _removePoint_unlocked(self) -> GPoint:
        point: GPoint = None
        if self.points.getSize() > 0:
            lastPoint: int = self.points.getSize() - 1
            point = self.points.getPoints().removeAt(lastPoint)
            index: int = self.pointTreeNodeVector.size() - 1
            if index > 0:
                self.treeNode.remove(self.pointTreeNodeVector.get(index))
                self.pointTreeNodeVector.remove(index)
        return point
    

    def isActive(self) -> bool:
        return self.active
    

    def deactivate(self) -> None:
        self.active = False
    

    def activate(self) -> None:
        self.active = True
    

    # throws Exception
    def duplicatePoints(self, list_: BasicArrayList) -> None:
        size: int = list_.size()
        for index in range(0, size):
            point: GPoint = list_.get(index)
            if point is not None:
                self.points.getPoints().add(PointFactory.getInstance().createXY(point.getX(), point.getY()))
                self.pointTreeNodeVector.add(DefaultMutableTreeNode(str(point)))
                self.treeNode.add(self.pointTreeNodeVector.get(self.pointTreeNodeVector.size() - 1))
    

    # throws Exception
    def duplicate(self) -> GraphicItemInterface:
        linesGraphicItem: LinesGraphicItem = LinesGraphicItem()
        linesGraphicItem.duplicatePoints(self.points.getPoints())
        linesGraphicItem.deactivate()
        return linesGraphicItem
    

    def getAngle(self) -> float:
        return math.degrees(self.theta)
    

    def setFulcrumPoint(self, point: GPoint) -> None:
        self.fulcrumPoint = point
    

    def paint(self, g: Graphics, canvasAngle: float, dimension: IntegerDimension, x: int, y: int) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.BasicStroke import BasicStroke
        from org.allbinary.graphics.j2me.workarea.tools.PointsUtil import PointsUtil
        try:
            graphics: Graphics2D = g
            graphics.setColor(self.getColor())
            graphics.setStroke(BasicStroke(x))
            if self.isActive() and self.currentMousePoint is not None:
                self.points.getPoints().add(self.currentMousePoint)
            tempPointVector: BasicArrayList = PointsUtil.getInstance().doTransforms(self.points.getPoints(), canvasAngle, PointFactory.getInstance().createXY(dimension.getWidth(), dimension.getHeight()))
            if self.isActive() and self.currentMousePoint is not None:
                self.currentMousePoint = self.points.getPoints().removeAt(self.points.getSize() - 1)
            size: int = tempPointVector.size()
            firstPoint: GPoint = None
            if size > 0:
                firstPoint = tempPointVector.get(0)
            for index in range(1, size):
                secondPoint: GPoint = tempPointVector.get(index)
                graphics.drawLine((firstPoint.getX() * x) - (int(x / 4)), (firstPoint.getY() * y) - (int(y / 4)), (secondPoint.getX() * x) - (int(x / 4)), (secondPoint.getY() * y) - (int(y / 4)))
                firstPoint = secondPoint
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "mouseMoved", e)
    

    # throws Exception
    def toDom(self, canvasDom: CanvasDom) -> Node:
        from org.allbinary.graphics.j2me.workarea.tools.PointsDomUtil import PointsDomUtil
        return PointsDomUtil.getInstance().toDom(canvasDom, self.points.getPoints())
    

    def isValid(self) -> bool:
        return self.points.isValid()
    

    def getPointsInterface(self) -> Points:
        return self.points
    

    def setPointsInterface(self, points: Points) -> None:
        self.points = points
    

    def getColor(self) -> Color:
        return self.color
    

    def setColor(self, color: Color) -> None:
        self.color = color
    

    def mouseClicked(self, mouseEvent: MouseEvent, x: int, y: int) -> None:
        try:
            mousePoint: GPoint = PointFactory.getInstance().createXY(mouseEvent.getPoint().x, mouseEvent.getPoint().y)
            if (mouseEvent.getModifiers() & mouseEvent.BUTTON1_MASK) == mouseEvent.BUTTON1_MASK:
                point: GPoint = PointFactory.getInstance().createXY(mousePoint.getX() / x, mousePoint.getY() / y)
                StatusFactory.getInstance().setStatus("Line Point Added: " + str(point))
                self.addPoint(point)
            elif (mouseEvent.getModifiers() & mouseEvent.BUTTON3_MASK) == mouseEvent.BUTTON3_MASK:
                StatusFactory.getInstance().setStatus("Line Point Removed")
                self.removePoint()
            self.currentMousePoint = mousePoint
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "mouseMoved", e)
    

    def mouseEntered(self, mouseEvent: MouseEvent) -> None:
        pass
    

    def mouseExited(self, mouseEvent: MouseEvent) -> None:
        pass
    

    def mousePressed(self, mouseEvent: MouseEvent, xPixelsPerCell: int, yPixelsPerCell: int) -> None:
        pass
    

    def mouseReleased(self, mouseEvent: MouseEvent, xPixelsPerCell: int, yPixelsPerCell: int) -> None:
        pass
    

    def mouseDragged(self, mouseEvent: MouseEvent, xPixelsPerCell: int, yPixelsPerCell: int) -> None:
        pass
    

    def mouseMoved(self, mouseEvent: MouseEvent, x: int, y: int) -> None:
        try:
            mousePoint: GPoint = PointFactory.getInstance().createXY(mouseEvent.getPoint().x, mouseEvent.getPoint().y)
            point: GPoint = PointFactory.getInstance().createXY(mousePoint.getX() / x, mousePoint.getY() / y)
            self.currentMousePoint = point
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "mouseMoved", e)
    

    def keyPressed(self, keyEvent: KeyEvent) -> None:
        try:
            keyCode: int = keyEvent.getKeyCode()
            if keyCode == keyEvent.VK_ESCAPE:
                StatusFactory.getInstance().setStatus("Deactivated")
                self.deactivate()
            elif keyCode == keyEvent.VK_UP:
                self.translate(0, -1)
            elif keyCode == keyEvent.VK_DOWN:
                self.translate(0, 1)
            elif keyCode == keyEvent.VK_LEFT:
                self.translate(-1, 0)
            elif keyCode == keyEvent.VK_RIGHT:
                self.translate(1, 0)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.gameInputStrings.KEY_PRESSED, e)
    

    def keyReleased(self, keyEvent: KeyEvent) -> None:
        pass
    

    def keyTyped(self, keyEvent: KeyEvent) -> None:
        pass
# from java.awt import *
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.swing.tree.DefaultMutableTreeNode import DefaultMutableTreeNode
# from javax.swing.tree.MutableTreeNode import MutableTreeNode
from org.allbinary.dom.DomHelper import DomHelper
from org.allbinary.game.input.GameInputStrings import GameInputStrings
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
from org.allbinary.graphics.j2me.workarea.canvas.CanvasDom import CanvasDom
from org.allbinary.graphics.j2me.workarea.canvas.IntegerDimension import IntegerDimension
from org.allbinary.graphics.pipeline.BasicGraphicsPipeline import BasicGraphicsPipeline
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.math.PositionStrings import PositionStrings
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList
from org.allbinary.graphics.j2me.workarea.tools.Color import Color


