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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_divide
from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage


#This is not actually VBO impl
@java_inherited_overloads
class OpenGLESGL11VBOImage(OpenGLESImage):
    def _java_defaults(self):
        vars(self).setdefault("glUtil", None)
        vars(self).setdefault("textureVertexFloatBuffer", None)
        vars(self).setdefault("regionRectangleFloatArray", None)
        vars(self).setdefault("regionRectangleVertexFloatBuffer", None)
        vars(self).setdefault("regionTextureRectangleFloatArray", None)
        vars(self).setdefault("regionTextureVertexFloatBuffer", None)

    def _init_fields(self) -> None:
        from org.allbinary.opengles.GLUtil import GLUtil
        self.glUtil: GLUtil = GLUtil.getInstance()
        self.textureVertexFloatBuffer: FloatBuffer = ByteBuffer.allocateDirect(4 * 4 * 2).order(ByteOrder.nativeOrder()).asFloatBuffer()
        self.regionRectangleFloatArray: list[float] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.regionRectangleVertexFloatBuffer: FloatBuffer = ByteBuffer.allocateDirect(4 * 4 * 3).order(ByteOrder.nativeOrder()).asFloatBuffer()
        self.regionTextureRectangleFloatArray: list[float] = [0.0] * (8)
        self.regionTextureVertexFloatBuffer: FloatBuffer = ByteBuffer.allocateDirect(4 * 4 * 2).order(ByteOrder.nativeOrder()).asFloatBuffer()
    

    def __init__(self, image: Image, bitmapFactory: PlatformBitmapBaseFactory, textureFactory: PlatformTextureBaseFactory) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory
        from org.allbinary.platform.opengles.PlatformTextureBaseFactory import PlatformTextureBaseFactory
        super().__init__(image, bitmapFactory, textureFactory)
        __class__._init_fields(self)
        self.initVertices()
        self.regionRectangleVertexFloatBuffer.put(FloatBuffer.wrap(self.regionRectangleFloatArray))
        self.regionTextureVertexFloatBuffer.put(FloatBuffer.wrap(self.regionTextureRectangleFloatArray))
    

    def initVertices(self) -> None:
        self.textureVertexFloatBuffer.put(0.0)
        self.textureVertexFloatBuffer.put(1.0)
        self.textureVertexFloatBuffer.put(1.0)
        self.textureVertexFloatBuffer.put(1.0)
        self.textureVertexFloatBuffer.put(0.0)
        self.textureVertexFloatBuffer.put(0.0)
        self.textureVertexFloatBuffer.put(1.0)
        self.textureVertexFloatBuffer.put(0.0)
        self.textureVertexFloatBuffer.rewind()
    

    def set(self, gl: GL) -> None:
        from javax.microedition.khronos.opengles.GL import GL
        from javax.microedition.khronos.opengles.GL10 import GL10
        from org.allbinary.graphics.opengles.OpenGLLogUtil import OpenGLLogUtil
        gl10: GL10 = gl
        if java_super_call(super(), "initTexture", gl10):
            self.textureFactory.load(gl10, GL10.GL_TEXTURE_2D, 0, self, 0, True)
            gl10.glDisable(GL10.GL_TEXTURE_2D)
            OpenGLLogUtil.getInstance().logError(gl10, self)
    

    def drawRegion(self, gl: GL10, viewHeight: int, x_src: float, y_src: float, width: float, height: float, x: int, y: int, z: int) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        self.regionRectangleFloatArray[0] = float(x)
        self.regionRectangleFloatArray[7] = float(viewHeight - y)
        self.regionRectangleFloatArray[1] = self.regionRectangleFloatArray[7] - height
        self.regionRectangleFloatArray[3] = float(x) + width
        self.regionRectangleFloatArray[4] = self.regionRectangleFloatArray[1]
        self.regionRectangleFloatArray[6] = float(x)
        self.regionRectangleFloatArray[9] = self.regionRectangleFloatArray[3]
        self.regionRectangleFloatArray[10] = self.regionRectangleFloatArray[7]
        self.regionTextureRectangleFloatArray[0] = x_src / self.getWidth()
        self.regionTextureRectangleFloatArray[1] = (y_src + height) / self.getHeight()
        self.regionTextureRectangleFloatArray[2] = (x_src + width) / self.getWidth()
        self.regionTextureRectangleFloatArray[3] = self.regionTextureRectangleFloatArray[1]
        self.regionTextureRectangleFloatArray[4] = self.regionTextureRectangleFloatArray[0]
        self.regionTextureRectangleFloatArray[5] = y_src / self.getHeight()
        self.regionTextureRectangleFloatArray[6] = self.regionTextureRectangleFloatArray[2]
        self.regionTextureRectangleFloatArray[7] = self.regionTextureRectangleFloatArray[5]
        self.glUtil.position(self.regionRectangleVertexFloatBuffer, 0)
        gl.glVertexPointer(3, GL10.GL_FLOAT, 0, self.regionRectangleVertexFloatBuffer)
        gl.glEnableClientState(GL10.GL_VERTEX_ARRAY)
        gl.glEnable(GL10.GL_TEXTURE_2D)
        gl.glBindTexture(GL10.GL_TEXTURE_2D, self.openGLESImageProperties.textureID)
        gl.glEnableClientState(GL10.GL_TEXTURE_COORD_ARRAY)
        self.glUtil.position(self.regionTextureVertexFloatBuffer, 0)
        gl.glTexCoordPointer(2, GL10.GL_FLOAT, 0, self.regionTextureVertexFloatBuffer)
        gl.glDrawArrays(GL10.GL_TRIANGLE_STRIP, 0, 4)
        gl.glDisableClientState(GL10.GL_VERTEX_ARRAY)
        gl.glDisableClientState(GL10.GL_TEXTURE_COORD_ARRAY)
        gl.glDisable(GL10.GL_TEXTURE_2D)
    

    def draw(self, gl: GL10, x: int, y: int, z: int) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        self.regionRectangleFloatArray[0] = float(x)
        self.regionRectangleFloatArray[7] = float((DisplayInfoSingleton.getInstance().getLastHeight() - y))
        self.regionRectangleFloatArray[1] = self.regionRectangleFloatArray[7] - self.getHeight()
        self.regionRectangleFloatArray[3] = float((x + self.getWidth()))
        self.regionRectangleFloatArray[4] = self.regionRectangleFloatArray[1]
        self.regionRectangleFloatArray[6] = float(x)
        self.regionRectangleFloatArray[9] = self.regionRectangleFloatArray[3]
        self.regionRectangleFloatArray[10] = self.regionRectangleFloatArray[7]
        self.glUtil.position(self.regionRectangleVertexFloatBuffer, 0)
        gl.glVertexPointer(3, GL10.GL_FLOAT, 0, self.regionRectangleVertexFloatBuffer)
        gl.glEnableClientState(GL10.GL_VERTEX_ARRAY)
        gl.glEnable(GL10.GL_TEXTURE_2D)
        gl.glBindTexture(GL10.GL_TEXTURE_2D, self.openGLESImageProperties.textureID)
        gl.glEnableClientState(GL10.GL_TEXTURE_COORD_ARRAY)
        self.glUtil.position(self.textureVertexFloatBuffer, 0)
        gl.glTexCoordPointer(2, GL10.GL_FLOAT, 0, self.textureVertexFloatBuffer)
        gl.glDrawArrays(GL10.GL_TRIANGLE_STRIP, 0, 4)
        gl.glDisableClientState(GL10.GL_VERTEX_ARRAY)
        gl.glDisableClientState(GL10.GL_TEXTURE_COORD_ARRAY)
        gl.glDisable(GL10.GL_TEXTURE_2D)
# from java.nio.ByteBuffer import ByteBuffer
# from java.nio.ByteOrder import ByteOrder
# from java.nio.FloatBuffer import FloatBuffer
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.graphics.opengles.OpenGLLogUtil import OpenGLLogUtil
# from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
# from org.allbinary.opengles.GLUtil import GLUtil
# from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory
# from org.allbinary.platform.opengles.PlatformTextureBaseFactory import PlatformTextureBaseFactory


