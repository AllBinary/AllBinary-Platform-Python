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

from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage


class OpenGLESGL10Image(OpenGLESImage):

    def _init_fields(self) -> None:
        self.textureVertexFloatBuffer: FloatBuffer = ByteBuffer.allocateDirect(4 * 4 * 2).order(ByteOrder.nativeOrder()).asFloatBuffer()
        self.realOpenGLESImageDraw: OpenGLESImageDraw = (OpenGLESImageDraw()  # Java anonymous class body:
#         self.glUtil: GLUtil = GLUtil.getInstance()
#         self.displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
#         self.textureVertexFloatBuffer: FloatBuffer = self.textureVertexFloatBuffer
#         self.regionTextureRectangleFloatArray: list[float] = [0.0] * (8)
#         self.regionTextureVertexFloatBuffer: FloatBuffer = ByteBuffer.allocateDirect(4 * 4 * 2).order(ByteOrder.nativeOrder()).asFloatBuffer()
#         self.regionRectangleFloatArray: list[float] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#         self.regionRectangleVertexFloatBuffer: FloatBuffer = ByteBuffer.allocateDirect(4 * 4 * 3).order(ByteOrder.nativeOrder()).asFloatBuffer()
#         self.openGLESImageProperties: OpenGLESImageProperties = self.openGLESImageProperties
#         
# 
#         def drawRegion(self, gl: GL10, viewHeight: int, x_src: float, y_src: float, width: float, height: float, x: int, y: int, z: int) -> None:
#             imageWidth: int = self.getWidth()
#             imageHeight: int = self.getHeight()
#             self.regionRectangleFloatArray[7] = viewHeight
#             self.regionRectangleFloatArray[1] = self.regionRectangleFloatArray[7] - height
#             self.regionRectangleFloatArray[3] = width
#             self.regionRectangleFloatArray[4] = self.regionRectangleFloatArray[1]
#             self.regionRectangleFloatArray[9] = self.regionRectangleFloatArray[3]
#             self.regionRectangleFloatArray[10] = self.regionRectangleFloatArray[7]
#             self.regionTextureRectangleFloatArray[0] = x_src / imageWidth
#             self.regionTextureRectangleFloatArray[1] = ((y_src + height)) / imageHeight
#             self.regionTextureRectangleFloatArray[2] = ((x_src + width)) / imageWidth
#             self.regionTextureRectangleFloatArray[3] = self.regionTextureRectangleFloatArray[1]
#             self.regionTextureRectangleFloatArray[4] = self.regionTextureRectangleFloatArray[0]
#             self.regionTextureRectangleFloatArray[5] = y_src / imageHeight
#             self.regionTextureRectangleFloatArray[6] = self.regionTextureRectangleFloatArray[2]
#             self.regionTextureRectangleFloatArray[7] = self.regionTextureRectangleFloatArray[5]
#             u_center: float = (self.regionTextureRectangleFloatArray[0] + self.regionTextureRectangleFloatArray[2]) / 2.0
#             v_center: float = (self.regionTextureRectangleFloatArray[5] + self.regionTextureRectangleFloatArray[1]) / 2.0
#             self.glUtil.rotateUVs(self.regionTextureRectangleFloatArray, -self.openGLESImageProperties.angle, u_center, v_center)
#             gl.glPushMatrix()
#             imageProcessor: OpenGLESImageProcessor = self.imageProcessor
#             self.openGLESImageTranslate.translate(gl, self, x, -y)
#             imageProcessor.scale(gl, self.openGLESImageProperties.scaleX, self.openGLESImageProperties.scaleY)
#             imageProcessor.colorMask(gl, self.openGLESImageProperties.redf, self.openGLESImageProperties.greenf, self.openGLESImageProperties.bluef, self.openGLESImageProperties.alphaf)
#             self.openGLESImageTranslate.translate2(gl, self)
#             self.regionRectangleVertexFloatBuffer.put(self.regionRectangleFloatArray)
#             self.glUtil.position(self.regionRectangleVertexFloatBuffer, 0)
#             gl.glVertexPointer(3, self.GL10.GL_FLOAT, 0, self.regionRectangleVertexFloatBuffer)
#             gl.glEnableClientState(self.GL10.GL_VERTEX_ARRAY)
#             gl.glEnable(self.GL10.GL_TEXTURE_2D)
#             gl.glBindTexture(self.GL10.GL_TEXTURE_2D, self.openGLESImageProperties.textureID)
#             gl.glEnableClientState(self.GL10.GL_TEXTURE_COORD_ARRAY)
#             self.regionTextureVertexFloatBuffer.put(self.regionTextureRectangleFloatArray)
#             self.glUtil.position(self.regionTextureVertexFloatBuffer, 0)
#             gl.glTexCoordPointer(2, self.GL10.GL_FLOAT, 0, self.regionTextureVertexFloatBuffer)
#             gl.glDrawArrays(self.GL10.GL_TRIANGLE_STRIP, 0, 4)
#             gl.glDisableClientState(self.GL10.GL_VERTEX_ARRAY)
#             gl.glDisableClientState(self.GL10.GL_TEXTURE_COORD_ARRAY)
#             gl.glDisable(self.GL10.GL_TEXTURE_2D)
#             gl.glPopMatrix()
#         
# 
#         def draw(self, gl: GL10, x: int, y: int, z: int) -> None:
#             width: int = self.getWidth()
#             height: int = self.getHeight()
#             self.regionRectangleFloatArray[7] = self.displayInfoSingleton.getLastHeight()
#             self.regionRectangleFloatArray[1] = self.regionRectangleFloatArray[7] - height
#             self.regionRectangleFloatArray[3] = width
#             self.regionRectangleFloatArray[4] = self.regionRectangleFloatArray[1]
#             self.regionRectangleFloatArray[9] = self.regionRectangleFloatArray[3]
#             self.regionRectangleFloatArray[10] = self.regionRectangleFloatArray[7]
#             self.regionTextureRectangleFloatArray[0] = 0
#             self.regionTextureRectangleFloatArray[1] = 1
#             self.regionTextureRectangleFloatArray[2] = 1
#             self.regionTextureRectangleFloatArray[3] = 1
#             self.regionTextureRectangleFloatArray[4] = 0
#             self.regionTextureRectangleFloatArray[5] = 0
#             self.regionTextureRectangleFloatArray[6] = 1
#             self.regionTextureRectangleFloatArray[7] = 0
#             gl.glPushMatrix()
#             self.openGLESImageTranslate.translate(gl, self, x, -y)
#             imageProcessor: OpenGLESImageProcessor = self.imageProcessor
#             imageProcessor.scale(gl, self.openGLESImageProperties.scaleX, self.openGLESImageProperties.scaleY)
#             imageProcessor.colorMask(gl, self.openGLESImageProperties.redf, self.openGLESImageProperties.greenf, self.openGLESImageProperties.bluef, self.openGLESImageProperties.alphaf)
#             self.openGLESImageTranslate.translate2(gl, self)
#             self.regionRectangleVertexFloatBuffer.put(self.regionRectangleFloatArray)
#             self.glUtil.position(self.regionRectangleVertexFloatBuffer, 0)
#             gl.glVertexPointer(3, self.GL10.GL_FLOAT, 0, self.regionRectangleVertexFloatBuffer)
#             gl.glEnableClientState(self.GL10.GL_VERTEX_ARRAY)
#             gl.glEnable(self.GL10.GL_TEXTURE_2D)
#             gl.glBindTexture(self.GL10.GL_TEXTURE_2D, self.openGLESImageProperties.textureID)
#             gl.glEnableClientState(self.GL10.GL_TEXTURE_COORD_ARRAY)
#             self.glUtil.rotateUVs(self.regionTextureRectangleFloatArray, -self.openGLESImageProperties.angle, 0.5, 0.5)
#             self.glUtil.position(self.textureVertexFloatBuffer, 0)
#             self.textureVertexFloatBuffer.put(self.regionTextureRectangleFloatArray)
#             self.glUtil.position(self.textureVertexFloatBuffer, 0)
#             gl.glTexCoordPointer(2, self.GL10.GL_FLOAT, 0, self.textureVertexFloatBuffer)
#             gl.glDrawArrays(self.GL10.GL_TRIANGLE_STRIP, 0, 4)
#             gl.glDisableClientState(self.GL10.GL_VERTEX_ARRAY)
#             gl.glDisableClientState(self.GL10.GL_TEXTURE_COORD_ARRAY)
#             gl.glDisable(self.GL10.GL_TEXTURE_2D)
#             gl.glPopMatrix()
)
        self.openGLESImageDraw: OpenGLESImageDraw = OpenGLESImageDraw.getInstance()
    

    def __init__(self, image: Image, bitmapFactory: PlatformBitmapBaseFactory, textureFactory: PlatformTextureBaseFactory) -> None:
        super().__init__(image, bitmapFactory, textureFactory)
        self._init_fields()
        self.initVertices()
    

    def initVertices(self) -> None:
        self.textureVertexFloatBuffer.put(0)
        self.textureVertexFloatBuffer.put(1)
        self.textureVertexFloatBuffer.put(1)
        self.textureVertexFloatBuffer.put(1)
        self.textureVertexFloatBuffer.put(0)
        self.textureVertexFloatBuffer.put(0)
        self.textureVertexFloatBuffer.put(1)
        self.textureVertexFloatBuffer.put(0)
        self.textureVertexFloatBuffer.rewind()
    

    def set(self, gl: GL) -> None:
        gl10: GL10 = gl
        if super().initTexture(gl10):
            self.textureFactory.load(gl10, self.GL10.GL_TEXTURE_2D, 0, self, 0, True)
            gl10.glDisable(self.GL10.GL_TEXTURE_2D)
            self.openGLESImageDraw = self.realOpenGLESImageDraw
            OpenGLLogUtil.getInstance().logError(gl10, self)
    

    def drawRegion(self, gl: GL10, viewHeight: int, x_src: float, y_src: float, width: float, height: float, x: int, y: int, z: int) -> None:
        self.openGLESImageDraw.drawRegion(gl, viewHeight, x_src, y_src, width, height, x, y, z)
    

    def draw(self, gl: GL10, x: int, y: int, z: int) -> None:
        self.openGLESImageDraw.draw(gl, x, y, z)
# from java.nio.ByteBuffer import ByteBuffer
# from java.nio.ByteOrder import ByteOrder
# from java.nio.FloatBuffer import FloatBuffer
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Image import Image
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.opengles.OpenGLLogUtil import OpenGLLogUtil
from org.allbinary.opengles.GLUtil import GLUtil
from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory
from org.allbinary.platform.opengles.PlatformTextureBaseFactory import PlatformTextureBaseFactory
from org.allbinary.image.opengles.OpenGLESImageDraw import OpenGLESImageDraw


