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

from java.lang.JavaRuntimeStatic import java_divide
from java.lang.JavaRuntimeStatic import lazy_static


class ImagesRatioUtil:
    instance: ImagesRatioUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.imageUtil: ImageUtil = ImageUtil.getInstance()
    

    @staticmethod
    def getInstance() -> ImagesRatioUtil:
        return ImagesRatioUtil.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def isEqual(self, bufferedImageArray: list[BufferedImage], totalImages: int) -> bool:
        end: int = totalImages
        if len(bufferedImageArray) < totalImages:
            end = len(bufferedImageArray)
        ratio: float = (float(bufferedImageArray[0].getWidth()) / bufferedImageArray[0].getHeight())
        for index in range(1, end):
            if ratio != (float(bufferedImageArray[index].getWidth()) / bufferedImageArray[index].getHeight()):
                return False
        return True
    

    def getAverage(self, bufferedImageArray: list[BufferedImage], totalImages: int) -> float:
        ratio: float = 0.0
        end: int = totalImages
        if len(bufferedImageArray) < totalImages:
            end = len(bufferedImageArray)
        for index in range(0, end):
            ratio += (float(bufferedImageArray[index].getWidth()) / bufferedImageArray[index].getHeight())
        return (ratio / float(end))
    

    # throws Exception
    def fudge_j2(self, bufferedImage: BufferedImage, ratio: float) -> BufferedImage:
        from org.allbinary.string.CommonLabels import CommonLabels
        imageRatio: float = (float(bufferedImage.getWidth()) / bufferedImage.getHeight())
        point: Point = Point()
        newHeight: int = bufferedImage.getHeight()
        newWidth: int = bufferedImage.getWidth()
        if ratio > imageRatio:
            newWidth = int((float(bufferedImage.getHeight()) * ratio))
            point.x = java_divide((newWidth - bufferedImage.getWidth()), 2)
        else:
            newHeight = int((float(bufferedImage.getWidth()) / ratio))
            point.y = java_divide((newHeight - bufferedImage.getHeight()), 2)
        commonLabels: CommonLabels = CommonLabels.getInstance()
        self.logUtil.putF(str(commonLabels.WIDTH_LABEL + bufferedImage.getWidth()) + " newWidth: " + str(newWidth) + str(commonLabels.HEIGHT_LABEL) + str(bufferedImage.getHeight()) + " newHeight: " + str(newHeight) + " needed ratio: " + str((float(newWidth) / float(newHeight))), self, "fudge")
        newBufferedImage: BufferedImage = self.imageUtil.create(newWidth, newHeight)
        g: Graphics2D = newBufferedImage.createGraphics()
        if point.x > 0:
            firstColumnBufferedImage: BufferedImage = bufferedImage.getSubimage(0, 0, 1, bufferedImage.getHeight())
            lastColumnBufferedImage: BufferedImage = bufferedImage.getSubimage(bufferedImage.getWidth() - 1, 0, 1, bufferedImage.getHeight())
            self.logUtil.putF("Draw some columns to fill in gap", self, "fudge")
            for index in range(0, point.x):
                g.drawImage(firstColumnBufferedImage, index, 0, None)
                g.drawImage(lastColumnBufferedImage, newWidth - index, 0, None)
        if point.y > 0:
            firstRowBufferedImage: BufferedImage = bufferedImage.getSubimage(0, 0, bufferedImage.getWidth(), 1)
            lastRowBufferedImage: BufferedImage = bufferedImage.getSubimage(0, bufferedImage.getHeight() - 1, bufferedImage.getWidth(), 1)
            self.logUtil.putF("Draw some rows to fill in gap", self, "fudge")
            for index in range(0, point.y):
                g.drawImage(firstRowBufferedImage, 0, index, None)
                g.drawImage(lastRowBufferedImage, 0, newHeight - index, None)
        g.drawImage(bufferedImage, point.x, point.y, bufferedImage.getWidth(), bufferedImage.getHeight(), None)
        return newBufferedImage
    

    # throws Exception
    def fudge_j3(self, bufferedImageArray: list[BufferedImage], totalImages: int, ratio: float) -> list[BufferedImage]:
        end: int = totalImages
        if len(bufferedImageArray) < totalImages:
            end = len(bufferedImageArray)
        fudgedBufferedImageArray: list[BufferedImage] = [None] * (end)
        for index in range(0, end):
            fudgedBufferedImageArray[index] = self.fudge(bufferedImageArray[index], ratio)
        return fudgedBufferedImageArray

    def fudge(self, *args):
        implementation = __class__.__dict__.get("fudge_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().fudge(*args)
# from java.awt.Point import Point
# from java.awt.Graphics2D import Graphics2D
# from java.awt.image.BufferedImage import BufferedImage
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.media.image.ImageUtil import ImageUtil


def _ImagesRatioUtil_instance() -> object:
    return ImagesRatioUtil()

lazy_static(ImagesRatioUtil, "instance", _ImagesRatioUtil_instance)

