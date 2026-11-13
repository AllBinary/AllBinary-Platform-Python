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

from java.lang.JavaRuntimeStatic import lazy_static
from javax.microedition.lcdui.Image import Image
from org.allbinary.image.opengles.OpenGLSurfaceChangedInterface import OpenGLSurfaceChangedInterface


#OpenGLESNullImageJavaLibrary
class OpenGLESImage(Image, OpenGLSurfaceChangedInterface):
    NULL_OPENGL_IMAGE: OpenGLESImage = None
    texture2dList: BasicArrayList = None
    TYPE: int = 4

    def _init_fields(self) -> None:
        from org.allbinary.platform.graphics.PlatformBitmapBase import PlatformBitmapBase
        from org.allbinary.platform.opengles.PlatformTextureBaseFactory import PlatformTextureBaseFactory
        from org.allbinary.string.CommonStrings import CommonStrings
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.textureFactory: PlatformTextureBaseFactory = None
        self.openGLBitmap: PlatformBitmapBase = None
        self.openGLESImageProperties: OpenGLESImageProperties = OpenGLESImageProperties()
        self.imageProcessor: OpenGLESImageProcessor = OpenGLESImageProcessor.getInstance()
        self.openGLESImageTranslate: OpenGLESImageTranslate = OpenGLESImageTranslate.getInstance()
    

    def __init__(self, image: Image, bitmapFactory: PlatformBitmapBaseFactory, textureFactory: PlatformTextureBaseFactory) -> None:
        from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory
        from org.allbinary.platform.opengles.PlatformTextureBaseFactory import PlatformTextureBaseFactory
        super().__init__()
        self._init_fields()
        self.openGLBitmap = bitmapFactory.createBitmap(image)
        self.textureFactory = textureFactory
    

    # throws Exception
    def set(self, gl: GL) -> None:
        from javax.microedition.khronos.opengles.GL import GL
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    def initTexture(self, gl: GL10) -> bool:
        from javax.microedition.khronos.opengles.GL10 import GL10
        return False
    

    def drawRegion(self, gl: GL10, viewHeight: int, x_src: float, y_src: float, width: float, height: float, x: int, y: int, z: int) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        pass
    

    def draw(self, gl: GL10, x: int, y: int, z: int) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        pass
    

    def getType(self) -> int:
        return OpenGLESImage.TYPE
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.NullImage import NullImage
# from org.allbinary.platform.graphics.PlatformBitmapBase import PlatformBitmapBase
# from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory
# from org.allbinary.platform.opengles.PlatformTextureBaseFactory import PlatformTextureBaseFactory
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.image.opengles.OpenGLESImageProperties import OpenGLESImageProperties
from org.allbinary.image.opengles.OpenGLESImageProcessor import OpenGLESImageProcessor
from org.allbinary.image.opengles.OpenGLESImageTranslate import OpenGLESImageTranslate


def _OpenGLESImage_NULL_OPENGL_IMAGE() -> object:
    from javax.microedition.lcdui.NullImage import NullImage
    from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory
    from org.allbinary.platform.opengles.PlatformTextureBaseFactory import PlatformTextureBaseFactory
    return OpenGLESImage(NullImage.NULL_IMAGE, PlatformBitmapBaseFactory.NULL_PLATFORM_BITMAP_BASE_FACTORY, PlatformTextureBaseFactory.NULL_PLATFORM_TEXTURE_BASE_FACTORY)

lazy_static(OpenGLESImage, "NULL_OPENGL_IMAGE", _OpenGLESImage_NULL_OPENGL_IMAGE)

def _OpenGLESImage_texture2dList() -> object:
    from org.allbinary.util.BasicArrayList import BasicArrayList
    from org.allbinary.util.BasicArrayListD import BasicArrayListD
    return BasicArrayListD()

lazy_static(OpenGLESImage, "texture2dList", _OpenGLESImage_texture2dList)

