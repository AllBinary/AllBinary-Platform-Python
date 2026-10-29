# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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



class CanvasExpandUtil:
    instance: CanvasExpandUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.stringUtil: StringUtil = StringUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CanvasExpandUtil:
        return CanvasExpandUtil.instance
    

    # throws Exception
    def process(self, imageProcessorInput: ImageProcessorInput, increaseX: int, increaseY: int, visitor: ImageProcessedVisitor) -> None:
        from org.allbinary.media.image.ImageUtil import ImageUtil
        imageUtil: ImageUtil = ImageUtil.getInstance()
        bufferedImageArray: list[BufferedImage] = imageProcessorInput.getBufferedImageArray()
        subBufferedImageArray: list[BufferedImage] = [None] * (len(bufferedImageArray))
        size: int = len(bufferedImageArray)
        bufferedImage: BufferedImage = None
        for index in range(0, size):
            bufferedImage = bufferedImageArray[index]
            subBufferedImageArray[index] = imageUtil.createBufferedImage(bufferedImage, bufferedImage.getWidth() + increaseX, bufferedImage.getHeight() + increaseY, False)
            visitor.visit(subBufferedImageArray[index], self.stringUtil.EMPTY_STRING, index)
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil


CanvasExpandUtil.instance = CanvasExpandUtil()

