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

from org.allbinary.animation.image.BaseImageAnimationFactory import BaseImageAnimationFactory


class AllBinaryScreenRelationalImageAnimationInterfaceFactory(BaseImageAnimationFactory):

    def _init_fields(self) -> None:
        self.lastImage: Image = NullImage.NULL_IMAGE
    

    def __init__(self, image: Image, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        super().__init__(image, PrimitiveIntUtil.getArrayInstance(), 0, 0, 0, 0, animationBehaviorFactory)
        self._init_fields()
        if self.lastImage != NullImage.NULL_IMAGE:
            androidImageInterface: AndroidImageInterface = self.lastImage
            androidImageInterface.getBitmap().recycle()
        scale: float = ScreenRelationalUtil.getInstance().getScaleImage(image)
        self.lastImage = ImageScaleUtil.getInstance().createImage(GameFeatureImageCacheFactory.getInstance(), self.getImage(), scale, scale, False)
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.ImageAnimation import ImageAnimation
        return ImageAnimation(self.lastImage, self.animationBehaviorFactory.getOrCreateInstance())
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.image.GameFeatureImageCacheFactory import GameFeatureImageCacheFactory
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.graphics.displayable.ScreenRelationalUtil import ScreenRelationalUtil
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
from org.allbinary.media.image.ImageScaleUtil import ImageScaleUtil
from org.microemu.android.device.AndroidImageInterface import AndroidImageInterface


