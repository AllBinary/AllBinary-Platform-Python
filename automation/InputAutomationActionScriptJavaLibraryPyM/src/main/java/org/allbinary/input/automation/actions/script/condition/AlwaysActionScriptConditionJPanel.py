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
# package org.allbinary.input.automation.actions.script.condition

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
# from javax.swing.JPanel import JPanel


@java_inherited_overloads
class AlwaysActionScriptConditionJPanel(JPanel):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("alwaysActionScriptConditionInterface", None)
        vars(self).setdefault("alwaysActionJButton", None)
        vars(self).setdefault("alwaysActionJDialog", None)
        vars(self).setdefault("alwaysJComboBox", None)
        vars(self).setdefault("jLabel1", None)
        vars(self).setdefault("jLabel2", None)
        vars(self).setdefault("okJButton", None)
        vars(self).setdefault("titleJLabel", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "alwaysActionScriptConditionInterface" not in vars(self): self.alwaysActionScriptConditionInterface: AlwaysActionScriptConditionInterface = None
        if "alwaysActionJButton" not in vars(self): self.alwaysActionJButton: JButton = None
        if "alwaysActionJDialog" not in vars(self): self.alwaysActionJDialog: JDialog = None
        if "alwaysJComboBox" not in vars(self): self.alwaysJComboBox: JComboBox = None
        if "jLabel1" not in vars(self): self.jLabel1: JLabel = None
        if "jLabel2" not in vars(self): self.jLabel2: JLabel = None
        if "okJButton" not in vars(self): self.okJButton: JButton = None
        if "titleJLabel" not in vars(self): self.titleJLabel: JLabel = None
    

    def __init__(self, alwaysActionScriptConditionInterface: AlwaysActionScriptConditionInterface) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.initComponents()
        self.alwaysActionScriptConditionInterface = alwaysActionScriptConditionInterface
        self.set()
    

    def set(self) -> None:
        if java_predicate(self.alwaysActionScriptConditionInterface, "isIsOn"):
            self.alwaysJComboBox.setSelectedIndex(0)
        else:
            self.alwaysJComboBox.setSelectedIndex(1)
        self.alwaysActionScriptConditionInterface.log()
    

    def update(self) -> None:
        if self.alwaysJComboBox.getSelectedIndex() == 0:
            self.alwaysActionScriptConditionInterface.setIsOn(True)
        else:
            self.alwaysActionScriptConditionInterface.setIsOn(False)
        self.alwaysActionScriptConditionInterface.log()
    

    def getAlwaysActionJDialog(self) -> JDialog:
        return self.alwaysActionJDialog
    

    def setAlwaysActionJDialog(self, alwaysActionJDialog: JDialog) -> None:
        self.alwaysActionJDialog = alwaysActionJDialog
    

    def initComponents(self) -> None:
        self.alwaysActionJDialog = JDialog()
        self.titleJLabel = JLabel()
        self.okJButton = JButton()
        self.jLabel2 = JLabel()
        self.alwaysJComboBox = JComboBox()
        self.alwaysActionJButton = JButton()
        self.jLabel1 = JLabel()
        self.alwaysActionJDialog.setMinimumSize(Dimension(250, 150))
        self.titleJLabel.setText("Always Condition Options")
        self.okJButton.setText("OK")
        _java_listener_owner = self
        class _JavaListenerN66985(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "okJButtonActionPerformed") else _java_listener_owner).okJButtonActionPerformed(evt)
        self.okJButton.addActionListener(_JavaListenerN66985()
            )
        self.jLabel2.setText("On:")
        self.alwaysJComboBox.setModel(DefaultComboBoxModel(["true", "false"]))
        alwaysActionJDialogLayout: GroupLayout = GroupLayout(self.alwaysActionJDialog.getContentPane())
        self.alwaysActionJDialog.getContentPane().setLayout(alwaysActionJDialogLayout)
        alwaysActionJDialogLayout.setHorizontalGroup(alwaysActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(alwaysActionJDialogLayout.createSequentialGroup().addGroup(alwaysActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(alwaysActionJDialogLayout.createSequentialGroup().addGap(47, 47, 47).addGroup(alwaysActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING, False).addGroup(GroupLayout.Alignment.TRAILING, alwaysActionJDialogLayout.createSequentialGroup().addComponent(self.jLabel2).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addComponent(self.alwaysJComboBox, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)).addComponent(self.titleJLabel))).addGroup(alwaysActionJDialogLayout.createSequentialGroup().addGap(79, 79, 79).addComponent(self.okJButton))).addContainerGap(45, Short.MAX_VALUE)))
        alwaysActionJDialogLayout.setVerticalGroup(alwaysActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(alwaysActionJDialogLayout.createSequentialGroup().addContainerGap().addComponent(self.titleJLabel).addGap(20, 20, 20).addGroup(alwaysActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.alwaysJComboBox, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel2)).addGap(15, 15, 15).addComponent(self.okJButton).addContainerGap()))
        self.setMinimumSize(Dimension(100, 0))
        self.alwaysActionJButton.setText("Edit")
        _java_listener_owner = self
        class _JavaListenerN68280(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "alwaysActionJButtonActionPerformed") else _java_listener_owner).alwaysActionJButtonActionPerformed(evt)
        self.alwaysActionJButton.addActionListener(_JavaListenerN68280()
            )
        self.jLabel1.setText("Always:")
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jLabel1).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, 33, Short.MAX_VALUE).addComponent(self.alwaysActionJButton)))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.alwaysActionJButton)))
    

    def okJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.update()
        self.getAlwaysActionJDialog().setVisible(False)
    

    def alwaysActionJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.getAlwaysActionJDialog().setVisible(True)
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from java.awt.Dimension import Dimension
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.DefaultComboBoxModel import DefaultComboBoxModel
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JButton import JButton
# from javax.swing.JComboBox import JComboBox
# from javax.swing.JDialog import JDialog
# from javax.swing.JLabel import JLabel
# from javax.swing.LayoutStyle import LayoutStyle


