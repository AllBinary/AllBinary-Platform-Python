# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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
# package org.allbinary.game.layer.item

from __future__ import annotations

from org.allbinary.animation.Animation import Animation
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface


class RTSLayerTextAnimation(Animation, UpdateMyFontInterface):

    def _init_fields(self) -> None:
        self.image: Image = None
        self.text: str = None
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.fontHeight: int = 0
    

    def __init__(self, text: str, image: Image) -> None:
        super().__init__()
        self._init_fields()
        self.text = text
        self.image = image
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.fontHeight = font.getHeight()
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.myFontProcessor.process(graphics)
        super().paintXY(graphics, x, y)
        adjustedCostY: int = self.image.getHeight() - self.fontHeight
        graphics.drawString(self.text, x, y + adjustedCostY, 0)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor


