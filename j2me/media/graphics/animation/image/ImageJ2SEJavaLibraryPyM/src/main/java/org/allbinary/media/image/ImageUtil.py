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



class ImageUtil:
    instance: ImageUtil = None

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.IIOIMAGE_POOL_NAME: str = "IIOIMAGE_POOL_NAME"
        self.CREATE_BUFFERED_IMAGE: str = "createBufferedImage"
    

    @staticmethod
    def getInstance() -> ImageUtil:
        return ImageUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getDefaultConfiguration(self) -> GraphicsConfiguration:
        ge: GraphicsEnvironment = GraphicsEnvironment.getLocalGraphicsEnvironment()
        gd: GraphicsDevice = ge.getDefaultScreenDevice()
        return gd.getDefaultConfiguration()
    

    def create(self, width: int, height: int) -> BufferedImage:
        graphicsConfiguration: GraphicsConfiguration = self.getDefaultConfiguration()
        return graphicsConfiguration.createCompatibleImage(width, height, Transparency.TRANSLUCENT)
    

    # throws Exception
    def createBufferedImageForResize(self, bufferedImageArray: list[BufferedImage], percent: int, scale: bool) -> list[BufferedImage]:
        size: int = len(bufferedImageArray)
        scaledBufferedImageArray: list[BufferedImage] = [None] * (size)
        bufferedImage: BufferedImage = None
        for index in range(0, size):
            bufferedImage = bufferedImageArray[index]
            newWidth: int = int((bufferedImage.getWidth() * percent / 100))
            newHeight: int = int((bufferedImage.getHeight() * percent / 100))
            scaledBufferedImageArray[index] = self.createBufferedImage(bufferedImage, newWidth, newHeight, scale)
        return scaledBufferedImageArray
    

    # throws Exception
    def createBufferedImage2(self, bufferedImageArray: list[BufferedImage], percent: float, scale: bool) -> list[BufferedImage]:
        size: int = len(bufferedImageArray)
        scaledBufferedImageArray: list[BufferedImage] = [None] * (size)
        bufferedImage: BufferedImage = None
        for index in range(0, size):
            bufferedImage = bufferedImageArray[index]
            newWidth: int = int((bufferedImage.getWidth() * percent))
            newHeight: int = int((bufferedImage.getHeight() * percent))
            scaledBufferedImageArray[index] = self.createBufferedImage(bufferedImage, newWidth, newHeight, scale)
        return scaledBufferedImageArray
    

    # throws Exception
    def createBufferedImage3(self, bufferedImageArray: list[BufferedImage], width: int, height: int, scale: bool) -> list[BufferedImage]:
        size: int = len(bufferedImageArray)
        scaledBufferedImageArray: list[BufferedImage] = [None] * (size)
        for index in range(0, size):
            scaledBufferedImageArray[index] = self.createBufferedImage(bufferedImageArray[index], width, height, scale)
        return scaledBufferedImageArray
    

    # throws Exception
    def createBufferedImageForSave(self, bufferedImage: BufferedImage, newWidth: int, newHeight: int) -> BufferedImage:
        return self.createBufferedImage(bufferedImage, newWidth, newHeight, True)
    

    # throws Exception
    def createBufferedImage(self, bufferedImage: BufferedImage, newWidth: int, newHeight: int, scale: bool) -> BufferedImage:
        return self.createBufferedImageAllowTranslate(bufferedImage, newWidth, newHeight, scale, False)
    

    # throws Exception
    def createBufferedImageAllowTranslate(self, bufferedImage: BufferedImage, newWidth: int, newHeight: int, scale: bool, allowTranslate: bool) -> BufferedImage:
        width: float = bufferedImage.getWidth()
        height: float = bufferedImage.getHeight()
        d_newWidth: float = float(newWidth)
        d_newHeight: float = float(newHeight)
        widthRatio: float = d_newWidth / width
        heightRatio: float = d_newHeight / height
        ratioX: float = 1.0
        ratioY: float = 1.0
        if scale:
            ratioX = widthRatio
            ratioY = heightRatio
        affineTransform: AffineTransform = AffineTransform.getScaleInstance(ratioX, ratioY)
        if not scale and allowTranslate:
            dx: float = (float(newWidth) - width) / 2.0
            dy: float = (float(newHeight) - height) / 2.0
            affineTransform.translate(dx, dy)
        newBufferedImage: BufferedImage = BufferedImage(newWidth, newHeight, BufferedImage.TYPE_INT_ARGB_PRE)
        graphics: Graphics2D = newBufferedImage.createGraphics()
        graphics.drawRenderedImage(bufferedImage, affineTransform)
        return newBufferedImage
    

    # throws Exception
    def createBufferedImageWithLargerCanvas(self, bufferedImage: BufferedImage, newWidth: int, newHeight: int) -> BufferedImage:
        width: float = bufferedImage.getWidth()
        height: float = bufferedImage.getHeight()
        d_newWidth: float = float(newWidth)
        d_newHeight: float = float(newHeight)
        widthRatio: float = d_newWidth / width
        heightRatio: float = d_newHeight / height
        dx2: int = int((float(newWidth) - width))
        dy2: int = int((float(newHeight) - height))
        dx: int = int(dx2 / 2)
        dy: int = int(dy2 / 2)
        dx4: int = int(dx2 / 4)
        dy4: int = int(dy2 / 4)
        newBufferedImage: BufferedImage = BufferedImage(newWidth, newHeight, BufferedImage.TYPE_INT_ARGB_PRE)
        graphics: Graphics2D = newBufferedImage.createGraphics()
        graphics.drawImage(bufferedImage, dx4, dy4, None)
        return newBufferedImage
    

    def convertToBufferedImage(self, toolkitImage: Image) -> BufferedImage:
        if toolkitImage is None:
            return None
        bufferedImage: BufferedImage = BufferedImage(toolkitImage.getWidth(None), toolkitImage.getHeight(None), BufferedImage.TYPE_INT_ARGB)
        g2d: Graphics2D = bufferedImage.createGraphics()
        g2d.drawImage(toolkitImage, 0, 0, None)
        g2d.dispose()
        return bufferedImage
    

    def getBufferedImage(self, image: Image) -> BufferedImage:
        bufferedImage: BufferedImage = None
        if image.isMutable():
            j2seImage: J2SEMutableImage = image
            bufferedImage = j2seImage.getImage()
        else:
            j2seImage: J2SEImmutableImage = image
            bufferedImage = j2seImage.getImage()
        return bufferedImage
    

    def toString(self, bufferedImage: BufferedImage) -> str:
        commonLabels: CommonLabels = CommonLabels.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(" BufferedImage -")
        stringBuffer.append(commonLabels.WIDTH_LABEL)
        stringBuffer.appendint(int(bufferedImage.getWidth()))
        stringBuffer.append(commonLabels.HEIGHT_LABEL)
        stringBuffer.appendint(int(bufferedImage.getHeight()))
        stringBuffer.append(" Type: ")
        stringBuffer.appendint(int(bufferedImage.getType()))
        return str(stringBuffer)
# from java.awt.Graphics2D import Graphics2D
# from java.awt.GraphicsConfiguration import GraphicsConfiguration
# from java.awt.GraphicsDevice import GraphicsDevice
# from java.awt.GraphicsEnvironment import GraphicsEnvironment
# from java.awt.Transparency import Transparency
# from java.awt.geom.AffineTransform import AffineTransform
# from java.awt.image.BufferedImage import BufferedImage
# from javax.microedition.lcdui.Image import Image
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.microemu.device.j2se.J2SEImmutableImage import J2SEImmutableImage
from org.microemu.device.j2se.J2SEMutableImage import J2SEMutableImage


ImageUtil.instance = ImageUtil()

