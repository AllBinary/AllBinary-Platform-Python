#
# AllBinary Open License Version 1
# Copyright (c) 2023 AllBinary
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


class ImageJ2MEScaleUtil:
    instance: ImageJ2MEScaleUtil = None
    

    @staticmethod
    def getInstance() -> ImageJ2MEScaleUtil:
        return ImageJ2MEScaleUtil.instance
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def scaleArray(self, images: list[Image], width: int, height: int) -> list[Image]:
        from javax.microedition.lcdui.Image import Image
        scaledImages: list[Image] = [None] * (len(images))
        index = len(images)
        while (index := index - 1) >= 0:
            scaledImages[index] = self.scale(images[index], width, height)
        return scaledImages
    

    # throws Exception
    def scale(self, image: Image, width: int, height: int) -> Image:
        from javax.microedition.lcdui.Image import Image
        return image
# from javax.microedition.lcdui.Image import Image


def _ImageJ2MEScaleUtil_instance() -> object:
    return ImageJ2MEScaleUtil()

lazy_static(ImageJ2MEScaleUtil, "instance", _ImageJ2MEScaleUtil_instance)

