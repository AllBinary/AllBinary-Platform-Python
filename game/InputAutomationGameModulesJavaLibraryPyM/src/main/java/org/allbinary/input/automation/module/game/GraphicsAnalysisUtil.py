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
# package org.allbinary.input.automation.module.game

from __future__ import annotations



class GraphicsAnalysisUtil:
    MAX: int = 122
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getNominator(bufferedImage: BufferedImage, min_x: int, max_x: int, y: int) -> float:
        for index in range(int(max_x), int(min_x), -1):
            colorInteger: int = str(bufferedImage.getRGB(index, int(y)))
            automaticCacheInterface: AutomaticCacheInterface = ColorCacheFactory.getInstance()
            colorCacheable: ColorCacheable = automaticCacheInterface.get(colorInteger)
            color: Color = colorCacheable.getColor()
            if color.getRed() < GraphicsAnalysisUtil.MAX and color.getGreen() < GraphicsAnalysisUtil.MAX and color.getBlue() < GraphicsAnalysisUtil.MAX:
                pass
            else:
                return index - int(min_x)
        return 0.0
# from java.awt import *
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.graphics.color.ColorCacheFactory import ColorCacheFactory
from org.allbinary.graphics.color.ColorCacheable import ColorCacheable
from org.allbinary.logic.util.cache.AutomaticCacheInterface import AutomaticCacheInterface


