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
# package org.allbinary.input.automation.module.generic.configuration.profile.actions

from __future__ import annotations

from org.allbinary.input.automation.module.generic.configuration.profile.actions.JPanel import JPanel


class GenericProfileActionJPanel(JPanel):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.genericProfileAction: GenericProfileAction = None
        self.genericProfileActionScriptJPanel: GenericProfileActionScriptJPanel = None
        self.blankProfileActionScriptJPanel: JPanel = None
        self.genericProfileActionScriptJScrollPane: JScrollPane = None
        self.ifJLabel: JLabel = None
        self.newAlwaysJButton: JButton = None
        self.newColorAtJButton: JButton = None
        self.newTimeIntervalJButton: JButton = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.initComponents()
    

    def updateProfileActionUI(self) -> None:
        self.blankProfileActionScriptJPanel.removeAll()
        genericProfileActionScriptJPanel: GenericProfileActionScriptJPanel = GenericProfileActionScriptJPanel()
        JTreeInterfaceFactory.getInstance().set(genericProfileActionScriptJPanel)
        self.setGenericProfileActionScriptJPanel(genericProfileActionScriptJPanel)
        self.getGenericProfileActionScriptJPanel().setGenericProfileActionScript(self.getGenericProfileAction().getGenericProfileActionScript())
        self.getGenericProfileActionScriptJPanel().updateJTree()
        layout: GroupLayout = self.blankProfileActionScriptJPanel.getLayout()
        layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGap(0, 395, Short.MAX_VALUE).addComponent(self.getGenericProfileActionScriptJPanel(), javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
        layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGap(0, 256, Short.MAX_VALUE).addComponent(self.getGenericProfileActionScriptJPanel(), javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
        self.logUtil.putF("Updated UI", self, "updateUI")
    

    def getGenericProfileAction(self) -> GenericProfileAction:
        return self.genericProfileAction
    

    def setGenericProfileAction(self, genericProfileAction: GenericProfileAction) -> None:
        self.genericProfileAction = genericProfileAction
    

    def getGenericProfileActionScriptJPanel(self) -> GenericProfileActionScriptJPanel:
        return self.genericProfileActionScriptJPanel
    

    def setGenericProfileActionScriptJPanel(self, genericProfileActionScriptJPanel: GenericProfileActionScriptJPanel) -> None:
        self.genericProfileActionScriptJPanel = genericProfileActionScriptJPanel
    

    def initComponents(self) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.JScrollPane import JScrollPane
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.JPanel import JPanel
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.JLabel import JLabel
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.JButton import JButton
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.JButton import JButton
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.JButton import JButton
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.Dimension import Dimension
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.Dimension import Dimension
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.Dimension import Dimension
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.Dimension import Dimension
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GroupLayout import GroupLayout
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.ActionListener import ActionListener
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.ActionListener import ActionListener
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.ActionListener import ActionListener
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GroupLayout import GroupLayout
        self.genericProfileActionScriptJScrollPane = JScrollPane()
        self.blankProfileActionScriptJPanel = JPanel()
        self.ifJLabel = JLabel()
        self.newColorAtJButton = JButton()
        self.newTimeIntervalJButton = JButton()
        self.newAlwaysJButton = JButton()
        self.setMinimumSize(Dimension(440, 275))
        self.setPreferredSize(Dimension(440, 275))
        self.genericProfileActionScriptJScrollPane.setPreferredSize(Dimension(474, 270))
        self.blankProfileActionScriptJPanel.setMinimumSize(Dimension(400, 200))
        blankProfileActionScriptJPanelLayout: GroupLayout = GroupLayout(self.blankProfileActionScriptJPanel)
        self.blankProfileActionScriptJPanel.setLayout(blankProfileActionScriptJPanelLayout)
        blankProfileActionScriptJPanelLayout.setHorizontalGroup(blankProfileActionScriptJPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGap(0, 9996, Short.MAX_VALUE))
        blankProfileActionScriptJPanelLayout.setVerticalGroup(blankProfileActionScriptJPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGap(0, 9967, Short.MAX_VALUE))
        self.genericProfileActionScriptJScrollPane.setViewportView(self.blankProfileActionScriptJPanel)
        self.ifJLabel.setText("Conditions:")
        self.newColorAtJButton.setText("Color Range At")
        self.newColorAtJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.newColorAtJButtonActionPerformed(evt)
))
        self.newTimeIntervalJButton.setText("Time Interval")
        self.newTimeIntervalJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.newTimeIntervalJButtonActionPerformed(evt)
))
        self.newAlwaysJButton.setText("Always On/Off")
        self.newAlwaysJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.newAlwaysJButtonActionPerformed(evt)
))
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.ifJLabel).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.newColorAtJButton).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.newTimeIntervalJButton).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.newAlwaysJButton).addContainerGap(61, Short.MAX_VALUE)).addComponent(self.genericProfileActionScriptJScrollPane, javax.swing.GroupLayout.DEFAULT_SIZE, 440, Short.MAX_VALUE))
        layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.ifJLabel, javax.swing.GroupLayout.PREFERRED_SIZE, 14, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.newColorAtJButton).addComponent(self.newTimeIntervalJButton).addComponent(self.newAlwaysJButton)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.genericProfileActionScriptJScrollPane, javax.swing.GroupLayout.DEFAULT_SIZE, 246, Short.MAX_VALUE)))
    

    def newTimeIntervalJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.logUtil.putF("New Time Interval Action Condition", self, "newTimeIntervalJButtonActionPerformed")
        self.getGenericProfileAction().getGenericProfileActionScript().addCondition(TimeIntervalActionScriptCondition())
        self.updateProfileActionUI()
    

    def newAlwaysJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.logUtil.putF("New EveryTime Action Condition", self, "newEveryTimeJButtonActionPerformed")
        self.getGenericProfileAction().getGenericProfileActionScript().addCondition(AlwaysActionScriptCondition())
        self.updateProfileActionUI()
    

    def newColorAtJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.logUtil.putF("New Color At Action Condition", self, "newColorAtJButtonActionPerformed")
        self.getGenericProfileAction().getGenericProfileActionScript().addCondition(ColorAtActionScriptCondition())
        self.updateProfileActionUI()
from org.allbinary.input.automation.actions.script.JTreeInterfaceFactory import JTreeInterfaceFactory
from org.allbinary.input.automation.actions.script.condition.AlwaysActionScriptCondition import AlwaysActionScriptCondition
from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptCondition import ColorAtActionScriptCondition
from org.allbinary.input.automation.actions.script.condition.ProfileActionScriptConditionInterface import ProfileActionScriptConditionInterface
from org.allbinary.input.automation.actions.script.condition.TimeIntervalActionScriptCondition import TimeIntervalActionScriptCondition
from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.GenericProfileActionScriptJPanel import GenericProfileActionScriptJPanel
from org.allbinary.logic.communication.log.LogUtil import LogUtil


