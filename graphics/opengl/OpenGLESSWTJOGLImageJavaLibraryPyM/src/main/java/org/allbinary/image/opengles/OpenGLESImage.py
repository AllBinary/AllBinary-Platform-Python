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

# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory
from org.allbinary.platform.opengles.PlatformTextureBaseFactory import PlatformTextureBaseFactory
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.image.opengles.OpenGLSurfaceChangedInterface import OpenGLSurfaceChangedInterface


#OpenGLESSWTJOGLImageJavaLibrary
class OpenGLESImage(Image, OpenGLSurfaceChangedInterface):
    NULL_OPENGL_IMAGE: OpenGLESImage = None
    texture2dList: BasicArrayList = BasicArrayListD()
    TYPE: int = 4

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.textureFactory: PlatformTextureBaseFactory = None
        self.openGLBitmap: PlatformBitmapBase = None
        self.imageProcessor: OpenGLESImageProcessor = OpenGLESImageProcessor.getInstance()
        self.openGLESImageTranslate: OpenGLESImageTranslate = OpenGLESImageTranslate.getInstance()
        self.openGLESImageProperties: OpenGLESImageProperties = OpenGLESImageProperties()
    

    def __init__(self, image: Image, bitmapFactory: PlatformBitmapBaseFactory, textureFactory: PlatformTextureBaseFactory) -> None:
        from org.allbinary.image.opengles.OpenGLImageCacheFactory import OpenGLImageCacheFactory
        super().__init__(image.getName(), PostLoadImageProcessor.NULL_POST_LOAD_IMAGE_PROCESSOR)
        self._init_fields()
        self.openGLBitmap = bitmapFactory.createBitmap(image)
        self.textureFactory = textureFactory
        OpenGLImageCacheFactory.getInstance().init(self)
        self.platformImage = OpenGLESPostLoadPlatformImage.getInstance()
    

    def getHeight(self) -> int:
        return int((self.openGLBitmap.getHeight() * self.openGLESImageProperties.scaleY2))
    

    def getWidth(self) -> int:
        return int((self.openGLBitmap.getWidth() * self.openGLESImageProperties.scaleX2))
    

    # throws Exception
    def set(self, gl: GL) -> None:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    def initTexture(self, gl: GL10) -> bool:
        if not OpenGLESImage.texture2dList.contains(self):
            OpenGLESImage.texture2dList.add(self)
            textures: list[int] = [0] * (1)
            gl.glEnable(self.GL10.GL_TEXTURE_2D)
            if self.openGLESImageProperties.textureID != -1:
                textures[0] = self.openGLESImageProperties.textureID
                gl.glDeleteTextures(1, textures, 0)
            gl.glGenTextures(1, textures, 0)
            self.openGLESImageProperties.textureID = textures[0]
            gl.glBindTexture(self.GL10.GL_TEXTURE_2D, self.openGLESImageProperties.textureID)
            gl.glTexParameterf(self.GL10.GL_TEXTURE_2D, self.GL10.GL_TEXTURE_MIN_FILTER, self.GL10.GL_NEAREST)
            gl.glTexParameterf(self.GL10.GL_TEXTURE_2D, self.GL10.GL_TEXTURE_WRAP_S, self.GL10.GL_CLAMP_TO_EDGE)
            gl.glTexParameterf(self.GL10.GL_TEXTURE_2D, self.GL10.GL_TEXTURE_WRAP_T, self.GL10.GL_CLAMP_TO_EDGE)
            return True
        return False
    

    def drawRegion(self, gl: GL10, viewHeight: int, x_src: float, y_src: float, width: float, height: float, x: int, y: int, z: int) -> None:
        pass
    

    def draw(self, gl: GL10, x: int, y: int, z: int) -> None:
        pass
    

    def getType(self) -> int:
        return OpenGLESImage.TYPE
    

    def toString(self) -> str:
        graphicsStrings: GraphicsStrings = GraphicsStrings.getInstance()
        return str(StringMaker().append(self.getName()).append(str(super())).append(graphicsStrings.OPACITY).appendfloat(float(self.openGLESImageProperties.alphaf)))

    def __str__(self) -> str:
        return self.toString()
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.OpenGLESPostLoadPlatformImage import OpenGLESPostLoadPlatformImage
# from javax.microedition.lcdui.PostLoadImageProcessor import PostLoadImageProcessor
from org.allbinary.graphics.GraphicsStrings import GraphicsStrings
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.platform.graphics.PlatformBitmapBase import PlatformBitmapBase
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.image.opengles.OpenGLESImageProcessor import OpenGLESImageProcessor
from org.allbinary.image.opengles.OpenGLESImageTranslate import OpenGLESImageTranslate
from org.allbinary.image.opengles.OpenGLESImageProperties import OpenGLESImageProperties


OpenGLESImage.NULL_OPENGL_IMAGE = OpenGLESImage(NullImage.NULL_IMAGE, PlatformBitmapBaseFactory.NULL_PLATFORM_BITMAP_BASE_FACTORY, PlatformTextureBaseFactory.NULL_PLATFORM_TEXTURE_BASE_FACTORY)

