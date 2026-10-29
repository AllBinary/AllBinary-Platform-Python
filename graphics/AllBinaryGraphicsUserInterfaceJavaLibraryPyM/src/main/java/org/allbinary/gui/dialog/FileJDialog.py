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

from org.allbinary.gui.dialog.JDialog import JDialog


class FileJDialog(JDialog):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.finishedListenerInterface: FileJDialogListenerInterface = None
        self.jFileChooser1: JFileChooser = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 2:
            self._constructor2(*args)
    

    def _constructor0(self) -> None:
        super().__init__()
        self._init_fields()
        self.initComponents()
        self.getJFileChooser1().setMultiSelectionEnabled(True)
    

    def _constructor2(self, parent: Frame, modal: bool) -> None:
        super().__init__(parent, modal)
        self._init_fields()
        self.initComponents()
        self.getJFileChooser1().setMultiSelectionEnabled(True)
    

    def addFinishedListener(self, finishedListenerInterface: FileJDialogListenerInterface) -> None:
        self.finishedListenerInterface = finishedListenerInterface
    

    def initComponents(self) -> None:
        from org.allbinary.gui.dialog.JFileChooser import JFileChooser
        from org.allbinary.gui.dialog.ActionListener import ActionListener
        from org.allbinary.gui.dialog.GroupLayout import GroupLayout
        self.jFileChooser1 = JFileChooser()
        self.setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE)
        self.jFileChooser1.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.jFileChooser1ActionPerformed(evt)
))
        layout: GroupLayout = GroupLayout(self.getContentPane())
        self.getContentPane().setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(org.jdesktop.layout.GroupLayout.TRAILING, layout.createSequentialGroup().addContainerGap(org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).add(self.jFileChooser1, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE).addContainerGap()))
        layout.setVerticalGroup(layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(layout.createSequentialGroup().addContainerGap().add(self.jFileChooser1, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, 357, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE).addContainerGap(org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
        self.pack()
    

    def jFileChooser1ActionPerformed(self, evt: ActionEvent) -> None:
        self.logUtil.putF("Starting Action Command: " + str(evt.getActionCommand()), self, "ActionPerformed")
        files: list[File] = self.getJFileChooser1().getSelectedFiles()
        if evt.getActionCommand() == self.getJFileChooser1().CANCEL_SELECTION:
            self.setVisible(False)
        if evt.getActionCommand() == self.getJFileChooser1().APPROVE_SELECTION:
            if files is not None and len(files) > 0:
                self.finishedListenerInterface.onFiles(files)
    

    @staticmethod
    def main(args: list[str]) -> None:
        from org.allbinary.gui.dialog.JFrame import JFrame
        java.awt.EventQueue.invokeLater((ARunnable()  # Java anonymous class body:
#             
# 
#             def run(self) -> None:
#                 from org.allbinary.gui.dialog.JFrame import JFrame
#                 FileJDialog(JFrame(), True).setVisible(True)
))
    

    def getJFileChooser1(self) -> JFileChooser:
        return self.jFileChooser1
    

    def setJFileChooser1(self, jFileChooser1: JFileChooser) -> None:
        self.jFileChooser1 = jFileChooser1
from org.allbinary.thread.ARunnable import ARunnable
# from java.io.File import File
from org.allbinary.logic.communication.log.LogUtil import LogUtil


