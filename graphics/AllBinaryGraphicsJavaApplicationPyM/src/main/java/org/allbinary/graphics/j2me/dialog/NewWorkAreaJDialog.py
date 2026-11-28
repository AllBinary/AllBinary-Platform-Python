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
# from javax.swing.JDialog import JDialog


@java_inherited_overloads
class NewWorkAreaJDialog(JDialog):
    def _java_defaults(self):
        vars(self).setdefault("parent", None)
        vars(self).setdefault("dimension", None)
        vars(self).setdefault("xSizeJTextField", None)
        vars(self).setdefault("ySizeJTextField", None)
        vars(self).setdefault("nameJTextField", None)

    def _init_fields(self) -> None:
        if "parent" not in vars(self): self.parent: MyFrame = None
        if "dimension" not in vars(self): self.dimension: Dimension = None
        if "xSizeJTextField" not in vars(self): self.xSizeJTextField: JTextField = None
        if "ySizeJTextField" not in vars(self): self.ySizeJTextField: JTextField = None
        if "nameJTextField" not in vars(self): self.nameJTextField: JTextField = None
    

    def __init__(self, parent: MyFrame, modal: bool, dimension: Dimension, newName: str) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.j2me.MyFrame import MyFrame
        super().__init__(parent, modal)
        __class__._init_fields(self)
        try:
            self.initComponents()
            self.parent = parent
            self.xSizeJTextField = JTextField("12")
            self.ySizeJTextField = JTextField("12")
            self.nameJTextField = JTextField(newName)
            self.dimension = dimension
            submitButton: JButton = JButton("Ok")
            _java_listener_owner = self
            class _JavaListenerN66406(ActionListener):
            
                

                def actionPerformed(self, evt: ActionEvent) -> None:
                    try:
                        (self if hasattr(self, "disposeNewDialog") else _java_listener_owner).disposeNewDialog()
                    except Exception as e:
                        pass
            submitButton.addActionListener(_JavaListenerN66406()
            )
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
        from org.allbinary.graphics.j2me.GraphicsException import GraphicsException
        from org.allbinary.graphics.j2me.workarea.WorkAreaJPanel import WorkAreaJPanel
        from org.allbinary.graphics.j2me.workarea.WorkAreaJPanelInterface import WorkAreaJPanelInterface
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
        _java_listener_owner = self
        class _JavaListenerN67645(WindowAdapter):
            
            

            def windowClosing(self, evt: WindowEvent) -> None:
                (self if hasattr(self, "closeDialog") else _java_listener_owner).closeDialog(evt)
        self.addWindowListener(_JavaListenerN67645()
            )
        self.pack()
    

    def closeDialog(self, evt: WindowEvent) -> None:
        self.setVisible(False)
        self.dispose()
    

    @staticmethod
    def main(args: list[str]) -> None:
        from org.allbinary.graphics.j2me.MyFrame import MyFrame
        try:
            NewWorkAreaJDialog(MyFrame(), True, Dimension(100, 100), "testing").show()
        except Exception as e:
            pass
# from java.awt.Dimension import Dimension
# from java.awt.GridLayout import GridLayout
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.JTextField import JTextField
# from javax.swing.JButton import JButton
# from javax.swing.JLabel import JLabel
# from org.allbinary.graphics.j2me.GraphicsException import GraphicsException
# from org.allbinary.graphics.j2me.MyFrame import MyFrame
# from org.allbinary.graphics.j2me.workarea.WorkAreaJPanel import WorkAreaJPanel
# from org.allbinary.graphics.j2me.workarea.WorkAreaJPanelInterface import WorkAreaJPanelInterface
# from java.awt.Frame import Frame
# from java.awt.event.WindowAdapter import WindowAdapter
# from java.awt.event.WindowEvent import WindowEvent


