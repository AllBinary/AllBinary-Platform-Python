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
# package org.allbinary.gui.dialog

from __future__ import annotations

# from javax.swing.JDialog import JDialog


class BasicTextJDialog(JDialog):

    def _init_fields(self) -> None:
        self.closeListenerInterface: CloseJDialogListenerInterface = None
        self.jButton1: JButton = None
        self.textJLabel: JLabel = None

    def __init__(self, *args) -> None:
        if len(args) == 3:
            self._constructor3(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor3(self, parent: Frame, modal: bool, text: str) -> None:
        super().__init__(parent, modal)
        self._init_fields()
        self.initComponents()
        self.setText(text)
    

    def setText(self, text: str) -> None:
        self.textJLabel.setText(text)
    

    def addCloseListener(self, closeListenerInterface: CloseJDialogListenerInterface) -> None:
        self.closeListenerInterface = closeListenerInterface
    

    def _constructor1(self, text: str) -> None:
        super().__init__()
        self._init_fields()
        self.initComponents()
        self.textJLabel.setText(text)
    

    def initComponents(self) -> None:
        self.jButton1 = JButton()
        self.textJLabel = JLabel()
        self.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)
        self.jButton1.setText("OK")
        self.jButton1.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.jButton1ActionPerformed(evt)
))
        self.textJLabel.setText("No Text Set")
        layout: GroupLayout = GroupLayout(self.getContentPane())
        self.getContentPane().setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addGap(80, 80, 80).addComponent(self.jButton1)).addGroup(layout.createSequentialGroup().addContainerGap().addComponent(self.textJLabel, GroupLayout.DEFAULT_SIZE, 184, Short.MAX_VALUE))).addContainerGap()))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addGap(20, 20, 20).addComponent(self.textJLabel, GroupLayout.PREFERRED_SIZE, 20, GroupLayout.PREFERRED_SIZE).addGap(30, 30, 30).addComponent(self.jButton1)))
        self.pack()
    

    def jButton1ActionPerformed(self, evt: ActionEvent) -> None:
        self.setVisible(False)
        if self.closeListenerInterface is not None:
            self.closeListenerInterface.onClose()
    

    @staticmethod
    def main(args: list[str]) -> None:
        from org.allbinary.thread.ARunnable import ARunnable
        EventQueue.invokeLater((ARunnable()  # Java anonymous class body:
#             
# 
#             def run(self) -> None:
#                 BasicTextJDialog(JFrame(), True, "Test").setVisible(True)
))
# from org.allbinary.thread.ARunnable import ARunnable
# from java.awt.EventQueue import EventQueue
# from java.awt.Frame import Frame
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JButton import JButton
# from javax.swing.JFrame import JFrame
# from javax.swing.JLabel import JLabel
# from javax.swing.WindowConstants import WindowConstants


