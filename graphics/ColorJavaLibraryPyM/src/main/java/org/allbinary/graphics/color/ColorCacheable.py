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

from org.allbinary.logic.util.cache.CacheableInterface import CacheableInterface


class ColorCacheable(CacheableInterface):

    def _init_fields(self) -> None:
        self.key: object = None
        self.color: Color = None
    

    def __init__(self, key: object) -> None:
        from org.allbinary.graphics.color.Color import Color
        self._init_fields()
        self.key = key
        self.color = Color(int((key)))
    

    def getKey(self) -> object:
        return self.key
    

    def getColor(self) -> Color:
        return self.color
    

    def setColor(self, color: Color) -> None:
        self.color = color
# from java.awt import *


