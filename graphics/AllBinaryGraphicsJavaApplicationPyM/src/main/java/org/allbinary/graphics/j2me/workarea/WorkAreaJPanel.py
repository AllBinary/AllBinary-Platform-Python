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
# package org.allbinary.graphics.j2me.workarea

from __future__ import annotations

import time
import threading
# from java.util.EventListener import EventListener
from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventListener import MyCanvasEventListener
from org.allbinary.graphics.j2me.workarea.JPanel import JPanel
from org.allbinary.graphics.j2me.workarea.WorkAreaJPanelInterface import WorkAreaJPanelInterface


class WorkAreaJPanel(JPanel, WorkAreaJPanelInterface, MyCanvasEventListener, EventListener, object):
    document: Document = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.canvasJPanelList: LinkedList = None
        self.canvasHolderJPanel: JPanel = None
        self.name: str = None
        self.selectedFrame: int = 0
        self.propertiesJPanel: PropertiesJPanel = None
        self.workAreaJTreeJPanel: WorkAreaJTreeJPanel = None
        self.isPlaying: bool = False
        self.innerJPanel: JPanel = None

    def __init__(self, *args) -> None:
        if len(args) == 4:
            self._constructor4(*args)
        elif len(args) == 2:
            self._constructor2(*args)
    

    def _constructor4(self, name: str, dimension: Dimension, x: int, y: int) -> None:
        from org.allbinary.graphics.j2me.workarea.WorkAreaJTreeJPanel import WorkAreaJTreeJPanel
        super().__init__()
        self._init_fields()
        try:
            self.initComponents()
            self.name = name
            self.initMyComponents(dimension)
            self.workAreaJTreeJPanel = WorkAreaJTreeJPanel(self.name)
            canvasJPanel: CanvasJPanel = CanvasJPanel(self.workAreaJTreeJPanel, self.getSize(), x, y)
            self.canvasJPanelList.add(canvasJPanel)
            self.selectedFrame = 0
            self.propertiesJPanel.set(self.workAreaJTreeJPanel)
            self.canvasHolderJPanel.add(canvasJPanel)
        except Exception as e:
            raise e
    

    def _constructor2(self, workAreaDom: WorkAreaDom, dimension: Dimension) -> None:
        super().__init__()
        self._init_fields()
        try:
            self.initComponents()
            self.name = workAreaDom.getName()
            self.initMyComponents(dimension)
            canvasNodeList: BasicArrayList = workAreaDom.getCanvasNodes()
            numberOfFrames: int = canvasNodeList.size()
            for index in range(0, numberOfFrames):
                node: Node = canvasNodeList.get(index)
                canvasJPanel: CanvasJPanel = CanvasJPanel(self.workAreaJTreeJPanel, self.getSize(), CanvasDom(node))
                self.canvasJPanelList.add(canvasJPanel)
            self.selectedFrame = 0
            self.canvasHolderJPanel.add(self.getCurrentFrame())
            self.propertiesJPanel.set(self.workAreaJTreeJPanel)
        except Exception as e:
            if self.LOGGING.contains(self.LOGGING.LOADINGERROR):
                self.logUtil.put("Constructor Error", self, "WorkAreaJPanel", e)
            raise e
    

    def initMyComponents(self, dimension: Dimension) -> None:
        from org.allbinary.graphics.j2me.workarea.WorkAreaJTreeJPanel import WorkAreaJTreeJPanel
        from org.allbinary.graphics.j2me.workarea.JPanel import JPanel
        from org.allbinary.graphics.j2me.workarea.GridLayout import GridLayout
        from org.allbinary.graphics.j2me.workarea.GridBagLayout import GridBagLayout
        from org.allbinary.graphics.j2me.workarea.GridBagConstraints import GridBagConstraints
        from org.allbinary.graphics.j2me.workarea.GridBagConstraints import GridBagConstraints
        from org.allbinary.graphics.j2me.workarea.GridBagConstraints import GridBagConstraints
        self.workAreaJTreeJPanel = WorkAreaJTreeJPanel(self.name)
        self.canvasHolderJPanel = JPanel()
        self.canvasHolderJPanel.setSize(dimension)
        self.canvasHolderJPanel.setLayout(GridLayout(1, 1))
        self.setSize(dimension)
        self.canvasJPanelList = LinkedList()
        gridBagLayout: GridBagLayout = GridBagLayout()
        gridBagConstraints: GridBagConstraints = GridBagConstraints()
        self.innerJPanel.setLayout(gridBagLayout)
        gridBagConstraints.gridx = 0
        gridBagConstraints.gridy = 0
        gridBagConstraints.gridwidth = 1
        gridBagConstraints.fill = java.awt.GridBagConstraints.BOTH
        gridBagConstraints.weightx = .05
        gridBagConstraints.weighty = .05
        toolJPanel: ToolJPanel = ToolJPanel()
        gridBagLayout.setConstraints(toolJPanel, gridBagConstraints)
        self.innerJPanel.add(toolJPanel)
        gridBagConstraints = GridBagConstraints()
        gridBagConstraints.gridx = 1
        gridBagConstraints.gridy = 0
        gridBagConstraints.gridwidth = 6
        gridBagConstraints.fill = java.awt.GridBagConstraints.BOTH
        gridBagConstraints.weightx = 1
        gridBagConstraints.weighty = 1
        gridBagLayout.setConstraints(self.canvasHolderJPanel, gridBagConstraints)
        self.innerJPanel.add(self.canvasHolderJPanel)
        gridBagConstraints = GridBagConstraints()
        gridBagConstraints.gridx = 8
        gridBagConstraints.gridy = 0
        gridBagConstraints.gridwidth = java.awt.GridBagConstraints.REMAINDER
        gridBagConstraints.fill = java.awt.GridBagConstraints.BOTH
        gridBagConstraints.weightx = .1
        gridBagConstraints.weighty = .1
        self.propertiesJPanel = PropertiesJPanel()
        gridBagLayout.setConstraints(self.propertiesJPanel, gridBagConstraints)
        self.innerJPanel.add(self.propertiesJPanel)
        MyCanvasEventService.addListener(self)
    

    def getCanvasHashMap(self) -> dict:
        canvasJPanelHashMap: dict = StdUtil.getInstance().createHashMap()
        size: int = self.canvasJPanelList.size()
        for index in range(0, size):
            canvasJPanel: CanvasJPanel = self.canvasJPanelList.get(index)
            canvasJPanelHashMap.put(canvasJPanel.getTreeNode(), int(index))
        return canvasJPanelHashMap
    

    def play(self) -> None:
        with self._lock:
            return self._play_unlocked()

    def _play_unlocked(self) -> None:
        self.isPlaying = True
    

    def stop(self) -> None:
        with self._lock:
            return self._stop_unlocked()

    def _stop_unlocked(self) -> None:
        self.isPlaying = False
    

    def isPlaying(self) -> bool:
        with self._lock:
            return self._isPlaying_unlocked()

    def _isPlaying_unlocked(self) -> bool:
        return self.isPlaying
    

    def getName(self) -> str:
        return self.name
    

    def setName(self, value: str) -> None:
        self.name = value
    

    def disableCanvas(self) -> None:
        self.canvasHolderJPanel.removeAll()
    

    def enableCanvas(self) -> None:
        self.canvasHolderJPanel.add(self.getCurrentFrame())
    

    def deselect(self) -> None:
        super().setVisible(False)
    

    def select(self) -> None:
        super().setVisible(True)
        if self.canvasHolderJPanel.getComponentCount() == 1:
            component: Component = self.canvasHolderJPanel.getComponent(0)
            if component is not None:
                component.repaint()
    

    def changeZoom(self, factor: int) -> None:
        size: int = self.canvasJPanelList.size()
        for index in range(0, size):
            canvasJPanel: CanvasJPanel = self.canvasJPanelList.get(index)
            canvasJPanel.getGrid().setZoom(canvasJPanel.getGrid().getZoom() + factor)
    

    def getCurrentFrame(self) -> CanvasJPanel:
        return self.canvasJPanelList.get(self.selectedFrame)
    

    def initDuplicate(self, newCanvasJPanel: CanvasJPanel) -> None:
        if newCanvasJPanel is not None:
            self.canvasJPanelList.add(newCanvasJPanel)
            self.select(self.canvasJPanelList.size() - 1)
    

    # throws Exception
    def duplicate(self, treeNode: MutableTreeNode) -> None:
        canvasJPanelHashMap: dict = self.getCanvasHashMap()
        if canvasJPanelHashMap.containsKey(treeNode):
            frameInteger: int = canvasJPanelHashMap.get(treeNode)
            canvasJPanel: CanvasJPanel = self.canvasJPanelList.get(int(frameInteger))
            self.initDuplicate(canvasJPanel.duplicate())
    

    # throws Exception
    def autoRotate(self, increments: int, totalAngle: int) -> None:
        incrementAngle: int = (int(totalAngle / increments))
        for index in range(1, increments):
            canvasJPanel: CanvasJPanel = self.getCurrentFrame()
            newCanvasJPanel: CanvasJPanel = canvasJPanel.duplicate()
            newCanvasJPanel.setAngle(incrementAngle * index)
            self.initDuplicate(newCanvasJPanel)
    

    def explodeAll(self) -> None:
        canvasJPanel: CanvasJPanel = self.getCurrentFrame()
        canvasJPanel.explodeAll()
    

    # throws Exception
    def autoExplode(self, numberOfFrames: int, explodeType: int) -> None:
        for index in range(1, numberOfFrames):
            canvasJPanel: CanvasJPanel = self.getCurrentFrame()
            newCanvasJPanel: CanvasJPanel = canvasJPanel.duplicate()
            newCanvasJPanel.explode(index + 1, explodeType)
            self.initDuplicate(newCanvasJPanel)
    

    # throws Exception
    def autoMirror(self) -> None:
        canvasJPanel: CanvasJPanel = self.getCurrentFrame()
        newCanvasJPanel: CanvasJPanel = canvasJPanel.duplicate()
        newCanvasJPanel.mirror()
        self.initDuplicate(newCanvasJPanel)
    

    # Java overloaded method: Python keeps the last definition
    def select(self, index: int) -> None:
        with self._lock:
            return self._select_unlocked(index)

    def _select_unlocked(self, index: int) -> None:
        if index < self.canvasJPanelList.size():
            canvasJPanel: CanvasJPanel = self.canvasJPanelList.get(index)
            if canvasJPanel is not None:
                self.canvasHolderJPanel.removeAll()
                self.canvasHolderJPanel.add(canvasJPanel)
                self.selectedFrame = index
                canvasJPanel.changed()
                self.canvasHolderJPanel.repaint()
                canvasJPanel.repaint()
    

    # Java overloaded method: Python keeps the last definition
    def select(self, treeNode: MutableTreeNode) -> None:
        canvasJPanelHashMap: dict = self.getCanvasHashMap()
        frameInteger: int = canvasJPanelHashMap.get(treeNode)
        if frameInteger is not None:
            self.select(int(frameInteger))
    

    @staticmethod
    def getDocument() -> Document:
        return WorkAreaJPanel.document
    

    # throws Exception
    def toDocument(self) -> Document:
        from org.allbinary.graphics.j2me.workarea.WorkAreaDom import WorkAreaDom
        from org.allbinary.graphics.j2me.workarea.WorkAreaDom import WorkAreaDom
        from org.allbinary.graphics.j2me.workarea.WorkAreaDom import WorkAreaDom
        WorkAreaJPanel.document = DomHelper.getInstance().createDocument()
        workAreaNode: Node = WorkAreaJPanel.document.createElement(WorkAreaDom.WORKAREA)
        nameNode: Node = WorkAreaJPanel.document.createElement(WorkAreaDom.NAME)
        nameTextNode: Node = WorkAreaJPanel.document.createTextNode(self.name)
        nameNode.appendChild(nameTextNode)
        framesNode: Node = WorkAreaJPanel.document.createElement(WorkAreaDom.FRAMES)
        size: int = self.canvasJPanelList.size()
        for index in range(0, size):
            canvasJPanel: CanvasJPanel = self.canvasJPanelList.get(index)
            framesNode.appendChild(canvasJPanel.toDom())
        workAreaNode.appendChild(nameNode)
        workAreaNode.appendChild(framesNode)
        WorkAreaJPanel.document.appendChild(workAreaNode)
        return WorkAreaJPanel.document
    

    def initComponents(self) -> None:
        from org.allbinary.graphics.j2me.workarea.JPanel import JPanel
        from org.allbinary.graphics.j2me.workarea.GridLayout import GridLayout
        from org.allbinary.graphics.j2me.workarea.KeyAdapter import KeyAdapter
        self.innerJPanel = JPanel()
        self.setLayout(GridLayout(1, 1))
        self.innerJPanel.addKeyListener((KeyAdapter()  # Java anonymous class body:
#             
# 
#             def keyTyped(self, evt: KeyEvent) -> None:
#                 self.innerJPanelKeyTyped(evt)
#             
# 
#             def keyPressed(self, evt: KeyEvent) -> None:
#                 self.innerJPanelKeyPressed(evt)
#             
# 
#             def keyReleased(self, evt: KeyEvent) -> None:
#                 self.innerJPanelKeyReleased(evt)
))
        self.add(self.innerJPanel)
    

    def innerJPanelKeyReleased(self, evt: KeyEvent) -> None:
        StatusFactory.getInstance().setStatus("Key Pressed1")
    

    def innerJPanelKeyPressed(self, evt: KeyEvent) -> None:
        StatusFactory.getInstance().setStatus("Key Pressed2")
    

    def innerJPanelKeyTyped(self, evt: KeyEvent) -> None:
        StatusFactory.getInstance().setStatus("Key Pressed3")
    

    def keyPressed(self, keyEvent: KeyEvent) -> None:
        self.getCurrentFrame().keyPressed(keyEvent)
    

    def keyReleased(self, keyEvent: KeyEvent) -> None:
        pass
    

    def keyTyped(self, keyEvent: KeyEvent) -> None:
        pass
    

    def delete(self, evt: MyCanvasEvent) -> None:
        canvasJPanelHashMap: dict = self.getCanvasHashMap()
        if canvasJPanelHashMap.containsKey(evt.getTreeNode()):
            self.canvasHolderJPanel.removeAll()
            frameInt: int = canvasJPanelHashMap.get(evt.getTreeNode())
            self.canvasJPanelList.remove(int(frameInt))
            self.select(int(frameInt))
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def duplicate(self, evt: MyCanvasEvent) -> None:
        self.duplicate(evt.getTreeNode())
    

    # Java overloaded method: Python keeps the last definition
    def select(self, evt: MyCanvasEvent) -> None:
        self.select(evt.getTreeNode())
        StatusFactory.getInstance().setStatus("Frame Selected")
    

    def rotate(self, evt: MyCanvasEvent) -> None:
        canvasJPanelHashMap: dict = self.getCanvasHashMap()
        treeNode: MutableTreeNode = evt.getTreeNode()
        frameInt: int = canvasJPanelHashMap.get(evt.getTreeNode())
        canvasJPanel: CanvasJPanel = self.canvasJPanelList.get(int(frameInt))
        if canvasJPanel is not None:
            canvasJPanel.addAngle(evt.getAngle())
            self.select(int(frameInt))
        StatusFactory.getInstance().setStatus("Canvas Rotated")
    

    def explode(self, evt: MyCanvasEvent) -> None:
        self.explodeAll()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def autoExplode(self, evt: MyCanvasEvent) -> None:
        self.autoExplode(10, 0)
    

    # throws Exception
    def center(self) -> None:
        canvasJPanel: CanvasJPanel = self.getCurrentFrame()
        canvasJPanel.center()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def center(self, evt: MyCanvasEvent) -> None:
        self.center()
    

    def run(self) -> None:
        try:
            while True:
                if self.isPlaying():
                    size: int = self.canvasJPanelList.size()
                    for index in range(0, size):
                        if not self.isPlaying():
                            break
                        self.select(index)
                        time.sleep((100) / 1000)
                else:
                    time.sleep((500) / 1000)
                time.sleep((250) / 1000)
        except Exception as e:
            pass
# from java.awt import *
# from java.util.HashMap import HashMap
# from java.util.LinkedList import LinkedList
# from javax.swing import *
# from javax.swing.tree.MutableTreeNode import MutableTreeNode
from org.allbinary.dom.DomHelper import DomHelper
from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
from org.allbinary.graphics.j2me.workarea.canvas.CanvasDom import CanvasDom
from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventService import MyCanvasEventService
from org.allbinary.graphics.j2me.workarea.properties.PropertiesJPanel import PropertiesJPanel
from org.allbinary.graphics.j2me.workarea.tools.ToolJPanel import ToolJPanel
from org.allbinary.log.LOGGING import LOGGING
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


