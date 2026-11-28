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
# package org.allbinary.media.image.analysis

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_divide
from java.lang.JavaRuntimeStatic import lazy_static


class ImageAnalysis:
    instance: ImageAnalysis = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> ImageAnalysis:
        return ImageAnalysis.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def process_j2_1(self, bufferedImageArray: list[BufferedImage], colorRangeInterface: ColorRangeInterface) -> list[ImageAnalysisResults]:
        from org.allbinary.string.CommonLabels import CommonLabels
        from org.allbinary.string.CommonStrings import CommonStrings
        commonStrings: CommonStrings = CommonStrings.getInstance()
        self.logUtil.putF(str(CommonLabels.getInstance().START) + str(colorRangeInterface), self, commonStrings.PROCESS)
        imageAnalysisResultsArray: list[ImageAnalysisResults] = [None] * (len(bufferedImageArray))
        for index in range(0, len(bufferedImageArray)):
            imageAnalysisResultsArray[index] = ImageAnalysis.process(bufferedImageArray[index], colorRangeInterface)
        return imageAnalysisResultsArray
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def process_j2_2(bufferedImage: BufferedImage, colorRangeInterface: ColorRangeInterface) -> ImageAnalysisResults:
        from org.allbinary.media.image.analysis.ImageAnalysisResults import ImageAnalysisResults
        from org.allbinary.graphics.color.ColorCacheFactory import ColorCacheFactory
        from org.allbinary.graphics.color.ColorCacheable import ColorCacheable
        imageAnalysisResults: ImageAnalysisResults = ImageAnalysisResults()
        redTotal: int = 0
        greenTotal: int = 0
        blueTotal: int = 0
        for indexY in range(0, bufferedImage.getHeight()):
            for indexX in range(0, bufferedImage.getWidth()):
                keyInteger: int = str(bufferedImage.getRGB(indexX, indexY))
                colorCacheable: ColorCacheable = ColorCacheFactory.getInstance().get(keyInteger)
                color: Color = colorCacheable.getColor()
                ImageAnalysis.processColorRangeResults(imageAnalysisResults, colorRangeInterface, color)
                ImageAnalysis.processImageColorResults(imageAnalysisResults.getImageColorResults(), colorRangeInterface, color)
                redTotal += color.getRed()
                greenTotal += color.getGreen()
                blueTotal += color.getBlue()
        totalPixels: int = imageAnalysisResults.getImageColorRangeResults().getTotalPixelsChecked()
        colorAverage: ColorAverage = imageAnalysisResults.getImageColorResults().getColorAverage()
        colorAverage.setAvgRed(float(redTotal) / float(totalPixels))
        colorAverage.setAvgGreen(float(greenTotal) / float(totalPixels))
        colorAverage.setAvgBlue(float(blueTotal) / float(totalPixels))
        return imageAnalysisResults

    def process(self, *args):
        if len(args) == 2 and True and (args[0] is None or isinstance(args[0], list)) and (args[1] is None or any(base.__name__ == "ColorRangeInterface" for base in type(args[1]).__mro__)):
            return __class__.__dict__["process_j2_1"].__get__(self, __class__)(*args)
        if len(args) == 2:
            return __class__.__dict__["process_j2_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("process_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().process(*args)
    

    @staticmethod
    def processColorRangeResults(imageAnalysisResults: ImageAnalysisResults, colorRangeInterface: ColorRangeInterface, color: Color) -> None:
        if colorRangeInterface.isInRange(color):
            imageAnalysisResults.getImageColorRangeResults().addMatchingPixelsChecked()
        else:
            pass
        imageAnalysisResults.getImageColorRangeResults().addTotalPixelsChecked()
    

    @staticmethod
    def processImageColorResults(imageColorResults: ImageColorResults, colorRangeInterface: ColorRangeInterface, color: Color) -> None:
        if color.getRed() < imageColorResults.getColorRange().getMinRed():
            imageColorResults.getColorRange().setMinRed(color.getRed())
        if color.getGreen() < imageColorResults.getColorRange().getMinGreen():
            imageColorResults.getColorRange().setMinGreen(color.getGreen())
        if color.getBlue() < imageColorResults.getColorRange().getMinBlue():
            imageColorResults.getColorRange().setMinBlue(color.getBlue())
        if color.getRed() > imageColorResults.getColorRange().getMaxRed():
            imageColorResults.getColorRange().setMaxRed(color.getRed())
        if color.getGreen() > imageColorResults.getColorRange().getMaxGreen():
            imageColorResults.getColorRange().setMaxGreen(color.getGreen())
        if color.getBlue() > imageColorResults.getColorRange().getMaxBlue():
            imageColorResults.getColorRange().setMaxBlue(color.getBlue())
# from java.awt.Color import Color
# from java.awt.image.BufferedImage import BufferedImage
# from org.allbinary.graphics.color.ColorCacheFactory import ColorCacheFactory
# from org.allbinary.graphics.color.ColorCacheable import ColorCacheable
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonLabels import CommonLabels
# from org.allbinary.string.CommonStrings import CommonStrings


def _ImageAnalysis_instance() -> object:
    return ImageAnalysis()

lazy_static(ImageAnalysis, "instance", _ImageAnalysis_instance)

