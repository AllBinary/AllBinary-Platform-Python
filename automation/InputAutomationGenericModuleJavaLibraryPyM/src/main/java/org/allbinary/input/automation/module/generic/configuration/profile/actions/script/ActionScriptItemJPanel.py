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

from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.JPanel import JPanel


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
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.JPanel import JPanel
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.JPanel import JPanel
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.JPanel import JPanel
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.JPanel import JPanel
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.JPanel import JPanel
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.GridLayout import GridLayout
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.GroupLayout import GroupLayout
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.GridLayout import GridLayout
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.GridLayout import GridLayout
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.GridLayout import GridLayout
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.Dimension import Dimension
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.GroupLayout import GroupLayout
        self.newActionScriptInputJPanel = JPanel()
        self.childActionScriptConditionJPanel = JPanel()
        self.newActionScriptConditionJPanel = JPanel()
        self.scriptItemJPanel = JPanel()
        self.removeJPanel = JPanel()
        self.newActionScriptInputJPanel.setLayout(GridLayout(1, 0))
        childActionScriptConditionJPanelLayout: GroupLayout = GroupLayout(self.childActionScriptConditionJPanel)
        self.childActionScriptConditionJPanel.setLayout(childActionScriptConditionJPanelLayout)
        childActionScriptConditionJPanelLayout.setHorizontalGroup(childActionScriptConditionJPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGap(0, 229, Short.MAX_VALUE))
        childActionScriptConditionJPanelLayout.setVerticalGroup(childActionScriptConditionJPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGap(0, 8, Short.MAX_VALUE))
        self.newActionScriptConditionJPanel.setLayout(GridLayout(1, 0))
        self.scriptItemJPanel.setLayout(GridLayout(1, 1))
        self.removeJPanel.setLayout(GridLayout(1, 1))
        self.removeJPanel.setMinimumSize(Dimension(30, 20))
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.scriptItemJPanel, javax.swing.GroupLayout.PREFERRED_SIZE, 167, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.removeJPanel, javax.swing.GroupLayout.DEFAULT_SIZE, 56, Short.MAX_VALUE)).addComponent(self.newActionScriptInputJPanel, javax.swing.GroupLayout.DEFAULT_SIZE, 229, Short.MAX_VALUE).addComponent(self.newActionScriptConditionJPanel, javax.swing.GroupLayout.DEFAULT_SIZE, 229, Short.MAX_VALUE).addComponent(self.childActionScriptConditionJPanel, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.scriptItemJPanel, javax.swing.GroupLayout.DEFAULT_SIZE, 31, Short.MAX_VALUE).addComponent(self.removeJPanel, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, 31, Short.MAX_VALUE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.childActionScriptConditionJPanel, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.newActionScriptConditionJPanel, javax.swing.GroupLayout.PREFERRED_SIZE, 28, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.newActionScriptInputJPanel, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)))


