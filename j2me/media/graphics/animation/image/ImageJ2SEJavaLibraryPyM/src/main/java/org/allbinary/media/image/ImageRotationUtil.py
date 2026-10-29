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
        self.imageJ2SERotationUtil: ImageJ2SERotationUtil = ImageJ2SERotationUtil.getInstance()
    

    @staticmethod
    def getInstance() -> ImageRotationUtil:
        return ImageRotationUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def rotateImage(self, originalImage: Image, image: Image, totalAngle: int) -> None:
        if image.isMutable():
            j2seImage: J2SEMutableImage = image
            newBufferedImage: BufferedImage = j2seImage.getImage()
            originalAwtImage: Image = None
            if originalImage.isMutable():
                originalJ2SEImage: J2SEMutableImage = originalImage
                originalAwtImage = originalJ2SEImage.getImage()
            else:
                originalJ2SEImage: J2SEImmutableImage = originalImage
                originalAwtImage = originalJ2SEImage.getImage()
            self.imageJ2SERotationUtil.rotateImage(originalAwtImage, newBufferedImage, totalAngle)
        else:
            PreLogUtil.putOE("Not Mutable", self, "getRotatedImage", Exception())
    

    # throws Exception
    def createRotatedImage(self, originalImage: Image, rotationInDegrees: int) -> Image:
        from org.allbinary.media.image.ImageCreationUtil import ImageCreationUtil
        image: Image = ImageCreationUtil.getInstance().createImageWH(originalImage.getWidth(), originalImage.getHeight())
        if image.isMutable():
            originalAwtImage: Image = None
            if originalImage.isMutable():
                originalJ2SEImage: J2SEMutableImage = originalImage
                originalAwtImage = originalJ2SEImage.getImage()
            else:
                originalJ2SEImage: J2SEImmutableImage = originalImage
                originalAwtImage = originalJ2SEImage.getImage()
            j2seImage: J2SEMutableImage = image
            newBufferedImage: BufferedImage = j2seImage.getImage()
            bufferedImage: BufferedImage = self.imageJ2SERotationUtil.createRotatedImage(originalAwtImage, newBufferedImage, rotationInDegrees)
            return image
        else:
            raise Exception("Not Mutable")
# from java.awt.image.BufferedImage import BufferedImage
# from javax.microedition.lcdui.Image import Image
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.microemu.device.j2se.J2SEImmutableImage import J2SEImmutableImage
from org.microemu.device.j2se.J2SEMutableImage import J2SEMutableImage
from org.allbinary.media.image.ImageJ2SERotationUtil import ImageJ2SERotationUtil


ImageRotationUtil.instance = ImageRotationUtil()

