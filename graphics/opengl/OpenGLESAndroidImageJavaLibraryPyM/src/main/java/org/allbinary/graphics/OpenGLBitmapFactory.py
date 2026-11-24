# Generated Code Do Not Modify
# package org.allbinary.graphics

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory


class OpenGLBitmapFactory(PlatformBitmapBaseFactory):
    instance: OpenGLBitmapFactory = None

    def _init_fields(self) -> None:
        from android.graphics.Bitmap import Bitmap
        self.ARGB_8888: OpenGLBitmapConfig = OpenGLBitmapConfig(Bitmap.Config.ARGB_8888)

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> OpenGLBitmapFactory:
        return OpenGLBitmapFactory.instance
    

    def createBitmap_j3(self, width: int, height: int, config: OpenGLBitmapConfig) -> OpenGLBitmap:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        from android.graphics.Bitmap import Bitmap
        return OpenGLBitmap(Bitmap.createBitmap(width, height, config.bitmapConfig))
    

    # throws IOException
    def decodeStream(self, inputStream: InputStream) -> OpenGLBitmap:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        from java.io.InputStream import InputStream
        from android.graphics.BitmapFactory import BitmapFactory
        return OpenGLBitmap(BitmapFactory.decodeStream(inputStream))
    

    def createBitmap_j1(self, image: Image) -> PlatformBitmapBase:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.platform.graphics.PlatformBitmapBase import PlatformBitmapBase
        from org.microemu.android.device.AndroidImageInterface import AndroidImageInterface
        return OpenGLBitmap((image).getBitmap())

    def createBitmap(self, *args):
        return getattr(self, "createBitmap_j" + str(len(args)))(*args)
# from java.io.InputStream import InputStream
# from javax.microedition.lcdui.Image import Image
# from android.graphics.Bitmap import Bitmap
# from android.graphics.BitmapFactory import BitmapFactory
# from java.io.IOException import IOException
# from org.allbinary.platform.graphics.PlatformBitmapBase import PlatformBitmapBase
# from org.microemu.android.device.AndroidImageInterface import AndroidImageInterface
from org.allbinary.graphics.OpenGLBitmapConfig import OpenGLBitmapConfig


def _OpenGLBitmapFactory_instance() -> object:
    return OpenGLBitmapFactory()

lazy_static(OpenGLBitmapFactory, "instance", _OpenGLBitmapFactory_instance)

