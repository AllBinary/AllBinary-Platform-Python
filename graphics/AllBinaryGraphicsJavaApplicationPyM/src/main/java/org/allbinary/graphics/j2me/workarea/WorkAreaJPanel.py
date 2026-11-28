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
from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_divide
import threading
from java.lang.JavaRuntimeStatic import java_bases
from java.util.EventListener import EventListener
from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventListener import MyCanvasEventListener
# from javax.swing.JPanel import JPanel
from org.allbinary.graphics.j2me.workarea.WorkAreaJPanelInterface import WorkAreaJPanelInterface


@java_inherited_overloads
class WorkAreaJPanel(*java_bases(JPanel, WorkAreaJPanelInterface, MyCanvasEventListener, EventListener, object)):
    document: Document = None
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("canvasJPanelList", None)
        vars(self).setdefault("canvasHolderJPanel", None)
        vars(self).setdefault("name", None)
        vars(self).setdefault("selectedFrame", 0)
        vars(self).setdefault("propertiesJPanel", None)
        vars(self).setdefault("workAreaJTreeJPanel", None)
        vars(self).setdefault("isPlaying_field", False)
        vars(self).setdefault("innerJPanel", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "canvasJPanelList" not in vars(self): self.canvasJPanelList: LinkedList = None
        if "canvasHolderJPanel" not in vars(self): self.canvasHolderJPanel: JPanel = None
        if "name" not in vars(self): self.name: str = None
        if "selectedFrame" not in vars(self): self.selectedFrame: int = 0
        if "propertiesJPanel" not in vars(self): self.propertiesJPanel: PropertiesJPanel = None
        if "workAreaJTreeJPanel" not in vars(self): self.workAreaJTreeJPanel: WorkAreaJTreeJPanel = None
        self.isPlaying_field: bool = False
        if "innerJPanel" not in vars(self): self.innerJPanel: JPanel = None

    def __init__(self, *args) -> None:
        if len(args) == 4:
            __class__._constructor4(self, *args)
        elif len(args) == 2:
            __class__._constructor2(self, *args)
    

    def _constructor4(self, name: str, dimension: Dimension, x: int, y: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.j2me.workarea.WorkAreaJTreeJPanel import WorkAreaJTreeJPanel
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
        super().__init__()
        __class__._init_fields(self)
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
        __class__._java_defaults(self)
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasDom import CanvasDom
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
        from org.allbinary.log.LOGGING import LOGGING
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.w3c.dom.Node import Node
        super().__init__()
        __class__._init_fields(self)
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
            if LOGGING.contains(LOGGING.LOADINGERROR):
                self.logUtil.put("Constructor Error", self, "WorkAreaJPanel", e)
            raise e
    

    def initMyComponents(self, dimension: Dimension) -> None:
        from org.allbinary.graphics.j2me.workarea.WorkAreaJTreeJPanel import WorkAreaJTreeJPanel
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventService import MyCanvasEventService
        from org.allbinary.graphics.j2me.workarea.properties.PropertiesJPanel import PropertiesJPanel
        from org.allbinary.graphics.j2me.workarea.tools.ToolJPanel import ToolJPanel
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
        gridBagConstraints.fill = GridBagConstraints.BOTH
        gridBagConstraints.weightx = .05
        gridBagConstraints.weighty = .05
        toolJPanel: ToolJPanel = ToolJPanel()
        gridBagLayout.setConstraints(toolJPanel, gridBagConstraints)
        self.innerJPanel.add(toolJPanel)
        gridBagConstraints = GridBagConstraints()
        gridBagConstraints.gridx = 1
        gridBagConstraints.gridy = 0
        gridBagConstraints.gridwidth = 6
        gridBagConstraints.fill = GridBagConstraints.BOTH
        gridBagConstraints.weightx = 1
        gridBagConstraints.weighty = 1
        gridBagLayout.setConstraints(self.canvasHolderJPanel, gridBagConstraints)
        self.innerJPanel.add(self.canvasHolderJPanel)
        gridBagConstraints = GridBagConstraints()
        gridBagConstraints.gridx = 8
        gridBagConstraints.gridy = 0
        gridBagConstraints.gridwidth = GridBagConstraints.REMAINDER
        gridBagConstraints.fill = GridBagConstraints.BOTH
        gridBagConstraints.weightx = .1
        gridBagConstraints.weighty = .1
        self.propertiesJPanel = PropertiesJPanel()
        gridBagLayout.setConstraints(self.propertiesJPanel, gridBagConstraints)
        self.innerJPanel.add(self.propertiesJPanel)
        MyCanvasEventService.addListener(self)
    

    def getCanvasHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
        from org.allbinary.logic.StdUtil import StdUtil
        canvasJPanelHashMap: HashMap = StdUtil.getInstance().createHashMap()
        size: int = self.canvasJPanelList.size()
        for index in range(0, size):
            canvasJPanel: CanvasJPanel = self.canvasJPanelList.get(index)
            canvasJPanelHashMap.put(canvasJPanel.getTreeNode(), int(index))
        return canvasJPanelHashMap
    

    def play(self) -> None:
        with self._lock:
            return __class__.__dict__["_play_unlocked"].__get__(self, __class__)()

    def _play_unlocked(self) -> None:
        self.isPlaying_field = True
    

    def stop(self) -> None:
        with self._lock:
            return __class__.__dict__["_stop_unlocked"].__get__(self, __class__)()

    def _stop_unlocked(self) -> None:
        self.isPlaying_field = False
    

    def isPlaying(self) -> bool:
        with self._lock:
            return __class__.__dict__["_isPlaying_unlocked"].__get__(self, __class__)()

    def _isPlaying_unlocked(self) -> bool:
        return self.isPlaying_field
    

    def getName(self) -> str:
        return self.name
    

    def setName(self, value: str) -> None:
        self.name = value
    

    def disableCanvas(self) -> None:
        self.canvasHolderJPanel.removeAll()
    

    def enableCanvas(self) -> None:
        self.canvasHolderJPanel.add(self.getCurrentFrame())
    

    def deselect(self) -> None:
        java_super_call(super(), "setVisible", False)
    

    def select_j0(self) -> None:
        java_super_call(super(), "setVisible", True)
        if self.canvasHolderJPanel.getComponentCount() == 1:
            component: Component = self.canvasHolderJPanel.getComponent(0)
            if component is not None:
                component.repaint()
    

    def changeZoom(self, factor: int) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
        size: int = self.canvasJPanelList.size()
        for index in range(0, size):
            canvasJPanel: CanvasJPanel = self.canvasJPanelList.get(index)
            canvasJPanel.getGrid().setZoom(canvasJPanel.getGrid().getZoom() + factor)
    

    def getCurrentFrame(self) -> CanvasJPanel:
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
        return self.canvasJPanelList.get(self.selectedFrame)
    

    def initDuplicate(self, newCanvasJPanel: CanvasJPanel) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
        if newCanvasJPanel is not None:
            self.canvasJPanelList.add(newCanvasJPanel)
            self.select(self.canvasJPanelList.size() - 1)
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def duplicate_j1_1(self, treeNode: MutableTreeNode) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
        canvasJPanelHashMap: HashMap = self.getCanvasHashMap()
        if canvasJPanelHashMap.containsKey(treeNode):
            frameInteger: int = canvasJPanelHashMap.get(treeNode)
            canvasJPanel: CanvasJPanel = self.canvasJPanelList.get(int(frameInteger))
            self.initDuplicate(canvasJPanel.duplicate())
    

    # throws Exception
    def autoRotate(self, increments: int, totalAngle: int) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
        incrementAngle: int = (int(totalAngle / increments))
        for index in range(1, increments):
            canvasJPanel: CanvasJPanel = self.getCurrentFrame()
            newCanvasJPanel: CanvasJPanel = canvasJPanel.duplicate()
            newCanvasJPanel.setAngle(incrementAngle * index)
            self.initDuplicate(newCanvasJPanel)
    

    def explodeAll(self) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
        canvasJPanel: CanvasJPanel = self.getCurrentFrame()
        canvasJPanel.explodeAll()
    

    # throws Exception
    def autoExplode_j2(self, numberOfFrames: int, explodeType: int) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
        for index in range(1, numberOfFrames):
            canvasJPanel: CanvasJPanel = self.getCurrentFrame()
            newCanvasJPanel: CanvasJPanel = canvasJPanel.duplicate()
            newCanvasJPanel.explode(index + 1, explodeType)
            self.initDuplicate(newCanvasJPanel)
    

    # throws Exception
    def autoMirror(self) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
        canvasJPanel: CanvasJPanel = self.getCurrentFrame()
        newCanvasJPanel: CanvasJPanel = canvasJPanel.duplicate()
        newCanvasJPanel.mirror()
        self.initDuplicate(newCanvasJPanel)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def select_j1_1(self, index: int) -> None:
        with self._lock:
            return __class__.__dict__["_select_j1_1_unlocked"].__get__(self, __class__)(index)

    def _select_j1_1_unlocked(self, index: int) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
        if index < self.canvasJPanelList.size():
            canvasJPanel: CanvasJPanel = self.canvasJPanelList.get(index)
            if canvasJPanel is not None:
                self.canvasHolderJPanel.removeAll()
                self.canvasHolderJPanel.add(canvasJPanel)
                self.selectedFrame = index
                canvasJPanel.changed()
                self.canvasHolderJPanel.repaint()
                canvasJPanel.repaint()
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def select_j1_2(self, treeNode: MutableTreeNode) -> None:
        from java.util.HashMap import HashMap
        canvasJPanelHashMap: HashMap = self.getCanvasHashMap()
        frameInteger: int = canvasJPanelHashMap.get(treeNode)
        if frameInteger is not None:
            self.select(int(frameInteger))
    

    @staticmethod
    def getDocument() -> Document:
        from org.w3c.dom.Document import Document
        return WorkAreaJPanel.document
    

    # throws Exception
    def toDocument(self) -> Document:
        from org.allbinary.graphics.j2me.workarea.WorkAreaDom import WorkAreaDom
        from org.allbinary.graphics.j2me.workarea.WorkAreaDom import WorkAreaDom
        from org.allbinary.graphics.j2me.workarea.WorkAreaDom import WorkAreaDom
        from org.allbinary.dom.DomHelper import DomHelper
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
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
        self.innerJPanel = JPanel()
        self.setLayout(GridLayout(1, 1))
        _java_listener_owner = self
        class _JavaListenerN73513(KeyAdapter):
            
            

            def keyTyped(self, evt: KeyEvent) -> None:
                (self if hasattr(self, "innerJPanelKeyTyped") else _java_listener_owner).innerJPanelKeyTyped(evt)
            

            def keyPressed(self, evt: KeyEvent) -> None:
                (self if hasattr(self, "innerJPanelKeyPressed") else _java_listener_owner).innerJPanelKeyPressed(evt)
            

            def keyReleased(self, evt: KeyEvent) -> None:
                (self if hasattr(self, "innerJPanelKeyReleased") else _java_listener_owner).innerJPanelKeyReleased(evt)
        self.innerJPanel.addKeyListener(_JavaListenerN73513()
            )
        self.add(self.innerJPanel)
    

    def innerJPanelKeyReleased(self, evt: KeyEvent) -> None:
        from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
        StatusFactory.getInstance().setStatus("Key Pressed1")
    

    def innerJPanelKeyPressed(self, evt: KeyEvent) -> None:
        from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
        StatusFactory.getInstance().setStatus("Key Pressed2")
    

    def innerJPanelKeyTyped(self, evt: KeyEvent) -> None:
        from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
        StatusFactory.getInstance().setStatus("Key Pressed3")
    

    def keyPressed(self, keyEvent: KeyEvent) -> None:
        self.getCurrentFrame().keyPressed(keyEvent)
    

    def keyReleased(self, keyEvent: KeyEvent) -> None:
        pass
    

    def keyTyped(self, keyEvent: KeyEvent) -> None:
        pass
    

    def delete(self, evt: MyCanvasEvent) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
        canvasJPanelHashMap: HashMap = self.getCanvasHashMap()
        if canvasJPanelHashMap.containsKey(evt.getTreeNode()):
            self.canvasHolderJPanel.removeAll()
            frameInt: int = canvasJPanelHashMap.get(evt.getTreeNode())
            self.canvasJPanelList.remove(int(frameInt))
            self.select(int(frameInt))
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def duplicate_j1_2(self, evt: MyCanvasEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
        self.duplicate(evt.getTreeNode())

    def duplicate(self, *args):
        if len(args) == 1 and True and (args[0] is None or any(base.__name__ == "MutableTreeNode" for base in type(args[0]).__mro__)):
            return __class__.__dict__["duplicate_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["duplicate_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("duplicate_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().duplicate(*args)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def select_j1_3(self, evt: MyCanvasEvent) -> None:
        from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
        self.select(evt.getTreeNode())
        StatusFactory.getInstance().setStatus("Frame Selected")

    def select(self, *args):
        if len(args) == 1 and True and isinstance(args[0], int) and not isinstance(args[0], bool):
            return __class__.__dict__["select_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1 and True and (args[0] is None or any(base.__name__ == "MutableTreeNode" for base in type(args[0]).__mro__)):
            return __class__.__dict__["select_j1_2"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["select_j1_3"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("select_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().select(*args)
    

    def rotate(self, evt: MyCanvasEvent) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
        canvasJPanelHashMap: HashMap = self.getCanvasHashMap()
        treeNode: MutableTreeNode = evt.getTreeNode()
        frameInt: int = canvasJPanelHashMap.get(evt.getTreeNode())
        canvasJPanel: CanvasJPanel = self.canvasJPanelList.get(int(frameInt))
        if canvasJPanel is not None:
            canvasJPanel.addAngle(evt.getAngle())
            self.select(int(frameInt))
        StatusFactory.getInstance().setStatus("Canvas Rotated")
    

    def explode(self, evt: MyCanvasEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
        self.explodeAll()
    

    # throws Exception
    def autoExplode_j1(self, evt: MyCanvasEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
        self.autoExplode(10, 0)

    def autoExplode(self, *args):
        implementation = __class__.__dict__.get("autoExplode_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().autoExplode(*args)
    

    # throws Exception
    def center_j0(self) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
        canvasJPanel: CanvasJPanel = self.getCurrentFrame()
        canvasJPanel.center()
    

    # throws Exception
    def center_j1(self, evt: MyCanvasEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
        self.center()

    def center(self, *args):
        implementation = __class__.__dict__.get("center_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().center(*args)
    

    def run(self) -> None:
        try:
            while True:
                if java_predicate(self, "isPlaying"):
                    size: int = self.canvasJPanelList.size()
                    for index in range(0, size):
                        if not (java_predicate(self, "isPlaying")):
                            break
                        self.select(index)
                        time.sleep((100) / 1000)
                else:
                    time.sleep((500) / 1000)
                time.sleep((250) / 1000)
        except Exception as e:
            pass
# from java.awt.Component import Component
# from java.awt.Dimension import Dimension
# from java.awt.GridBagLayout import GridBagLayout
# from java.util.HashMap import HashMap
# from java.util.LinkedList import LinkedList
# from javax.swing import *
# from javax.swing.tree.MutableTreeNode import MutableTreeNode
# from org.allbinary.dom.DomHelper import DomHelper
# from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
# from org.allbinary.graphics.j2me.workarea.canvas.CanvasDom import CanvasDom
# from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel
# from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
# from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventService import MyCanvasEventService
# from org.allbinary.graphics.j2me.workarea.properties.PropertiesJPanel import PropertiesJPanel
# from org.allbinary.graphics.j2me.workarea.tools.ToolJPanel import ToolJPanel
# from org.allbinary.log.LOGGING import LOGGING
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from java.awt.GridBagConstraints import GridBagConstraints
# from java.awt.GridLayout import GridLayout
# from java.awt.event.KeyAdapter import KeyAdapter
# from java.awt.event.KeyEvent import KeyEvent


