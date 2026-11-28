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
        if "bitmap" not in vars(self): self.bitmap: object = None
    

    def __init__(self, bitmap: object) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.bitmap = bitmap
    

    def getPixels(self, pixels: list[int], offset: int, stride: int, x: int, y: int, width: int, height: int) -> None:
        pass
    

    def setPixels(self, pixels: list[int], offset: int, stride: int, x: int, y: int, width: int, height: int) -> None:
        pass
    

    def recycle(self) -> None:
        pass


