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

from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_divide
from java.lang.JavaRuntimeStatic import lazy_static


class ImageSwtRotationUtil:
    instance: ImageSwtRotationUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.game.configuration.feature.Features import Features
        from org.allbinary.game.configuration.feature.GameFeatureFactory import GameFeatureFactory
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.imageUtil: ImageUtil = ImageUtil.getInstance()
        self.gameFeatureFactory: GameFeatureFactory = GameFeatureFactory.getInstance()
        self.features: Features = Features.getInstance()
        self.NO_COPY: str = "SWT should not copy images after initial loading as the alpha is not honored"
    

    @staticmethod
    def getInstance() -> ImageSwtRotationUtil:
        return ImageSwtRotationUtil.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def getRotatedImage(self, bufferedImage: Image, totalAngle: int) -> Image:
        from org.eclipse.swt.graphics.Image import Image
        if not (self.features.isFeature(self.gameFeatureFactory.POST_IMAGE_LOADING_MODIFICATION)):
            self.logUtil.putF(self.NO_COPY, self, self.commonStrings.CONSTRUCTOR)
            return bufferedImage
        return bufferedImage
    

    def getRotatedImage2(self, bufferedImage: Image, newBufferedImage: Image, gc: GC, angle: float) -> Image:
        from org.eclipse.swt.graphics.GC import GC
        from org.eclipse.swt.graphics.Image import Image
        if not (self.features.isFeature(self.gameFeatureFactory.POST_IMAGE_LOADING_MODIFICATION)):
            self.logUtil.putF(self.NO_COPY, self, self.commonStrings.CONSTRUCTOR)
            return bufferedImage
        return bufferedImage
    

    def rotateImage(self, originalSwtImage: Image, newSwtImage: Image, gc: GC, totalAngle: int) -> Image:
        from org.eclipse.swt.graphics.GC import GC
        from org.eclipse.swt.graphics.Image import Image
        return self.getRotatedImage2(originalSwtImage, newSwtImage, gc, totalAngle)
    

    def getRotatedImageSWT(self, bufferedImage: Image, newSwtImage: Image, gc: GC, totalAngle: int) -> Image:
        from org.eclipse.swt.graphics.GC import GC
        from org.eclipse.swt.graphics.Image import Image
        return self.getRotatedImage2(bufferedImage, newSwtImage, gc, totalAngle)
    

    def getRotatedImages(self, bufferedImage: Image, numberOfFrames: int, totalAngle: int) -> list[Image]:
        from org.eclipse.swt.graphics.Image import Image
        bufferedImageArray: list[Image] = [None] * (numberOfFrames)
        angle: int = 0
        size: int = len(bufferedImageArray)
        for index in range(0, size):
            angle = (int(totalAngle / size)) * index
            bufferedImageArray[index] = self.getRotatedImage(bufferedImage, angle)
        return bufferedImageArray
    

    def createSpriteImage(self, bufferedImageArray: list[Image]) -> Image:
        from org.eclipse.swt.SWT import SWT
        from org.eclipse.swt.graphics.GC import GC
        from org.eclipse.swt.graphics.ImageData import ImageData
        from org.eclipse.swt.graphics.Image import Image
        columns: int = 9
        rows: int = 0
        size: int = len(bufferedImageArray)
        if size < columns:
            columns = size
        rows = (int(size / columns))
        if size % columns != 0:
            rows += 1
        firstBufferedImage: Image = bufferedImageArray[0]
        imageData: ImageData = firstBufferedImage.getImageData()
        bufferedImage: Image = self.imageUtil.create(imageData.width * columns, imageData.height * rows)
        gc: GC = GC(bufferedImage)
        gc.setAntialias(SWT.ON)
        gc.setInterpolation(SWT.HIGH)
        columnIndex: int = 0
        rowIndex: int = 0
        nextBufferedImage: Image = None
        for index in range(0, size):
            if int(index / 9) != 0 and index % 9 == 0:
                rowIndex += 1
                columnIndex = 0
            nextBufferedImage = bufferedImageArray[index]
            imageData = nextBufferedImage.getImageData()
            gc.drawImage(bufferedImage, 0, 0, bufferedImage.getBounds().width, bufferedImage.getBounds().height, imageData.width * columnIndex, imageData.height * rowIndex, imageData.width, imageData.height)
            columnIndex += 1
        gc.dispose()
        return bufferedImage
# from org.allbinary.game.configuration.feature.Features import Features
# from org.allbinary.game.configuration.feature.GameFeatureFactory import GameFeatureFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.eclipse.swt.SWT import SWT
# from org.eclipse.swt.graphics.GC import GC
# from org.eclipse.swt.graphics.ImageData import ImageData
# from org.eclipse.swt.graphics.Image import Image
from org.allbinary.media.image.ImageUtil import ImageUtil


def _ImageSwtRotationUtil_instance() -> object:
    return ImageSwtRotationUtil()

lazy_static(ImageSwtRotationUtil, "instance", _ImageSwtRotationUtil_instance)

