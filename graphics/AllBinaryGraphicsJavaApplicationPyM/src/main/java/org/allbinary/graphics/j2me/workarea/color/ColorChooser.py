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
# package org.allbinary.graphics.j2me.workarea.color

from __future__ import annotations

from org.allbinary.graphics.j2me.workarea.color.JPanel import JPanel


class ColorChooser(JPanel):

    def _init_fields(self) -> None:
        self.jColorChooser1: JColorChooser = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.initComponents()
    

    def initComponents(self) -> None:
        from org.allbinary.graphics.j2me.workarea.color.JColorChooser import JColorChooser
        from org.allbinary.graphics.j2me.workarea.color.BorderLayout import BorderLayout
        self.jColorChooser1 = JColorChooser()
        self.setLayout(BorderLayout())
        self.add(self.jColorChooser1, java.awt.BorderLayout.CENTER)


