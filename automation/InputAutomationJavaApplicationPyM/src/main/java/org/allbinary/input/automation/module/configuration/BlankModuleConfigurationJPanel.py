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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
# from javax.swing.JPanel import JPanel


@java_inherited_overloads
class BlankModuleConfigurationJPanel(JPanel):
    def _java_defaults(self):
        vars(self).setdefault("jLabel1", None)

    def _init_fields(self) -> None:
        if "jLabel1" not in vars(self): self.jLabel1: JLabel = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.initComponents()
    

    def initComponents(self) -> None:
        self.jLabel1 = JLabel()
        self.jLabel1.setText("No Configuration Available")
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(GroupLayout.Alignment.TRAILING, layout.createSequentialGroup().addContainerGap(231, Short.MAX_VALUE).addComponent(self.jLabel1).addGap(225, 225, 225)))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addContainerGap().addComponent(self.jLabel1).addContainerGap(362, Short.MAX_VALUE)))
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JLabel import JLabel


