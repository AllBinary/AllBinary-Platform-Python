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
# package org.allbinary.input.automation.module.generic.configuration.profile.actions.script

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.input.automation.actions.script.JTreeInterface import JTreeInterface
# from javax.swing.JPanel import JPanel


@java_inherited_overloads
class GenericProfileActionScriptJPanel(*java_bases(JPanel, JTreeInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("defaultMutableTreeNode", None)
        vars(self).setdefault("genericProfileActionScript", None)
        vars(self).setdefault("actionScriptJTree", None)
        vars(self).setdefault("jScrollPane1", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.defaultMutableTreeNode: DefaultMutableTreeNode = DefaultMutableTreeNode("Root")
        if "genericProfileActionScript" not in vars(self): self.genericProfileActionScript: GenericProfileActionScript = None
        if "actionScriptJTree" not in vars(self): self.actionScriptJTree: JTree = None
        if "jScrollPane1" not in vars(self): self.jScrollPane1: JScrollPane = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.initComponents()
    

    def updateJTree(self) -> None:
        defaultTreeModel: DefaultTreeModel = DefaultTreeModel(self.getGenericProfileActionScript())
        self.getActionScriptJTree().setModel(defaultTreeModel)
        self.repaint()
        self.logUtil.putF("Updated UI", self, "updateJTree")
    

    def getGenericProfileActionScript(self) -> GenericProfileActionScript:
        return self.genericProfileActionScript
    

    def setGenericProfileActionScript(self, genericProfileActionScript: GenericProfileActionScript) -> None:
        self.genericProfileActionScript = genericProfileActionScript
    

    def getActionScriptJTree(self) -> JTree:
        return self.actionScriptJTree
    

    def setActionScriptJTree(self, actionScriptJTree: JTree) -> None:
        self.actionScriptJTree = actionScriptJTree
    

    def initComponents(self) -> None:
        self.jScrollPane1 = JScrollPane()
        self.actionScriptJTree = JTree()
        self.setLayout(GridLayout(1, 0))
        self.actionScriptJTree.setPreferredSize(Dimension(500, 500))
        _java_listener_owner = self
        class _JavaListenerN66909(MouseAdapter):
            
            

            def mouseClicked(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "actionScriptJTreeMouseClicked") else _java_listener_owner).actionScriptJTreeMouseClicked(evt)
            

            def mouseReleased(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "actionScriptJTreeMouseReleased") else _java_listener_owner).actionScriptJTreeMouseReleased(evt)
        self.actionScriptJTree.addMouseListener(_JavaListenerN66909()
            )
        self.jScrollPane1.setViewportView(self.actionScriptJTree)
        self.add(self.jScrollPane1)
    

    def actionScriptJTreeMouseReleased(self, evt: MouseEvent) -> None:
        from org.allbinary.input.automation.actions.script.condition.CustomTreeNodeInterface import CustomTreeNodeInterface
        button: int = evt.getButton()
        if button == MouseEvent.BUTTON3:
            treePath: TreePath = self.getActionScriptJTree().getSelectionPath()
            if treePath is not None:
                anyType: object = treePath.getLastPathComponent()
                if isinstance(anyType, CustomTreeNodeInterface):
                    customTreeNodeInterface: CustomTreeNodeInterface = anyType
                    jPopupMenu: JPopupMenu = customTreeNodeInterface.getJPopupMenu()
                    jPopupMenu.show(evt.getSource(), evt.getX(), evt.getY())
    

    def actionScriptJTreeMouseClicked(self, evt: MouseEvent) -> None:
        pass
# from java.awt.event.MouseEvent import MouseEvent
# from javax.swing.JPopupMenu import JPopupMenu
# from javax.swing.JComponent import JComponent
# from javax.swing.tree.DefaultMutableTreeNode import DefaultMutableTreeNode
# from javax.swing.tree.DefaultTreeModel import DefaultTreeModel
# from javax.swing.tree.TreePath import TreePath
# from org.allbinary.input.automation.actions.script.condition.CustomTreeNodeInterface import CustomTreeNodeInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from java.awt.Dimension import Dimension
# from java.awt.GridLayout import GridLayout
# from java.awt.event.MouseAdapter import MouseAdapter
# from javax.swing.JScrollPane import JScrollPane
# from javax.swing.JTree import JTree


