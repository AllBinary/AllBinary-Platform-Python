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
# package org.allbinary.media.image

from __future__ import annotations



class ImageRotationUtil:
    instance: ImageRotationUtil = None

    def _init_fields(self) -> None:
        self.anchor: int = Anchor.TOP_LEFT
    

    @staticmethod
    def getInstance() -> ImageRotationUtil:
        return ImageRotationUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def createRotatedImage(self, originalImage: Image, rotationInDegrees: int) -> Image:
        return originalImage
# from javax.microedition.lcdui.Image import Image
from org.allbinary.graphics.Anchor import Anchor


ImageRotationUtil.instance = ImageRotationUtil()

