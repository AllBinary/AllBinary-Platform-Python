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



class ImageAnalysisResults:

    def _init_fields(self) -> None:
        self.imageColorRangeResults: ImageColorRangeResults = None
        self.imageColorResults: ImageColorResults = None
        self.averageAmbientLevel: float = 0.0
    

    def __init__(self) -> None:
        from org.allbinary.media.image.analysis.ImageColorRangeResults import ImageColorRangeResults
        from org.allbinary.media.image.analysis.ImageColorResults import ImageColorResults
        self._init_fields()
        self.imageColorRangeResults = ImageColorRangeResults()
        self.imageColorResults = ImageColorResults()
    

    def getImageColorRangeResults(self) -> ImageColorRangeResults:
        return self.imageColorRangeResults
    

    def setImageColorRangeResults(self, imageColorRangeResults: ImageColorRangeResults) -> None:
        self.imageColorRangeResults = imageColorRangeResults
    

    def getAverageAmbientLevel(self) -> float:
        return self.averageAmbientLevel
    

    def setAverageAmbientLevel(self, averageAmbientLevel: float) -> None:
        self.averageAmbientLevel = averageAmbientLevel
    

    def getImageColorResults(self) -> ImageColorResults:
        return self.imageColorResults
    

    def setImageColorResults(self, imageColorResults: ImageColorResults) -> None:
        self.imageColorResults = imageColorResults


