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

from org.allbinary.input.automation.actions.script.condition.JPanel import JPanel


class AlwaysActionScriptConditionJPanel(JPanel):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.alwaysActionScriptConditionInterface: AlwaysActionScriptConditionInterface = None
        self.alwaysActionJButton: JButton = None
        self.alwaysActionJDialog: JDialog = None
        self.alwaysJComboBox: JComboBox = None
        self.jLabel1: JLabel = None
        self.jLabel2: JLabel = None
        self.okJButton: JButton = None
        self.titleJLabel: JLabel = None
    

    def __init__(self, alwaysActionScriptConditionInterface: AlwaysActionScriptConditionInterface) -> None:
        super().__init__()
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.initComponents()
        self.alwaysActionScriptConditionInterface = alwaysActionScriptConditionInterface
        self.set()
    

    def set(self) -> None:
        if self.alwaysActionScriptConditionInterface.isIsOn():
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
        from org.allbinary.input.automation.actions.script.condition.JDialog import JDialog
        from org.allbinary.input.automation.actions.script.condition.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.JButton import JButton
        from org.allbinary.input.automation.actions.script.condition.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.JComboBox import JComboBox
        from org.allbinary.input.automation.actions.script.condition.JButton import JButton
        from org.allbinary.input.automation.actions.script.condition.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.Dimension import Dimension
        from org.allbinary.input.automation.actions.script.condition.ActionListener import ActionListener
        from org.allbinary.input.automation.actions.script.condition.DefaultComboBoxModel import DefaultComboBoxModel
        from org.allbinary.input.automation.actions.script.condition.GroupLayout import GroupLayout
        from org.allbinary.input.automation.actions.script.condition.Dimension import Dimension
        from org.allbinary.input.automation.actions.script.condition.ActionListener import ActionListener
        from org.allbinary.input.automation.actions.script.condition.GroupLayout import GroupLayout
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
        self.okJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.okJButtonActionPerformed(evt)
))
        self.jLabel2.setText("On:")
        self.alwaysJComboBox.setModel(DefaultComboBoxModel(["true", "false"]))
        alwaysActionJDialogLayout: GroupLayout = GroupLayout(self.alwaysActionJDialog.getContentPane())
        self.alwaysActionJDialog.getContentPane().setLayout(alwaysActionJDialogLayout)
        alwaysActionJDialogLayout.setHorizontalGroup(alwaysActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(alwaysActionJDialogLayout.createSequentialGroup().addGroup(alwaysActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(alwaysActionJDialogLayout.createSequentialGroup().addGap(47, 47, 47).addGroup(alwaysActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, False).addGroup(javax.swing.GroupLayout.Alignment.TRAILING, alwaysActionJDialogLayout.createSequentialGroup().addComponent(self.jLabel2).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addComponent(self.alwaysJComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addComponent(self.titleJLabel))).addGroup(alwaysActionJDialogLayout.createSequentialGroup().addGap(79, 79, 79).addComponent(self.okJButton))).addContainerGap(45, Short.MAX_VALUE)))
        alwaysActionJDialogLayout.setVerticalGroup(alwaysActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(alwaysActionJDialogLayout.createSequentialGroup().addContainerGap().addComponent(self.titleJLabel).addGap(20, 20, 20).addGroup(alwaysActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.alwaysJComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel2)).addGap(15, 15, 15).addComponent(self.okJButton).addContainerGap()))
        self.setMinimumSize(Dimension(100, 0))
        self.alwaysActionJButton.setText("Edit")
        self.alwaysActionJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.alwaysActionJButtonActionPerformed(evt)
))
        self.jLabel1.setText("Always:")
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jLabel1).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 33, Short.MAX_VALUE).addComponent(self.alwaysActionJButton)))
        layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.alwaysActionJButton)))
    

    def okJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.update()
        self.getAlwaysActionJDialog().setVisible(False)
    

    def alwaysActionJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.getAlwaysActionJDialog().setVisible(True)
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


