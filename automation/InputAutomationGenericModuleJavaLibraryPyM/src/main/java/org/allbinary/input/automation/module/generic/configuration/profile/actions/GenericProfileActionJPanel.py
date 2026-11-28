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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
# from javax.swing.JPanel import JPanel


@java_inherited_overloads
class GenericProfileActionJPanel(JPanel):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("genericProfileAction", None)
        vars(self).setdefault("genericProfileActionScriptJPanel", None)
        vars(self).setdefault("blankProfileActionScriptJPanel", None)
        vars(self).setdefault("genericProfileActionScriptJScrollPane", None)
        vars(self).setdefault("ifJLabel", None)
        vars(self).setdefault("newAlwaysJButton", None)
        vars(self).setdefault("newColorAtJButton", None)
        vars(self).setdefault("newTimeIntervalJButton", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "genericProfileAction" not in vars(self): self.genericProfileAction: GenericProfileAction = None
        if "genericProfileActionScriptJPanel" not in vars(self): self.genericProfileActionScriptJPanel: GenericProfileActionScriptJPanel = None
        if "blankProfileActionScriptJPanel" not in vars(self): self.blankProfileActionScriptJPanel: JPanel = None
        if "genericProfileActionScriptJScrollPane" not in vars(self): self.genericProfileActionScriptJScrollPane: JScrollPane = None
        if "ifJLabel" not in vars(self): self.ifJLabel: JLabel = None
        if "newAlwaysJButton" not in vars(self): self.newAlwaysJButton: JButton = None
        if "newColorAtJButton" not in vars(self): self.newColorAtJButton: JButton = None
        if "newTimeIntervalJButton" not in vars(self): self.newTimeIntervalJButton: JButton = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.initComponents()
    

    def updateProfileActionUI(self) -> None:
        from org.allbinary.input.automation.actions.script.JTreeInterfaceFactory import JTreeInterfaceFactory
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.GenericProfileActionScriptJPanel import GenericProfileActionScriptJPanel
        self.blankProfileActionScriptJPanel.removeAll()
        genericProfileActionScriptJPanel: GenericProfileActionScriptJPanel = GenericProfileActionScriptJPanel()
        JTreeInterfaceFactory.getInstance().set(genericProfileActionScriptJPanel)
        self.setGenericProfileActionScriptJPanel(genericProfileActionScriptJPanel)
        self.getGenericProfileActionScriptJPanel().setGenericProfileActionScript(self.getGenericProfileAction().getGenericProfileActionScript())
        self.getGenericProfileActionScriptJPanel().updateJTree()
        layout: GroupLayout = self.blankProfileActionScriptJPanel.getLayout()
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 395, Short.MAX_VALUE).addComponent(self.getGenericProfileActionScriptJPanel(), GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 256, Short.MAX_VALUE).addComponent(self.getGenericProfileActionScriptJPanel(), GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))
        self.logUtil.putF("Updated UI", self, "updateUI")
    

    def getGenericProfileAction(self) -> GenericProfileAction:
        return self.genericProfileAction
    

    def setGenericProfileAction(self, genericProfileAction: GenericProfileAction) -> None:
        self.genericProfileAction = genericProfileAction
    

    def getGenericProfileActionScriptJPanel(self) -> GenericProfileActionScriptJPanel:
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.GenericProfileActionScriptJPanel import GenericProfileActionScriptJPanel
        return self.genericProfileActionScriptJPanel
    

    def setGenericProfileActionScriptJPanel(self, genericProfileActionScriptJPanel: GenericProfileActionScriptJPanel) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.GenericProfileActionScriptJPanel import GenericProfileActionScriptJPanel
        self.genericProfileActionScriptJPanel = genericProfileActionScriptJPanel
    

    def initComponents(self) -> None:
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
        blankProfileActionScriptJPanelLayout.setHorizontalGroup(blankProfileActionScriptJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 9996, Short.MAX_VALUE))
        blankProfileActionScriptJPanelLayout.setVerticalGroup(blankProfileActionScriptJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 9967, Short.MAX_VALUE))
        self.genericProfileActionScriptJScrollPane.setViewportView(self.blankProfileActionScriptJPanel)
        self.ifJLabel.setText("Conditions:")
        self.newColorAtJButton.setText("Color Range At")
        _java_listener_owner = self
        class _JavaListenerN67962(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "newColorAtJButtonActionPerformed") else _java_listener_owner).newColorAtJButtonActionPerformed(evt)
        self.newColorAtJButton.addActionListener(_JavaListenerN67962()
            )
        self.newTimeIntervalJButton.setText("Time Interval")
        _java_listener_owner = self
        class _JavaListenerN68101(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "newTimeIntervalJButtonActionPerformed") else _java_listener_owner).newTimeIntervalJButtonActionPerformed(evt)
        self.newTimeIntervalJButton.addActionListener(_JavaListenerN68101()
            )
        self.newAlwaysJButton.setText("Always On/Off")
        _java_listener_owner = self
        class _JavaListenerN68240(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "newAlwaysJButtonActionPerformed") else _java_listener_owner).newAlwaysJButtonActionPerformed(evt)
        self.newAlwaysJButton.addActionListener(_JavaListenerN68240()
            )
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.ifJLabel).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.newColorAtJButton).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.newTimeIntervalJButton).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.newAlwaysJButton).addContainerGap(61, Short.MAX_VALUE)).addComponent(self.genericProfileActionScriptJScrollPane, GroupLayout.DEFAULT_SIZE, 440, Short.MAX_VALUE))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.ifJLabel, GroupLayout.PREFERRED_SIZE, 14, GroupLayout.PREFERRED_SIZE).addComponent(self.newColorAtJButton).addComponent(self.newTimeIntervalJButton).addComponent(self.newAlwaysJButton)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.genericProfileActionScriptJScrollPane, GroupLayout.DEFAULT_SIZE, 246, Short.MAX_VALUE)))
    

    def newTimeIntervalJButtonActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.input.automation.actions.script.condition.ProfileActionScriptConditionInterface import ProfileActionScriptConditionInterface
        from org.allbinary.input.automation.actions.script.condition.TimeIntervalActionScriptCondition import TimeIntervalActionScriptCondition
        self.logUtil.putF("New Time Interval Action Condition", self, "newTimeIntervalJButtonActionPerformed")
        self.getGenericProfileAction().getGenericProfileActionScript().addCondition(TimeIntervalActionScriptCondition())
        self.updateProfileActionUI()
    

    def newAlwaysJButtonActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.input.automation.actions.script.condition.AlwaysActionScriptCondition import AlwaysActionScriptCondition
        from org.allbinary.input.automation.actions.script.condition.ProfileActionScriptConditionInterface import ProfileActionScriptConditionInterface
        self.logUtil.putF("New EveryTime Action Condition", self, "newEveryTimeJButtonActionPerformed")
        self.getGenericProfileAction().getGenericProfileActionScript().addCondition(AlwaysActionScriptCondition())
        self.updateProfileActionUI()
    

    def newColorAtJButtonActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptCondition import ColorAtActionScriptCondition
        from org.allbinary.input.automation.actions.script.condition.ProfileActionScriptConditionInterface import ProfileActionScriptConditionInterface
        self.logUtil.putF("New Color At Action Condition", self, "newColorAtJButtonActionPerformed")
        self.getGenericProfileAction().getGenericProfileActionScript().addCondition(ColorAtActionScriptCondition())
        self.updateProfileActionUI()
# from org.allbinary.input.automation.actions.script.JTreeInterfaceFactory import JTreeInterfaceFactory
# from org.allbinary.input.automation.actions.script.condition.AlwaysActionScriptCondition import AlwaysActionScriptCondition
# from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptCondition import ColorAtActionScriptCondition
# from org.allbinary.input.automation.actions.script.condition.ProfileActionScriptConditionInterface import ProfileActionScriptConditionInterface
# from org.allbinary.input.automation.actions.script.condition.TimeIntervalActionScriptCondition import TimeIntervalActionScriptCondition
# from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.GenericProfileActionScriptJPanel import GenericProfileActionScriptJPanel
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from java.awt.Dimension import Dimension
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JButton import JButton
# from javax.swing.JLabel import JLabel
# from javax.swing.JScrollPane import JScrollPane
# from javax.swing.LayoutStyle import LayoutStyle


