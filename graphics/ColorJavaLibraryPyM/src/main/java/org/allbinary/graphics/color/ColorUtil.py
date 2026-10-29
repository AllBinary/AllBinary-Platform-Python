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
# package org.allbinary.graphics.color

from __future__ import annotations

import math


class ColorUtil:
    instance: ColorUtil = None
    

    @staticmethod
    def getInstance() -> ColorUtil:
        return ColorUtil.instance
    

    def isGreyishOrWhiteLike(self, color: Color) -> bool:
        if abs(color.getRed() - color.getGreen()) > 20 or abs(color.getRed() - color.getBlue()) > 20 or abs(color.getGreen() - color.getBlue()) > 20:
            return False
        return True
    

    def isDark(self, color: Color) -> bool:
        if color.getRed() < 0x77 and color.getRed() < 0x77 and color.getRed() < 0x77:
            return True
        return False
# from java.awt import *


ColorUtil.instance = ColorUtil()

