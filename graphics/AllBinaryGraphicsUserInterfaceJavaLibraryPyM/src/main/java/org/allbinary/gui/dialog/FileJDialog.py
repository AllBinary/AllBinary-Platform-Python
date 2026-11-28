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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
# from javax.swing.JDialog import JDialog


@java_inherited_overloads
class FileJDialog(JDialog):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("finishedListenerInterface", None)
        vars(self).setdefault("jFileChooser1", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "finishedListenerInterface" not in vars(self): self.finishedListenerInterface: FileJDialogListenerInterface = None
        if "jFileChooser1" not in vars(self): self.jFileChooser1: JFileChooser = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 2:
            __class__._constructor2(self, *args)
    

    def _constructor0(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.initComponents()
        self.getJFileChooser1().setMultiSelectionEnabled(True)
    

    def _constructor2(self, parent: Frame, modal: bool) -> None:
        __class__._java_defaults(self)
        super().__init__(parent, modal)
        __class__._init_fields(self)
        self.initComponents()
        self.getJFileChooser1().setMultiSelectionEnabled(True)
    

    def addFinishedListener(self, finishedListenerInterface: FileJDialogListenerInterface) -> None:
        self.finishedListenerInterface = finishedListenerInterface
    

    def initComponents(self) -> None:
        self.jFileChooser1 = JFileChooser()
        self.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)
        _java_listener_owner = self
        class _JavaListenerN66294(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "jFileChooser1ActionPerformed") else _java_listener_owner).jFileChooser1ActionPerformed(evt)
        self.jFileChooser1.addActionListener(_JavaListenerN66294()
            )
        layout: GroupLayout = GroupLayout(self.getContentPane())
        self.getContentPane().setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.TRAILING, layout.createSequentialGroup().addContainerGap(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).add(self.jFileChooser1, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE).addContainerGap()))
        layout.setVerticalGroup(layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(layout.createSequentialGroup().addContainerGap().add(self.jFileChooser1, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE, 357, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE).addContainerGap(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
        self.pack()
    

    def jFileChooser1ActionPerformed(self, evt: ActionEvent) -> None:
        from java.io.File import File
        self.logUtil.putF("Starting Action Command: " + str(evt.getActionCommand()), self, "ActionPerformed")
        files: list[File] = self.getJFileChooser1().getSelectedFiles()
        if evt.getActionCommand() == self.getJFileChooser1().CANCEL_SELECTION:
            self.setVisible(False)
        if evt.getActionCommand() == self.getJFileChooser1().APPROVE_SELECTION:
            if files is not None and len(files) > 0:
                self.finishedListenerInterface.onFiles(files)
    

    @staticmethod
    def main(args: list[str]) -> None:
        from org.allbinary.thread.ARunnable import ARunnable
        class _JavaListenerN67615(ARunnable):
            
            

            def run(self) -> None:
                FileJDialog(JFrame(), True).setVisible(True)
        EventQueue.invokeLater(_JavaListenerN67615()
            )
    

    def getJFileChooser1(self) -> JFileChooser:
        return self.jFileChooser1
    

    def setJFileChooser1(self, jFileChooser1: JFileChooser) -> None:
        self.jFileChooser1 = jFileChooser1
# from org.allbinary.thread.ARunnable import ARunnable
# from java.io.File import File
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from java.awt.EventQueue import EventQueue
# from java.awt.Frame import Frame
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.JFileChooser import JFileChooser
# from javax.swing.JFrame import JFrame
# from javax.swing.WindowConstants import WindowConstants


