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
# package org.allbinary.graphics.j2me.workarea.canvas

from __future__ import annotations



class CanvasDom:
    FRAME: str = "frame"
    ROTATE: str = "rotate"
    SIZE: str = "size"
    X: str = "X"
    Y: str = "Y"
    ZOOM: str = "zoom"
    GRID: str = "grid"
    ENABLED: str = "enabled"
    POSSIBLE: str = "possible"
    GRAPHICITEMS: str = "graphicItems"
    REAL_SIZE: str = "realSize"

    def _init_fields(self) -> None:
        self.graphicsStrings: GraphicsStrings = GraphicsStrings.getInstance()
        self.graphicItemHashMap: dict = None
        self.angle: float = None
        self.dimension: IntegerDimension = None
        self.grid: Grid = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, canvasNode: Node) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.Grid import Grid
        from org.allbinary.graphics.j2me.workarea.canvas.IntegerDimension import IntegerDimension
        self._init_fields()
        self.grid = Grid()
        self.grid.grid = PointFactory.getInstance().createXY(0, 0)
        self.dimension = IntegerDimension(0, 0)
        name: str = canvasNode.getNodeName()
        if ((name > CanvasDom.FRAME) - (name < CanvasDom.FRAME)) == 0:
            self.graphicItemHashMap = StdUtil.getInstance().createHashMap()
            angleNode: Node = DomHelper.getInstance().searchNodeList(self.ROTATE, canvasNode.getChildNodes())
            angleTextNode: Node = angleNode.getFirstChild()
            angle: float = float(float(angleTextNode.getNodeValue()))
            self.setAngle(angle)
            sizeNode: Node = DomHelper.getInstance().searchNodeList(self.SIZE, canvasNode.getChildNodes())
            xNode: Node = DomHelper.getInstance().searchNodeList(self.X, sizeNode.getChildNodes())
            xTextNode: Node = xNode.getFirstChild()
            x: int = int(int(xTextNode.getNodeValue()))
            yNode: Node = DomHelper.getInstance().searchNodeList(self.Y, sizeNode.getChildNodes())
            yTextNode: Node = yNode.getFirstChild()
            y: int = int(int(yTextNode.getNodeValue()))
            self.setWorkArea(x, y)
            zoomNode: Node = DomHelper.getInstance().searchNodeList(self.ZOOM, canvasNode.getChildNodes())
            zoomTextNode: Node = zoomNode.getFirstChild()
            self.grid.setZoom(int(int(zoomTextNode.getNodeValue())))
            gridNode: Node = DomHelper.getInstance().searchNodeList(self.GRID, canvasNode.getChildNodes())
            gridSizeNode: Node = DomHelper.getInstance().searchNodeList(self.SIZE, gridNode.getChildNodes())
            gridXNode: Node = DomHelper.getInstance().searchNodeList(self.X, gridSizeNode.getChildNodes())
            gridXTextNode: Node = gridXNode.getFirstChild()
            gridX: int = int(int(gridXTextNode.getNodeValue()))
            gridYNode: Node = DomHelper.getInstance().searchNodeList(self.Y, gridSizeNode.getChildNodes())
            gridYTextNode: Node = gridYNode.getFirstChild()
            gridY: int = int(int(gridYTextNode.getNodeValue()))
            self.setGrid(gridX, gridY)
            enableNode: Node = DomHelper.getInstance().searchNodeList(self.ENABLED, gridNode.getChildNodes())
            enableTextNode: Node = enableNode.getFirstChild()
            self.grid.showGrid(enableTextNode.getNodeValue())
            possibleNode: Node = DomHelper.getInstance().searchNodeList(self.POSSIBLE, gridNode.getChildNodes())
            possibleTextNode: Node = possibleNode.getFirstChild()
            self.grid.isGridPossible = possibleTextNode.getNodeValue()
            graphicItemNodeList: BasicArrayList = DomHelper.getInstance().getChildrenWithoutTextNodes(self.GRAPHICITEMS, canvasNode.getChildNodes())
            if graphicItemNodeList is not None:
                self.graphicItemHashMap = GraphicItemFactory.getInstance().getInstance(graphicItemNodeList)
        else:
            raise Exception("Frame Element Not Found but Found: " + name)
    

    def _constructor1(self, canvasJPanel: CanvasJPanel) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.Grid import Grid
        self._init_fields()
        self.angle = canvasJPanel.getAngle()
        self.graphicItemHashMap = canvasJPanel.getGraphicItemHashMap()
        self.dimension = canvasJPanel.getCanvasDimension()
        self.grid = Grid(canvasJPanel.getGrid())
        self.angle = canvasJPanel.getAngle()
    

    def getAngle(self) -> float:
        return self.angle
    

    def getGraphicItemHashMap(self) -> dict:
        return self.graphicItemHashMap
    

    def setAngle(self, angle: float) -> None:
        self.angle = angle
    

    # throws Exception
    def setWorkArea(self, x: int, y: int) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.IntegerDimension import IntegerDimension
        self.setDimension(IntegerDimension(x, y))
    

    # throws Exception
    def setGrid(self, gridX: int, gridY: int) -> None:
        self.grid.grid = PointFactory.getInstance().createXY(gridX, gridY)
    

    def getPointNode(self, point: GPoint, pointName: str) -> Node:
        document: Document = WorkAreaJPanel.getDocument()
        pointNode: Node = document.createElement(pointName)
        xNode: Node = document.createElement(self.X)
        xTextNode: Node = document.createTextNode(str(point.getX()))
        xNode.appendChild(xTextNode)
        yNode: Node = document.createElement(self.Y)
        yTextNode: Node = document.createTextNode(str(point.getY()))
        yNode.appendChild(yTextNode)
        pointNode.appendChild(xNode)
        pointNode.appendChild(yNode)
        return pointNode
    

    # throws Exception
    def toDom(self) -> Node:
        document: Document = WorkAreaJPanel.getDocument()
        frameNode: Node = document.createElement(self.FRAME)
        angleNode: Node = document.createElement(self.ROTATE)
        angleTextNode: Node = document.createTextNode(str(float(self.getAngle())))
        angleNode.appendChild(angleTextNode)
        sizeNode: Node = self.getPointNode(PointFactory.getInstance().createXY(self.getDimension().getWidth(), self.getDimension().getHeight()), self.SIZE)
        zoomNode: Node = document.createElement(self.ZOOM)
        zoomTextNode: Node = document.createTextNode(str(int(self.getGrid().getZoom())))
        zoomNode.appendChild(zoomTextNode)
        gridNode: Node = document.createElement(self.GRID)
        gridSizeNode: Node = self.getPointNode(self.getGrid().grid, self.SIZE)
        gridNode.appendChild(gridSizeNode)
        enableNode: Node = document.createElement(self.ENABLED)
        enableTextNode: Node = document.createTextNode(str(self.getGrid().isGridOn()))
        enableNode.appendChild(enableTextNode)
        gridNode.appendChild(enableNode)
        possibleNode: Node = document.createElement(self.POSSIBLE)
        possibleTextNode: Node = document.createTextNode(str(self.getGrid().isGridPossible()))
        possibleNode.appendChild(possibleTextNode)
        gridNode.appendChild(possibleNode)
        realSizeNode: Node = document.createElement(CanvasDom.REAL_SIZE)
        vectorCenterGenerator: VectorCenterGenerator = VectorCenterGenerator()
        vectorCenterGenerator.calculate(self.getGraphicItemHashMap())
        widthNode: Node = document.createElement(self.graphicsStrings.WIDTH)
        widthTextNode: Node = document.createTextNode(str(vectorCenterGenerator.getWidth()))
        widthNode.appendChild(widthTextNode)
        realSizeNode.appendChild(widthNode)
        heightNode: Node = document.createElement(self.graphicsStrings.HEIGHT)
        heightTextNode: Node = document.createTextNode(str(vectorCenterGenerator.getHeight()))
        heightNode.appendChild(heightTextNode)
        realSizeNode.appendChild(heightNode)
        frameNode.appendChild(angleNode)
        frameNode.appendChild(sizeNode)
        frameNode.appendChild(zoomNode)
        frameNode.appendChild(gridNode)
        frameNode.appendChild(realSizeNode)
        graphicItemNode: Node = document.createElement(self.GRAPHICITEMS)
        graphicItemArray: list[object] = self.getGraphicItemHashMap().keySet().toArray()
        size: int = len(graphicItemArray)
        for index in range(0, size):
            item: GraphicItemInterface = self.graphicItemHashMap.get(graphicItemArray[index])
            if item.getName() == LinesGraphicItem.getStaticName():
                if item.isValid():
                    graphicItemNode.appendChild(item.toDom(self))
        frameNode.appendChild(graphicItemNode)
        return frameNode
    

    def getDimension(self) -> IntegerDimension:
        return self.dimension
    

    def setDimension(self, dimension: IntegerDimension) -> None:
        self.dimension = dimension
    

    def getGrid(self) -> Grid:
        return self.grid
# from java.util.HashMap import HashMap
from org.allbinary.animation.vector.VectorCenterGenerator import VectorCenterGenerator
from org.allbinary.dom.DomHelper import DomHelper
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.GraphicsStrings import GraphicsStrings
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.j2me.workarea.WorkAreaJPanel import WorkAreaJPanel
from org.allbinary.graphics.j2me.workarea.tools.GraphicItemFactory import GraphicItemFactory
from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
from org.allbinary.graphics.j2me.workarea.tools.LinesGraphicItem import LinesGraphicItem
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.w3c.dom.Node import Node


