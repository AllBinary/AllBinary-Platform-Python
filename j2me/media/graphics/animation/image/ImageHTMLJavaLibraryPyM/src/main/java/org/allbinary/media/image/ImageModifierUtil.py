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
    instance: ImageModifierUtil = None
    

    @staticmethod
    def getInstanceOrCreate() -> ImageModifierUtil:
        return ImageModifierUtil.instance
    

    def setColor(self, unusedOriginalImage: Image, image: Image, imageIndex: int, basicColor: BasicColor) -> None:
        pass
    

    def changeColor(self, unusedOriginalImage: Image, image: Image, imageIndex: int, basicColor: BasicColor) -> None:
        pass
    

    def setAlpha(self, originalImage: Image, image: Image, imageIndex: int, alphaInt: int) -> None:
        pass
    

    def getImageArray(self, originalImageArray: list[Image]) -> list[Image]:
        return originalImageArray
    

    def handleImage(self, imageArray: list[Image], index: int, image: Image) -> None:
        pass
    

    def reset(self) -> None:
        pass
# from javax.microedition.lcdui.Image import Image
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.microemu.device.playn.PlaynMutableImage import PlaynMutableImage
from playn.core.CanvasImage import CanvasImage
from playn.core.CanvasSurface import CanvasSurface


ImageModifierUtil.instance = ImageModifierUtil()

