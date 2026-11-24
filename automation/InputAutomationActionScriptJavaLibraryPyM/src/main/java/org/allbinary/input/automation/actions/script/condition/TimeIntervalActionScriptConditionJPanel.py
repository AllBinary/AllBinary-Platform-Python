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

# from javax.swing.JPanel import JPanel


class TimeIntervalActionScriptConditionJPanel(JPanel):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.timeIntervalActionScriptConditionInterface: TimeIntervalActionScriptConditionInterface = None
        self.jLabel1: JLabel = None
        self.jLabel2: JLabel = None
        self.okJButton: JButton = None
        self.timeIntervalActionJButton: JButton = None
        self.timeIntervalActionJDialog: JDialog = None
        self.timeIntervalJTextField: JTextField = None
        self.titleJLabel: JLabel = None
    

    def __init__(self, timeIntervalActionScriptConditionInterface: TimeIntervalActionScriptConditionInterface) -> None:
        super().__init__()
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.initComponents()
        self.timeIntervalActionScriptConditionInterface = timeIntervalActionScriptConditionInterface
        self.set()
    

    def set(self) -> None:
        self.getTimeIntervalJTextField().setText(str(self.timeIntervalActionScriptConditionInterface.getTimeDelayHelper().delay))
        self.timeIntervalActionScriptConditionInterface.log()
    

    def update(self) -> None:
        self.timeIntervalActionScriptConditionInterface.getTimeDelayHelper().delay = str(self.getTimeIntervalJTextField().getText())
        self.timeIntervalActionScriptConditionInterface.log()
    

    def getTimeIntervalJTextField(self) -> JTextField:
        return self.timeIntervalJTextField
    

    def setTimeIntervalJTextField(self, timeIntervalJTextField: JTextField) -> None:
        self.timeIntervalJTextField = timeIntervalJTextField
    

    def getTimeIntervalActionJDialog(self) -> JDialog:
        return self.timeIntervalActionJDialog
    

    def setTimeIntervalActionJDialog(self, timeIntervalActionJDialog: JDialog) -> None:
        self.timeIntervalActionJDialog = timeIntervalActionJDialog
    

    def initComponents(self) -> None:
        self.timeIntervalActionJDialog = JDialog()
        self.titleJLabel = JLabel()
        self.okJButton = JButton()
        self.jLabel2 = JLabel()
        self.timeIntervalJTextField = JTextField()
        self.timeIntervalActionJButton = JButton()
        self.jLabel1 = JLabel()
        self.timeIntervalActionJDialog.setMinimumSize(Dimension(250, 150))
        self.titleJLabel.setText("Time Interval Condition Options")
        self.okJButton.setText("OK")
        self.okJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.okJButtonActionPerformed(evt)
))
        self.jLabel2.setText("Time (ms):")
        timeIntervalActionJDialogLayout: GroupLayout = GroupLayout(self.timeIntervalActionJDialog.getContentPane())
        self.timeIntervalActionJDialog.getContentPane().setLayout(timeIntervalActionJDialogLayout)
        timeIntervalActionJDialogLayout.setHorizontalGroup(timeIntervalActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(timeIntervalActionJDialogLayout.createSequentialGroup().addGroup(timeIntervalActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.TRAILING).addGroup(GroupLayout.Alignment.LEADING, timeIntervalActionJDialogLayout.createSequentialGroup().addGap(82, 82, 82).addComponent(self.okJButton)).addGroup(GroupLayout.Alignment.LEADING, timeIntervalActionJDialogLayout.createSequentialGroup().addGap(32, 32, 32).addGroup(timeIntervalActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(timeIntervalActionJDialogLayout.createSequentialGroup().addComponent(self.jLabel2).addGap(16, 16, 16).addComponent(self.timeIntervalJTextField, GroupLayout.DEFAULT_SIZE, 85, Short.MAX_VALUE)).addComponent(self.titleJLabel)))).addContainerGap(36, Short.MAX_VALUE)))
        timeIntervalActionJDialogLayout.setVerticalGroup(timeIntervalActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(timeIntervalActionJDialogLayout.createSequentialGroup().addContainerGap().addComponent(self.titleJLabel).addGap(20, 20, 20).addGroup(timeIntervalActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jLabel2).addComponent(self.timeIntervalJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)).addGap(15, 15, 15).addComponent(self.okJButton).addContainerGap()))
        self.setMinimumSize(Dimension(100, 0))
        self.timeIntervalActionJButton.setText("Edit")
        self.timeIntervalActionJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.timeIntervalActionJButtonActionPerformed(evt)
))
        self.jLabel1.setText("Time Interval:")
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jLabel1).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addComponent(self.timeIntervalActionJButton)))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.timeIntervalActionJButton)))
    

    def okJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.update()
        self.getTimeIntervalActionJDialog().setVisible(False)
    

    def timeIntervalActionJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.getTimeIntervalActionJDialog().setVisible(True)
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from java.awt.Dimension import Dimension
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JButton import JButton
# from javax.swing.JDialog import JDialog
# from javax.swing.JLabel import JLabel
# from javax.swing.JTextField import JTextField
# from javax.swing.LayoutStyle import LayoutStyle


