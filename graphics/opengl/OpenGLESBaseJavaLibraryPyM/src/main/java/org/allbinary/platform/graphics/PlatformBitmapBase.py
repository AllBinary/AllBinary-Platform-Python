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
# package org.allbinary.platform.graphics

from __future__ import annotations



class PlatformBitmapBase:
    NULL_PLATFORM_BITMAP_BASE: PlatformBitmapBase = None

    def _init_fields(self) -> None:
        self.alpha: int = 255
        self.basicColor: BasicColor = BasicColorFactory.getInstance().NULL_COLOR

    def __init__(self) -> None:
        self._init_fields()
    

    def getWidth(self) -> int:
        return 0
    

    def getHeight(self) -> int:
        return 0
    

    def getImage(self) -> Image:
        return NullImage.NULL_IMAGE
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory


PlatformBitmapBase.NULL_PLATFORM_BITMAP_BASE = PlatformBitmapBase()

