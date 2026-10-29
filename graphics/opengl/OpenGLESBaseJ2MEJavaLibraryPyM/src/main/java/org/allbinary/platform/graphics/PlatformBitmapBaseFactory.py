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



class PlatformBitmapBaseFactory:
    NULL_PLATFORM_BITMAP_BASE_FACTORY: PlatformBitmapBaseFactory = None
    

    def createBitmap(self, image: Image) -> PlatformBitmapBase:
        raise RuntimeError()
# from javax.microedition.lcdui.Image import Image


PlatformBitmapBaseFactory.NULL_PLATFORM_BITMAP_BASE_FACTORY = PlatformBitmapBaseFactory()

