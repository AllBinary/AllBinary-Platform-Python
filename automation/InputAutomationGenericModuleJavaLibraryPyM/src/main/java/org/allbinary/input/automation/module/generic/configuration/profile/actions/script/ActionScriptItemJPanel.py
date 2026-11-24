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

# from javax.swing.JPanel import JPanel


class ActionScriptItemJPanel(JPanel):

    def _init_fields(self) -> None:
        self.childActionScriptConditionJPanel: JPanel = None
        self.newActionScriptConditionJPanel: JPanel = None
        self.newActionScriptInputJPanel: JPanel = None
        self.removeJPanel: JPanel = None
        self.scriptItemJPanel: JPanel = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.initComponents()
    

    def getNewActionScriptInputJPanel(self) -> JPanel:
        return self.newActionScriptInputJPanel
    

    def setNewActionScriptInputJPanel(self, newActionScriptInputJPanel: JPanel) -> None:
        self.newActionScriptInputJPanel = newActionScriptInputJPanel
    

    def getRemoveJPanel(self) -> JPanel:
        return self.removeJPanel
    

    def setRemoveJPanel(self, removeJPanel: JPanel) -> None:
        self.removeJPanel = removeJPanel
    

    def getScriptItemJPanel(self) -> JPanel:
        return self.scriptItemJPanel
    

    def setScriptItemJPanel(self, scriptItemJPanel: JPanel) -> None:
        self.scriptItemJPanel = scriptItemJPanel
    

    def getNewActionScriptConditionJPanel(self) -> JPanel:
        return self.newActionScriptConditionJPanel
    

    def setNewActionScriptConditionJPanel(self, newActionScriptConditionJPanel: JPanel) -> None:
        self.newActionScriptConditionJPanel = newActionScriptConditionJPanel
    

    def getChildActionScriptConditionJPanel(self) -> JPanel:
        return self.childActionScriptConditionJPanel
    

    def setChildActionScriptConditionJPanel(self, childActionScriptConditionJPanel: JPanel) -> None:
        self.childActionScriptConditionJPanel = childActionScriptConditionJPanel
    

    def initComponents(self) -> None:
        self.newActionScriptInputJPanel = JPanel()
        self.childActionScriptConditionJPanel = JPanel()
        self.newActionScriptConditionJPanel = JPanel()
        self.scriptItemJPanel = JPanel()
        self.removeJPanel = JPanel()
        self.newActionScriptInputJPanel.setLayout(GridLayout(1, 0))
        childActionScriptConditionJPanelLayout: GroupLayout = GroupLayout(self.childActionScriptConditionJPanel)
        self.childActionScriptConditionJPanel.setLayout(childActionScriptConditionJPanelLayout)
        childActionScriptConditionJPanelLayout.setHorizontalGroup(childActionScriptConditionJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 229, Short.MAX_VALUE))
        childActionScriptConditionJPanelLayout.setVerticalGroup(childActionScriptConditionJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 8, Short.MAX_VALUE))
        self.newActionScriptConditionJPanel.setLayout(GridLayout(1, 0))
        self.scriptItemJPanel.setLayout(GridLayout(1, 1))
        self.removeJPanel.setLayout(GridLayout(1, 1))
        self.removeJPanel.setMinimumSize(Dimension(30, 20))
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.scriptItemJPanel, GroupLayout.PREFERRED_SIZE, 167, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.removeJPanel, GroupLayout.DEFAULT_SIZE, 56, Short.MAX_VALUE)).addComponent(self.newActionScriptInputJPanel, GroupLayout.DEFAULT_SIZE, 229, Short.MAX_VALUE).addComponent(self.newActionScriptConditionJPanel, GroupLayout.DEFAULT_SIZE, 229, Short.MAX_VALUE).addComponent(self.childActionScriptConditionJPanel, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.scriptItemJPanel, GroupLayout.DEFAULT_SIZE, 31, Short.MAX_VALUE).addComponent(self.removeJPanel, GroupLayout.Alignment.TRAILING, GroupLayout.DEFAULT_SIZE, 31, Short.MAX_VALUE)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.childActionScriptConditionJPanel, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.newActionScriptConditionJPanel, GroupLayout.PREFERRED_SIZE, 28, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.newActionScriptInputJPanel, GroupLayout.PREFERRED_SIZE, 30, GroupLayout.PREFERRED_SIZE)))
# from java.awt.Dimension import Dimension
# from java.awt.GridLayout import GridLayout
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.LayoutStyle import LayoutStyle


