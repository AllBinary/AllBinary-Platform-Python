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
# package org.allbinary.graphics.j2me.dialog

from __future__ import annotations

import sys
from org.allbinary.graphics.j2me.dialog.JDialog import JDialog


class RotateJDialog(JDialog):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.hashMap: dict = StdUtil.getInstance().createHashMap()
        self.angleIncrementJTextField: JTextField = None
        self.jButton1: JButton = None
        self.jLabel1: JLabel = None
        self.jLabel2: JLabel = None
        self.jPanel1: JPanel = None
        self.totalRotationJTextField: JTextField = None
    

    def __init__(self, parent: Frame, modal: bool) -> None:
        super().__init__(parent, modal)
        self._init_fields()
        self.initComponents()
    

    def initComponents(self) -> None:
        from org.allbinary.graphics.j2me.dialog.JTextField import JTextField
        from org.allbinary.graphics.j2me.dialog.JLabel import JLabel
        from org.allbinary.graphics.j2me.dialog.JTextField import JTextField
        from org.allbinary.graphics.j2me.dialog.JLabel import JLabel
        from org.allbinary.graphics.j2me.dialog.JPanel import JPanel
        from org.allbinary.graphics.j2me.dialog.JButton import JButton
        from org.allbinary.graphics.j2me.dialog.ActionListener import ActionListener
        from org.allbinary.graphics.j2me.dialog.GroupLayout import GroupLayout
        from org.allbinary.graphics.j2me.dialog.GroupLayout import GroupLayout
        self.angleIncrementJTextField = JTextField()
        self.jLabel1 = JLabel()
        self.totalRotationJTextField = JTextField()
        self.jLabel2 = JLabel()
        self.jPanel1 = JPanel()
        self.jButton1 = JButton()
        self.setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE)
        self.angleIncrementJTextField.setText("36")
        self.jLabel1.setText("Angle Increment:")
        self.totalRotationJTextField.setText("360")
        self.jLabel2.setText("Total Angular Rotation:")
        self.jButton1.setText("OK")
        self.jButton1.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.jButton1ActionPerformed(evt)
))
        jPanel1Layout: GroupLayout = GroupLayout(self.jPanel1)
        self.jPanel1.setLayout(jPanel1Layout)
        jPanel1Layout.setHorizontalGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(jPanel1Layout.createSequentialGroup().addGap(62, 62, 62).addComponent(self.jButton1).addContainerGap(62, Short.MAX_VALUE)))
        jPanel1Layout.setVerticalGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.jButton1))
        layout: GroupLayout = GroupLayout(self.getContentPane())
        self.getContentPane().setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addContainerGap().addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING).addComponent(self.jLabel1).addComponent(self.jLabel2)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.totalRotationJTextField, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, 31, Short.MAX_VALUE).addComponent(self.angleIncrementJTextField, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 31, javax.swing.GroupLayout.PREFERRED_SIZE)).addContainerGap()).addComponent(self.jPanel1, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addContainerGap().addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.angleIncrementJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel1)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.totalRotationJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel2)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 16, Short.MAX_VALUE).addComponent(self.jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addContainerGap()))
        self.pack()
    

    def jButton1ActionPerformed(self, evt: ActionEvent) -> None:
        try:
            self.hashMap.put(str(0), str(self.angleIncrementJTextField.getText()))
            self.hashMap.put(str(1), str(self.totalRotationJTextField.getText()))
            (self.getParent()).onHashMap(self.hashMap)
            self.setVisible(False)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.EXCEPTION, self, "jButton1ActionPerformed")
    

    @staticmethod
    def main(args: list[str]) -> None:
        from org.allbinary.graphics.j2me.dialog.JFrame import JFrame
        from org.allbinary.graphics.j2me.dialog.WindowAdapter import WindowAdapter
        java.awt.EventQueue.invokeLater((ARunnable()  # Java anonymous class body:
#             
# 
#             def run(self) -> None:
#                 from org.allbinary.graphics.j2me.dialog.JFrame import JFrame
#                 from org.allbinary.graphics.j2me.dialog.WindowAdapter import WindowAdapter
#                 dialog: RotateJDialog = RotateJDialog(JFrame(), True)
#                 dialog.addWindowListener((WindowAdapter()  # Java anonymous class body:
# #                     
# # 
# #                     def windowClosing(self, e: WindowEvent) -> None:
# #                         sys.exit(0)
# ))
#                 dialog.setVisible(True)
))
from org.allbinary.thread.ARunnable import ARunnable
# from java.util.HashMap import HashMap
from org.allbinary.gui.dialog.HashMapJDialogListenerInterface import HashMapJDialogListenerInterface
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


