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
from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface


class SelectionTool(GraphicItemInterface):
    NAME: str = "Selection Tool"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.canvasJPanel: CanvasJPanel = None
        self.active: bool = True
        self.controlIdDown: bool = False
        self.rectColor: Color = Color(int(BasicColorFactory.getInstance().RED))
        self.startPoint: GPoint = PointFactory.getInstance().ZERO_ZERO
        self.endPoint: GPoint = self.startPoint
    

    def __init__(self, canvasJPanel: CanvasJPanel) -> None:
        self._init_fields()
        self.canvasJPanel = canvasJPanel
    

    def setColor(self, color: Color) -> None:
        pass
    

    def getTreeNode(self) -> MutableTreeNode:
        return None
    

    def getPointsInterface(self) -> Points:
        return None
    

    def setPointsInterface(self, points: Points) -> None:
        pass
    

    def isValid(self) -> bool:
        return True
    

    def isActive(self) -> bool:
        return self.active
    

    def deactivate(self) -> None:
        pass
    

    def activate(self) -> None:
        pass
    

    def setFulcrumPoint(self, point: GPoint) -> None:
        pass
    

    # throws Exception
    def translate(self, x: int, y: int) -> None:
        pass
    

    def setRotate(self, theta: float) -> None:
        pass
    

    def addRotate(self, theta: float) -> None:
        pass
    

    def setAngle(self, angle: float) -> None:
        pass
    

    def addAngle(self, angle: float) -> None:
        pass
    

    def getAngle(self) -> float:
        return 0.0
    

    def makeSelection(self) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.LinesGraphicItem import LinesGraphicItem
        from org.allbinary.graphics.j2me.workarea.tools.Color import Color
        from org.allbinary.graphics.j2me.workarea.tools.Color import Color
        xRect: int = self.getXRect()
        xRect2: int = abs(self.endPoint.getX() - self.startPoint.getX()) + xRect
        yRect: int = self.getYRect()
        yRect2: int = abs(self.endPoint.getY() - self.startPoint.getY()) + yRect
        hashMap: dict = self.canvasJPanel.getGraphicItemHashMap()
        graphicItemArray: list[object] = hashMap.keySet().toArray()
        size: int = len(graphicItemArray)
        for index in range(0, size):
            item: GraphicItemInterface = hashMap.get(graphicItemArray[index])
            if item.getName() == LinesGraphicItem.getStaticName():
                if RectangleCollisionPointUtil.allPointsInsideCell(xRect, yRect, xRect2, yRect2, item.getPointsInterface().getPoints(), self.canvasJPanel.getXPixelsPerWorkAreaPixel(), self.canvasJPanel.getYPixelsPerWorkAreaPixel()):
                    item.setColor(Color.YELLOW)
                    item.activate()
                elif not self.controlIdDown:
                    item.setColor(Color.WHITE)
                    item.deactivate()
    

    def getXRect(self) -> int:
        xDiff: int = self.endPoint.getX() - self.startPoint.getX()
        xRect: int = self.startPoint.getX()
        if xDiff < 0:
            xRect = self.endPoint.getX()
        return xRect
    

    def getYRect(self) -> int:
        yDiff: int = self.endPoint.getY() - self.startPoint.getY()
        yRect: int = self.startPoint.getY()
        if yDiff < 0:
            yRect = self.endPoint.getY()
        return yRect
    

    def paint(self, g: Graphics, canvasAngle: float, dimension: IntegerDimension, x: int, y: int) -> None:
        g.setColor(self.rectColor)
        xRect: int = self.getXRect()
        width: int = abs(self.endPoint.getX() - self.startPoint.getX())
        yRect: int = self.getYRect()
        height: int = abs(self.endPoint.getY() - self.startPoint.getY())
        g.drawRect(xRect, yRect, width, height)
    

    # throws Exception
    def toDom(self, canvasDom: CanvasDom) -> Node:
        return None
    

    def removePoint(self) -> GPoint:
        return None
    

    def addPoint(self, point: GPoint) -> None:
        pass
    

    def getName(self) -> str:
        return SelectionTool.NAME
    

    @staticmethod
    def getStaticName() -> str:
        return SelectionTool.NAME
    

    def mouseClicked(self, mouseEvent: MouseEvent, xPixelsPerCell: int, yPixelsPerCell: int) -> None:
        pass
    

    def mouseMoved(self, mouseEvent: MouseEvent, xPixelsPerCell: int, yPixelsPerCell: int) -> None:
        pass
    

    def mouseEntered(self, mouseEvent: MouseEvent) -> None:
        pass
    

    def mouseExited(self, mouseEvent: MouseEvent) -> None:
        pass
    

    def mousePressed(self, mouseEvent: MouseEvent, xPixelsPerCell: int, yPixelsPerCell: int) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.MouseStrings import MouseStrings
        self.logUtil.putF(self.commonStrings.START, self, MouseStrings.getInstance().MOUSE_PRESSED)
        self.startPoint = PointFactory.getInstance().createXY(mouseEvent.getX(), mouseEvent.getY())
        self.endPoint = self.startPoint
    

    def mouseReleased(self, mouseEvent: MouseEvent, xPixelsPerCell: int, yPixelsPerCell: int) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.MouseStrings import MouseStrings
        self.logUtil.putF(self.commonStrings.START, self, MouseStrings.getInstance().MOUSE_RELEASED)
        self.endPoint = PointFactory.getInstance().createXY(mouseEvent.getX(), mouseEvent.getY())
        self.active = False
        self.makeSelection()
    

    def mouseDragged(self, mouseEvent: MouseEvent, xPixelsPerCell: int, yPixelsPerCell: int) -> None:
        self.endPoint = PointFactory.getInstance().createXY(mouseEvent.getX(), mouseEvent.getY())
    

    def keyPressed(self, keyEvent: KeyEvent) -> None:
        if keyEvent.getKeyCode() == keyEvent.VK_CONTROL:
            self.controlIdDown = True
    

    def keyReleased(self, keyEvent: KeyEvent) -> None:
        if keyEvent.getKeyCode() == keyEvent.VK_CONTROL:
            self.controlIdDown = False
    

    def keyTyped(self, keyEvent: KeyEvent) -> None:
        pass
    

    # throws Exception
    def duplicate(self) -> GraphicItemInterface:
        return None
# from java.awt import *
# from java.util.HashMap import HashMap
# from javax.swing.tree.MutableTreeNode import MutableTreeNode
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.j2me.workarea.canvas.CanvasDom import CanvasDom
from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
from org.allbinary.graphics.j2me.workarea.canvas.IntegerDimension import IntegerDimension
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.math.RectangleCollisionPointUtil import RectangleCollisionPointUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Node import Node
from org.allbinary.graphics.j2me.workarea.tools.Color import Color


