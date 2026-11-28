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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
# from javax.swing.JPanel import JPanel


@java_inherited_overloads
class WorkAreaJTreeJPanel(JPanel):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("rootTreeNode", None)
        vars(self).setdefault("workAreaJTree", None)
        vars(self).setdefault("highlightedBasicArrayList", None)
        vars(self).setdefault("copyJMenuItem", None)
        vars(self).setdefault("deleteJMenuItem", None)
        vars(self).setdefault("itemJPopupMenu", None)
        vars(self).setdefault("itemJScrollPane1", None)
        vars(self).setdefault("rotateJMenuItem", None)
        vars(self).setdefault("workAreaPropertiesJPanel", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "rootTreeNode" not in vars(self): self.rootTreeNode: DefaultMutableTreeNode = None
        if "workAreaJTree" not in vars(self): self.workAreaJTree: JTree = None
        if "highlightedBasicArrayList" not in vars(self): self.highlightedBasicArrayList: BasicArrayList = None
        if "copyJMenuItem" not in vars(self): self.copyJMenuItem: JMenuItem = None
        if "deleteJMenuItem" not in vars(self): self.deleteJMenuItem: JMenuItem = None
        if "itemJPopupMenu" not in vars(self): self.itemJPopupMenu: JPopupMenu = None
        if "itemJScrollPane1" not in vars(self): self.itemJScrollPane1: JScrollPane = None
        if "rotateJMenuItem" not in vars(self): self.rotateJMenuItem: JMenuItem = None
        if "workAreaPropertiesJPanel" not in vars(self): self.workAreaPropertiesJPanel: JPanel = None
    

    def __init__(self, workAreaName: str) -> None:
        __class__._java_defaults(self)
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        super().__init__()
        __class__._init_fields(self)
        self.initComponents()
        self.rootTreeNode = DefaultMutableTreeNode(workAreaName)
        self.workAreaPropertiesJPanel.removeAll()
        self.updateTree()
        self.highlightedBasicArrayList = BasicArrayListD()
    

    def add(self, treeNode: MutableTreeNode) -> None:
        self.rootTreeNode.add(treeNode)
    

    def updateTree(self) -> None:
        self.workAreaJTree = JTree(self.rootTreeNode)
        _java_listener_owner = self
        class _JavaListenerN66826(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "workAreaJTreeMousePressed") else _java_listener_owner).workAreaJTreeMousePressed(evt)
        self.workAreaJTree.addMouseListener(_JavaListenerN66826()
            )
        self.workAreaPropertiesJPanel.removeAll()
        self.workAreaPropertiesJPanel.add(self.workAreaJTree)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getNode_j1_1(self, treePathArray: list[TreePath]) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        basicArrayList: BasicArrayList = BasicArrayListD()
        if treePathArray is not None:
            for index in range(0, len(treePathArray)):
                basicArrayList.add(self.getNode(treePathArray[index]))
        return basicArrayList
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getNode_j1_2(self, treePath: TreePath) -> DefaultMutableTreeNode:
        if treePath is not None:
            obj: list[object] = treePath.getPath()
            if obj is not None:
                node: DefaultMutableTreeNode = obj[len(obj) - 1]
                return node
        return None

    def getNode(self, *args):
        if len(args) == 1 and True and (args[0] is None or isinstance(args[0], list)):
            return __class__.__dict__["getNode_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["getNode_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("getNode_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getNode(*args)
    

    # throws Exception
    def deselectAll(self) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEvent import MyGraphicItemEvent
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEventService import MyGraphicItemEventService
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEventSource import MyGraphicItemEventSource
        size: int = self.highlightedBasicArrayList.size()
        self.logUtil.putF("size: " + str(size), self, "deselectAll")
        for index in range(0, size):
            node: DefaultMutableTreeNode = self.highlightedBasicArrayList.get(index)
            MyGraphicItemEventService.fire(MyGraphicItemEvent(MyGraphicItemEventSource(MyGraphicItemEventService.DESELECT, node)))
        self.highlightedBasicArrayList.clear()
    

    # throws Exception
    def selectGraphicItem(self, node: DefaultMutableTreeNode) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEvent import MyGraphicItemEvent
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEventService import MyGraphicItemEventService
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEventSource import MyGraphicItemEventSource
        self.highlightedBasicArrayList.add(node)
        MyGraphicItemEventService.fire(MyGraphicItemEvent(MyGraphicItemEventSource(MyGraphicItemEventService.SELECT, node)))
    

    # throws Exception
    def removeGraphicItem(self, node: DefaultMutableTreeNode) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEvent import MyGraphicItemEvent
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEventService import MyGraphicItemEventService
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEventSource import MyGraphicItemEventSource
        MyGraphicItemEventService.fire(MyGraphicItemEvent(MyGraphicItemEventSource(MyGraphicItemEventService.DELETE, node)))
    

    # throws Exception
    def removeCanvas(self, node: DefaultMutableTreeNode) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventService import MyCanvasEventService
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventSource import MyCanvasEventSource
        MyCanvasEventService.fire(MyCanvasEvent(MyCanvasEventSource(MyCanvasEventService.DELETE, node)))
    

    # throws Exception
    def remove(self, treePath: TreePath) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasTreeLabel import CanvasTreeLabel
        node: DefaultMutableTreeNode = self.getNode(treePath)
        if node is not None:
            if isinstance(node.getUserObject(), CanvasTreeLabel):
                self.removeCanvas(node)
            else:
                self.removeGraphicItem(node)
        parent: DefaultMutableTreeNode = node.getParent()
        parent.remove(node)
    

    # throws Exception
    def copy_j0(self) -> None:
        treePath: TreePath = self.workAreaJTree.getSelectionPath()
        self.copy(treePath)
        self.updateTree()
        self.expand()
        self.repaint()
    

    # throws Exception
    def copy_j1(self, treePath: TreePath) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasTreeLabel import CanvasTreeLabel
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventService import MyCanvasEventService
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventSource import MyCanvasEventSource
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEvent import MyGraphicItemEvent
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEventService import MyGraphicItemEventService
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEventSource import MyGraphicItemEventSource
        node: DefaultMutableTreeNode = self.getNode(treePath)
        if node is not None:
            if isinstance(node.getUserObject(), CanvasTreeLabel):
                MyCanvasEventService.fire(MyCanvasEvent(MyCanvasEventSource(MyCanvasEventService.DUPLICATE, node)))
            else:
                MyGraphicItemEventService.fire(MyGraphicItemEvent(MyGraphicItemEventSource(MyGraphicItemEventService.DUPLICATE, node)))

    def copy(self, *args):
        implementation = __class__.__dict__.get("copy_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().copy(*args)
    

    # throws Exception
    def rotate(self, treePath: TreePath, angle: float) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasTreeLabel import CanvasTreeLabel
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventService import MyCanvasEventService
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventSource import MyCanvasEventSource
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEvent import MyGraphicItemEvent
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEventService import MyGraphicItemEventService
        from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEventSource import MyGraphicItemEventSource
        node: DefaultMutableTreeNode = self.getNode(treePath)
        if node is not None:
            if isinstance(node.getUserObject(), CanvasTreeLabel):
                MyCanvasEventService.fire(MyCanvasEvent(MyCanvasEventSource(MyCanvasEventService.ROTATE, angle, node)))
            else:
                MyGraphicItemEventService.fire(MyGraphicItemEvent(MyGraphicItemEventSource(MyGraphicItemEventService.ROTATE, angle, node)))
    

    def getRootTreeNode(self) -> MutableTreeNode:
        return self.rootTreeNode
    

    def expand_j0(self) -> None:
        self.workAreaJTree.expandRow(0)
        self.workAreaJTree.expandRow(1)
    

    def expand_j1(self, treePath: TreePath) -> None:
        self.workAreaJTree.expandPath(treePath)

    def expand(self, *args):
        implementation = __class__.__dict__.get("expand_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().expand(*args)
    

    def initComponents(self) -> None:
        self.itemJPopupMenu = JPopupMenu()
        self.deleteJMenuItem = JMenuItem()
        self.copyJMenuItem = JMenuItem()
        self.rotateJMenuItem = JMenuItem()
        self.itemJScrollPane1 = JScrollPane()
        self.workAreaPropertiesJPanel = JPanel()
        _java_listener_owner = self
        class _JavaListenerN69996(PopupMenuListener):
            
            

            def popupMenuCanceled(self, evt: PopupMenuEvent) -> None:
                pass
            

            def popupMenuWillBecomeInvisible(self, evt: PopupMenuEvent) -> None:
                (self if hasattr(self, "itemJPopupMenuPopupMenuWillBecomeInvisible") else _java_listener_owner).itemJPopupMenuPopupMenuWillBecomeInvisible(evt)
            

            def popupMenuWillBecomeVisible(self, evt: PopupMenuEvent) -> None:
                (self if hasattr(self, "itemJPopupMenuPopupMenuWillBecomeVisible") else _java_listener_owner).itemJPopupMenuPopupMenuWillBecomeVisible(evt)
        self.itemJPopupMenu.addPopupMenuListener(_JavaListenerN69996()
            )
        self.deleteJMenuItem.setText("Delete")
        _java_listener_owner = self
        class _JavaListenerN70244(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "deleteJMenuItemMousePressed") else _java_listener_owner).deleteJMenuItemMousePressed(evt)
        self.deleteJMenuItem.addMouseListener(_JavaListenerN70244()
            )
        self.itemJPopupMenu.add(self.deleteJMenuItem)
        self.copyJMenuItem.setText("Copy")
        _java_listener_owner = self
        class _JavaListenerN70420(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "copyJMenuItemMousePressed") else _java_listener_owner).copyJMenuItemMousePressed(evt)
        self.copyJMenuItem.addMouseListener(_JavaListenerN70420()
            )
        self.itemJPopupMenu.add(self.copyJMenuItem)
        self.rotateJMenuItem.setText("Rotate 45*")
        _java_listener_owner = self
        class _JavaListenerN70596(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "rotateJMenuItemMousePressed") else _java_listener_owner).rotateJMenuItemMousePressed(evt)
        self.rotateJMenuItem.addMouseListener(_JavaListenerN70596()
            )
        self.itemJPopupMenu.add(self.rotateJMenuItem)
        self.setLayout(GridLayout(1, 1))
        _java_listener_owner = self
        class _JavaListenerN70780(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "workAreaPropertiesJPanelMousePressed") else _java_listener_owner).workAreaPropertiesJPanelMousePressed(evt)
        self.workAreaPropertiesJPanel.addMouseListener(_JavaListenerN70780()
            )
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
        from org.allbinary.graphics.j2me.workarea.canvas.CanvasTreeLabel import CanvasTreeLabel
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventService import MyCanvasEventService
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventSource import MyCanvasEventSource
        from org.allbinary.util.BasicArrayList import BasicArrayList
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
# from javax.swing.JTree import JTree
# from javax.swing.tree.DefaultMutableTreeNode import DefaultMutableTreeNode
# from javax.swing.tree.MutableTreeNode import MutableTreeNode
# from javax.swing.tree.TreePath import TreePath
# from org.allbinary.graphics.j2me.workarea.canvas.CanvasTreeLabel import CanvasTreeLabel
# from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
# from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventService import MyCanvasEventService
# from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventSource import MyCanvasEventSource
# from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEvent import MyGraphicItemEvent
# from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEventService import MyGraphicItemEventService
# from org.allbinary.graphics.j2me.workarea.tools.event.MyGraphicItemEventSource import MyGraphicItemEventSource
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from java.awt.GridLayout import GridLayout
# from java.awt.event.MouseAdapter import MouseAdapter
# from java.awt.event.MouseEvent import MouseEvent
# from javax.swing.JMenuItem import JMenuItem
# from javax.swing.JPopupMenu import JPopupMenu
# from javax.swing.JScrollPane import JScrollPane
# from javax.swing.event.PopupMenuEvent import PopupMenuEvent
# from javax.swing.event.PopupMenuListener import PopupMenuListener


