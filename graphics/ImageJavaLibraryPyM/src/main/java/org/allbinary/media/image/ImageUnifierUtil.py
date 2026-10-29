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



class ImageUnifierUtil:
    instance: ImageUnifierUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.imageUtil: ImageUtil = ImageUtil.getInstance()
    

    @staticmethod
    def getInstance() -> ImageUnifierUtil:
        return ImageUnifierUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getDefaultConfiguration(self) -> GraphicsConfiguration:
        from org.allbinary.media.image.GraphicsEnvironment import GraphicsEnvironment
        ge: GraphicsEnvironment = GraphicsEnvironment.getLocalGraphicsEnvironment()
        gd: GraphicsDevice = ge.getDefaultScreenDevice()
        return gd.getDefaultConfiguration()
    

    def getImage(self, bufferedImageArray: list[BufferedImage], imageUnifierProperties: ImageUnifierProperties) -> BufferedImage:
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
# from java.awt import *
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.media.image.ImageUtil import ImageUtil


ImageUnifierUtil.instance = ImageUnifierUtil()

