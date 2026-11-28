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
# from javax.swing.JPanel import JPanel


@java_inherited_overloads
class InputAutomationTypeJPanel(JPanel):
    def _java_defaults(self):
        vars(self).setdefault("inputAutomationTypeJComboBox", None)
        vars(self).setdefault("jLabel1", None)

    def _init_fields(self) -> None:
        if "inputAutomationTypeJComboBox" not in vars(self): self.inputAutomationTypeJComboBox: JComboBox = None
        if "jLabel1" not in vars(self): self.jLabel1: JLabel = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.initComponents()
    

    def getInputAutomationTypeJComboBox(self) -> JComboBox:
        return self.inputAutomationTypeJComboBox
    

    def setInputAutomationTypeJComboBox(self, inputAutomationTypeJComboBox: JComboBox) -> None:
        self.inputAutomationTypeJComboBox = inputAutomationTypeJComboBox
    

    def initComponents(self) -> None:
        self.inputAutomationTypeJComboBox = JComboBox()
        self.jLabel1 = JLabel()
        self.inputAutomationTypeJComboBox.setModel(DefaultComboBoxModel(["DirectX", "DirectX 8", "Low Level", "Java Robot"]))
        self.jLabel1.setText("Input Type:")
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jLabel1).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.inputAutomationTypeJComboBox, 0, 98, Short.MAX_VALUE)))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.inputAutomationTypeJComboBox, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)))
# from javax.swing.DefaultComboBoxModel import DefaultComboBoxModel
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JComboBox import JComboBox
# from javax.swing.JLabel import JLabel
# from javax.swing.LayoutStyle import LayoutStyle


