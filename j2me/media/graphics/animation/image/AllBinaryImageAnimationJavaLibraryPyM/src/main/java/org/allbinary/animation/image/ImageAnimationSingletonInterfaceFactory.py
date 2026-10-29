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
# package org.allbinary.animation.image

from __future__ import annotations

from org.allbinary.animation.SingletonAnimationInterfaceFactory import SingletonAnimationInterfaceFactory


class ImageAnimationSingletonInterfaceFactory(SingletonAnimationInterfaceFactory):
    

    def __init__(self, animationInterface: Animation, width: int, height: int) -> None:
        from org.allbinary.animation.image.ImageAnimation import ImageAnimation
        super().__init__(ImageAnimation(AnimationFrameToImageUtil.getInstance().getInstanceWH(width, height, animationInterface), AnimationBehavior.getInstance()))
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.image.AnimationFrameToImageUtil import AnimationFrameToImageUtil


