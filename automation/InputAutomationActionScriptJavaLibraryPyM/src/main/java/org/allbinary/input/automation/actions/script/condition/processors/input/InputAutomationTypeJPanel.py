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


class InputAutomationTypeJPanel(JPanel):

    def _init_fields(self) -> None:
        self.inputAutomationTypeJComboBox: JComboBox = None
        self.jLabel1: JLabel = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.initComponents()
    

    def getInputAutomationTypeJComboBox(self) -> JComboBox:
        return self.inputAutomationTypeJComboBox
    

    def setInputAutomationTypeJComboBox(self, inputAutomationTypeJComboBox: JComboBox) -> None:
        self.inputAutomationTypeJComboBox = inputAutomationTypeJComboBox
    

    def initComponents(self) -> None:
        from org.allbinary.input.automation.actions.script.condition.processors.input.JComboBox import JComboBox
        from org.allbinary.input.automation.actions.script.condition.processors.input.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.processors.input.DefaultComboBoxModel import DefaultComboBoxModel
        from org.allbinary.input.automation.actions.script.condition.processors.input.GroupLayout import GroupLayout
        self.inputAutomationTypeJComboBox = JComboBox()
        self.jLabel1 = JLabel()
        self.inputAutomationTypeJComboBox.setModel(DefaultComboBoxModel(["DirectX", "DirectX 8", "Low Level", "Java Robot"]))
        self.jLabel1.setText("Input Type:")
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jLabel1).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.inputAutomationTypeJComboBox, 0, 98, Short.MAX_VALUE)))
        layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.inputAutomationTypeJComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))


