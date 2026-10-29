# Generated Code Do Not Modify
# package org.platform.opengl

from __future__ import annotations



class OpenGLGLUUtils:
    instance: OpenGLGLUUtils = None
    

    @staticmethod
    def getInstance() -> OpenGLGLUUtils:
        return OpenGLGLUUtils.instance
    

    def makeByteBuffer(self, bmp: OpenGLBitmap, flip: bool) -> ByteBuffer:
        raise RuntimeError()
    

    def texImage2D(self, gl: GL10, glVersion: str, target: int, level: int, generateMipMap: bool, openGLESImage: OpenGLESImage, border: int, flip: bool) -> None:
        raise RuntimeError()
    

    # Java overloaded method: Python keeps the last definition
    def texImage2D(self, gl: GL10, glVersion: str, target: int, level: int, generateMipMap: bool, bitmap: OpenGLBitmap, border: int, flip: bool) -> None:
        raise RuntimeError()
# from java.nio.ByteBuffer import ByteBuffer
# from javax.microedition.khronos.opengles.GL10 import GL10
from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage


OpenGLGLUUtils.instance = OpenGLGLUUtils()

