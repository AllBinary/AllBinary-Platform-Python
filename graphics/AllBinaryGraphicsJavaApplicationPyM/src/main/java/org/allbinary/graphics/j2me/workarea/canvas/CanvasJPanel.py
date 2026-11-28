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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_divide
from java.lang.JavaRuntimeStatic import lazy_static
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEventListener import MyGraphicItemEventListener
# from java.awt.event.KeyListener import KeyListener
# from java.awt.event.MouseListener import MouseListener
# from java.awt.event.MouseMotionListener import MouseMotionListener
# from javax.swing.JPanel import JPanel


@java_inherited_overloads
class CanvasJPanel(*java_bases(JPanel, MouseListener, MouseMotionListener, KeyListener, MyGraphicItemEventListener)):
    frame: int = 0
    gridColor: Color = None
    backgroundColor: Color = None
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("guiLog", None)
        vars(self).setdefault("gameInputStrings", None)
        vars(self).setdefault("selectedTool", None)
        vars(self).setdefault("graphicItemHashMap", None)
        vars(self).setdefault("canvasDimension", None)
        vars(self).setdefault("angle", 0.0)
        vars(self).setdefault("canvasTreeNode", None)
        vars(self).setdefault("frameLabel", None)
        vars(self).setdefault("workAreaJTreeJPanel", None)
        vars(self).setdefault("grid", None)

    def _init_fields(self) -> None:
        from org.allbinary.game.input.GameInputStrings import GameInputStrings
        from org.allbinary.logic.communication.log.GuiLog import GuiLog
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.guiLog: GuiLog = GuiLog.getInstance()
        self.gameInputStrings: GameInputStrings = GameInputStrings.getInstance()
        self.selectedTool: GraphicItemInterface = None
        if "graphicItemHashMap" not in vars(self): self.graphicItemHashMap: HashMap = None
        if "canvasDimension" not in vars(self): self.canvasDimension: IntegerDimension = None
        self.angle: float = 0.0
        if "canvasTreeNode" not in vars(self): self.canvasTreeNode: DefaultMutableTreeNode = None
        if "frameLabel" not in vars(self): self.frameLabel: CanvasTreeLabel = None
        if "workAreaJTreeJPanel" not in vars(self): self.workAreaJTreeJPanel: WorkAreaJTreeJPanel = None
        if "grid" not in vars(self): self.grid: Grid = None

    def __init__(self, *args) -> None:
        if len(args) == 4:
            __class__._constructor4(self, *args)
        elif len(args) == 3:
            __class__._constructor3(self, *args)
    

    def _constructor4(self, workAreaJTreeJPanel: WorkAreaJTreeJPanel, dimension: Dimension, x: int, y: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.j2me.workarea.canvas.Grid import Grid
        from org.allbinary.graphics.j2me.workarea.WorkAreaJTreeJPanel import WorkAreaJTreeJPanel
        from org.allbinary.log.LOGGING import LOGGING
        super().__init__()
        __class__._init_fields(self)
        self.grid = Grid()
        try:
            self.workAreaJTreeJPanel = workAreaJTreeJPanel
            self.initComponents()
            self.initMyComponents()
            self.setSize(dimension)
            self.setCanvasSize(x, y)
        except Exception as e:
            if LOGGING.contains(LOGGING.GRAPHICSCREATION):
                self.guiLog.put("Constructor Error", self, "contructor", e)
    

    def _constructor3(self, workAreaJTreeJPanel: WorkAreaJTreeJPanel, dimension: Dimension, canvasDom: CanvasDom) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.j2me.workarea.canvas.Grid import Grid
        from org.allbinary.graphics.j2me.workarea.WorkAreaJTreeJPanel import WorkAreaJTreeJPanel
        from org.allbinary.log.LOGGING import LOGGING
        super().__init__()
        __class__._init_fields(self)
        self.grid = Grid(canvasDom.getGrid())
        try:
            self.workAreaJTreeJPanel = workAreaJTreeJPanel
            self.initComponents()
            self.initMyComponents()
            self.setSize(dimension)
            self.setCanvasSize(canvasDom.getDimension().getWidth(), canvasDom.getDimension().getHeight())
            self.graphicItemHashMap = canvasDom.getGraphicItemHashMap()
            graphicItemArray: list[object] = self.graphicItemHashMap.keySet().toArray()
            size: int = len(graphicItemArray)
            for index in range(0, size):
                graphicItemTreeNode: MutableTreeNode = graphicItemArray[index]
                self.canvasTreeNode.add(graphicItemTreeNode)
            self.repaint()
            self.setAngle(canvasDom.getAngle())
            self.workAreaJTreeJPanel.updateTree()
            self.workAreaJTreeJPanel.expand()
            self.workAreaJTreeJPanel.repaint()
        except Exception as e:
            if LOGGING.contains(LOGGING.GRAPHICSCREATION):
                self.guiLog.put("Constructor Error", self, "contructor", e)
    

    # throws Exception
    def initMyComponents(self) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasTreeLabel import CanvasTreeLabel
        from org.allbinary.graphics.j2me.workarea.canvas.IntegerDimension import IntegerDimension
        from org.allbinary.graphics.PointFactory import PointFactory
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEventService import MyGraphicItemEventService
        from org.allbinary.logic.StdUtil import StdUtil
        self.frameLabel = CanvasTreeLabel("FrameLabel" + str(int(CanvasJPanel.frame)))
        self.canvasTreeNode = DefaultMutableTreeNode(self.frameLabel)
        CanvasJPanel.frame += 1
        self.workAreaJTreeJPanel.add(self.getTreeNode())
        self.graphicItemHashMap = StdUtil.getInstance().createHashMap()
        self.grid.grid = PointFactory.getInstance().createXY(0, 0)
        self.setCanvasDimension(IntegerDimension(0, 0))
        self.selectedTool = None
        self.addKeyListener(self)
        self.addMouseListener(self)
        self.addMouseMotionListener(self)
        MyGraphicItemEventService.addListener(self)
    

    def getTreeNode(self) -> MutableTreeNode:
        return self.canvasTreeNode
    

    def initComponents(self) -> None:
        self.setLayout(GridLayout(1, 1))
    

    # throws Exception
    def setCanvasSize(self, x: int, y: int) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.IntegerDimension import IntegerDimension
        from org.allbinary.graphics.j2me.GraphicsException import GraphicsException
        self.grid.isGridPossible = True
        if x <= 0:
            self.grid.isGridPossible = False
            raise GraphicsException("X Size Error: " + str(x), self, "setWorkAreaSize")
        if y <= 0:
            self.grid.isGridPossible = False
            raise GraphicsException("Y Size Error: " + str(y), self, "setWorkAreaSize")
        if x > self.getWidth():
            self.grid.isGridPossible = False
        if y > self.getHeight():
            self.grid.isGridPossible = False
        self.setCanvasDimension(IntegerDimension(x, y))
        self.grid.isChanged = True
    

    def setGrid_j1(self, point: GPoint) -> None:
        from org.allbinary.graphics.GPoint import GPoint
        self.setGrid(point.getX(), point.getY())
    

    def setGrid_j2(self, xSize: int, ySize: int) -> None:
        from org.allbinary.graphics.PointFactory import PointFactory
        from org.allbinary.graphics.j2me.GraphicsException import GraphicsException
        try:
            if xSize >= java_divide(self.getCanvasDimension().getWidth(), 2) or xSize < 1:
                raise GraphicsException("X Size Error: " + str(xSize) + " WorkArea X: " + str(self.getCanvasDimension().getWidth()), self, "setGrid")
            if ySize >= java_divide(self.getCanvasDimension().getHeight(), 2) or ySize < 1:
                raise GraphicsException("Y Size Error" + str(ySize) + " WorkArea Y: " + str(self.getCanvasDimension().getHeight()), self, "setGrid")
            self.grid.grid = PointFactory.getInstance().createXY(xSize, ySize)
            self.grid.isChanged = True
        except Exception as e:
            pass

    def setGrid(self, *args):
        implementation = __class__.__dict__.get("setGrid_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().setGrid(*args)
    

    # throws Exception
    def setDefaultGrid(self) -> None:
        xPixelsPerWorkAreaPixel: int = java_divide(self.getWidth(), self.getCanvasDimension().getWidth())
        yPixelsPerWorkAreaPixel: int = java_divide(self.getHeight(), self.getCanvasDimension().getHeight())
        self.setGrid(1, 1)
        self.grid.isChanged = True
    

    def getAngle(self) -> float:
        return self.angle
    

    def setAngle(self, angle: float) -> None:
        self.angle = angle
    

    def addAngle(self, angle: float) -> None:
        self.setAngle(self.angle + angle)
    

    def explodeAll(self) -> None:
        from org.allbinary.graphics.GPoint import GPoint
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemFactory import GraphicItemFactory
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
        from org.allbinary.graphics.j2me.workarea.tools.LinesGraphicItem import LinesGraphicItem
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        newPoints: BasicArrayList = BasicArrayListD()
        graphicItemArray: list[object] = self.getGraphicItemHashMap().keySet().toArray()
        size: int = len(graphicItemArray)
        for index in range(0, size):
            graphicItemNode: MutableTreeNode = graphicItemArray[index]
            graphicItem: GraphicItemInterface = self.getGraphicItemHashMap().get(graphicItemNode)
            if graphicItem.getName() == LinesGraphicItem.getStaticName():
                while graphicItem.getPointsInterface().getSize() > 2:
                    newGraphicItem: GraphicItemInterface = GraphicItemFactory.getInstance().getInstance(graphicItem.getName()).getInstance(self)
                    pointOne: GPoint = GPoint.getInstance(graphicItem.removePoint())
                    pointTwo: GPoint = GPoint.getInstance(graphicItem.removePoint())
                    if pointOne is not None and pointTwo is not None:
                        newGraphicItem.addPoint(pointOne)
                        newGraphicItem.addPoint(pointTwo)
                    newPoints.add(newGraphicItem)
        size2: int = newPoints.size()
        for index in range(0, size2):
            newGraphicItem: GraphicItemInterface = newPoints.get(index)
            self.canvasTreeNode.add(newGraphicItem.getTreeNode())
            self.getGraphicItemHashMap().put(newGraphicItem.getTreeNode(), newGraphicItem)
        self.workAreaJTreeJPanel.updateTree()
        self.workAreaJTreeJPanel.expand()
        self.workAreaJTreeJPanel.repaint()
    

    # throws Exception
    def explode(self, howMuch: int, explosionType: int) -> None:
        from org.allbinary.animation.VectorExplosionGenerator import VectorExplosionGenerator
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
        from org.allbinary.graphics.j2me.workarea.tools.Points import Points
        from org.allbinary.graphics.pipeline.RandomRotationFactory import RandomRotationFactory
        from org.allbinary.util.BasicArrayList import BasicArrayList
        graphicItemArray: list[object] = self.getGraphicItemHashMap().keySet().toArray()
        size: int = len(graphicItemArray)
        for index in range(0, size):
            item: GraphicItemInterface = self.getGraphicItemHashMap().get(graphicItemArray[index])
            basicArrayList: BasicArrayList = VectorExplosionGenerator.getInstance().createList(item.getPointsInterface().getPoints(), howMuch, VectorExplosionGenerator.getInstance().RANDOM)
            newPoints: Points = Points()
            newPoints.addPoints(basicArrayList)
            item.setPointsInterface(newPoints)
            angleDelta: int = RandomRotationFactory.getInstance().getNextRandomAngle(howMuch)
            item.setAngle(angleDelta)
        self.repaint()
    

    # throws Exception
    def mirror(self) -> None:
        from org.allbinary.animation.VectorMirrorGenerator import VectorMirrorGenerator
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
        from org.allbinary.graphics.j2me.workarea.tools.Points import Points
        from org.allbinary.util.BasicArrayList import BasicArrayList
        width: int = self.getCanvasDimension().getWidth()
        graphicItemArray: list[object] = self.getGraphicItemHashMap().keySet().toArray()
        size: int = len(graphicItemArray)
        for index in range(0, size):
            item: GraphicItemInterface = self.getGraphicItemHashMap().get(graphicItemArray[index])
            basicArrayList: BasicArrayList = VectorMirrorGenerator.getInstance().getInstance(item.getPointsInterface().getPoints(), width)
            newPoints: Points = Points()
            newPoints.addPoints(basicArrayList)
            item.setPointsInterface(newPoints)
        self.repaint()
    

    # throws Exception
    def center(self) -> None:
        from org.allbinary.animation.vector.VectorCenterGenerator import VectorCenterGenerator
        VectorCenterGenerator().transform(self.getGraphicItemHashMap())
        self.repaint()
    

    def setNewTool(self) -> None:
        from org.allbinary.graphics.j2me.GraphicsException import GraphicsException
        from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
        from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
        try:
            StatusFactory.getInstance().setStatus("Tool Selected")
            self.selectedTool = ToolFactory.getInstance().getSelectedToolFactory().getInstance(self)
            newNode: MutableTreeNode = self.selectedTool.getTreeNode()
            self.getGraphicItemHashMap().put(newNode, self.selectedTool)
            self.canvasTreeNode.add(newNode)
            if self.getSelectedTool() is None:
                raise GraphicsException("No Tool Selected", self, "setSelectedTool")
        except Exception as e:
            pass
    

    # throws Exception
    def duplicateGraphicItem(self, graphicItem: GraphicItemInterface) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
        graphicItemClone: GraphicItemInterface = graphicItem.duplicate()
        self.getGraphicItemHashMap().put(graphicItemClone.getTreeNode(), graphicItemClone)
        self.canvasTreeNode.add(graphicItemClone.getTreeNode())
    

    # throws Exception
    def duplicateGraphicItemHashMap(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
        mutableTreeNodeArray: list[object] = hashMap.keySet().toArray()
        size: int = len(mutableTreeNodeArray)
        for index in range(0, size):
            treeNode: MutableTreeNode = mutableTreeNodeArray[index]
            graphicItem: GraphicItemInterface = hashMap.get(treeNode)
            self.duplicateGraphicItem(graphicItem)
    

    def getGraphicItemHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        return self.graphicItemHashMap
    

    def getXPixelsPerWorkAreaPixel(self) -> int:
        x: int = java_divide(self.getGrid().grid.getX() * (self.getWidth() - 10), self.getCanvasDimension().getWidth())
        if self.getGrid().getZoom() == 1:
            return 1
        else:
            return x
    

    def getYPixelsPerWorkAreaPixel(self) -> int:
        y: int = java_divide(self.getGrid().grid.getY() * (self.getHeight() - 10), self.getCanvasDimension().getHeight())
        if self.getGrid().getZoom() == 1:
            return 1
        else:
            return y
    

    def getSelectedTool(self) -> GraphicItemInterface:
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
        return self.selectedTool
    

    def drawItems(self, graphics: Graphics) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
        angleDouble: float = float(self.angle)
        graphicItemArray: list[object] = self.getGraphicItemHashMap().keySet().toArray()
        size: int = len(graphicItemArray)
        for index in range(0, size):
            item: GraphicItemInterface = self.getGraphicItemHashMap().get(graphicItemArray[index])
            item.paint(graphics, angleDouble, self.getCanvasDimension(), self.getXPixelsPerWorkAreaPixel(), self.getYPixelsPerWorkAreaPixel())
    

    def drawGrid(self, graphics: Graphics) -> None:
        xAdjust: int = java_divide((self.getWidth() % self.getXPixelsPerWorkAreaPixel()), 2)
        yAdjust: int = java_divide((self.getHeight() % self.getYPixelsPerWorkAreaPixel()), 2)
        xLeft: int = xAdjust
        yUpper: int = yAdjust
        xRight: int = self.getWidth() - xAdjust
        yLower: int = self.getHeight() - yAdjust
        graphics.setColor(CanvasJPanel.gridColor)
        for value in range(yAdjust, self.getHeight() - yAdjust + 1, self.getYPixelsPerWorkAreaPixel()):
            graphics.drawLine(xLeft, value, xRight, value)
        for value in range(xAdjust, self.getWidth() - xAdjust + 1, self.getYPixelsPerWorkAreaPixel()):
            graphics.drawLine(value, yUpper, value, yLower)
    

    def paint(self, graphics: Graphics) -> None:
        try:
            if self.getGrid().isChanged:
                graphics.setColor(CanvasJPanel.backgroundColor)
                graphics.fillRect(0, 0, self.getWidth(), self.getHeight())
                if self.getGrid().getZoom() > 2 and self.getGrid().isGridOn and self.getGrid().isGridPossible:
                    self.setDefaultGrid()
                    self.drawGrid(graphics)
                self.drawItems(graphics)
                graphics.drawString(str(float(self.getAngle())), self.getWidth() - 75, self.getHeight() - 15)
                self.grid.isChanged = False
        except Exception as e:
            pass
    

    def repaint(self) -> None:
        if self.grid is not None:
            self.grid.isChanged = True
        java_super_call(super(), "repaint")
    

    # throws Exception
    def toDom(self) -> Node:
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasDom import CanvasDom
        from org.w3c.dom.Node import Node
        return CanvasDom(self).toDom()
    

    def changed(self) -> None:
        self.grid.isChanged = True
    

    def mouseClicked(self, mouseEvent: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
        from org.allbinary.graphics.j2me.workarea.tools.MouseStrings import MouseStrings
        StatusFactory.getInstance().setStatusNoLog(MouseStrings.getInstance().MOUSE_CLICKED_LABEL + self.logMouseEvent(mouseEvent))
        if self.getSelectedTool() is not None and java_predicate(self.getSelectedTool(), "isActive"):
            graphicItem: GraphicItemInterface = self.getSelectedTool()
            graphicItem.mouseClicked(mouseEvent, self.getXPixelsPerWorkAreaPixel(), self.getYPixelsPerWorkAreaPixel())
        else:
            self.setNewTool()
            graphicItem: GraphicItemInterface = self.getSelectedTool()
            if graphicItem is not None:
                graphicItem.mouseClicked(mouseEvent, self.getXPixelsPerWorkAreaPixel(), self.getYPixelsPerWorkAreaPixel())
        self.grid.isChanged = True
        self.repaint()
        self.workAreaJTreeJPanel.updateTree()
        self.workAreaJTreeJPanel.expand()
        self.workAreaJTreeJPanel.repaint()
    

    def mouseEntered(self, mouseEvent: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
        StatusFactory.getInstance().setStatusNoLog(self.logMouseEvent(mouseEvent))
    

    def mouseExited(self, mouseEvent: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
        StatusFactory.getInstance().setStatusNoLog(self.logMouseEvent(mouseEvent))
    

    def mousePressed(self, mouseEvent: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
        from org.allbinary.graphics.j2me.workarea.tools.MouseStrings import MouseStrings
        StatusFactory.getInstance().setStatusNoLog(MouseStrings.getInstance().MOUSE_PRESSED_LABEL + self.logMouseEvent(mouseEvent))
        if self.getSelectedTool() is not None:
            graphicItem: GraphicItemInterface = self.getSelectedTool()
            graphicItem.mousePressed(mouseEvent, self.getXPixelsPerWorkAreaPixel(), self.getYPixelsPerWorkAreaPixel())
        self.requestFocus()
        self.grid.isChanged = True
        self.repaint()
    

    def mouseReleased(self, mouseEvent: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
        from org.allbinary.graphics.j2me.workarea.tools.MouseStrings import MouseStrings
        StatusFactory.getInstance().setStatusNoLog(MouseStrings.getInstance().MOUSE_RELEASED_LABEL + self.logMouseEvent(mouseEvent))
        graphicItem: GraphicItemInterface = self.getSelectedTool()
        if graphicItem is not None:
            graphicItem.mouseReleased(mouseEvent, self.getXPixelsPerWorkAreaPixel(), self.getYPixelsPerWorkAreaPixel())
        self.requestFocus()
        self.grid.isChanged = True
        self.repaint()
    

    def mouseDragged(self, mouseEvent: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
        from org.allbinary.graphics.j2me.workarea.tools.MouseStrings import MouseStrings
        StatusFactory.getInstance().setStatusNoLog(MouseStrings.getInstance().MOUSE_DRAGGED_LABEL + self.logMouseEvent(mouseEvent))
        graphicItem: GraphicItemInterface = self.getSelectedTool()
        if graphicItem is not None:
            graphicItem.mouseDragged(mouseEvent, self.getXPixelsPerWorkAreaPixel(), self.getYPixelsPerWorkAreaPixel())
        self.requestFocus()
        self.grid.isChanged = True
        self.repaint()
    

    def mouseMoved(self, mouseEvent: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
        from org.allbinary.graphics.j2me.workarea.tools.MouseStrings import MouseStrings
        StatusFactory.getInstance().setStatusNoLog(MouseStrings.getInstance().MOUSE_MOVED_LABEL + self.logMouseEvent(mouseEvent))
        if self.getSelectedTool() is not None and java_predicate(self.getSelectedTool(), "isActive"):
            graphicItem: GraphicItemInterface = self.getSelectedTool()
            graphicItem.mouseMoved(mouseEvent, self.getXPixelsPerWorkAreaPixel(), self.getYPixelsPerWorkAreaPixel())
        self.requestFocus()
        self.grid.isChanged = True
        self.repaint()
    

    def logMouseEvent(self, mouseEvent: MouseEvent) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.math.PositionStrings import PositionStrings
        from org.allbinary.string.CommonSeps import CommonSeps
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(PositionStrings.getInstance().X_LABEL)
        stringBuffer.appendint(int(java_divide(mouseEvent.getX(), self.getXPixelsPerWorkAreaPixel())))
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(PositionStrings.getInstance().Y_LABEL)
        stringBuffer.appendint(int(java_divide(mouseEvent.getY(), self.getYPixelsPerWorkAreaPixel())))
        return str(stringBuffer)
    

    def keyPressed(self, keyEvent: KeyEvent) -> None:
        from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
        from org.allbinary.string.CommonStrings import CommonStrings
        StatusFactory.getInstance().setStatus("Key Pressed")
        try:
            graphicItemArray: list[object] = self.graphicItemHashMap.keySet().toArray()
            size: int = len(graphicItemArray)
            for index in range(0, size):
                graphicItemInterface: GraphicItemInterface = self.graphicItemHashMap.get(graphicItemArray[index])
                keyCode: int = keyEvent.getKeyCode()
                if java_predicate(graphicItemInterface, "isActive"):
                    if keyCode == keyEvent.VK_UP:
                        graphicItemInterface.translate(0, -1)
                    elif keyCode == keyEvent.VK_DOWN:
                        graphicItemInterface.translate(0, 1)
                    elif keyCode == keyEvent.VK_LEFT:
                        graphicItemInterface.translate(-1, 0)
                    elif keyCode == keyEvent.VK_RIGHT:
                        graphicItemInterface.translate(1, 0)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, self.gameInputStrings.KEY_PRESSED, e)
        if self.getSelectedTool() is not None and java_predicate(self.getSelectedTool(), "isActive"):
            StatusFactory.getInstance().setStatus("Key Pressed for Tool")
            graphicItem: GraphicItemInterface = self.getSelectedTool()
            graphicItem.keyPressed(keyEvent)
        else:
            self.setNewTool()
        self.grid.isChanged = True
        self.repaint()
    

    def keyReleased(self, keyEvent: KeyEvent) -> None:
        pass
    

    def keyTyped(self, keyEvent: KeyEvent) -> None:
        pass
    

    def delete(self, evt: MyGraphicItemEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEvent import MyGraphicItemEvent
        self.getGraphicItemHashMap().remove(evt.getTreeNode())
        self.workAreaJTreeJPanel.updateTree()
        self.workAreaJTreeJPanel.expand()
        self.workAreaJTreeJPanel.repaint()
    

    def deselect(self, evt: MyGraphicItemEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEvent import MyGraphicItemEvent
        graphicItemInterface: GraphicItemInterface = self.getGraphicItemHashMap().get(evt.getTreeNode())
        if graphicItemInterface is not None:
            graphicItemInterface.setColor(Color.WHITE)
            graphicItemInterface.deactivate()
            self.workAreaJTreeJPanel.repaint()
    

    def highlight(self, evt: MyGraphicItemEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEvent import MyGraphicItemEvent
        graphicItemInterface: GraphicItemInterface = self.getGraphicItemHashMap().get(evt.getTreeNode())
        if graphicItemInterface is not None:
            graphicItemInterface.setColor(Color.YELLOW)
            graphicItemInterface.activate()
            self.workAreaJTreeJPanel.repaint()
    

    # throws Exception
    def duplicate_j0(self) -> CanvasJPanel:
        newCanvasJPanel: CanvasJPanel = CanvasJPanel(self.workAreaJTreeJPanel, self.getSize(), self.getCanvasDimension().getWidth(), self.getCanvasDimension().getHeight())
        newCanvasJPanel.setGrid(self.getGrid().getGrid())
        newCanvasJPanel.setAngle(self.getAngle())
        newCanvasJPanel.duplicateGraphicItemHashMap(self.getGraphicItemHashMap())
        self.workAreaJTreeJPanel.updateTree()
        self.workAreaJTreeJPanel.expand()
        self.workAreaJTreeJPanel.repaint()
        return newCanvasJPanel
    

    # throws Exception
    def duplicate_j1(self, event: MyGraphicItemEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEvent import MyGraphicItemEvent
        treeNode: MutableTreeNode = event.getTreeNode()
        graphicItem: GraphicItemInterface = self.getGraphicItemHashMap().get(treeNode)
        if graphicItem is not None:
            self.duplicateGraphicItem(graphicItem)
            self.workAreaJTreeJPanel.updateTree()
            self.workAreaJTreeJPanel.expand()
            self.workAreaJTreeJPanel.repaint()

    def duplicate(self, *args):
        implementation = __class__.__dict__.get("duplicate_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().duplicate(*args)
    

    def rotate(self, event: MyGraphicItemEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEvent import MyGraphicItemEvent
        treeNode: MutableTreeNode = event.getTreeNode()
        graphicItem: GraphicItemInterface = self.getGraphicItemHashMap().get(treeNode)
        if graphicItem is not None:
            graphicItem.addAngle(event.getAngle())
    

    def getCanvasDimension(self) -> IntegerDimension:
        return self.canvasDimension
    

    def setCanvasDimension(self, canvasDimension: IntegerDimension) -> None:
        self.canvasDimension = canvasDimension
    

    def getGrid(self) -> Grid:
        return self.grid
# from java.awt.Color import Color
# from java.awt.Dimension import Dimension
# from java.awt.Graphics import Graphics
# from java.util.HashMap import HashMap
# from javax.swing.tree.DefaultMutableTreeNode import DefaultMutableTreeNode
# from javax.swing.tree.MutableTreeNode import MutableTreeNode
# from org.allbinary.animation.VectorExplosionGenerator import VectorExplosionGenerator
# from org.allbinary.animation.VectorMirrorGenerator import VectorMirrorGenerator
# from org.allbinary.animation.vector.VectorCenterGenerator import VectorCenterGenerator
# from org.allbinary.game.input.GameInputStrings import GameInputStrings
# from org.allbinary.graphics.GPoint import GPoint
# from org.allbinary.graphics.PointFactory import PointFactory
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.graphics.j2me.GraphicsException import GraphicsException
# from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
# from org.allbinary.graphics.j2me.workarea.WorkAreaJTreeJPanel import WorkAreaJTreeJPanel
# from org.allbinary.graphics.j2me.workarea.tools.GraphicItemFactory import GraphicItemFactory
# from org.allbinary.graphics.j2me.workarea.tools.GraphicItemInterface import GraphicItemInterface
# from org.allbinary.graphics.j2me.workarea.tools.LinesGraphicItem import LinesGraphicItem
# from org.allbinary.graphics.j2me.workarea.tools.MouseStrings import MouseStrings
# from org.allbinary.graphics.j2me.workarea.tools.Points import Points
# from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
# from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEvent import MyGraphicItemEvent
# from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEventService import MyGraphicItemEventService
# from org.allbinary.graphics.pipeline.RandomRotationFactory import RandomRotationFactory
# from org.allbinary.log.LOGGING import LOGGING
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.GuiLog import GuiLog
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.math.PositionStrings import PositionStrings
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.w3c.dom.Node import Node
# from java.awt.GridLayout import GridLayout
# from java.awt.event.KeyEvent import KeyEvent
# from java.awt.event.MouseEvent import MouseEvent


def _CanvasJPanel_gridColor() -> object:
    from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
    return Color(int(BasicColorFactory.getInstance().WHITE))

lazy_static(CanvasJPanel, "gridColor", _CanvasJPanel_gridColor)

def _CanvasJPanel_backgroundColor() -> object:
    from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
    return Color(int(BasicColorFactory.getInstance().CLEAR_COLOR))

lazy_static(CanvasJPanel, "backgroundColor", _CanvasJPanel_backgroundColor)

