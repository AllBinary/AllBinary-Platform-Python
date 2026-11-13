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

from java.lang.JavaRuntimeStatic import lazy_static


class ImageModifierUtil:
    instance: ImageModifierUtil = None
    

    @staticmethod
    def getInstanceOrCreate() -> ImageModifierUtil:
        return ImageModifierUtil.instance
    

    def setColor(self, unusedOriginalImage: Image, image: Image, imageIndex: int, basicColor: BasicColor) -> None:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.graphics.color.BasicColor import BasicColor
        pass
    

    def changeColor(self, unusedOriginalImage: Image, image: Image, imageIndex: int, basicColor: BasicColor) -> None:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.graphics.color.BasicColor import BasicColor
        pass
    

    def setAlpha(self, originalImage: Image, image: Image, imageIndex: int, alphaInt: int) -> None:
        from javax.microedition.lcdui.Image import Image
        pass
    

    def getImageArray(self, originalImageArray: list[Image]) -> list[Image]:
        from javax.microedition.lcdui.Image import Image
        return originalImageArray
    

    def handleImage(self, imageArray: list[Image], index: int, image: Image) -> None:
        from javax.microedition.lcdui.Image import Image
        pass
    

    def reset(self) -> None:
        pass
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.graphics.color.BasicColor import BasicColor


def _ImageModifierUtil_instance() -> object:
    return ImageModifierUtil()

lazy_static(ImageModifierUtil, "instance", _ImageModifierUtil_instance)

