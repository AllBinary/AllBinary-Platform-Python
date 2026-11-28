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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
# from javax.swing.JPanel import JPanel


@java_inherited_overloads
class KeyboardActionScriptInputJPanel(JPanel):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("keyActionScriptInputInterface", None)
        vars(self).setdefault("addKeyJLabel", None)
        vars(self).setdefault("delayBetweenJLabel", None)
        vars(self).setdefault("delayJTextField", None)
        vars(self).setdefault("holdTimeJLabel", None)
        vars(self).setdefault("inputAutomationTypeJComboBox", None)
        vars(self).setdefault("inputTypeJLabel", None)
        vars(self).setdefault("jLabel1", None)
        vars(self).setdefault("jPanel1", None)
        vars(self).setdefault("keyActionJButton", None)
        vars(self).setdefault("keyActionJDialog", None)
        vars(self).setdefault("keyIntegerJComboBox", None)
        vars(self).setdefault("keyNameJComboBox", None)
        vars(self).setdefault("normalJRadioButton", None)
        vars(self).setdefault("okJButton", None)
        vars(self).setdefault("pressJRadioButton", None)
        vars(self).setdefault("releaseJRadioButton", None)
        vars(self).setdefault("sequenceJRadioButton", None)
        vars(self).setdefault("simultaneousJRadioButton", None)
        vars(self).setdefault("testJLabel", None)
        vars(self).setdefault("textJTextField", None)
        vars(self).setdefault("timeJTextField", None)
        vars(self).setdefault("titleJLabel", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "keyActionScriptInputInterface" not in vars(self): self.keyActionScriptInputInterface: KeyboardActionScriptInputInterface = None
        if "addKeyJLabel" not in vars(self): self.addKeyJLabel: JLabel = None
        if "delayBetweenJLabel" not in vars(self): self.delayBetweenJLabel: JLabel = None
        if "delayJTextField" not in vars(self): self.delayJTextField: JTextField = None
        if "holdTimeJLabel" not in vars(self): self.holdTimeJLabel: JLabel = None
        if "inputAutomationTypeJComboBox" not in vars(self): self.inputAutomationTypeJComboBox: JComboBox = None
        if "inputTypeJLabel" not in vars(self): self.inputTypeJLabel: JLabel = None
        if "jLabel1" not in vars(self): self.jLabel1: JLabel = None
        if "jPanel1" not in vars(self): self.jPanel1: JPanel = None
        if "keyActionJButton" not in vars(self): self.keyActionJButton: JButton = None
        if "keyActionJDialog" not in vars(self): self.keyActionJDialog: JDialog = None
        if "keyIntegerJComboBox" not in vars(self): self.keyIntegerJComboBox: JComboBox = None
        if "keyNameJComboBox" not in vars(self): self.keyNameJComboBox: JComboBox = None
        if "normalJRadioButton" not in vars(self): self.normalJRadioButton: JRadioButton = None
        if "okJButton" not in vars(self): self.okJButton: JButton = None
        if "pressJRadioButton" not in vars(self): self.pressJRadioButton: JRadioButton = None
        if "releaseJRadioButton" not in vars(self): self.releaseJRadioButton: JRadioButton = None
        if "sequenceJRadioButton" not in vars(self): self.sequenceJRadioButton: JRadioButton = None
        if "simultaneousJRadioButton" not in vars(self): self.simultaneousJRadioButton: JRadioButton = None
        if "testJLabel" not in vars(self): self.testJLabel: JLabel = None
        if "textJTextField" not in vars(self): self.textJTextField: JTextField = None
        if "timeJTextField" not in vars(self): self.timeJTextField: JTextField = None
        if "titleJLabel" not in vars(self): self.titleJLabel: JLabel = None
    

    def __init__(self, keyActionScriptInputInterface: KeyboardActionScriptInputInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyNameDefaultComboBoxModelFactory import KeyNameDefaultComboBoxModelFactory
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyCharDefaultComboBoxModelFactory import KeyCharDefaultComboBoxModelFactory
        from org.allbinary.input.automation.robot.InputRobot import InputRobot
        from org.allbinary.input.automation.robot.TempInputRobotNames import TempInputRobotNames
        super().__init__()
        __class__._init_fields(self)
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.initComponents()
        self.keyActionScriptInputInterface = keyActionScriptInputInterface
        defaultComboBoxModel: DefaultComboBoxModel = DefaultComboBoxModel()
        defaultComboBoxModel.addElement(TempInputRobotNames.DX_NAME)
        defaultComboBoxModel.addElement(InputRobot.NAME)
        self.inputAutomationTypeJComboBox.setModel(defaultComboBoxModel)
        self.keyNameJComboBox.setModel(KeyNameDefaultComboBoxModelFactory.getInstance())
        self.keyIntegerJComboBox.setModel(KeyCharDefaultComboBoxModelFactory.getInstance())
        if java_predicate(self.keyActionScriptInputInterface, "isNormal"):
            self.normalJRadioButton.setSelected(True)
            self.pressJRadioButton.setSelected(False)
            self.releaseJRadioButton.setSelected(False)
        elif java_predicate(self.keyActionScriptInputInterface, "isPress"):
            self.normalJRadioButton.setSelected(False)
            self.pressJRadioButton.setSelected(True)
            self.releaseJRadioButton.setSelected(False)
        elif java_predicate(self.keyActionScriptInputInterface, "isRelease"):
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
        from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        comboBoxModel: ComboBoxModel = self.inputAutomationTypeJComboBox.getModel()
        selectedItem: str = comboBoxModel.getSelectedItem()
        if not (StringValidationUtil.getInstance().isEmpty(selectedItem)):
            self.keyActionScriptInputInterface.setInputRobotInterface(InputRobotFactory.getInstance().get(selectedItem))
    

    def getSelectedKey(self) -> int:
        from org.allbinary.input.KeySingletonFactory import KeySingletonFactory
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        comboBoxModel: ComboBoxModel = self.keyNameJComboBox.getModel()
        selectedItem: str = comboBoxModel.getSelectedItem()
        if not (StringValidationUtil.getInstance().isEmpty(selectedItem)):
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
        from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
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
        self.titleJLabel.setHorizontalAlignment(SwingConstants.CENTER)
        self.titleJLabel.setText("Keyboard Input Options")
        self.addKeyJLabel.setText("Add Key:")
        _java_listener_owner = self
        class _JavaListenerN69196(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "keyNameJComboBoxActionPerformed") else _java_listener_owner).keyNameJComboBoxActionPerformed(evt)
        self.keyNameJComboBox.addActionListener(_JavaListenerN69196()
            )
        self.timeJTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        self.holdTimeJLabel.setText("Hold Time (ms):")
        self.inputTypeJLabel.setText("Input Type:")
        self.delayJTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        self.delayBetweenJLabel.setText("Delay Between Keys (ms):")
        self.testJLabel.setText("Text:")
        self.textJTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        self.pressJRadioButton.setText("Press")
        self.pressJRadioButton.setBorder(BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.pressJRadioButton.setMargin(Insets(0, 0, 0, 0))
        _java_listener_owner = self
        class _JavaListenerN69723(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "pressJRadioButtonActionPerformed") else _java_listener_owner).pressJRadioButtonActionPerformed(evt)
        self.pressJRadioButton.addActionListener(_JavaListenerN69723()
            )
        self.releaseJRadioButton.setText("Release")
        self.releaseJRadioButton.setBorder(BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.releaseJRadioButton.setMargin(Insets(0, 0, 0, 0))
        _java_listener_owner = self
        class _JavaListenerN69980(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "releaseJRadioButtonActionPerformed") else _java_listener_owner).releaseJRadioButtonActionPerformed(evt)
        self.releaseJRadioButton.addActionListener(_JavaListenerN69980()
            )
        self.normalJRadioButton.setSelected(True)
        self.normalJRadioButton.setText("Normal")
        self.normalJRadioButton.setBorder(BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.normalJRadioButton.setMargin(Insets(0, 0, 0, 0))
        _java_listener_owner = self
        class _JavaListenerN70267(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "normalJRadioButtonActionPerformed") else _java_listener_owner).normalJRadioButtonActionPerformed(evt)
        self.normalJRadioButton.addActionListener(_JavaListenerN70267()
            )
        self.simultaneousJRadioButton.setSelected(True)
        self.simultaneousJRadioButton.setText("Simultaneous")
        self.simultaneousJRadioButton.setBorder(BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.simultaneousJRadioButton.setMargin(Insets(0, 0, 0, 0))
        _java_listener_owner = self
        class _JavaListenerN70554(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "simultaneousJRadioButtonActionPerformed") else _java_listener_owner).simultaneousJRadioButtonActionPerformed(evt)
        self.simultaneousJRadioButton.addActionListener(_JavaListenerN70554()
            )
        self.sequenceJRadioButton.setText("Sequence")
        self.sequenceJRadioButton.setBorder(BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.sequenceJRadioButton.setMargin(Insets(0, 0, 0, 0))
        _java_listener_owner = self
        class _JavaListenerN70811(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "sequenceJRadioButtonActionPerformed") else _java_listener_owner).sequenceJRadioButtonActionPerformed(evt)
        self.sequenceJRadioButton.addActionListener(_JavaListenerN70811()
            )
        self.okJButton.setText("OK")
        self.okJButton.setHorizontalTextPosition(SwingConstants.CENTER)
        _java_listener_owner = self
        class _JavaListenerN70992(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "okJButtonActionPerformed") else _java_listener_owner).okJButtonActionPerformed(evt)
        self.okJButton.addActionListener(_JavaListenerN70992()
            )
        self.jPanel1.add(self.okJButton)
        _java_listener_owner = self
        class _JavaListenerN71138(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "keyIntegerJComboBoxActionPerformed") else _java_listener_owner).keyIntegerJComboBoxActionPerformed(evt)
        self.keyIntegerJComboBox.addActionListener(_JavaListenerN71138()
            )
        keyActionJDialogLayout: GroupLayout = GroupLayout(self.keyActionJDialog.getContentPane())
        self.keyActionJDialog.getContentPane().setLayout(keyActionJDialogLayout)
        keyActionJDialogLayout.setHorizontalGroup(keyActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(keyActionJDialogLayout.createSequentialGroup().addContainerGap().addGroup(keyActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(keyActionJDialogLayout.createSequentialGroup().addGroup(keyActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING, False).addComponent(self.addKeyJLabel, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addComponent(self.inputTypeJLabel, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(keyActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.TRAILING).addComponent(self.inputAutomationTypeJComboBox, 0, 148, Short.MAX_VALUE).addComponent(self.textJTextField, GroupLayout.Alignment.LEADING, GroupLayout.DEFAULT_SIZE, 148, Short.MAX_VALUE).addGroup(keyActionJDialogLayout.createSequentialGroup().addComponent(self.keyNameJComboBox, 0, 101, Short.MAX_VALUE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.keyIntegerJComboBox, GroupLayout.PREFERRED_SIZE, 41, GroupLayout.PREFERRED_SIZE)))).addComponent(self.testJLabel, GroupLayout.PREFERRED_SIZE, 60, GroupLayout.PREFERRED_SIZE).addGroup(keyActionJDialogLayout.createSequentialGroup().addComponent(self.normalJRadioButton).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.pressJRadioButton).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.releaseJRadioButton).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, 48, GroupLayout.PREFERRED_SIZE)).addGroup(GroupLayout.Alignment.TRAILING, keyActionJDialogLayout.createSequentialGroup().addComponent(self.holdTimeJLabel).addGap(22, 22, 22).addComponent(self.timeJTextField, GroupLayout.DEFAULT_SIZE, 113, Short.MAX_VALUE)).addGroup(keyActionJDialogLayout.createSequentialGroup().addComponent(self.delayBetweenJLabel).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, 15, Short.MAX_VALUE).addComponent(self.delayJTextField, GroupLayout.PREFERRED_SIZE, 68, GroupLayout.PREFERRED_SIZE)).addGroup(keyActionJDialogLayout.createSequentialGroup().addComponent(self.simultaneousJRadioButton).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.sequenceJRadioButton))).addContainerGap()).addComponent(self.titleJLabel, GroupLayout.Alignment.TRAILING, GroupLayout.DEFAULT_SIZE, 229, Short.MAX_VALUE).addComponent(self.jPanel1, GroupLayout.DEFAULT_SIZE, 229, Short.MAX_VALUE))
        keyActionJDialogLayout.setVerticalGroup(keyActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(keyActionJDialogLayout.createSequentialGroup().addComponent(self.titleJLabel).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(keyActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.inputTypeJLabel).addComponent(self.inputAutomationTypeJComboBox, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(keyActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.addKeyJLabel).addComponent(self.keyIntegerJComboBox, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addComponent(self.keyNameJComboBox, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(keyActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.testJLabel).addComponent(self.textJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(keyActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.pressJRadioButton).addComponent(self.normalJRadioButton).addComponent(self.releaseJRadioButton)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(keyActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.holdTimeJLabel).addComponent(self.timeJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(keyActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.delayBetweenJLabel).addComponent(self.delayJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(keyActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.simultaneousJRadioButton).addComponent(self.sequenceJRadioButton)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jPanel1, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addContainerGap()))
        self.setMinimumSize(Dimension(100, 0))
        self.keyActionJButton.setText("Edit")
        _java_listener_owner = self
        class _JavaListenerN74410(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "keyActionJButtonActionPerformed") else _java_listener_owner).keyActionJButtonActionPerformed(evt)
        self.keyActionJButton.addActionListener(_JavaListenerN74410()
            )
        self.jLabel1.setText("Key:")
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jLabel1).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, 49, Short.MAX_VALUE).addComponent(self.keyActionJButton)))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.keyActionJButton)))
    

    def prependText(self, integer: int) -> None:
        if integer is not None:
            newKey: str = "&#" + str(integer) + ";"
            self.textJTextField.setText(newKey + str(self.textJTextField.getText()))
    

    def keyIntegerJComboBoxActionPerformed(self, evt: ActionEvent) -> None:
        self.keyIntegerJComboBox.getSelectedIndex()
        self.keyNameJComboBox.setSelectedIndex(self.keyIntegerJComboBox.getSelectedIndex())
    

    def sequenceJRadioButtonActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
        if java_predicate(self.sequenceJRadioButton, "isSelected"):
            self.delayJTextField.setText(CommonPhoneStrings.getInstance().ONE)
            self.simultaneousJRadioButton.setSelected(False)
    

    def simultaneousJRadioButtonActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
        if java_predicate(self.simultaneousJRadioButton, "isSelected"):
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
        if java_predicate(self.normalJRadioButton, "isSelected"):
            self.keyActionScriptInputInterface.setNormal()
            self.pressJRadioButton.setSelected(False)
            self.releaseJRadioButton.setSelected(False)
    

    def releaseJRadioButtonActionPerformed(self, evt: ActionEvent) -> None:
        if java_predicate(self.releaseJRadioButton, "isSelected"):
            self.keyActionScriptInputInterface.setRelease(True)
            self.keyActionScriptInputInterface.setPress(False)
            self.pressJRadioButton.setSelected(False)
            self.normalJRadioButton.setSelected(False)
    

    def pressJRadioButtonActionPerformed(self, evt: ActionEvent) -> None:
        if java_predicate(self.pressJRadioButton, "isSelected"):
            self.keyActionScriptInputInterface.setPress(True)
            self.keyActionScriptInputInterface.setRelease(False)
            self.releaseJRadioButton.setSelected(False)
            self.normalJRadioButton.setSelected(False)
# from javax.swing.DefaultComboBoxModel import DefaultComboBoxModel
# from javax.swing.ComboBoxModel import ComboBoxModel
# from org.allbinary.input.KeySingletonFactory import KeySingletonFactory
# from org.allbinary.input.automation.robot.InputRobot import InputRobot
# from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory
# from org.allbinary.input.automation.robot.TempInputRobotNames import TempInputRobotNames
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
# from org.allbinary.string.CommonStrings import CommonStrings
# from java.awt.Dimension import Dimension
# from java.awt.Insets import Insets
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.BorderFactory import BorderFactory
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JButton import JButton
# from javax.swing.JComboBox import JComboBox
# from javax.swing.JDialog import JDialog
# from javax.swing.JLabel import JLabel
# from javax.swing.JRadioButton import JRadioButton
# from javax.swing.JTextField import JTextField
# from javax.swing.LayoutStyle import LayoutStyle
# from javax.swing.SwingConstants import SwingConstants


