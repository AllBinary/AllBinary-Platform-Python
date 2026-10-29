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
# package org.allbinary.platform.opengles

from __future__ import annotations



class PlatformTextureBaseFactory:
    NULL_PLATFORM_TEXTURE_BASE_FACTORY: PlatformTextureBaseFactory = None

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    def load(self, gl: GL10, target: int, level: int, image: Image, border: int, flip: bool) -> None:
        pass
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Image import Image
from org.allbinary.string.CommonStrings import CommonStrings


PlatformTextureBaseFactory.NULL_PLATFORM_TEXTURE_BASE_FACTORY = PlatformTextureBaseFactory()

