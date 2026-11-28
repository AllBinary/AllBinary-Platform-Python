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

from java.lang.JavaRuntimeStatic import lazy_static


class BasicColorUtil:
    instance: BasicColorUtil = None

    def _init_fields(self) -> None:
        self.ZERO_ARRAY: list[BasicColor] = [None] * (0)
        self.ALPHA: int = 0xFF000000
        self.isAlpha: bool = True
        self.ffOpaque: bool = True

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    @staticmethod
    def getInstance() -> BasicColorUtil:
        return BasicColorUtil.instance
    

    def getRGB(self, red: int, green: int, blue: int) -> int:
        value: int = 0
        if self.isAlpha:
            if self.ffOpaque:
                value = self.ALPHA
        value = (((((red) << ((16) & 31)) + 0x80000000) % 0x100000000 - 0x80000000)) | value
        value = (((((green) << ((8) & 31)) + 0x80000000) % 0x100000000 - 0x80000000)) | value
        value = blue | value
        return value
    

    def getARGB(self, alphaValue: int, r: int, g: int, b: int) -> int:
        return ((((((alphaValue) << ((24) & 31)) + 0x80000000) % 0x100000000 - 0x80000000)) & self.ALPHA) + ((((((r) << ((16) & 31)) + 0x80000000) % 0x100000000 - 0x80000000)) & 0x00FF0000) + ((((((g) << ((8) & 31)) + 0x80000000) % 0x100000000 - 0x80000000)) & 0x0000FF00) + (b & 0x000000FF)
    

    def get(self, alphaValue: int, color: int) -> int:
        return ((((((alphaValue) << ((24) & 31)) + 0x80000000) % 0x100000000 - 0x80000000)) & self.ALPHA) + color
    

    def invert(self, color: int) -> int:
        return (0xFFFFFF - color) | self.ALPHA


def _BasicColorUtil_instance() -> object:
    return BasicColorUtil()

lazy_static(BasicColorUtil, "instance", _BasicColorUtil_instance)

