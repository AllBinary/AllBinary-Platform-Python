# Generated Code Do Not Modify
# package org.allbinary.graphics

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory


class OpenGLBitmapFactory(PlatformBitmapBaseFactory):
    instance: OpenGLBitmapFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.NullUtil import NullUtil
        self.ARGB_8888: OpenGLBitmapConfig = OpenGLBitmapConfig(NullUtil.getInstance().NULL_OBJECT)

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> OpenGLBitmapFactory:
        return OpenGLBitmapFactory.instance
    

    def createBitmap_j3(self, width: int, height: int, config: OpenGLBitmapConfig) -> OpenGLBitmap:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        from org.allbinary.logic.NullUtil import NullUtil
        return OpenGLBitmap(NullUtil.getInstance().NULL_OBJECT)
    

    # throws IOException
    def decodeStream(self, inputStream: InputStream) -> OpenGLBitmap:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        from java.io.InputStream import InputStream
        from org.allbinary.logic.NullUtil import NullUtil
        return OpenGLBitmap(NullUtil.getInstance().NULL_OBJECT)
    

    def createBitmap_j1(self, image: Image) -> PlatformBitmapBase:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.logic.NullUtil import NullUtil
        from org.allbinary.platform.graphics.PlatformBitmapBase import PlatformBitmapBase
        return OpenGLBitmap(NullUtil.getInstance().NULL_OBJECT)

    def createBitmap(self, *args):
        return getattr(self, "createBitmap_j" + str(len(args)))(*args)
# from java.io.IOException import IOException
# from java.io.InputStream import InputStream
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.platform.graphics.PlatformBitmapBase import PlatformBitmapBase
from org.allbinary.graphics.OpenGLBitmapConfig import OpenGLBitmapConfig


def _OpenGLBitmapFactory_instance() -> object:
    return OpenGLBitmapFactory()

lazy_static(OpenGLBitmapFactory, "instance", _OpenGLBitmapFactory_instance)

