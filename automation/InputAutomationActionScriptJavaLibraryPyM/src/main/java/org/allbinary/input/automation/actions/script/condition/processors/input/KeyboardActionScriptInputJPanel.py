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


class KeyboardActionScriptInputJPanel(JPanel):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.keyActionScriptInputInterface: KeyboardActionScriptInputInterface = None
        self.addKeyJLabel: JLabel = None
        self.delayBetweenJLabel: JLabel = None
        self.delayJTextField: JTextField = None
        self.holdTimeJLabel: JLabel = None
        self.inputAutomationTypeJComboBox: JComboBox = None
        self.inputTypeJLabel: JLabel = None
        self.jLabel1: JLabel = None
        self.jPanel1: JPanel = None
        self.keyActionJButton: JButton = None
        self.keyActionJDialog: JDialog = None
        self.keyIntegerJComboBox: JComboBox = None
        self.keyNameJComboBox: JComboBox = None
        self.normalJRadioButton: JRadioButton = None
        self.okJButton: JButton = None
        self.pressJRadioButton: JRadioButton = None
        self.releaseJRadioButton: JRadioButton = None
        self.sequenceJRadioButton: JRadioButton = None
        self.simultaneousJRadioButton: JRadioButton = None
        self.testJLabel: JLabel = None
        self.textJTextField: JTextField = None
        self.timeJTextField: JTextField = None
        self.titleJLabel: JLabel = None
    

    def __init__(self, keyActionScriptInputInterface: KeyboardActionScriptInputInterface) -> None:
        from org.allbinary.input.automation.actions.script.condition.processors.input.DefaultComboBoxModel import DefaultComboBoxModel
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyNameDefaultComboBoxModelFactory import KeyNameDefaultComboBoxModelFactory
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyCharDefaultComboBoxModelFactory import KeyCharDefaultComboBoxModelFactory
        super().__init__()
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.initComponents()
        self.keyActionScriptInputInterface = keyActionScriptInputInterface
        defaultComboBoxModel: DefaultComboBoxModel = DefaultComboBoxModel()
        defaultComboBoxModel.addElement(TempInputRobotNames.DX_NAME)
        defaultComboBoxModel.addElement(InputRobot.NAME)
        self.inputAutomationTypeJComboBox.setModel(defaultComboBoxModel)
        self.keyNameJComboBox.setModel(KeyNameDefaultComboBoxModelFactory.getInstance())
        self.keyIntegerJComboBox.setModel(KeyCharDefaultComboBoxModelFactory.getInstance())
        if self.keyActionScriptInputInterface.isNormal():
            self.normalJRadioButton.setSelected(True)
            self.pressJRadioButton.setSelected(False)
            self.releaseJRadioButton.setSelected(False)
        elif self.keyActionScriptInputInterface.isPress():
            self.normalJRadioButton.setSelected(False)
            self.pressJRadioButton.setSelected(True)
            self.releaseJRadioButton.setSelected(False)
        elif self.keyActionScriptInputInterface.isRelease():
            self.normalJRadioButton.setSelected(False)
            self.pressJRadioButton.setSelected(False)
            self.releaseJRadioButton.setSelected(True)
        self.set()
    

    def set(self) -> None:
        inputTypeComboBoxModel: ComboBoxModel = self.inputAutomationTypeJComboBox.getModel()
        inputTypeComboBoxModel.setSelectedItem(self.keyActionScriptInputInterface.getInputRobotInterface().getName())
        self.textJTextField.setText(self.keyActionScriptInputInterface.getText())
        self.delayJTextField.setText(str(self.keyActionScriptInputInterface.getDelayBetweenKeys()))
        self.timeJTextField.setText(str(self.keyActionScriptInputInterface.getTime()))
        self.keyActionScriptInputInterface.log()
    

    # throws Exception
    def updateInputType(self) -> None:
        comboBoxModel: ComboBoxModel = self.inputAutomationTypeJComboBox.getModel()
        selectedItem: str = comboBoxModel.getSelectedItem()
        if not StringValidationUtil.getInstance().isEmpty(selectedItem):
            self.keyActionScriptInputInterface.setInputRobotInterface(InputRobotFactory.getInstance().get(selectedItem))
    

    def getSelectedKey(self) -> int:
        comboBoxModel: ComboBoxModel = self.keyNameJComboBox.getModel()
        selectedItem: str = comboBoxModel.getSelectedItem()
        if not StringValidationUtil.getInstance().isEmpty(selectedItem):
            return KeySingletonFactory.getHashtable().get(selectedItem)
        return None
    

    def updateKeys(self) -> None:
        text: str = self.textJTextField.getText()
        self.keyActionScriptInputInterface.setText(text)
    

    # throws Exception
    def update(self) -> None:
        self.updateInputType()
        self.updateKeys()
        self.keyActionScriptInputInterface.setTime(int(str(self.timeJTextField.getText())))
        self.keyActionScriptInputInterface.log()
    

    def getKeyActionJDialog(self) -> JDialog:
        return self.keyActionJDialog
    

    def setKeyActionJDialog(self, keyActionJDialog: JDialog) -> None:
        self.keyActionJDialog = keyActionJDialog
    

    def initComponents(self) -> None:
        from org.allbinary.input.automation.actions.script.condition.processors.input.JDialog import JDialog
        from org.allbinary.input.automation.actions.script.condition.processors.input.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.processors.input.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.processors.input.JComboBox import JComboBox
        from org.allbinary.input.automation.actions.script.condition.processors.input.JTextField import JTextField
        from org.allbinary.input.automation.actions.script.condition.processors.input.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.processors.input.JComboBox import JComboBox
        from org.allbinary.input.automation.actions.script.condition.processors.input.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.processors.input.JTextField import JTextField
        from org.allbinary.input.automation.actions.script.condition.processors.input.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.processors.input.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.processors.input.JTextField import JTextField
        from org.allbinary.input.automation.actions.script.condition.processors.input.JRadioButton import JRadioButton
        from org.allbinary.input.automation.actions.script.condition.processors.input.JRadioButton import JRadioButton
        from org.allbinary.input.automation.actions.script.condition.processors.input.JRadioButton import JRadioButton
        from org.allbinary.input.automation.actions.script.condition.processors.input.JRadioButton import JRadioButton
        from org.allbinary.input.automation.actions.script.condition.processors.input.JRadioButton import JRadioButton
        from org.allbinary.input.automation.actions.script.condition.processors.input.JPanel import JPanel
        from org.allbinary.input.automation.actions.script.condition.processors.input.JButton import JButton
        from org.allbinary.input.automation.actions.script.condition.processors.input.JComboBox import JComboBox
        from org.allbinary.input.automation.actions.script.condition.processors.input.JButton import JButton
        from org.allbinary.input.automation.actions.script.condition.processors.input.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.processors.input.Dimension import Dimension
        from org.allbinary.input.automation.actions.script.condition.processors.input.ActionListener import ActionListener
        from org.allbinary.input.automation.actions.script.condition.processors.input.Insets import Insets
        from org.allbinary.input.automation.actions.script.condition.processors.input.ActionListener import ActionListener
        from org.allbinary.input.automation.actions.script.condition.processors.input.Insets import Insets
        from org.allbinary.input.automation.actions.script.condition.processors.input.ActionListener import ActionListener
        from org.allbinary.input.automation.actions.script.condition.processors.input.Insets import Insets
        from org.allbinary.input.automation.actions.script.condition.processors.input.ActionListener import ActionListener
        from org.allbinary.input.automation.actions.script.condition.processors.input.Insets import Insets
        from org.allbinary.input.automation.actions.script.condition.processors.input.ActionListener import ActionListener
        from org.allbinary.input.automation.actions.script.condition.processors.input.Insets import Insets
        from org.allbinary.input.automation.actions.script.condition.processors.input.ActionListener import ActionListener
        from org.allbinary.input.automation.actions.script.condition.processors.input.ActionListener import ActionListener
        from org.allbinary.input.automation.actions.script.condition.processors.input.ActionListener import ActionListener
        from org.allbinary.input.automation.actions.script.condition.processors.input.GroupLayout import GroupLayout
        from org.allbinary.input.automation.actions.script.condition.processors.input.Dimension import Dimension
        from org.allbinary.input.automation.actions.script.condition.processors.input.ActionListener import ActionListener
        from org.allbinary.input.automation.actions.script.condition.processors.input.GroupLayout import GroupLayout
        self.keyActionJDialog = JDialog()
        self.titleJLabel = JLabel()
        self.addKeyJLabel = JLabel()
        self.keyNameJComboBox = JComboBox()
        self.timeJTextField = JTextField()
        self.holdTimeJLabel = JLabel()
        self.inputAutomationTypeJComboBox = JComboBox()
        self.inputTypeJLabel = JLabel()
        self.delayJTextField = JTextField()
        self.delayBetweenJLabel = JLabel()
        self.testJLabel = JLabel()
        self.textJTextField = JTextField()
        self.pressJRadioButton = JRadioButton()
        self.releaseJRadioButton = JRadioButton()
        self.normalJRadioButton = JRadioButton()
        self.simultaneousJRadioButton = JRadioButton()
        self.sequenceJRadioButton = JRadioButton()
        self.jPanel1 = JPanel()
        self.okJButton = JButton()
        self.keyIntegerJComboBox = JComboBox()
        self.keyActionJButton = JButton()
        self.jLabel1 = JLabel()
        self.keyActionJDialog.setMinimumSize(Dimension(255, 280))
        self.titleJLabel.setHorizontalAlignment(javax.swing.SwingConstants.CENTER)
        self.titleJLabel.setText("Keyboard Input Options")
        self.addKeyJLabel.setText("Add Key:")
        self.keyNameJComboBox.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.keyNameJComboBoxActionPerformed(evt)
))
        self.timeJTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        self.holdTimeJLabel.setText("Hold Time (ms):")
        self.inputTypeJLabel.setText("Input Type:")
        self.delayJTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        self.delayBetweenJLabel.setText("Delay Between Keys (ms):")
        self.testJLabel.setText("Text:")
        self.textJTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        self.pressJRadioButton.setText("Press")
        self.pressJRadioButton.setBorder(javax.swing.BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.pressJRadioButton.setMargin(Insets(0, 0, 0, 0))
        self.pressJRadioButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.pressJRadioButtonActionPerformed(evt)
))
        self.releaseJRadioButton.setText("Release")
        self.releaseJRadioButton.setBorder(javax.swing.BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.releaseJRadioButton.setMargin(Insets(0, 0, 0, 0))
        self.releaseJRadioButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.releaseJRadioButtonActionPerformed(evt)
))
        self.normalJRadioButton.setSelected(True)
        self.normalJRadioButton.setText("Normal")
        self.normalJRadioButton.setBorder(javax.swing.BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.normalJRadioButton.setMargin(Insets(0, 0, 0, 0))
        self.normalJRadioButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.normalJRadioButtonActionPerformed(evt)
))
        self.simultaneousJRadioButton.setSelected(True)
        self.simultaneousJRadioButton.setText("Simultaneous")
        self.simultaneousJRadioButton.setBorder(javax.swing.BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.simultaneousJRadioButton.setMargin(Insets(0, 0, 0, 0))
        self.simultaneousJRadioButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.simultaneousJRadioButtonActionPerformed(evt)
))
        self.sequenceJRadioButton.setText("Sequence")
        self.sequenceJRadioButton.setBorder(javax.swing.BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.sequenceJRadioButton.setMargin(Insets(0, 0, 0, 0))
        self.sequenceJRadioButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.sequenceJRadioButtonActionPerformed(evt)
))
        self.okJButton.setText("OK")
        self.okJButton.setHorizontalTextPosition(javax.swing.SwingConstants.CENTER)
        self.okJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.okJButtonActionPerformed(evt)
))
        self.jPanel1.add(self.okJButton)
        self.keyIntegerJComboBox.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.keyIntegerJComboBoxActionPerformed(evt)
))
        keyActionJDialogLayout: GroupLayout = GroupLayout(self.keyActionJDialog.getContentPane())
        self.keyActionJDialog.getContentPane().setLayout(keyActionJDialogLayout)
        keyActionJDialogLayout.setHorizontalGroup(keyActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(keyActionJDialogLayout.createSequentialGroup().addContainerGap().addGroup(keyActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(keyActionJDialogLayout.createSequentialGroup().addGroup(keyActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, False).addComponent(self.addKeyJLabel, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addComponent(self.inputTypeJLabel, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(keyActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING).addComponent(self.inputAutomationTypeJComboBox, 0, 148, Short.MAX_VALUE).addComponent(self.textJTextField, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, 148, Short.MAX_VALUE).addGroup(keyActionJDialogLayout.createSequentialGroup().addComponent(self.keyNameJComboBox, 0, 101, Short.MAX_VALUE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.keyIntegerJComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, 41, javax.swing.GroupLayout.PREFERRED_SIZE)))).addComponent(self.testJLabel, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE).addGroup(keyActionJDialogLayout.createSequentialGroup().addComponent(self.normalJRadioButton).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.pressJRadioButton).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.releaseJRadioButton).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 48, javax.swing.GroupLayout.PREFERRED_SIZE)).addGroup(javax.swing.GroupLayout.Alignment.TRAILING, keyActionJDialogLayout.createSequentialGroup().addComponent(self.holdTimeJLabel).addGap(22, 22, 22).addComponent(self.timeJTextField, javax.swing.GroupLayout.DEFAULT_SIZE, 113, Short.MAX_VALUE)).addGroup(keyActionJDialogLayout.createSequentialGroup().addComponent(self.delayBetweenJLabel).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 15, Short.MAX_VALUE).addComponent(self.delayJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 68, javax.swing.GroupLayout.PREFERRED_SIZE)).addGroup(keyActionJDialogLayout.createSequentialGroup().addComponent(self.simultaneousJRadioButton).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.sequenceJRadioButton))).addContainerGap()).addComponent(self.titleJLabel, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, 229, Short.MAX_VALUE).addComponent(self.jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, 229, Short.MAX_VALUE))
        keyActionJDialogLayout.setVerticalGroup(keyActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(keyActionJDialogLayout.createSequentialGroup().addComponent(self.titleJLabel).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(keyActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.inputTypeJLabel).addComponent(self.inputAutomationTypeJComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(keyActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.addKeyJLabel).addComponent(self.keyIntegerJComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.keyNameJComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(keyActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.testJLabel).addComponent(self.textJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(keyActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.pressJRadioButton).addComponent(self.normalJRadioButton).addComponent(self.releaseJRadioButton)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(keyActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.holdTimeJLabel).addComponent(self.timeJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(keyActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.delayBetweenJLabel).addComponent(self.delayJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(keyActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.simultaneousJRadioButton).addComponent(self.sequenceJRadioButton)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addContainerGap()))
        self.setMinimumSize(Dimension(100, 0))
        self.keyActionJButton.setText("Edit")
        self.keyActionJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.keyActionJButtonActionPerformed(evt)
))
        self.jLabel1.setText("Key:")
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jLabel1).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 49, Short.MAX_VALUE).addComponent(self.keyActionJButton)))
        layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.keyActionJButton)))
    

    def prependText(self, integer: int) -> None:
        if integer is not None:
            newKey: str = "&#" + str(integer) + ";"
            self.textJTextField.setText(newKey + str(self.textJTextField.getText()))
    

    def keyIntegerJComboBoxActionPerformed(self, evt: ActionEvent) -> None:
        self.keyIntegerJComboBox.getSelectedIndex()
        self.keyNameJComboBox.setSelectedIndex(self.keyIntegerJComboBox.getSelectedIndex())
    

    def sequenceJRadioButtonActionPerformed(self, evt: ActionEvent) -> None:
        if self.sequenceJRadioButton.isSelected():
            self.delayJTextField.setText(CommonPhoneStrings.getInstance().ONE)
            self.simultaneousJRadioButton.setSelected(False)
    

    def simultaneousJRadioButtonActionPerformed(self, evt: ActionEvent) -> None:
        if self.simultaneousJRadioButton.isSelected():
            self.delayJTextField.setText(CommonPhoneStrings.getInstance().ZERO)
            self.sequenceJRadioButton.setSelected(False)
    

    def keyNameJComboBoxActionPerformed(self, evt: ActionEvent) -> None:
        integer: int = self.getSelectedKey()
        self.prependText(integer)
        self.keyIntegerJComboBox.setSelectedIndex(self.keyNameJComboBox.getSelectedIndex())
    

    def okJButtonActionPerformed(self, evt: ActionEvent) -> None:
        try:
            self.update()
            self.getKeyActionJDialog().setVisible(False)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "okButtonActionPerformed", e)
    

    def keyActionJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.getKeyActionJDialog().setVisible(True)
    

    def normalJRadioButtonActionPerformed(self, evt: ActionEvent) -> None:
        if self.normalJRadioButton.isSelected():
            self.keyActionScriptInputInterface.setNormal()
            self.pressJRadioButton.setSelected(False)
            self.releaseJRadioButton.setSelected(False)
    

    def releaseJRadioButtonActionPerformed(self, evt: ActionEvent) -> None:
        if self.releaseJRadioButton.isSelected():
            self.keyActionScriptInputInterface.setRelease(True)
            self.keyActionScriptInputInterface.setPress(False)
            self.pressJRadioButton.setSelected(False)
            self.normalJRadioButton.setSelected(False)
    

    def pressJRadioButtonActionPerformed(self, evt: ActionEvent) -> None:
        if self.pressJRadioButton.isSelected():
            self.keyActionScriptInputInterface.setPress(True)
            self.keyActionScriptInputInterface.setRelease(False)
            self.releaseJRadioButton.setSelected(False)
            self.normalJRadioButton.setSelected(False)
# from javax.swing import *
from org.allbinary.input.KeySingletonFactory import KeySingletonFactory
from org.allbinary.input.automation.robot.InputRobot import InputRobot
from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory
from org.allbinary.input.automation.robot.TempInputRobotNames import TempInputRobotNames
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
from org.allbinary.string.CommonStrings import CommonStrings


