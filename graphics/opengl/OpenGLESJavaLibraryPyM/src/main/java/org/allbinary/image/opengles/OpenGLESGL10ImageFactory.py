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
# package org.allbinary.image.opengles

from __future__ import annotations

from org.allbinary.image.opengles.OpenGLImageFactory import OpenGLImageFactory


class OpenGLESGL10ImageFactory(OpenGLImageFactory):

    def __init__(self) -> None:
        super().__init__()
    

    def getInstance(self, image: Image, bitmapFactory: PlatformBitmapBaseFactory, textureFactory: PlatformTextureBaseFactory) -> Image:
        from org.allbinary.image.opengles.OpenGLESGL10Image import OpenGLESGL10Image
        return OpenGLESGL10Image(image, bitmapFactory, textureFactory)
# from javax.microedition.lcdui.Image import Image
from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory
from org.allbinary.platform.opengles.PlatformTextureBaseFactory import PlatformTextureBaseFactory


