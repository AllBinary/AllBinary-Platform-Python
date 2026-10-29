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
# package org.allbinary.image.gui

from __future__ import annotations

from org.allbinary.image.gui.JPanel import JPanel


class ImageJPanel(JPanel):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.canvasStrings: CanvasStrings = CanvasStrings.getInstance()
        self.isDrawn: bool = False
        self.bufferedImage: BufferedImage = None
    

    def __init__(self, bufferedImage: BufferedImage) -> None:
        super().__init__()
        self._init_fields()
        self.initComponents()
        self.bufferedImage = bufferedImage
        self.setSize(self.bufferedImage.getWidth(None), self.bufferedImage.getHeight(None))
    

    def paint(self, graphics: Graphics) -> None:
        if not self.isDrawn:
            self.logUtil.putF(self.commonStrings.START, self, self.canvasStrings.PAINT)
            graphics.drawImage(self.bufferedImage, 0, 0, self.bufferedImage.getWidth(None), self.bufferedImage.getHeight(None), None)
            self.isDrawn = True
    

    def initComponents(self) -> None:
        from org.allbinary.image.gui.GroupLayout import GroupLayout
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGap(0, 400, Short.MAX_VALUE))
        layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGap(0, 300, Short.MAX_VALUE))
# from java.awt import *
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


