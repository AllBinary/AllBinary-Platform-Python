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

from org.allbinary.graphics.j2me.workarea.properties.JPanel import JPanel


class PropertiesJPanel(JPanel):

    def _init_fields(self) -> None:
        self.rotateJButton: JButton = None
        self.copyVerticalJButton: JButton = None
        self.leftJButton: JButton = None
        self.rotateJPanel: JPanel = None
        self.angleJTextField: JTextField = None
        self.workAreaPropertiesJPanel: JPanel = None
        self.modifierJPanel: JPanel = None
        self.upJButton: JButton = None
        self.jPanel8: JPanel = None
        self.downJButton: JButton = None
        self.jPanel7: JPanel = None
        self.rightJButton: JButton = None
        self.copyHorizontalJButton: JButton = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.initComponents()
    

    def set(self, panel: JPanel) -> None:
        self.workAreaPropertiesJPanel.add(panel)
        self.repaint()
    

    def initComponents(self) -> None:
        from org.allbinary.graphics.j2me.workarea.properties.JPanel import JPanel
        from org.allbinary.graphics.j2me.workarea.properties.JPanel import JPanel
        from org.allbinary.graphics.j2me.workarea.properties.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.properties.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.properties.JPanel import JPanel
        from org.allbinary.graphics.j2me.workarea.properties.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.properties.JTextField import JTextField
        from org.allbinary.graphics.j2me.workarea.properties.JPanel import JPanel
        from org.allbinary.graphics.j2me.workarea.properties.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.properties.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.properties.JPanel import JPanel
        from org.allbinary.graphics.j2me.workarea.properties.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.properties.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.properties.GridLayout import GridLayout
        from org.allbinary.graphics.j2me.workarea.properties.GridLayout import GridLayout
        from org.allbinary.graphics.j2me.workarea.properties.GridLayout import GridLayout
        from org.allbinary.graphics.j2me.workarea.properties.Font import Font
        from org.allbinary.graphics.j2me.workarea.properties.Font import Font
        from org.allbinary.graphics.j2me.workarea.properties.GridLayout import GridLayout
        from org.allbinary.graphics.j2me.workarea.properties.Font import Font
        from org.allbinary.graphics.j2me.workarea.properties.GridLayout import GridLayout
        from org.allbinary.graphics.j2me.workarea.properties.Font import Font
        from org.allbinary.graphics.j2me.workarea.properties.Font import Font
        from org.allbinary.graphics.j2me.workarea.properties.GridLayout import GridLayout
        from org.allbinary.graphics.j2me.workarea.properties.Font import Font
        from org.allbinary.graphics.j2me.workarea.properties.Font import Font
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


