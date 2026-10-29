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



# Java interface
class GraphicItemInterface:
    

    def getName(self) -> str:
        raise NotImplementedError()
    

    def setColor(self, color: Color) -> None:
        raise NotImplementedError()
    

    def getTreeNode(self) -> MutableTreeNode:
        raise NotImplementedError()
    

    def getPointsInterface(self) -> Points:
        raise NotImplementedError()
    

    def setPointsInterface(self, points: Points) -> None:
        raise NotImplementedError()
    

    def isValid(self) -> bool:
        raise NotImplementedError()
    

    def isActive(self) -> bool:
        raise NotImplementedError()
    

    def deactivate(self) -> None:
        raise NotImplementedError()
    

    def activate(self) -> None:
        raise NotImplementedError()
    

    def setFulcrumPoint(self, point: GPoint) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def translate(self, x: int, y: int) -> None:
        raise NotImplementedError()
    

    def setRotate(self, theta: float) -> None:
        raise NotImplementedError()
    

    def addRotate(self, theta: float) -> None:
        raise NotImplementedError()
    

    def setAngle(self, angle: float) -> None:
        raise NotImplementedError()
    

    def addAngle(self, angle: float) -> None:
        raise NotImplementedError()
    

    def getAngle(self) -> float:
        raise NotImplementedError()
    

    def paint(self, g: Graphics, canvasAngle: float, dimension: IntegerDimension, x: int, y: int) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def toDom(self, canvasDom: CanvasDom) -> Node:
        raise NotImplementedError()
    

    def removePoint(self) -> GPoint:
        raise NotImplementedError()
    

    def addPoint(self, point: GPoint) -> None:
        raise NotImplementedError()
    

    def mouseClicked(self, mouseEvent: MouseEvent, xPixelsPerCell: int, yPixelsPerCell: int) -> None:
        raise NotImplementedError()
    

    def mouseEntered(self, mouseEvent: MouseEvent) -> None:
        raise NotImplementedError()
    

    def mouseExited(self, mouseEvent: MouseEvent) -> None:
        raise NotImplementedError()
    

    def mousePressed(self, mouseEvent: MouseEvent, xPixelsPerCell: int, yPixelsPerCell: int) -> None:
        raise NotImplementedError()
    

    def mouseReleased(self, mouseEvent: MouseEvent, xPixelsPerCell: int, yPixelsPerCell: int) -> None:
        raise NotImplementedError()
    

    def mouseDragged(self, mouseEvent: MouseEvent, xPixelsPerCell: int, yPixelsPerCell: int) -> None:
        raise NotImplementedError()
    

    def mouseMoved(self, mouseEvent: MouseEvent, xPixelsPerCell: int, yPixelsPerCell: int) -> None:
        raise NotImplementedError()
    

    def keyPressed(self, keyEvent: KeyEvent) -> None:
        raise NotImplementedError()
    

    def keyReleased(self, keyEvent: KeyEvent) -> None:
        raise NotImplementedError()
    

    def keyTyped(self, keyEvent: KeyEvent) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def duplicate(self) -> GraphicItemInterface:
        raise NotImplementedError()
# from java.awt import *
# from javax.swing.tree.MutableTreeNode import MutableTreeNode
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.j2me.workarea.canvas.CanvasDom import CanvasDom
from org.allbinary.graphics.j2me.workarea.canvas.IntegerDimension import IntegerDimension
from org.w3c.dom.Node import Node


