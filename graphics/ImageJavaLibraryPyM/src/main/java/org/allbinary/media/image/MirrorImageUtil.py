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



class MirrorImageUtil:
    instance: MirrorImageUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.imageUtil: ImageUtil = ImageUtil.getInstance()
    

    @staticmethod
    def getInstance() -> MirrorImageUtil:
        return MirrorImageUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getImage(self, bufferedImage: BufferedImage, verticle: bool, horizontal: bool) -> BufferedImage:
        self.logUtil.putF("Starting", self, "getImage")
        newBufferedImage: BufferedImage = self.imageUtil.create(bufferedImage.getWidth(None), bufferedImage.getHeight(None))
        g: Graphics2D = newBufferedImage.createGraphics()
        if verticle:
            tx: AffineTransform = AffineTransform.getScaleInstance(1, -1)
            tx.translate(0, -bufferedImage.getHeight(None))
            op: AffineTransformOp = AffineTransformOp(tx, AffineTransformOp.TYPE_NEAREST_NEIGHBOR)
            bufferedImage = op.filter(bufferedImage, None)
        if horizontal:
            tx: AffineTransform = AffineTransform.getScaleInstance(-1, 1)
            tx.translate(-bufferedImage.getWidth(None), 0)
            op: AffineTransformOp = AffineTransformOp(tx, AffineTransformOp.TYPE_NEAREST_NEIGHBOR)
            bufferedImage = op.filter(bufferedImage, None)
        g.drawImage(bufferedImage, 0, 0, bufferedImage.getWidth(None), bufferedImage.getHeight(None), None)
        g.dispose()
        return newBufferedImage
    

    def getImages(self, bufferedImage: BufferedImage, verticle: bool, horizontal: bool) -> list[BufferedImage]:
        width: int = bufferedImage.getWidth()
        height: int = bufferedImage.getHeight()
        cellHeight: int = height
        cellWidth: int = height
        numberOfFramesPerOrientation: int = int(width / cellWidth)
        numberOfFrames: int = numberOfFramesPerOrientation
        if verticle:
            numberOfFrames *= 2
        if horizontal:
            numberOfFrames *= 2
        self.logUtil.putF("numberOfFramesPerOrientation: " + str(numberOfFramesPerOrientation) + " numberOfFrames: " + str(numberOfFrames), self, "getImages")
        bufferedImageArray: list[BufferedImage] = [None] * (numberOfFrames)
        y: int = 0
        for index in range(0, numberOfFramesPerOrientation):
            x: int = index * cellWidth
            bufferedImageArray[index] = bufferedImage.getSubimage(x, y, cellWidth, cellHeight)
        for index in range(0, numberOfFramesPerOrientation):
            bufferedImageArray[index + numberOfFramesPerOrientation] = self.getImage(bufferedImageArray[index], verticle, horizontal)
        return bufferedImageArray
# from java.awt import *
# from java.awt.geom.AffineTransform import AffineTransform
# from java.awt.image.AffineTransformOp import AffineTransformOp
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.media.image.ImageUtil import ImageUtil


MirrorImageUtil.instance = MirrorImageUtil()

