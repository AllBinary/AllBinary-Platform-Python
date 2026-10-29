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
        self.imageSwtRotationUtil: ImageSwtRotationUtil = ImageSwtRotationUtil.getInstance()
        self.features: Features = Features.getInstance()
    

    @staticmethod
    def getInstance() -> ImageRotationUtil:
        return ImageRotationUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def rotateImage(self, originalImage: Image, image: Image, totalAngle: int) -> None:
        originalImage2: Image = originalImage
        if self.features.isFeature(OpenGLFeatureFactory.getInstance().OPENGL):
            if image.getType() >= OpenGLESImage.TYPE:
                openGLESImage: OpenGLESImage = (image)
                openGLESImage.openGLESImageProperties.angle = totalAngle
                return
            else:
                PreLogUtil.put("OpenGL but image is: " + str(image) + " type: " + str(image.getType()), self, "rotateImage")
        originalSwtImage: Image = (originalImage2.getImage())
        gc: GC = None
        copySwtImage: Image = None
        if image.isMutable():
            swtImage: SwtMutableImage = image
            copySwtImage = swtImage.getImage()
            gc = swtImage.getGc()
            self.imageSwtRotationUtil.rotateImage(originalSwtImage, copySwtImage, gc, totalAngle)
        else:
            PreLogUtil.put("No rotation for: " + str(image), self, "rotateImage")
    

    # throws Exception
    def createRotatedImage(self, originalImage: Image, rotationInDegrees: int) -> Image:
        return originalImage
# from javax.microedition.lcdui.Image import Image
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.eclipse.swt.graphics.GC import GC
from org.microemu.device.swt.SwtImmutableImage import SwtImmutableImage
from org.microemu.device.swt.SwtMutableImage import SwtMutableImage
from org.allbinary.media.image.ImageSwtRotationUtil import ImageSwtRotationUtil


ImageRotationUtil.instance = ImageRotationUtil()

