# Generated Code Do Not Modify
# package org.allbinary.graphics

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.platform.graphics.PlatformBitmapBase import PlatformBitmapBase


@java_inherited_overloads
class OpenGLBitmap(PlatformBitmapBase):
    def _java_defaults(self):
        vars(self).setdefault("bitmap", None)

    def _init_fields(self) -> None:
        if "bitmap" not in vars(self): self.bitmap: Bitmap = None
    

    def __init__(self, bitmap: object) -> None:
        __class__._java_defaults(self)
        from android.graphics.Bitmap import Bitmap
        super().__init__()
        __class__._init_fields(self)
        self.bitmap = bitmap
    

    def getPixels(self, pixels: list[int], offset: int, stride: int, x: int, y: int, width: int, height: int) -> None:
        self.bitmap.getPixels(pixels, offset, stride, x, y, width, height)
    

    def setPixels(self, pixels: list[int], offset: int, stride: int, x: int, y: int, width: int, height: int) -> None:
        self.bitmap.setPixels(pixels, offset, stride, x, y, width, height)
    

    def getWidth(self) -> int:
        return self.bitmap.getWidth()
    

    def getHeight(self) -> int:
        return self.bitmap.getHeight()
    

    def recycle(self) -> None:
        self.bitmap.recycle()
# from android.graphics.Bitmap import Bitmap


