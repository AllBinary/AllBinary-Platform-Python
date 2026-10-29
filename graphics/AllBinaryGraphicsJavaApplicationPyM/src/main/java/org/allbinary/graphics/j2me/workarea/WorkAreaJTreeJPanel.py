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

from org.allbinary.graphics.j2me.workarea.JPanel import JPanel


class WorkAreaJTreeJPanel(JPanel):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.rootTreeNode: DefaultMutableTreeNode = None
        self.workAreaJTree: JTree = None
        self.highlightedBasicArrayList: BasicArrayList = None
        self.copyJMenuItem: JMenuItem = None
        self.deleteJMenuItem: JMenuItem = None
        self.itemJPopupMenu: JPopupMenu = None
        self.itemJScrollPane1: JScrollPane = None
        self.rotateJMenuItem: JMenuItem = None
        self.workAreaPropertiesJPanel: JPanel = None
    

    def __init__(self, workAreaName: str) -> None:
        super().__init__()
        self._init_fields()
        self.initComponents()
        self.rootTreeNode = DefaultMutableTreeNode(workAreaName)
        self.workAreaPropertiesJPanel.removeAll()
        self.updateTree()
        self.highlightedBasicArrayList = BasicArrayListD()
    

    def add(self, treeNode: MutableTreeNode) -> None:
        self.rootTreeNode.add(treeNode)
    

    def updateTree(self) -> None:
        from org.allbinary.graphics.j2me.workarea.JTree import JTree
        from org.allbinary.graphics.j2me.workarea.MouseAdapter import MouseAdapter
        self.workAreaJTree = JTree(self.rootTreeNode)
        self.workAreaJTree.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.workAreaJTreeMousePressed(evt)
))
        self.workAreaPropertiesJPanel.removeAll()
        self.workAreaPropertiesJPanel.add(self.workAreaJTree)
    

    def getNode(self, treePathArray: list[TreePath]) -> BasicArrayList:
        basicArrayList: BasicArrayList = BasicArrayListD()
        if treePathArray is not None:
            for index in range(0, len(treePathArray)):
                basicArrayList.add(self.getNode(treePathArray[index]))
        return basicArrayList
    

    # Java overloaded method: Python keeps the last definition
    def getNode(self, treePath: TreePath) -> DefaultMutableTreeNode:
        if treePath is not None:
            obj: list[object] = treePath.getPath()
            if obj is not None:
                node: DefaultMutableTreeNode = obj[len(obj) - 1]
                return node
        return None
    

    # throws Exception
    def deselectAll(self) -> None:
        size: int = self.highlightedBasicArrayList.size()
        self.logUtil.putF("size: " + str(size), self, "deselectAll")
        for index in range(0, size):
            node: DefaultMutableTreeNode = self.highlightedBasicArrayList.get(index)
            MyGraphicItemEventService.fire(MyGraphicItemEvent(MyGraphicItemEventSource(MyGraphicItemEventService.DESELECT, node)))
        self.highlightedBasicArrayList.clear()
    

    # throws Exception
    def selectGraphicItem(self, node: DefaultMutableTreeNode) -> None:
        self.highlightedBasicArrayList.add(node)
        MyGraphicItemEventService.fire(MyGraphicItemEvent(MyGraphicItemEventSource(MyGraphicItemEventService.SELECT, node)))
    

    # throws Exception
    def removeGraphicItem(self, node: DefaultMutableTreeNode) -> None:
        MyGraphicItemEventService.fire(MyGraphicItemEvent(MyGraphicItemEventSource(MyGraphicItemEventService.DELETE, node)))
    

    # throws Exception
    def removeCanvas(self, node: DefaultMutableTreeNode) -> None:
        MyCanvasEventService.fire(MyCanvasEvent(MyCanvasEventSource(MyCanvasEventService.DELETE, node)))
    

    # throws Exception
    def remove(self, treePath: TreePath) -> None:
        node: DefaultMutableTreeNode = self.getNode(treePath)
        if node is not None:
            if isinstance(node.getUserObject(), CanvasTreeLabel):
                self.removeCanvas(node)
            else:
                self.removeGraphicItem(node)
        parent: DefaultMutableTreeNode = node.getParent()
        parent.remove(node)
    

    # throws Exception
    def copy(self) -> None:
        treePath: TreePath = self.workAreaJTree.getSelectionPath()
        self.copy(treePath)
        self.updateTree()
        self.expand()
        self.repaint()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def copy(self, treePath: TreePath) -> None:
        node: DefaultMutableTreeNode = self.getNode(treePath)
        if node is not None:
            if isinstance(node.getUserObject(), CanvasTreeLabel):
                MyCanvasEventService.fire(MyCanvasEvent(MyCanvasEventSource(MyCanvasEventService.DUPLICATE, node)))
            else:
                MyGraphicItemEventService.fire(MyGraphicItemEvent(MyGraphicItemEventSource(MyGraphicItemEventService.DUPLICATE, node)))
    

    # throws Exception
    def rotate(self, treePath: TreePath, angle: float) -> None:
        node: DefaultMutableTreeNode = self.getNode(treePath)
        if node is not None:
            if isinstance(node.getUserObject(), CanvasTreeLabel):
                MyCanvasEventService.fire(MyCanvasEvent(MyCanvasEventSource(MyCanvasEventService.ROTATE, angle, node)))
            else:
                MyGraphicItemEventService.fire(MyGraphicItemEvent(MyGraphicItemEventSource(MyGraphicItemEventService.ROTATE, angle, node)))
    

    def getRootTreeNode(self) -> MutableTreeNode:
        return self.rootTreeNode
    

    def expand(self) -> None:
        self.workAreaJTree.expandRow(0)
        self.workAreaJTree.expandRow(1)
    

    # Java overloaded method: Python keeps the last definition
    def expand(self, treePath: TreePath) -> None:
        self.workAreaJTree.expandPath(treePath)
    

    def initComponents(self) -> None:
        from org.allbinary.graphics.j2me.workarea.JPopupMenu import JPopupMenu
        from org.allbinary.graphics.j2me.workarea.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.workarea.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.workarea.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.workarea.JScrollPane import JScrollPane
        from org.allbinary.graphics.j2me.workarea.JPanel import JPanel
        from org.allbinary.graphics.j2me.workarea.PopupMenuListener import PopupMenuListener
        from org.allbinary.graphics.j2me.workarea.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.GridLayout import GridLayout
        from org.allbinary.graphics.j2me.workarea.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.GridLayout import GridLayout
        self.itemJPopupMenu = JPopupMenu()
        self.deleteJMenuItem = JMenuItem()
        self.copyJMenuItem = JMenuItem()
        self.rotateJMenuItem = JMenuItem()
        self.itemJScrollPane1 = JScrollPane()
        self.workAreaPropertiesJPanel = JPanel()
        self.itemJPopupMenu.addPopupMenuListener((PopupMenuListener()  # Java anonymous class body:
#             
# 
#             def popupMenuCanceled(self, evt: PopupMenuEvent) -> None:
#                 pass
#             
# 
#             def popupMenuWillBecomeInvisible(self, evt: PopupMenuEvent) -> None:
#                 self.itemJPopupMenuPopupMenuWillBecomeInvisible(evt)
#             
# 
#             def popupMenuWillBecomeVisible(self, evt: PopupMenuEvent) -> None:
#                 self.itemJPopupMenuPopupMenuWillBecomeVisible(evt)
))
        self.deleteJMenuItem.setText("Delete")
        self.deleteJMenuItem.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.deleteJMenuItemMousePressed(evt)
))
        self.itemJPopupMenu.add(self.deleteJMenuItem)
        self.copyJMenuItem.setText("Copy")
        self.copyJMenuItem.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.copyJMenuItemMousePressed(evt)
))
        self.itemJPopupMenu.add(self.copyJMenuItem)
        self.rotateJMenuItem.setText("Rotate 45*")
        self.rotateJMenuItem.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.rotateJMenuItemMousePressed(evt)
))
        self.itemJPopupMenu.add(self.rotateJMenuItem)
        self.setLayout(GridLayout(1, 1))
        self.workAreaPropertiesJPanel.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.workAreaPropertiesJPanelMousePressed(evt)
))
        self.workAreaPropertiesJPanel.setLayout(GridLayout(1, 0))
        self.itemJScrollPane1.setViewportView(self.workAreaPropertiesJPanel)
        self.add(self.itemJScrollPane1)
    

    def rotateJMenuItemMousePressed(self, evt: MouseEvent) -> None:
        try:
            treePath: TreePath = self.workAreaJTree.getSelectionPath()
            self.rotate(treePath, 45)
            self.updateTree()
            self.expand()
            self.repaint()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "rotateJMenuItemMousePressed", e)
    

    def workAreaJTreeMousePressed(self, evt: MouseEvent) -> None:
        try:
            selectedTreePathArray: list[TreePath] = self.workAreaJTree.getSelectionPaths()
            list_: BasicArrayList = self.getNode(selectedTreePathArray)
            if list_.size() > 0:
                if (evt.getModifiers() & evt.BUTTON3_MASK) == evt.BUTTON3_MASK:
                    for index in range(0, len(selectedTreePathArray)):
                        defaultMutableTreeNode: DefaultMutableTreeNode = list_.get(index)
                        if isinstance(defaultMutableTreeNode.getUserObject(), CanvasTreeLabel):
                            self.itemJPopupMenu.show(self, evt.getX(), evt.getY())
                        else:
                            self.itemJPopupMenu.show(self, evt.getX(), evt.getY())
                if (evt.getModifiers() & evt.BUTTON1_MASK) == evt.BUTTON1_MASK:
                    self.deselectAll()
                    for index in range(0, len(selectedTreePathArray)):
                        defaultMutableTreeNode: DefaultMutableTreeNode = list_.get(index)
                        if isinstance(defaultMutableTreeNode.getUserObject(), CanvasTreeLabel):
                            MyCanvasEventService.fire(MyCanvasEvent(MyCanvasEventSource(MyCanvasEventService.SELECT, defaultMutableTreeNode)))
                        else:
                            self.selectGraphicItem(defaultMutableTreeNode)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "workAreaJTreeMousePressed", e)
    

    def itemJPopupMenuPopupMenuWillBecomeInvisible(self, evt: PopupMenuEvent) -> None:
        pass
    

    def itemJPopupMenuPopupMenuWillBecomeVisible(self, evt: PopupMenuEvent) -> None:
        pass
    

    def copyJMenuItemMousePressed(self, evt: MouseEvent) -> None:
        try:
            self.copy()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "copyJMenuItemMousePressed", e)
    

    def deleteJMenuItemMousePressed(self, evt: MouseEvent) -> None:
        try:
            selectedTreePathArray: list[TreePath] = self.workAreaJTree.getSelectionPaths()
            for index in range(0, len(selectedTreePathArray)):
                treePath: TreePath = selectedTreePathArray[index]
                self.remove(treePath)
                self.updateTree()
                self.expand()
                self.repaint()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "deleteJMenuItemMousePressed", e)
    

    def workAreaPropertiesJPanelMousePressed(self, evt: MouseEvent) -> None:
        pass
# from javax.swing import *
# from javax.swing.tree.DefaultMutableTreeNode import DefaultMutableTreeNode
# from javax.swing.tree.MutableTreeNode import MutableTreeNode
# from javax.swing.tree.TreePath import TreePath
from org.allbinary.graphics.j2me.workarea.canvas.CanvasTreeLabel import CanvasTreeLabel
from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventService import MyCanvasEventService
from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventSource import MyCanvasEventSource
from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEvent import MyGraphicItemEvent
from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEventService import MyGraphicItemEventService
from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEventSource import MyGraphicItemEventSource
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


