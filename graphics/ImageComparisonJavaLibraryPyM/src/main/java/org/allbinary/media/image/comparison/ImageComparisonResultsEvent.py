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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


@java_inherited_overloads
class ImageComparisonResultsEvent(AllBinaryEventObject):
    def _java_defaults(self):
        vars(self).setdefault("imageComparisonResult", None)

    def _init_fields(self) -> None:
        if "imageComparisonResult" not in vars(self): self.imageComparisonResult: ImageComparisonResult = None
    

    def __init__(self, anyType: object, imageComparisonInfo: ImageComparisonResult) -> None:
        __class__._java_defaults(self)
        super().__init__(anyType)
        __class__._init_fields(self)
        self.setImageComparisonResult(imageComparisonInfo)
    

    def getImageComparisonResult(self) -> ImageComparisonResult:
        return self.imageComparisonResult
    

    def setImageComparisonResult(self, imageComparisonResult: ImageComparisonResult) -> None:
        self.imageComparisonResult = imageComparisonResult


