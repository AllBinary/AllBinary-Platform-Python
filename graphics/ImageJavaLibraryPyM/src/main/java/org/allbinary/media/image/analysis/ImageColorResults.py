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



class ImageColorResults:

    def _init_fields(self) -> None:
        self.colorRange: ColorRange = None
        self.colorAverage: ColorAverage = None
    

    def __init__(self) -> None:
        from org.allbinary.media.image.analysis.ColorRange import ColorRange
        from org.allbinary.media.image.analysis.ColorAverage import ColorAverage
        self._init_fields()
        self.setColorRange(ColorRange())
        self.getColorRange().setMaxRed(-1)
        self.getColorRange().setMaxGreen(-1)
        self.getColorRange().setMaxBlue(-1)
        self.getColorRange().setMinRed(256)
        self.getColorRange().setMinGreen(256)
        self.getColorRange().setMinBlue(256)
        self.setColorAverage(ColorAverage())
    

    def getColorRange(self) -> ColorRange:
        return self.colorRange
    

    def setColorRange(self, colorRange: ColorRange) -> None:
        self.colorRange = colorRange
    

    def getColorAverage(self) -> ColorAverage:
        return self.colorAverage
    

    def setColorAverage(self, colorAverage: ColorAverage) -> None:
        self.colorAverage = colorAverage


