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



class BasicColorUtil:
    instance: BasicColorUtil = None

    def _init_fields(self) -> None:
        self.ZERO_ARRAY: list[BasicColor] = [None] * (0)
        self.ALPHA: int = 0xFF000000
        self.isAlpha: bool = True
        self.ffOpaque: bool = True

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BasicColorUtil:
        return BasicColorUtil.instance
    

    def getRGB(self, red: int, green: int, blue: int) -> int:
        value: int = 0
        if self.isAlpha:
            if self.ffOpaque:
                value = self.ALPHA
        value = (red << 16) | value
        value = (green << 8) | value
        value = blue | value
        return value
    

    def getARGB(self, alphaValue: int, r: int, g: int, b: int) -> int:
        return ((alphaValue << 24) & self.ALPHA) + ((r << 16) & 0x00FF0000) + ((g << 8) & 0x0000FF00) + (b & 0x000000FF)
    

    def get(self, alphaValue: int, color: int) -> int:
        return ((alphaValue << 24) & self.ALPHA) + color
    

    def invert(self, color: int) -> int:
        return (0xFFFFFF - color) | self.ALPHA


BasicColorUtil.instance = BasicColorUtil()

