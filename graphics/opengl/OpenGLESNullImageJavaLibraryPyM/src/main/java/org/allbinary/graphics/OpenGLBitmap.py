# Generated Code Do Not Modify
# package org.allbinary.graphics

from __future__ import annotations

from org.allbinary.platform.graphics.PlatformBitmapBase import PlatformBitmapBase


class OpenGLBitmap(PlatformBitmapBase):

    def _init_fields(self) -> None:
        self.bitmap: object = None
    

    def __init__(self, bitmap: object) -> None:
        super().__init__()
        self._init_fields()
        self.bitmap = bitmap
    

    def getPixels(self, pixels: list[int], offset: int, stride: int, x: int, y: int, width: int, height: int) -> None:
        pass
    

    def setPixels(self, pixels: list[int], offset: int, stride: int, x: int, y: int, width: int, height: int) -> None:
        pass
    

    def recycle(self) -> None:
        pass


