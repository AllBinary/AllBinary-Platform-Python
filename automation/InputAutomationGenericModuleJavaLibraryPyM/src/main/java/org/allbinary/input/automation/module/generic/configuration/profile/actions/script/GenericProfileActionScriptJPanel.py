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

from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.input.automation.actions.script.JTreeInterface import JTreeInterface
# from javax.swing.JPanel import JPanel


class GenericProfileActionScriptJPanel(*java_bases(JPanel, JTreeInterface)):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.defaultMutableTreeNode: DefaultMutableTreeNode = DefaultMutableTreeNode("Root")
        self.genericProfileActionScript: GenericProfileActionScript = None
        self.actionScriptJTree: JTree = None
        self.jScrollPane1: JScrollPane = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
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
        self.actionScriptJTree.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mouseClicked(self, evt: MouseEvent) -> None:
#                 self.actionScriptJTreeMouseClicked(evt)
#             
# 
#             def mouseReleased(self, evt: MouseEvent) -> None:
#                 self.actionScriptJTreeMouseReleased(evt)
))
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


