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



class ImageScaleUtil:
    instance: ImageScaleUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.imageCopyUtil: ImageCopyUtil = ImageCopyUtil.getInstance()
        self.gameFeatureFactory: GameFeatureFactory = GameFeatureFactory.getInstance()
        self.features: Features = Features.getInstance()
        self.NO_COPY: str = "SWT should not copy images after initial loading as the alpha is not honored"
    

    @staticmethod
    def getInstance() -> ImageScaleUtil:
        return ImageScaleUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def createImage2(self, imageCache: ImageCache, originalImage: Image, scaleNominatorX: float, scaleDenominatorX: float, scaleNominatorY: float, scaleDenominatorY: float, cached: bool) -> Image:
        return self.createImage3(imageCache, originalImage, scaleNominatorX, scaleDenominatorX, scaleNominatorY, scaleDenominatorY, cached, True)
    

    # throws Exception
    def createImage3(self, imageCache: ImageCache, originalImage: Image, scaleNominatorX: float, scaleDenominatorX: float, scaleNominatorY: float, scaleDenominatorY: float, cached: bool, mutable: bool) -> Image:
        if not self.features.isFeature(self.gameFeatureFactory.POST_IMAGE_LOADING_MODIFICATION):
            self.logUtil.putF(self.NO_COPY, self, self.commonStrings.CONSTRUCTOR)
            return originalImage
        width: int = originalImage.getWidth()
        height: int = originalImage.getHeight()
        scaleX: float = scaleNominatorX / scaleDenominatorX
        scaleY: float = scaleNominatorY / scaleDenominatorY
        scaledImage: Image = self.imageCopyUtil.createImageWH(originalImage, int((scaleX * float(width))), int((scaleY * float(height))), mutable)
        return scaledImage
    

    # throws Exception
    def scale2(self, originalImage: Image, originalImageArray: list[Image], ximageToShowArray: list[Image], unused: int, scaleX: float, scaleY: float, maxScaleX: float, maxScaleY: float) -> None:
        self.scale(originalImage, originalImageArray, ximageToShowArray, unused, scaleX, scaleY, maxScaleX, maxScaleY, True)
    

    # throws Exception
    def scale(self, originalImage: Image, originalImageArray: list[Image], ximageToShowArray: list[Image], unused: int, scaleX: float, scaleY: float, maxScaleX: float, maxScaleY: float, mutable: bool) -> None:
        width: int = originalImage.getWidth()
        height: int = originalImage.getHeight()
        scaledImage: Image = self.imageCopyUtil.createImageWH(originalImage, int((scaleX * float(width))), int((scaleY * float(height))), mutable)
        originalImageArray[0] = scaledImage
# from javax.microedition.lcdui.Image import Image
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.GameFeatureFactory import GameFeatureFactory
from org.allbinary.image.ImageCache import ImageCache
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.media.image.ImageCopyUtil import ImageCopyUtil


ImageScaleUtil.instance = ImageScaleUtil()

