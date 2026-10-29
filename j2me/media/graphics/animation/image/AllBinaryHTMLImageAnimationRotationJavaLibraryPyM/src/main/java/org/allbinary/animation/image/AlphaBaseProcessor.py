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



class AlphaBaseProcessor:
    instance: AlphaBaseProcessor = None
    

    @staticmethod
    def getInstance() -> AlphaBaseProcessor:
        return AlphaBaseProcessor.instance
    

    def setAlpha(self, imageModifierUtil: ImageModifierUtil, originalImage: Image, imageToShow: Image, alpha: int) -> None:
        pass
# from javax.microedition.lcdui.Image import Image
from org.allbinary.media.image.ImageModifierUtil import ImageModifierUtil


AlphaBaseProcessor.instance = AlphaBaseProcessor()

