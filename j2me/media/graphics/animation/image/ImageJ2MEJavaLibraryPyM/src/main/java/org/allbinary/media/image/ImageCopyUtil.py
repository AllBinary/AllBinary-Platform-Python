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



class ImageCopyUtil:
    instance: ImageCopyUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.imageCreationUtil: ImageCreationUtil = ImageCreationUtil.getInstance()
        self.anchor: int = Anchor.TOP_LEFT
        self.gameFeatureFactory: GameFeatureFactory = GameFeatureFactory.getInstance()
        self.features: Features = Features.getInstance()
        self.NO_COPY: str = "J2ME does not need to copy images after initial loading"
    

    @staticmethod
    def getInstance() -> ImageCopyUtil:
        return ImageCopyUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def createImageForRotation(self, originalImage: Image) -> Image:
        return self.createImage(originalImage)
    

    # throws Exception
    def createImage(self, originalImage: Image) -> Image:
        if not self.features.isFeature(self.gameFeatureFactory.POST_IMAGE_LOADING_MODIFICATION):
            self.logUtil.put(self.NO_COPY, self, self.commonStrings.CONSTRUCTOR, Exception())
            return originalImage
        image: Image = self.imageCreationUtil.createImageWH(originalImage.getWidth(), originalImage.getHeight())
        if image.isMutable():
            image.getGraphics().drawImage(originalImage, 0, 0, self.anchor)
            return image
        else:
            raise Exception("Not Mutable")
    

    # throws Exception
    def createImageScale(self, originalImage: Image, canvasScale: float, resize: bool) -> Image:
        if not self.features.isFeature(self.gameFeatureFactory.POST_IMAGE_LOADING_MODIFICATION):
            self.logUtil.put(self.NO_COPY, self, self.commonStrings.CONSTRUCTOR, Exception())
            return originalImage
        newWidth: int = int((originalImage.getWidth() * canvasScale))
        newHeight: int = int((originalImage.getHeight() * canvasScale))
        if resize:
            if newWidth < newHeight:
                newWidth = newHeight
            if newHeight < newWidth:
                newHeight = newWidth
        image: Image = self.imageCreationUtil.createImageWH(newWidth, newHeight)
        if image.isMutable():
            halfWidthDelta: int = (newWidth - originalImage.getWidth()) / 2
            halfHeightDelta: int = (newHeight - originalImage.getHeight()) / 2
            graphics: Graphics = image.getGraphics()
            graphics.drawImage(originalImage, halfWidthDelta, halfHeightDelta, self.anchor)
            return image
        else:
            raise Exception("Not Mutable")
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.GameFeatureFactory import GameFeatureFactory
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.media.image.ImageCreationUtil import ImageCreationUtil


ImageCopyUtil.instance = ImageCopyUtil()

