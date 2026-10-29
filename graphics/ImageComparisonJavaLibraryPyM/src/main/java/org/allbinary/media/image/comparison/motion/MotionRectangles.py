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
# package org.allbinary.media.image.comparison.motion

from __future__ import annotations



class MotionRectangles:

    def _init_fields(self) -> None:
        self.name: str = None
        self.rectangleVector: BasicArrayList = None
        self.imageComparisonResult: ImageComparisonResult = None
        self.MAX_PIXEL_DISTANCE_THRESHOLD: int = 2
    

    def __init__(self, name: str, imageComparisonResult: ImageComparisonResult) -> None:
        self._init_fields()
        self.name = name
        self.setImageComparisonResult(imageComparisonResult)
        self.setVector(BasicArrayListD())
    

    def getVector(self) -> BasicArrayList:
        return self.rectangleVector
    

    def setVector(self, rectangleVector: BasicArrayList) -> None:
        self.rectangleVector = rectangleVector
    

    def getName(self) -> str:
        return self.name
    

    def getImageComparisonResult(self) -> ImageComparisonResult:
        return self.imageComparisonResult
    

    def setImageComparisonResult(self, imageComparisonResult: ImageComparisonResult) -> None:
        self.imageComparisonResult = imageComparisonResult
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.media.image.comparison.ImageComparisonResult import ImageComparisonResult


