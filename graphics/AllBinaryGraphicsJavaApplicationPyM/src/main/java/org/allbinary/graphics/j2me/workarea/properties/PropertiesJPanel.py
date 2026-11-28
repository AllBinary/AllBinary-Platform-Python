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
# package org.allbinary.graphics.j2me.workarea.properties

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
# from javax.swing.JPanel import JPanel


@java_inherited_overloads
class PropertiesJPanel(JPanel):
    def _java_defaults(self):
        vars(self).setdefault("rotateJButton", None)
        vars(self).setdefault("copyVerticalJButton", None)
        vars(self).setdefault("leftJButton", None)
        vars(self).setdefault("rotateJPanel", None)
        vars(self).setdefault("angleJTextField", None)
        vars(self).setdefault("workAreaPropertiesJPanel", None)
        vars(self).setdefault("modifierJPanel", None)
        vars(self).setdefault("upJButton", None)
        vars(self).setdefault("jPanel8", None)
        vars(self).setdefault("downJButton", None)
        vars(self).setdefault("jPanel7", None)
        vars(self).setdefault("rightJButton", None)
        vars(self).setdefault("copyHorizontalJButton", None)

    def _init_fields(self) -> None:
        if "rotateJButton" not in vars(self): self.rotateJButton: JButton = None
        if "copyVerticalJButton" not in vars(self): self.copyVerticalJButton: JButton = None
        if "leftJButton" not in vars(self): self.leftJButton: JButton = None
        if "rotateJPanel" not in vars(self): self.rotateJPanel: JPanel = None
        if "angleJTextField" not in vars(self): self.angleJTextField: JTextField = None
        if "workAreaPropertiesJPanel" not in vars(self): self.workAreaPropertiesJPanel: JPanel = None
        if "modifierJPanel" not in vars(self): self.modifierJPanel: JPanel = None
        if "upJButton" not in vars(self): self.upJButton: JButton = None
        if "jPanel8" not in vars(self): self.jPanel8: JPanel = None
        if "downJButton" not in vars(self): self.downJButton: JButton = None
        if "jPanel7" not in vars(self): self.jPanel7: JPanel = None
        if "rightJButton" not in vars(self): self.rightJButton: JButton = None
        if "copyHorizontalJButton" not in vars(self): self.copyHorizontalJButton: JButton = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.initComponents()
    

    def set(self, panel: JPanel) -> None:
        self.workAreaPropertiesJPanel.add(panel)
        self.repaint()
    

    def initComponents(self) -> None:
        self.workAreaPropertiesJPanel = JPanel()
        self.modifierJPanel = JPanel()
        self.copyVerticalJButton = JButton()
        self.copyHorizontalJButton = JButton()
        self.rotateJPanel = JPanel()
        self.rotateJButton = JButton()
        self.angleJTextField = JTextField()
        self.jPanel7 = JPanel()
        self.upJButton = JButton()
        self.downJButton = JButton()
        self.jPanel8 = JPanel()
        self.leftJButton = JButton()
        self.rightJButton = JButton()
        self.setLayout(GridLayout(2, 1))
        self.workAreaPropertiesJPanel.setLayout(GridLayout())
        self.add(self.workAreaPropertiesJPanel)
        self.modifierJPanel.setLayout(GridLayout(6, 0))
        self.copyVerticalJButton.setFont(Font("Dialog", 0, 10))
        self.copyVerticalJButton.setText("Copy Vertical")
        self.modifierJPanel.add(self.copyVerticalJButton)
        self.copyHorizontalJButton.setFont(Font("Dialog", 0, 10))
        self.copyHorizontalJButton.setText("Copy Horizontal")
        self.modifierJPanel.add(self.copyHorizontalJButton)
        self.rotateJPanel.setLayout(GridLayout(1, 2))
        self.rotateJButton.setFont(Font("Dialog", 0, 10))
        self.rotateJButton.setText("Rotate")
        self.rotateJPanel.add(self.rotateJButton)
        self.angleJTextField.setText("Angle")
        self.rotateJPanel.add(self.angleJTextField)
        self.modifierJPanel.add(self.rotateJPanel)
        self.jPanel7.setLayout(GridLayout(1, 2))
        self.upJButton.setFont(Font("Dialog", 0, 10))
        self.upJButton.setText("Up")
        self.jPanel7.add(self.upJButton)
        self.downJButton.setFont(Font("Dialog", 0, 10))
        self.downJButton.setText("Down")
        self.jPanel7.add(self.downJButton)
        self.modifierJPanel.add(self.jPanel7)
        self.jPanel8.setLayout(GridLayout(1, 2))
        self.leftJButton.setFont(Font("Dialog", 0, 10))
        self.leftJButton.setText("Left")
        self.jPanel8.add(self.leftJButton)
        self.rightJButton.setFont(Font("Dialog", 0, 10))
        self.rightJButton.setText("Right")
        self.jPanel8.add(self.rightJButton)
        self.modifierJPanel.add(self.jPanel8)
        self.add(self.modifierJPanel)
# from javax.swing import *
# from java.awt.Font import Font
# from java.awt.GridLayout import GridLayout
# from javax.swing.JButton import JButton
# from javax.swing.JTextField import JTextField


