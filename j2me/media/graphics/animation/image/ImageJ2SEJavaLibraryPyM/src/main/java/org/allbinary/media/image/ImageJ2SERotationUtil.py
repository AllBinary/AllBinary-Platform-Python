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

import math


class ImageJ2SERotationUtil:
    instance: ImageJ2SERotationUtil = None

    def _init_fields(self) -> None:
        self.imageUtil: ImageUtil = ImageUtil.getInstance()
        self.imageJ2SEUtil: ImageJ2SEUtil = ImageJ2SEUtil.getInstance()
        self.TWO_PIE: float = 2 * Math.PI
    

    @staticmethod
    def getInstance() -> ImageJ2SERotationUtil:
        return ImageJ2SERotationUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getRotatedImage(self, bufferedImage: Image, totalAngle: int) -> BufferedImage:
        return self.getRotatedImageRadians(bufferedImage, self.TWO_PIE * float(totalAngle) / 360.0)
    

    def getRotatedImageRadians(self, bufferedImage: Image, radians: float) -> BufferedImage:
        newBufferedImage: BufferedImage = self.imageUtil.create(bufferedImage.getWidth(None), bufferedImage.getHeight(None))
        return self.drawRotatedImageRadians(bufferedImage, newBufferedImage, newBufferedImage.createGraphics(), radians)
    

    def drawRotatedImageRadians(self, bufferedImage: Image, newBufferedImage: BufferedImage, g: Graphics2D, radians: float) -> BufferedImage:
        g.rotate(radians, newBufferedImage.getWidth(None) / 2, newBufferedImage.getHeight(None) / 2)
        g.drawImage(bufferedImage, 0, 0, bufferedImage.getWidth(None), bufferedImage.getHeight(None), None)
        g.dispose()
        return newBufferedImage
    

    def rotateImage(self, bufferedImage: Image, newBufferedImage: BufferedImage, totalAngle: int) -> BufferedImage:
        g: Graphics2D = newBufferedImage.createGraphics()
        g.setBackground(self.imageJ2SEUtil.TRANSPARENT_COLOR)
        g.clearRect(0, 0, newBufferedImage.getWidth(), newBufferedImage.getHeight())
        return self.drawRotatedImageRadians(bufferedImage, newBufferedImage, g, self.TWO_PIE * float(totalAngle) / 360.0)
    

    def createRotatedImage(self, bufferedImage: Image, newBufferedImage: BufferedImage, totalAngle: int) -> BufferedImage:
        g: Graphics2D = newBufferedImage.createGraphics()
        return self.drawRotatedImageRadians(bufferedImage, newBufferedImage, g, self.TWO_PIE * float(totalAngle) / 360.0)
    

    def getRotatedImages(self, bufferedImage: Image, numberOfFrames: int, totalAngle: int) -> list[BufferedImage]:
        bufferedImageArray: list[BufferedImage] = [None] * (numberOfFrames)
        arc: float = (self.TWO_PIE) * float(totalAngle) / 360.0
        size: int = len(bufferedImageArray)
        for index in range(0, size):
            radians: float = (arc / float(size)) * float(index)
            bufferedImageArray[index] = self.getRotatedImageRadians(bufferedImage, radians)
        return bufferedImageArray
    

    def createSpriteImage(self, bufferedImageArray: list[BufferedImage]) -> BufferedImage:
        columns: int = 9
        rows: int = 0
        size: int = len(bufferedImageArray)
        if size < columns:
            columns = size
        rows = (int(size / columns))
        if size % columns != 0:
            rows += 1
        firstBufferedImage: BufferedImage = bufferedImageArray[0]
        bufferedImage: BufferedImage = self.imageUtil.create(firstBufferedImage.getWidth(None) * columns, firstBufferedImage.getHeight(None) * rows)
        g: Graphics2D = bufferedImage.createGraphics()
        columnIndex: int = 0
        rowIndex: int = 0
        nextBufferedImage: BufferedImage = None
        for index in range(0, size):
            if int(index / 9) != 0 and index % 9 == 0:
                rowIndex += 1
                columnIndex = 0
            nextBufferedImage = bufferedImageArray[index]
            g.drawImage(nextBufferedImage, nextBufferedImage.getWidth(None) * columnIndex, nextBufferedImage.getHeight(None) * rowIndex, nextBufferedImage.getWidth(None), nextBufferedImage.getHeight(None), None)
            columnIndex += 1
        g.dispose()
        return bufferedImage
# from java.awt.Graphics2D import Graphics2D
# from java.awt.Image import Image
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.media.image.ImageUtil import ImageUtil
from org.allbinary.media.image.ImageJ2SEUtil import ImageJ2SEUtil


ImageJ2SERotationUtil.instance = ImageJ2SERotationUtil()

