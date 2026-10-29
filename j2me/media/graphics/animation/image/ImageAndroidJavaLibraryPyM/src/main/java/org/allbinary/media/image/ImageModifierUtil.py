# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.media.image

from __future__ import annotations



class ImageModifierUtil:

    def _init_fields(self) -> None:
        self.paint: Paint = Paint(Paint.ANTI_ALIAS_FLAG)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstanceOrCreate() -> ImageModifierUtil:
        return ImageModifierUtil()
    

    def setColor(self, unusedOriginalImage: Image, image: Image, imageIndex: int, basicColor: BasicColor) -> None:
        self.paint.setColorFilter(PorterDuffColorFilter(int(basicColor), PorterDuff.Mode.SRC_IN))
    

    def changeColor(self, unusedOriginalImage: Image, image: Image, imageIndex: int, basicColor: BasicColor) -> None:
        self.paint.setColorFilter(PorterDuffColorFilter(int(basicColor), PorterDuff.Mode.SRC_IN))
    

    def setAlpha(self, originalImage: Image, image: Image, imageIndex: int, alphaInt: int) -> None:
        if alphaInt != self.paint.getAlpha():
            self.paint.setAlpha(alphaInt)
    

    def getImageArray(self, originalImageArray: list[Image]) -> list[Image]:
        return originalImageArray
    

    def handleImage(self, imageArray: list[Image], index: int, image: Image) -> None:
        pass
    

    def reset(self) -> None:
        pass
from android.graphics.Paint import Paint
from android.graphics.PorterDuff import PorterDuff
from android.graphics.PorterDuffColorFilter import PorterDuffColorFilter
# from javax.microedition.lcdui.Image import Image
from org.allbinary.graphics.color.BasicColor import BasicColor


