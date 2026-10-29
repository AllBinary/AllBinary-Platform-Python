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
# package org.allbinary.animation.image

from __future__ import annotations

from org.allbinary.animation.image.ScaleBaseProcessor import ScaleBaseProcessor


class ScaleProcessor(ScaleBaseProcessor):
    instanceC: ScaleProcessor = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.imageScaleUtil: ImageScaleUtil = ImageScaleUtil.getInstance()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ScaleBaseProcessor:
        return ScaleProcessor.instanceC
    

    def update(self, originalImage: Image, originalImageArray: list[Image], ximageToShowArray: list[Image], unused: int, scaleX: float, scaleY: float, maxScaleX: float, maxScaleY: float) -> None:
        try:
            self.imageScaleUtil.scale2(originalImage, originalImageArray, ximageToShowArray, unused, scaleX, scaleY, maxScaleX, maxScaleY)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.UPDATE, e)
# from javax.microedition.lcdui.Image import Image
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.media.image.ImageScaleUtil import ImageScaleUtil
from org.allbinary.string.CommonStrings import CommonStrings


ScaleProcessor.instanceC = ScaleProcessor()

