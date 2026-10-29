# Generated Code Do Not Modify
# package org.allbinary.graphics

from __future__ import annotations

from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory


class OpenGLBitmapFactory(PlatformBitmapBaseFactory):
    instance: OpenGLBitmapFactory = None
    class Config:

        def _init_fields(self) -> None:
            self.bitmapConfig: Config = None
        

        def __init__(self, bitmapConfig: Config) -> None:
            self._init_fields()
            self.bitmapConfig = bitmapConfig

    def _init_fields(self) -> None:
        self.ARGB_8888: Config = Config(Bitmap.Config.ARGB_8888)

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> OpenGLBitmapFactory:
        return OpenGLBitmapFactory.instance
    

    def createBitmap(self, width: int, height: int, config: Config) -> OpenGLBitmap:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        return OpenGLBitmap(Bitmap.createBitmap(width, height, config.bitmapConfig))
    

    # throws IOException
    def decodeStream(self, inputStream: InputStream) -> OpenGLBitmap:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        return OpenGLBitmap(BitmapFactory.decodeStream(inputStream))
    

    # Java overloaded method: Python keeps the last definition
    def createBitmap(self, image: Image) -> PlatformBitmapBase:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        return OpenGLBitmap((image).getBitmap())
# from java.io.InputStream import InputStream
# from javax.microedition.lcdui.Image import Image
from android.graphics.Bitmap import Bitmap
from android.graphics.BitmapFactory import BitmapFactory
# from java.io.IOException import IOException
from org.allbinary.platform.graphics.PlatformBitmapBase import PlatformBitmapBase
from org.microemu.android.device.AndroidImageInterface import AndroidImageInterface
from org.allbinary.graphics.Config import Config


OpenGLBitmapFactory.instance = OpenGLBitmapFactory()

