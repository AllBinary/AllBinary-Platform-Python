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
# package org.allbinary.animation.image

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class ModifierBaseProcessor:
    instance: ModifierBaseProcessor = None
    

    @staticmethod
    def getInstance() -> ModifierBaseProcessor:
        return ModifierBaseProcessor.instance
    

    def updateColor(self, imageModifierUtil: ImageModifierUtil, originalImage: Image, imageToShow: Image, index: int, basicColor: BasicColor) -> None:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.graphics.color.BasicColor import BasicColor
        from org.allbinary.media.image.ImageModifierUtil import ImageModifierUtil
        pass
    

    def updateAlpha(self, imageModifierUtil: ImageModifierUtil, originalImage: Image, imageToShow: Image, index: int, alpha: int) -> None:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.media.image.ImageModifierUtil import ImageModifierUtil
        pass
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.media.image.ImageModifierUtil import ImageModifierUtil


def _ModifierBaseProcessor_instance() -> object:
    return ModifierBaseProcessor()

lazy_static(ModifierBaseProcessor, "instance", _ModifierBaseProcessor_instance)

