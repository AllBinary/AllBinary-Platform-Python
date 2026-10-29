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



class ImageColorRangeResults:

    def _init_fields(self) -> None:
        self.colorRangeInterface: ColorRangeInterface = None
        self.matchingPixelsChecked: int = 0
        self.totalPixelsChecked: int = 0
    

    def __init__(self) -> None:
        from org.allbinary.media.image.analysis.ColorRange import ColorRange
        self._init_fields()
        self.setColorRangeInterface(ColorRange())
    

    def getColorRangeInterface(self) -> ColorRangeInterface:
        return self.colorRangeInterface
    

    def setColorRangeInterface(self, colorRangeInterface: ColorRangeInterface) -> None:
        self.colorRangeInterface = colorRangeInterface
    

    def getMatchingPixelsChecked(self) -> int:
        return self.matchingPixelsChecked
    

    def setMatchingPixelsChecked(self, matchingPixelsChecked: int) -> None:
        self.matchingPixelsChecked = matchingPixelsChecked
    

    def addMatchingPixelsChecked(self) -> None:
        self.matchingPixelsChecked += 1
    

    def getTotalPixelsChecked(self) -> int:
        return self.totalPixelsChecked
    

    def addTotalPixelsChecked(self) -> None:
        self.totalPixelsChecked += 1
    

    def setTotalPixelsChecked(self, totalPixelsChecked: int) -> None:
        self.totalPixelsChecked = totalPixelsChecked
    

    def getPercent(self) -> float:
        return (float(self.getMatchingPixelsChecked()) / float(self.getTotalPixelsChecked()))


