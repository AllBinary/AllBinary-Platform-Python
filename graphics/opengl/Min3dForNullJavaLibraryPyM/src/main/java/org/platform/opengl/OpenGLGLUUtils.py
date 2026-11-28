# Generated Code Do Not Modify
# package org.platform.opengl

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class OpenGLGLUUtils:
    instance: OpenGLGLUUtils = None
    

    @staticmethod
    def getInstance() -> OpenGLGLUUtils:
        return OpenGLGLUUtils.instance
    

    def makeByteBuffer(self, bmp: OpenGLBitmap, flip: bool) -> ByteBuffer:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        raise RuntimeError()
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def texImage2D_j8_1(self, gl: GL10, glVersion: str, target: int, level: int, generateMipMap: bool, openGLESImage: OpenGLESImage, border: int, flip: bool) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage
        raise RuntimeError()
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def texImage2D_j8_2(self, gl: GL10, glVersion: str, target: int, level: int, generateMipMap: bool, bitmap: OpenGLBitmap, border: int, flip: bool) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        raise RuntimeError()

    def texImage2D(self, *args):
        if len(args) == 8 and True and (args[0] is None or any(base.__name__ == "GL10" for base in type(args[0]).__mro__)) and (args[1] is None or isinstance(args[1], str)) and isinstance(args[2], int) and not isinstance(args[2], bool) and isinstance(args[3], int) and not isinstance(args[3], bool) and isinstance(args[4], bool) and (args[5] is None or any(base.__name__ == "OpenGLESImage" for base in type(args[5]).__mro__)) and isinstance(args[6], int) and not isinstance(args[6], bool) and isinstance(args[7], bool):
            return __class__.__dict__["texImage2D_j8_1"].__get__(self, __class__)(*args)
        if len(args) == 8:
            return __class__.__dict__["texImage2D_j8_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("texImage2D_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().texImage2D(*args)
# from java.nio.ByteBuffer import ByteBuffer
# from javax.microedition.khronos.opengles.GL10 import GL10
# from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
# from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage


def _OpenGLGLUUtils_instance() -> object:
    return OpenGLGLUUtils()

lazy_static(OpenGLGLUUtils, "instance", _OpenGLGLUUtils_instance)

