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

from java.lang.JavaRuntimeStatic import lazy_static


class PlatformBitmapBaseFactory:
    NULL_PLATFORM_BITMAP_BASE_FACTORY: PlatformBitmapBaseFactory = None
    

    def createBitmap(self, image: Image) -> PlatformBitmapBase:
        from org.allbinary.platform.graphics.PlatformBitmapBase import PlatformBitmapBase
        from javax.microedition.lcdui.Image import Image
        return PlatformBitmapBase.NULL_PLATFORM_BITMAP_BASE
# from javax.microedition.lcdui.Image import Image


def _PlatformBitmapBaseFactory_NULL_PLATFORM_BITMAP_BASE_FACTORY() -> object:
    return PlatformBitmapBaseFactory()

lazy_static(PlatformBitmapBaseFactory, "NULL_PLATFORM_BITMAP_BASE_FACTORY", _PlatformBitmapBaseFactory_NULL_PLATFORM_BITMAP_BASE_FACTORY)

