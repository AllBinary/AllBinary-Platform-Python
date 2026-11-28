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

from java.lang.JavaRuntimeStatic import lazy_static


class ImageUnifierUtil:
    instance: ImageUnifierUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.imageUtil: ImageUtil = ImageUtil.getInstance()
    

    @staticmethod
    def getInstance() -> ImageUnifierUtil:
        return ImageUnifierUtil.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def getDefaultConfiguration(self) -> GraphicsConfiguration:
        ge: GraphicsEnvironment = GraphicsEnvironment.getLocalGraphicsEnvironment()
        gd: GraphicsDevice = ge.getDefaultScreenDevice()
        return gd.getDefaultConfiguration()
    

    def getImage(self, bufferedImageArray: list[BufferedImage], imageUnifierProperties: ImageUnifierProperties) -> BufferedImage:
        from org.allbinary.string.CommonLabels import CommonLabels
        newBufferedImage: BufferedImage = self.imageUtil.create(imageUnifierProperties.getWidth(), imageUnifierProperties.getHeight())
        commonLabels: CommonLabels = CommonLabels.getInstance()
        self.logUtil.putF("Setting Image - " + str(commonLabels.WIDTH_LABEL) + str(newBufferedImage.getWidth()) + str(commonLabels.HEIGHT_LABEL) + str(newBufferedImage.getHeight()), self, "getImage")
        g: Graphics2D = newBufferedImage.createGraphics()
        columnIndex: int = 0
        rowIndex: int = 0
        for index in range(0, len(bufferedImageArray)):
            x: int = int(imageUnifierProperties.getImageUnifierCell().getWidth()) * ((columnIndex := columnIndex + 1) - 1)
            y: int = int(imageUnifierProperties.getImageUnifierCell().getHeight()) * rowIndex
            self.logUtil.putF("Adding Image: " + str(index) + " x: " + str(x) + " y: " + str(y), self, "getImage")
            g.drawImage(bufferedImageArray[index], x, y, int(imageUnifierProperties.getImageUnifierCell().getWidth()), int(imageUnifierProperties.getImageUnifierCell().getHeight()), None)
            totalColumnsMinusOne: int = (int(imageUnifierProperties.getColumns()) - 1)
            if columnIndex > totalColumnsMinusOne:
                rowIndex += 1
                columnIndex = 0
        g.dispose()
        return newBufferedImage
# from java.awt.GraphicsEnvironment import GraphicsEnvironment
# from java.awt.GraphicsDevice import GraphicsDevice
# from java.awt.GraphicsConfiguration import GraphicsConfiguration
# from java.awt.Graphics2D import Graphics2D
# from java.awt.image.BufferedImage import BufferedImage
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.media.image.ImageUtil import ImageUtil


def _ImageUnifierUtil_instance() -> object:
    return ImageUnifierUtil()

lazy_static(ImageUnifierUtil, "instance", _ImageUnifierUtil_instance)

