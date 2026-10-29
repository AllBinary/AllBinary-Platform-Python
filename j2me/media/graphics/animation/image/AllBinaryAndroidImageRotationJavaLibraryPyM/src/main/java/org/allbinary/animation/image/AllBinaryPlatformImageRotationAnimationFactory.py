# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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

from org.allbinary.animation.image.AllBinaryAndroidImageRotationAnimationFactory import AllBinaryAndroidImageRotationAnimationFactory


class AllBinaryPlatformImageRotationAnimationFactory(AllBinaryAndroidImageRotationAnimationFactory):
    

    def __init__(self, image: Image, width: int, height: int, angleIncrement: int, animationBehaviorFactory: AnimationBehaviorFactory, resizeCanvasForRotation: bool) -> None:
        super().__init__(image, width, height, angleIncrement, animationBehaviorFactory, resizeCanvasForRotation)
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory


