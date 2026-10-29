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



class ImageArrayRotationUtil:
    instance: ImageArrayRotationUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.TOTAL_ANGLE: str = "totalAngle: "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ImageArrayRotationUtil:
        return ImageArrayRotationUtil.instance
    

    # throws IOException
    def process(self, imageProcessorInput: ImageProcessorInput, input: str, visitor: ImageProcessedVisitor) -> None:
        from org.allbinary.media.image.ImageJ2SERotationUtil import ImageJ2SERotationUtil
        totalAngle: int = None
        if input == self.commonStrings.UP:
            totalAngle = str(-90)
        elif input == self.commonStrings.DOWN:
            totalAngle = str(90)
        else:
            totalAngle = str(input)
        generatedBufferedImage: BufferedImage = None
        bufferedImageArray: list[BufferedImage] = imageProcessorInput.getBufferedImageArray()
        for index in range(0, len(bufferedImageArray)):
            self.logUtil.putF(self.TOTAL_ANGLE + str(totalAngle), self, self.commonStrings.RUN)
            generatedBufferedImage = ImageJ2SERotationUtil.getInstance().getRotatedImage(bufferedImageArray[index], int(totalAngle))
            visitor.visit(generatedBufferedImage, input, index)
# from java.awt.image.BufferedImage import BufferedImage
# from java.io.IOException import IOException
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


ImageArrayRotationUtil.instance = ImageArrayRotationUtil()

