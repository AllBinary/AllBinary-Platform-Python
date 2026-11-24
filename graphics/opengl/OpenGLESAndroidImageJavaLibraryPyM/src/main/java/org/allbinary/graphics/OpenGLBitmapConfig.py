# 
# AllBinary Open License Version 1 
# Copyright (c) 2026 AllBinary 
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
# package org.allbinary.graphics

from __future__ import annotations



class OpenGLBitmapConfig:

    def _init_fields(self) -> None:
        from android.graphics.Bitmap import Bitmap
        self.bitmapConfig: Config = None
    

    def __init__(self, bitmapConfig: Config) -> None:
        from android.graphics.Bitmap import Bitmap
        self._init_fields()
        self.bitmapConfig = bitmapConfig
# from android.graphics.Bitmap import Bitmap


