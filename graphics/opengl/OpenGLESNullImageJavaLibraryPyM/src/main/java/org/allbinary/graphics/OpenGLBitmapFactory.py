# Generated Code Do Not Modify
# package org.allbinary.graphics

from __future__ import annotations

from org.allbinary.platform.graphics.PlatformBitmapBaseFactory import PlatformBitmapBaseFactory


class OpenGLBitmapFactory(PlatformBitmapBaseFactory):
    instance: OpenGLBitmapFactory = None
    class Config:

        def _init_fields(self) -> None:
            self.bitmapConfig: object = None
        

        def __init__(self, bitmapConfig: object) -> None:
            self._init_fields()
            self.bitmapConfig = bitmapConfig

    def _init_fields(self) -> None:
        self.ARGB_8888: Config = Config(NullUtil.getInstance().NULL_OBJECT)

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> OpenGLBitmapFactory:
        return OpenGLBitmapFactory.instance
    

    def createBitmap(self, width: int, height: int, config: Config) -> OpenGLBitmap:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        return OpenGLBitmap(NullUtil.getInstance().NULL_OBJECT)
    

    # throws IOException
    def decodeStream(self, inputStream: InputStream) -> OpenGLBitmap:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        return OpenGLBitmap(NullUtil.getInstance().NULL_OBJECT)
    

    # Java overloaded method: Python keeps the last definition
    def createBitmap(self, image: Image) -> PlatformBitmapBase:
        from org.allbinary.graphics.OpenGLBitmap import OpenGLBitmap
        return OpenGLBitmap(NullUtil.getInstance().NULL_OBJECT)
# from java.io.IOException import IOException
# from java.io.InputStream import InputStream
# from javax.microedition.lcdui.Image import Image
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.platform.graphics.PlatformBitmapBase import PlatformBitmapBase
from org.allbinary.graphics.Config import Config


OpenGLBitmapFactory.instance = OpenGLBitmapFactory()

