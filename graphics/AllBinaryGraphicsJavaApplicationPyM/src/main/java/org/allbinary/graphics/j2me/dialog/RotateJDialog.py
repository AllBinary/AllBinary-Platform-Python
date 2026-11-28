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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
import sys
# from javax.swing.JDialog import JDialog


@java_inherited_overloads
class RotateJDialog(JDialog):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("hashMap", None)
        vars(self).setdefault("angleIncrementJTextField", None)
        vars(self).setdefault("jButton1", None)
        vars(self).setdefault("jLabel1", None)
        vars(self).setdefault("jLabel2", None)
        vars(self).setdefault("jPanel1", None)
        vars(self).setdefault("totalRotationJTextField", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.hashMap: HashMap = StdUtil.getInstance().createHashMap()
        if "angleIncrementJTextField" not in vars(self): self.angleIncrementJTextField: JTextField = None
        if "jButton1" not in vars(self): self.jButton1: JButton = None
        if "jLabel1" not in vars(self): self.jLabel1: JLabel = None
        if "jLabel2" not in vars(self): self.jLabel2: JLabel = None
        if "jPanel1" not in vars(self): self.jPanel1: JPanel = None
        if "totalRotationJTextField" not in vars(self): self.totalRotationJTextField: JTextField = None
    

    def __init__(self, parent: Frame, modal: bool) -> None:
        __class__._java_defaults(self)
        super().__init__(parent, modal)
        __class__._init_fields(self)
        self.initComponents()
    

    def initComponents(self) -> None:
        self.angleIncrementJTextField = JTextField()
        self.jLabel1 = JLabel()
        self.totalRotationJTextField = JTextField()
        self.jLabel2 = JLabel()
        self.jPanel1 = JPanel()
        self.jButton1 = JButton()
        self.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)
        self.angleIncrementJTextField.setText("36")
        self.jLabel1.setText("Angle Increment:")
        self.totalRotationJTextField.setText("360")
        self.jLabel2.setText("Total Angular Rotation:")
        self.jButton1.setText("OK")
        _java_listener_owner = self
        class _JavaListenerN66686(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "jButton1ActionPerformed") else _java_listener_owner).jButton1ActionPerformed(evt)
        self.jButton1.addActionListener(_JavaListenerN66686()
            )
        jPanel1Layout: GroupLayout = GroupLayout(self.jPanel1)
        self.jPanel1.setLayout(jPanel1Layout)
        jPanel1Layout.setHorizontalGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(jPanel1Layout.createSequentialGroup().addGap(62, 62, 62).addComponent(self.jButton1).addContainerGap(62, Short.MAX_VALUE)))
        jPanel1Layout.setVerticalGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.jButton1))
        layout: GroupLayout = GroupLayout(self.getContentPane())
        self.getContentPane().setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addContainerGap().addGroup(layout.createParallelGroup(GroupLayout.Alignment.TRAILING).addComponent(self.jLabel1).addComponent(self.jLabel2)).addPreferredGap(LayoutStyle.ComponentPlacement.UNRELATED).addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.totalRotationJTextField, GroupLayout.Alignment.TRAILING, GroupLayout.DEFAULT_SIZE, 31, Short.MAX_VALUE).addComponent(self.angleIncrementJTextField, GroupLayout.Alignment.TRAILING, GroupLayout.PREFERRED_SIZE, 31, GroupLayout.PREFERRED_SIZE)).addContainerGap()).addComponent(self.jPanel1, GroupLayout.Alignment.TRAILING, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addContainerGap().addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.angleIncrementJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel1)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.totalRotationJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel2)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, 16, Short.MAX_VALUE).addComponent(self.jPanel1, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addContainerGap()))
        self.pack()
    

    def jButton1ActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.gui.dialog.HashMapJDialogListenerInterface import HashMapJDialogListenerInterface
        from org.allbinary.string.CommonStrings import CommonStrings
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
        from org.allbinary.thread.ARunnable import ARunnable
        class _JavaListenerN68780(ARunnable):
            
            

            def run(self) -> None:
                dialog: RotateJDialog = RotateJDialog(JFrame(), True)
                class _JavaListenerN68879(WindowAdapter):
            
                    

                    def windowClosing(self, e: WindowEvent) -> None:
                        __import__("java.lang.System", fromlist=["System"]).System.exit(0)
                dialog.addWindowListener(_JavaListenerN68879()
            )
                dialog.setVisible(True)
        EventQueue.invokeLater(_JavaListenerN68780()
            )
# from org.allbinary.thread.ARunnable import ARunnable
# from java.util.HashMap import HashMap
# from org.allbinary.gui.dialog.HashMapJDialogListenerInterface import HashMapJDialogListenerInterface
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from java.awt.EventQueue import EventQueue
# from java.awt.Frame import Frame
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from java.awt.event.WindowAdapter import WindowAdapter
# from java.awt.event.WindowEvent import WindowEvent
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JButton import JButton
# from javax.swing.JFrame import JFrame
# from javax.swing.JLabel import JLabel
# from javax.swing.JPanel import JPanel
# from javax.swing.JTextField import JTextField
# from javax.swing.LayoutStyle import LayoutStyle
# from javax.swing.WindowConstants import WindowConstants


