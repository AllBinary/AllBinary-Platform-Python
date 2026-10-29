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
# package org.allbinary.input.automation.module.configuration

from __future__ import annotations

from org.allbinary.input.automation.module.configuration.JPanel import JPanel


class BlankModuleConfigurationJPanel(JPanel):

    def _init_fields(self) -> None:
        self.jLabel1: JLabel = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.initComponents()
    

    def initComponents(self) -> None:
        from org.allbinary.input.automation.module.configuration.JLabel import JLabel
        from org.allbinary.input.automation.module.configuration.GroupLayout import GroupLayout
        self.jLabel1 = JLabel()
        self.jLabel1.setText("No Configuration Available")
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup().addContainerGap(231, Short.MAX_VALUE).addComponent(self.jLabel1).addGap(225, 225, 225)))
        layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addContainerGap().addComponent(self.jLabel1).addContainerGap(362, Short.MAX_VALUE)))


