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
# package org.allbinary.graphics.color

from __future__ import annotations



class ColorTemperatureUtil:
    instance: ColorTemperatureUtil = None

    def _init_fields(self) -> None:
        self.basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ColorTemperatureUtil:
        return ColorTemperatureUtil.instance
    

    def getBasicColor(self, thirdTemp: int) -> BasicColor:
        basicColor: BasicColor = self.basicColorFactory.RED
        if thirdTemp > 3700:
            basicColor = self.basicColorFactory.PURPLE
        elif thirdTemp > 3200:
            basicColor = self.basicColorFactory.BLUE
        elif thirdTemp > 2700:
            basicColor = self.basicColorFactory.PUCE
        elif thirdTemp > 2200:
            basicColor = self.basicColorFactory.WHITE
        elif thirdTemp > 1700:
            basicColor = self.basicColorFactory.GREEN
        elif thirdTemp > 1200:
            basicColor = self.basicColorFactory.YELLOW
        elif thirdTemp > 700:
            basicColor = self.basicColorFactory.ORANGE
        return basicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory


ColorTemperatureUtil.instance = ColorTemperatureUtil()

