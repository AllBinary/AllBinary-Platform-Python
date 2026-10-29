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
# package org.allbinary.media.image.comparison

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class ImageComparisonResultsEvent(AllBinaryEventObject):

    def _init_fields(self) -> None:
        self.imageComparisonResult: ImageComparisonResult = None
    

    def __init__(self, anyType: object, imageComparisonInfo: ImageComparisonResult) -> None:
        super().__init__(anyType)
        self._init_fields()
        self.setImageComparisonResult(imageComparisonInfo)
    

    def getImageComparisonResult(self) -> ImageComparisonResult:
        return self.imageComparisonResult
    

    def setImageComparisonResult(self, imageComparisonResult: ImageComparisonResult) -> None:
        self.imageComparisonResult = imageComparisonResult


