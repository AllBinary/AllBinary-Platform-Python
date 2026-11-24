# Generated Code Do Not Modify
# package org.allbinary.graphics

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory


class OpenGLBitmapFactory(PlatformBitmapBaseFactory):
    instance: OpenGLBitmapFactory = None

    def _init_fields(self) -> None:
        self.ARGB_8888: OpenGLBitmapConfig = OpenGLBitmapConfig(None)

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> OpenGLBitmapFactory:
        return OpenGLBitmapFactory.instance
    

    def createBitmap_j3(self, width: int, height: int, config: OpenGLBitmapConfig) -> OpenGLBitmap:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        from javax.microedition.lcdui.Image import Image
        return OpenGLBitmap(Image.createImage(width, height))
    

    # throws Exception
    def decodeStream(self, inputStream: InputStream) -> OpenGLBitmap:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        from java.io.InputStream import InputStream
        from org.allbinary.image.ImageFactory import ImageFactory
        return OpenGLBitmap(ImageFactory.getInstance().createImageFromInputStream(inputStream))
    

    def createBitmap_j1(self, image: Image) -> PlatformBitmapBase:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.platform.graphics.PlatformBitmapBase import PlatformBitmapBase
        return OpenGLBitmap(image)

    def createBitmap(self, *args):
        return getattr(self, "createBitmap_j" + str(len(args)))(*args)
# from java.io.IOException import IOException
# from java.io.InputStream import InputStream
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.image.ImageFactory import ImageFactory
# from org.allbinary.platform.graphics.PlatformBitmapBase import PlatformBitmapBase
from org.allbinary.graphics.OpenGLBitmapConfig import OpenGLBitmapConfig


def _OpenGLBitmapFactory_instance() -> object:
    return OpenGLBitmapFactory()

lazy_static(OpenGLBitmapFactory, "instance", _OpenGLBitmapFactory_instance)

