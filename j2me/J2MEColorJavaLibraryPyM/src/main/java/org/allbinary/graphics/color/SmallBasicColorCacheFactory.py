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



class SmallBasicColorCacheFactory:
    instance: SmallBasicColorCacheFactory = None

    def _init_fields(self) -> None:
        self.SIZE: int = 255
        self.INDEX_TO_COLOR: list[int] = [0] * (self.SIZE)
        self.BASIC_COLOR_ARRAY: list[BasicColor] = [None] * (self.SIZE)
        self.colorIndex: int = 0
    

    @staticmethod
    def getInstance() -> SmallBasicColorCacheFactory:
        return SmallBasicColorCacheFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def add(self, basicDefaultColor: BasicColor) -> None:
        self.BASIC_COLOR_ARRAY[self.colorIndex] = basicDefaultColor
        self.INDEX_TO_COLOR[self.colorIndex] = int(basicDefaultColor)
        self.colorIndex += 1
    

    def getAndOrCreate(self, colorAsInt: int) -> BasicColor:
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        basicColor: BasicColor = None
        for index in range(0, self.SIZE):
            if self.INDEX_TO_COLOR[index] == colorAsInt:
                return self.BASIC_COLOR_ARRAY[index]
        ALPHA_MASK: int = 0xFF000000
        basicColor = BasicColorFactory.getInstance().createInstanceAN(colorAsInt & ALPHA_MASK, colorAsInt & 0x00FFFFFF, StringUtil.getInstance().EMPTY_STRING)
        self.add(basicColor)
        return basicColor
from org.allbinary.logic.string.StringUtil import StringUtil


SmallBasicColorCacheFactory.instance = SmallBasicColorCacheFactory()

