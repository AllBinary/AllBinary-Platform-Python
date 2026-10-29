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
# package org.allbinary.image

from __future__ import annotations



class IndexedAnimationToImageArrayUtil:
    

    # throws Exception
    @staticmethod
    def getInstance(width: int, height: int, sequentialAnimationInterface: IndexedAnimation) -> list[Image]:
        from org.allbinary.image.AnimationFrameToImageUtil import AnimationFrameToImageUtil
        size: int = sequentialAnimationInterface.getAnimationSize()
        imageArray: list[Image] = [None] * (size)
        for index in range(0, size):
            sequentialAnimationInterface.setFrame(index)
            imageArray[index] = AnimationFrameToImageUtil.getInstance().getInstanceWH(width, height, sequentialAnimationInterface)
        return imageArray
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.IndexedAnimation import IndexedAnimation


