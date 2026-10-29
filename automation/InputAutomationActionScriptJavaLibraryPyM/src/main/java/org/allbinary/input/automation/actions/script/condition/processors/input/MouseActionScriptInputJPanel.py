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
# package org.allbinary.input.automation.actions.script.condition.processors.input

from __future__ import annotations

from org.allbinary.input.automation.actions.script.condition.processors.input.JPanel import JPanel


class MouseActionScriptInputJPanel(JPanel):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.mouseActionScriptInputInterface: MouseActionScriptInputInterface = None
        self.button1JCheckBox: JCheckBox = None
        self.button2JCheckBox: JCheckBox = None
        self.inputAutomationTypeJComboBox: JComboBox = None
        self.inputTypeJLabel: JLabel = None
        self.jLabel1: JLabel = None
        self.jLabel2: JLabel = None
        self.jLabel3: JLabel = None
        self.jLabel4: JLabel = None
        self.jLabel5: JLabel = None
        self.jLabel6: JLabel = None
        self.mouseActionJButton: JButton = None
        self.mouseActionJDialog: JDialog = None
        self.mouseDelayJTextField: JTextField = None
        self.mouseXJTextField: JTextField = None
        self.mouseYJTextField: JTextField = None
        self.okJButton: JButton = None
        self.titleJLabel: JLabel = None
    

    def __init__(self, mouseActionScriptInputInterface: MouseActionScriptInputInterface) -> None:
        from org.allbinary.input.automation.actions.script.condition.processors.input.DefaultComboBoxModel import DefaultComboBoxModel
        super().__init__()
        self._init_fields()
        self.logUtil.putF(CommonLabels.getInstance().START + mouseActionScriptInputInterface, self, self.commonStrings.CONSTRUCTOR)
        self.initComponents()
        self.mouseActionScriptInputInterface = mouseActionScriptInputInterface
        defaultComboBoxModel: DefaultComboBoxModel = DefaultComboBoxModel()
        defaultComboBoxModel.addElement(TempInputRobotNames.LOW_NAME)
        defaultComboBoxModel.addElement(TempInputRobotNames.SYS_NAME)
        defaultComboBoxModel.addElement(InputRobot.NAME)
        self.inputAutomationTypeJComboBox.setModel(defaultComboBoxModel)
        self.set()
    

    def set(self) -> None:
        inputTypeComboBoxModel: ComboBoxModel = self.inputAutomationTypeJComboBox.getModel()
        inputTypeComboBoxModel.setSelectedItem(self.mouseActionScriptInputInterface.getInputRobotInterface().getName())
        if (self.mouseActionScriptInputInterface.getButtonClicks() & InputEvent.BUTTON1_MASK) != 0:
            self.button1JCheckBox.setSelected(True)
        else:
            self.button1JCheckBox.setSelected(False)
        if (self.mouseActionScriptInputInterface.getButtonClicks() & InputEvent.BUTTON2_MASK) != 0:
            self.button2JCheckBox.setSelected(True)
        else:
            self.button2JCheckBox.setSelected(False)
        self.mouseDelayJTextField.setText(str(self.mouseActionScriptInputInterface.getTime()))
        self.mouseXJTextField.setText(str(self.mouseActionScriptInputInterface.getPoint().x))
        self.mouseYJTextField.setText(str(self.mouseActionScriptInputInterface.getPoint().y))
        self.mouseActionScriptInputInterface.log()
    

    # throws Exception
    def updateInputType(self) -> None:
        comboBoxModel: ComboBoxModel = self.inputAutomationTypeJComboBox.getModel()
        selectedItem: str = comboBoxModel.getSelectedItem()
        if not StringValidationUtil.getInstance().isEmpty(selectedItem):
            self.mouseActionScriptInputInterface.setInputRobotInterface(InputRobotFactory.getInstance().get(selectedItem))
    

    # throws Exception
    def update(self) -> None:
        self.updateInputType()
        self.mouseActionScriptInputInterface.setTime(str(self.mouseDelayJTextField.getText()))
        self.logUtil.putF("Button State: " + str(self.mouseActionScriptInputInterface.getButtonClicks()), self, "update")
        if self.button1JCheckBox.isSelected():
            if (self.mouseActionScriptInputInterface.getButtonClicks() & InputEvent.BUTTON1_MASK) == 0:
                self.mouseActionScriptInputInterface.setButtonClicks(self.mouseActionScriptInputInterface.getButtonClicks() | InputEvent.BUTTON1_MASK)
                self.logUtil.putF("Button 1 Selected: " + str(self.mouseActionScriptInputInterface.getButtonClicks()), self, "update")
        else:
            if (self.mouseActionScriptInputInterface.getButtonClicks() & InputEvent.BUTTON1_MASK) != 0:
                self.mouseActionScriptInputInterface.setButtonClicks(self.mouseActionScriptInputInterface.getButtonClicks() ^ InputEvent.BUTTON1_MASK)
                self.logUtil.putF("Button 1 Deselected: " + str(self.mouseActionScriptInputInterface.getButtonClicks()), self, "update")
        if self.button2JCheckBox.isSelected():
            if (self.mouseActionScriptInputInterface.getButtonClicks() & InputEvent.BUTTON2_MASK) == 0:
                self.mouseActionScriptInputInterface.setButtonClicks(self.mouseActionScriptInputInterface.getButtonClicks() | InputEvent.BUTTON2_MASK)
                self.logUtil.putF("Button 2 Selected: " + str(self.mouseActionScriptInputInterface.getButtonClicks()), self, "update")
        else:
            if (self.mouseActionScriptInputInterface.getButtonClicks() & InputEvent.BUTTON2_MASK) != 0:
                self.mouseActionScriptInputInterface.setButtonClicks(self.mouseActionScriptInputInterface.getButtonClicks() ^ InputEvent.BUTTON2_MASK)
                self.logUtil.putF("Button 2 Deselected: " + str(self.mouseActionScriptInputInterface.getButtonClicks()), self, "update")
        mouseXString: str = self.mouseXJTextField.getText()
        if not StringValidationUtil.getInstance().isEmpty(mouseXString) and StringValidationUtil.getInstance().isNumber(mouseXString):
            self.mouseActionScriptInputInterface.getPoint().x = int(mouseXString)
        mouseYString: str = self.mouseYJTextField.getText()
        if not StringValidationUtil.getInstance().isEmpty(mouseYString) and StringValidationUtil.getInstance().isNumber(mouseYString):
            self.mouseActionScriptInputInterface.getPoint().y = int(mouseYString)
        self.mouseActionScriptInputInterface.log()
    

    def getMouseActionJDialog(self) -> JDialog:
        return self.mouseActionJDialog
    

    def setMouseActionJDialog(self, mouseActionJDialog: JDialog) -> None:
        self.mouseActionJDialog = mouseActionJDialog
    

    def initComponents(self) -> None:
        from org.allbinary.input.automation.actions.script.condition.processors.input.JDialog import JDialog
        from org.allbinary.input.automation.actions.script.condition.processors.input.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.processors.input.JButton import JButton
        from org.allbinary.input.automation.actions.script.condition.processors.input.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.processors.input.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.processors.input.JCheckBox import JCheckBox
        from org.allbinary.input.automation.actions.script.condition.processors.input.JCheckBox import JCheckBox
        from org.allbinary.input.automation.actions.script.condition.processors.input.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.processors.input.JTextField import JTextField
        from org.allbinary.input.automation.actions.script.condition.processors.input.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.processors.input.JTextField import JTextField
        from org.allbinary.input.automation.actions.script.condition.processors.input.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.processors.input.JComboBox import JComboBox
        from org.allbinary.input.automation.actions.script.condition.processors.input.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.processors.input.JTextField import JTextField
        from org.allbinary.input.automation.actions.script.condition.processors.input.JButton import JButton
        from org.allbinary.input.automation.actions.script.condition.processors.input.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.processors.input.Dimension import Dimension
        from org.allbinary.input.automation.actions.script.condition.processors.input.ActionListener import ActionListener
        from org.allbinary.input.automation.actions.script.condition.processors.input.Insets import Insets
        from org.allbinary.input.automation.actions.script.condition.processors.input.Insets import Insets
        from org.allbinary.input.automation.actions.script.condition.processors.input.ActionListener import ActionListener
        from org.allbinary.input.automation.actions.script.condition.processors.input.GroupLayout import GroupLayout
        from org.allbinary.input.automation.actions.script.condition.processors.input.Dimension import Dimension
        from org.allbinary.input.automation.actions.script.condition.processors.input.ActionListener import ActionListener
        from org.allbinary.input.automation.actions.script.condition.processors.input.GroupLayout import GroupLayout
        self.mouseActionJDialog = JDialog()
        self.titleJLabel = JLabel()
        self.okJButton = JButton()
        self.jLabel2 = JLabel()
        self.jLabel3 = JLabel()
        self.button1JCheckBox = JCheckBox()
        self.button2JCheckBox = JCheckBox()
        self.jLabel4 = JLabel()
        self.mouseXJTextField = JTextField()
        self.jLabel5 = JLabel()
        self.mouseYJTextField = JTextField()
        self.inputTypeJLabel = JLabel()
        self.inputAutomationTypeJComboBox = JComboBox()
        self.jLabel6 = JLabel()
        self.mouseDelayJTextField = JTextField()
        self.mouseActionJButton = JButton()
        self.jLabel1 = JLabel()
        self.mouseActionJDialog.setMinimumSize(Dimension(275, 185))
        self.titleJLabel.setText("Mouse Input Options")
        self.okJButton.setText("OK")
        self.okJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.okJButtonActionPerformed(evt)
))
        self.jLabel2.setText("Buttons:")
        self.jLabel3.setText("Move To:")
        self.button1JCheckBox.setText(CommonPhoneStrings.getInstance().ONE)
        self.button1JCheckBox.setBorder(javax.swing.BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.button1JCheckBox.setMargin(Insets(0, 0, 0, 0))
        self.button2JCheckBox.setText(CommonPhoneStrings.getInstance().TWO)
        self.button2JCheckBox.setBorder(javax.swing.BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.button2JCheckBox.setMargin(Insets(0, 0, 0, 0))
        self.button2JCheckBox.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.button2JCheckBoxActionPerformed(evt)
))
        self.jLabel4.setText("x:")
        self.mouseXJTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        self.jLabel5.setText("y:")
        self.mouseYJTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        self.inputTypeJLabel.setText("Input Type:")
        self.jLabel6.setText("Delay:")
        self.mouseDelayJTextField.setText("100")
        mouseActionJDialogLayout: GroupLayout = GroupLayout(self.mouseActionJDialog.getContentPane())
        self.mouseActionJDialog.getContentPane().setLayout(mouseActionJDialogLayout)
        mouseActionJDialogLayout.setHorizontalGroup(mouseActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(mouseActionJDialogLayout.createSequentialGroup().addContainerGap().addGroup(mouseActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.inputTypeJLabel).addGroup(javax.swing.GroupLayout.Alignment.TRAILING, mouseActionJDialogLayout.createSequentialGroup().addGroup(mouseActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(javax.swing.GroupLayout.Alignment.TRAILING, mouseActionJDialogLayout.createSequentialGroup().addComponent(self.jLabel2).addGap(25, 25, 25)).addGroup(mouseActionJDialogLayout.createSequentialGroup().addGroup(mouseActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.jLabel3).addComponent(self.jLabel6)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED))).addGroup(mouseActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.mouseDelayJTextField, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, 154, Short.MAX_VALUE).addGroup(mouseActionJDialogLayout.createSequentialGroup().addComponent(self.titleJLabel).addGap(45, 45, 45)).addGroup(javax.swing.GroupLayout.Alignment.TRAILING, mouseActionJDialogLayout.createSequentialGroup().addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.inputAutomationTypeJComboBox, 0, 154, Short.MAX_VALUE)).addGroup(mouseActionJDialogLayout.createSequentialGroup().addComponent(self.button1JCheckBox).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.button2JCheckBox)).addGroup(mouseActionJDialogLayout.createSequentialGroup().addGroup(mouseActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING).addGroup(mouseActionJDialogLayout.createSequentialGroup().addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.okJButton)).addGroup(mouseActionJDialogLayout.createSequentialGroup().addComponent(self.jLabel4).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 5, Short.MAX_VALUE).addComponent(self.mouseXJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 59, javax.swing.GroupLayout.PREFERRED_SIZE))).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel5).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.mouseYJTextField, javax.swing.GroupLayout.DEFAULT_SIZE, 62, Short.MAX_VALUE))))).addContainerGap()))
        mouseActionJDialogLayout.setVerticalGroup(mouseActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(mouseActionJDialogLayout.createSequentialGroup().addComponent(self.titleJLabel).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(mouseActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.inputTypeJLabel).addComponent(self.inputAutomationTypeJComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(mouseActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.jLabel2, javax.swing.GroupLayout.PREFERRED_SIZE, 15, javax.swing.GroupLayout.PREFERRED_SIZE).addGroup(mouseActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.button1JCheckBox).addComponent(self.button2JCheckBox))).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(mouseActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel6).addComponent(self.mouseDelayJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(mouseActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel3).addComponent(self.jLabel4).addComponent(self.jLabel5).addComponent(self.mouseYJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.mouseXJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addComponent(self.okJButton).addContainerGap()))
        self.setMinimumSize(Dimension(100, 0))
        self.mouseActionJButton.setText("Edit")
        self.mouseActionJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.mouseActionJButtonActionPerformed(evt)
))
        self.jLabel1.setText("Mouse:")
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jLabel1).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 36, Short.MAX_VALUE).addComponent(self.mouseActionJButton)))
        layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.mouseActionJButton)))
    

    def button2JCheckBoxActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def okJButtonActionPerformed(self, evt: ActionEvent) -> None:
        try:
            self.update()
            self.getMouseActionJDialog().setVisible(False)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "okButtonActionPerformed", e)
    

    def mouseActionJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.getMouseActionJDialog().setVisible(True)
# from java.awt.event.InputEvent import InputEvent
# from javax.swing import *
from org.allbinary.input.automation.robot.InputRobot import InputRobot
from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory
from org.allbinary.input.automation.robot.TempInputRobotNames import TempInputRobotNames
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
from org.allbinary.string.CommonStrings import CommonStrings


