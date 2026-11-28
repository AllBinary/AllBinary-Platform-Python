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


@java_inherited_overloads
class OpenGLESGL10Image(OpenGLESImage):
    def _java_defaults(self):
        vars(self).setdefault("textureVertexFloatBuffer", None)
        vars(self).setdefault("realOpenGLESImageDraw", None)
        vars(self).setdefault("openGLESImageDraw", None)

    def _init_fields(self) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        from org.allbinary.opengles.GLUtil import GLUtil
        self.textureVertexFloatBuffer: FloatBuffer = ByteBuffer.allocateDirect(4 * 4 * 2).order(ByteOrder.nativeOrder()).asFloatBuffer()
        self.realOpenGLESImageDraw: OpenGLESImageDraw = (OpenGLESImageDraw()  # Java anonymous class body:
#         self.glUtil: GLUtil = GLUtil.getInstance()
#         self.displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
#         self.textureVertexFloatBuffer: FloatBuffer = _java_listener_owner.textureVertexFloatBuffer
#         self.regionTextureRectangleFloatArray: list[float] = [0.0] * (8)
#         self.regionTextureVertexFloatBuffer: FloatBuffer = ByteBuffer.allocateDirect(4 * 4 * 2).order(ByteOrder.nativeOrder()).asFloatBuffer()
#         self.regionRectangleFloatArray: list[float] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#         self.regionRectangleVertexFloatBuffer: FloatBuffer = ByteBuffer.allocateDirect(4 * 4 * 3).order(ByteOrder.nativeOrder()).asFloatBuffer()
#         self.openGLESImageProperties: OpenGLESImageProperties = _java_listener_owner.openGLESImageProperties
#         
# 
#         def drawRegion(self, gl: GL10, viewHeight: int, x_src: float, y_src: float, width: float, height: float, x: int, y: int, z: int) -> None:
#             from javax.microedition.khronos.opengles.GL10 import GL10
#             imageWidth: int = _java_listener_owner.getWidth()
#             imageHeight: int = _java_listener_owner.getHeight()
#             self.regionRectangleFloatArray[7] = float(viewHeight)
#             self.regionRectangleFloatArray[1] = self.regionRectangleFloatArray[7] - height
#             self.regionRectangleFloatArray[3] = width
#             self.regionRectangleFloatArray[4] = self.regionRectangleFloatArray[1]
#             self.regionRectangleFloatArray[9] = self.regionRectangleFloatArray[3]
#             self.regionRectangleFloatArray[10] = self.regionRectangleFloatArray[7]
#             self.regionTextureRectangleFloatArray[0] = java_divide(x_src, imageWidth)
#             
#             self.regionTextureRectangleFloatArray[1] = java_divide((y_src + height), imageHeight)
#             
#             self.regionTextureRectangleFloatArray[2] = java_divide((x_src + width), imageWidth)
#             
#             self.regionTextureRectangleFloatArray[3] = self.regionTextureRectangleFloatArray[1]
#             self.regionTextureRectangleFloatArray[4] = self.regionTextureRectangleFloatArray[0]
#             self.regionTextureRectangleFloatArray[5] = java_divide(y_src, imageHeight)
#             
#             self.regionTextureRectangleFloatArray[6] = self.regionTextureRectangleFloatArray[2]
#             self.regionTextureRectangleFloatArray[7] = self.regionTextureRectangleFloatArray[5]
#             u_center: float = (self.regionTextureRectangleFloatArray[0] + self.regionTextureRectangleFloatArray[2]) / 2.0
#             v_center: float = (self.regionTextureRectangleFloatArray[5] + self.regionTextureRectangleFloatArray[1]) / 2.0
#             self.glUtil.rotateUVs(self.regionTextureRectangleFloatArray, float(-self.openGLESImageProperties.angle), u_center, v_center)
#             gl.glPushMatrix()
#             imageProcessor: OpenGLESImageProcessor = _java_listener_owner.imageProcessor
#             _java_listener_owner.openGLESImageTranslate.translate(gl, _java_listener_owner, float(x), float(-y))
#             imageProcessor.scale(gl, self.openGLESImageProperties.scaleX, self.openGLESImageProperties.scaleY)
#             imageProcessor.colorMask(gl, self.openGLESImageProperties.redf, self.openGLESImageProperties.greenf, self.openGLESImageProperties.bluef, self.openGLESImageProperties.alphaf)
#             _java_listener_owner.openGLESImageTranslate.translate2(gl, _java_listener_owner)
#             self.regionRectangleVertexFloatBuffer.put(self.regionRectangleFloatArray)
#             self.glUtil.position(self.regionRectangleVertexFloatBuffer, 0)
#             gl.glVertexPointer(3, GL10.GL_FLOAT, 0, self.regionRectangleVertexFloatBuffer)
#             gl.glEnableClientState(GL10.GL_VERTEX_ARRAY)
#             gl.glEnable(GL10.GL_TEXTURE_2D)
#             gl.glBindTexture(GL10.GL_TEXTURE_2D, self.openGLESImageProperties.textureID)
#             gl.glEnableClientState(GL10.GL_TEXTURE_COORD_ARRAY)
#             self.regionTextureVertexFloatBuffer.put(self.regionTextureRectangleFloatArray)
#             self.glUtil.position(self.regionTextureVertexFloatBuffer, 0)
#             gl.glTexCoordPointer(2, GL10.GL_FLOAT, 0, self.regionTextureVertexFloatBuffer)
#             gl.glDrawArrays(GL10.GL_TRIANGLE_STRIP, 0, 4)
#             gl.glDisableClientState(GL10.GL_VERTEX_ARRAY)
#             gl.glDisableClientState(GL10.GL_TEXTURE_COORD_ARRAY)
#             gl.glDisable(GL10.GL_TEXTURE_2D)
#             gl.glPopMatrix()
#         
# 
#         def draw(self, gl: GL10, x: int, y: int, z: int) -> None:
#             from javax.microedition.khronos.opengles.GL10 import GL10
#             width: int = _java_listener_owner.getWidth()
#             height: int = _java_listener_owner.getHeight()
#             self.regionRectangleFloatArray[7] = float(self.displayInfoSingleton.getLastHeight())
#             self.regionRectangleFloatArray[1] = self.regionRectangleFloatArray[7] - height
#             self.regionRectangleFloatArray[3] = float(width)
#             self.regionRectangleFloatArray[4] = self.regionRectangleFloatArray[1]
#             self.regionRectangleFloatArray[9] = self.regionRectangleFloatArray[3]
#             self.regionRectangleFloatArray[10] = self.regionRectangleFloatArray[7]
#             self.regionTextureRectangleFloatArray[0] = 0.0
#             self.regionTextureRectangleFloatArray[1] = 1.0
#             self.regionTextureRectangleFloatArray[2] = 1.0
#             self.regionTextureRectangleFloatArray[3] = 1.0
#             self.regionTextureRectangleFloatArray[4] = 0.0
#             self.regionTextureRectangleFloatArray[5] = 0.0
#             self.regionTextureRectangleFloatArray[6] = 1.0
#             self.regionTextureRectangleFloatArray[7] = 0.0
#             gl.glPushMatrix()
#             _java_listener_owner.openGLESImageTranslate.translate(gl, _java_listener_owner, float(x), float(-y))
#             imageProcessor: OpenGLESImageProcessor = _java_listener_owner.imageProcessor
#             imageProcessor.scale(gl, self.openGLESImageProperties.scaleX, self.openGLESImageProperties.scaleY)
#             imageProcessor.colorMask(gl, self.openGLESImageProperties.redf, self.openGLESImageProperties.greenf, self.openGLESImageProperties.bluef, self.openGLESImageProperties.alphaf)
#             _java_listener_owner.openGLESImageTranslate.translate2(gl, _java_listener_owner)
#             self.regionRectangleVertexFloatBuffer.put(self.regionRectangleFloatArray)
#             self.glUtil.position(self.regionRectangleVertexFloatBuffer, 0)
#             gl.glVertexPointer(3, GL10.GL_FLOAT, 0, self.regionRectangleVertexFloatBuffer)
#             gl.glEnableClientState(GL10.GL_VERTEX_ARRAY)
#             gl.glEnable(GL10.GL_TEXTURE_2D)
#             gl.glBindTexture(GL10.GL_TEXTURE_2D, self.openGLESImageProperties.textureID)
#             gl.glEnableClientState(GL10.GL_TEXTURE_COORD_ARRAY)
#             self.glUtil.rotateUVs(self.regionTextureRectangleFloatArray, float(-self.openGLESImageProperties.angle), 0.5, 0.5)
#             self.glUtil.position(self.textureVertexFloatBuffer, 0)
#             self.textureVertexFloatBuffer.put(self.regionTextureRectangleFloatArray)
#             self.glUtil.position(self.textureVertexFloatBuffer, 0)
#             gl.glTexCoordPointer(2, GL10.GL_FLOAT, 0, self.textureVertexFloatBuffer)
#             gl.glDrawArrays(GL10.GL_TRIANGLE_STRIP, 0, 4)
#             gl.glDisableClientState(GL10.GL_VERTEX_ARRAY)
#             gl.glDisableClientState(GL10.GL_TEXTURE_COORD_ARRAY)
#             gl.glDisable(GL10.GL_TEXTURE_2D)
#             gl.glPopMatrix()
)
        self.openGLESImageDraw: OpenGLESImageDraw = OpenGLESImageDraw.getInstance()
    

    def __init__(self, image: Image, bitmapFactory: PlatformBitmapBaseFactory, textureFactory: PlatformTextureBaseFactory) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory
        from org.allbinary.platform.opengles.PlatformTextureBaseFactory import PlatformTextureBaseFactory
        super().__init__(image, bitmapFactory, textureFactory)
        __class__._init_fields(self)
        self.initVertices()
    

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
            self.openGLESImageDraw = self.realOpenGLESImageDraw
            OpenGLLogUtil.getInstance().logError(gl10, self)
    

    def drawRegion(self, gl: GL10, viewHeight: int, x_src: float, y_src: float, width: float, height: float, x: int, y: int, z: int) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        self.openGLESImageDraw.drawRegion(gl, viewHeight, x_src, y_src, width, height, x, y, z)
    

    def draw(self, gl: GL10, x: int, y: int, z: int) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        self.openGLESImageDraw.draw(gl, x, y, z)
# from java.nio.ByteBuffer import ByteBuffer
# from java.nio.ByteOrder import ByteOrder
# from java.nio.FloatBuffer import FloatBuffer
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
# from org.allbinary.graphics.opengles.OpenGLLogUtil import OpenGLLogUtil
# from org.allbinary.opengles.GLUtil import GLUtil
# from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory
# from org.allbinary.platform.opengles.PlatformTextureBaseFactory import PlatformTextureBaseFactory
from org.allbinary.image.opengles.OpenGLESImageDraw import OpenGLESImageDraw


