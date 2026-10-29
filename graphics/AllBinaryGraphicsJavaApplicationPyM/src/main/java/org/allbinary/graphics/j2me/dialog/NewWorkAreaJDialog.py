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

from org.allbinary.graphics.j2me.dialog.JDialog import JDialog


class NewWorkAreaJDialog(JDialog):

    def _init_fields(self) -> None:
        self.parent: MyFrame = None
        self.dimension: Dimension = None
        self.xSizeJTextField: JTextField = None
        self.ySizeJTextField: JTextField = None
        self.nameJTextField: JTextField = None
    

    def __init__(self, parent: MyFrame, modal: bool, dimension: Dimension, newName: str) -> None:
        from org.allbinary.graphics.j2me.dialog.JTextField import JTextField
        from org.allbinary.graphics.j2me.dialog.JTextField import JTextField
        from org.allbinary.graphics.j2me.dialog.JTextField import JTextField
        from org.allbinary.graphics.j2me.dialog.JButton import JButton
        from org.allbinary.graphics.j2me.dialog.GridLayout import GridLayout
        from org.allbinary.graphics.j2me.dialog.JLabel import JLabel
        from org.allbinary.graphics.j2me.dialog.JLabel import JLabel
        from org.allbinary.graphics.j2me.dialog.JLabel import JLabel
        from org.allbinary.graphics.j2me.dialog.JLabel import JLabel
        from org.allbinary.graphics.j2me.dialog.JLabel import JLabel
        super().__init__(parent, modal)
        self._init_fields()
        try:
            self.initComponents()
            self.parent = parent
            self.xSizeJTextField = JTextField("12")
            self.ySizeJTextField = JTextField("12")
            self.nameJTextField = JTextField(newName)
            self.dimension = dimension
            submitButton: JButton = JButton("Ok")
            submitButton.addActionListener((ActionListener()  # Java anonymous class body:
#                 
# 
#                 def actionPerformed(self, evt: ActionEvent) -> None:
#                     try:
#                         self.disposeNewDialog()
#                     except Exception as e:
#                         pass
))
            self.setSize(150, 100)
            self.getContentPane().setLayout(GridLayout(5, 2))
            self.getContentPane().add(JLabel("Please enter"))
            self.getContentPane().add(JLabel(" the size."))
            self.getContentPane().add(JLabel("Name:"))
            self.getContentPane().add(self.nameJTextField)
            self.getContentPane().add(JLabel("X: "))
            self.getContentPane().add(self.xSizeJTextField)
            self.getContentPane().add(JLabel("Y: "))
            self.getContentPane().add(self.ySizeJTextField)
            self.getContentPane().add(submitButton)
            self.show()
        except Exception as e:
            raise e
    

    # throws Exception
    def disposeNewDialog(self) -> None:
        from org.allbinary.graphics.j2me.dialog.GridLayout import GridLayout
        try:
            canvasWidth: int = int(self.xSizeJTextField.getText())
            canvasHeight: int = int(self.ySizeJTextField.getText())
            newName: str = self.nameJTextField.getText()
            if newName is None:
                raise GraphicsException("No Name", self, "disposeNewDialog")
            workAreaJPanel: WorkAreaJPanel = WorkAreaJPanel(newName, self.dimension, int(canvasWidth), int(canvasHeight))
            workAreaJPanel.setLayout(GridLayout(1, 1))
            self.parent.add(workAreaJPanel)
            self.dispose()
        except Exception as e:
            raise e
    

    def initComponents(self) -> None:
        from org.allbinary.graphics.j2me.dialog.WindowAdapter import WindowAdapter
        self.addWindowListener((WindowAdapter()  # Java anonymous class body:
#             
# 
#             def windowClosing(self, evt: WindowEvent) -> None:
#                 self.closeDialog(evt)
))
        self.pack()
    

    def closeDialog(self, evt: WindowEvent) -> None:
        self.setVisible(False)
        self.dispose()
    

    @staticmethod
    def main(args: list[str]) -> None:
        from org.allbinary.graphics.j2me.dialog.Dimension import Dimension
        try:
            NewWorkAreaJDialog(MyFrame(), True, Dimension(100, 100), "testing").show()
        except Exception as e:
            pass
# from java.awt import *
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing import *
from org.allbinary.graphics.j2me.GraphicsException import GraphicsException
from org.allbinary.graphics.j2me.MyFrame import MyFrame
from org.allbinary.graphics.j2me.workarea.WorkAreaJPanel import WorkAreaJPanel
from org.allbinary.graphics.j2me.workarea.WorkAreaJPanelInterface import WorkAreaJPanelInterface


