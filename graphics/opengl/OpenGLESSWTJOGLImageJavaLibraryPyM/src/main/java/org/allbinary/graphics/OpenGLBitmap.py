# Generated Code Do Not Modify
# package org.allbinary.graphics

from __future__ import annotations

from org.allbinary.platform.graphics.PlatformBitmapBase import PlatformBitmapBase


class OpenGLBitmap(PlatformBitmapBase):

    def _init_fields(self) -> None:
        self.image: Image = None
    

    def __init__(self, bitmap: object) -> None:
        super().__init__()
        self._init_fields()
        self.image = bitmap
    

    def getImage(self) -> Image:
        return self.image
    

    def getDepth(self) -> int:
        if self.image.isMutable():
            mutableImage: SwtMutableImage = self.image
            return mutableImage.getDepth()
        else:
            immutableImage: SwtImmutableImage = self.image
            return immutableImage.getDepth()
    

    def getPixels(self, pixels: list[int], offset: int, stride: int, x: int, y: int, width: int, height: int) -> None:
        if self.image.isMutable():
            mutableImage: SwtMutableImage = self.image
            mutableImage.getRGB(pixels, offset, stride, x, y, width, height)
        else:
            immutableImage: SwtImmutableImage = self.image
            immutableImage.getRGB(pixels, offset, stride, x, y, width, height)
    

    def setPixels(self, pixels: list[int], offset: int, stride: int, x: int, y: int, width: int, height: int) -> None:
        self.image.setRGB2(pixels, offset, height, x, y, width, height)
    

    def getWidth(self) -> int:
        return self.image.getWidth()
    

    def getHeight(self) -> int:
        return self.image.getHeight()
    

    def recycle(self) -> None:
        DisposalUtil.getInstance().disposeImage(self.image)
# from javax.microedition.lcdui.Image import Image
from org.allbinary.DisposalUtil import DisposalUtil
from org.microemu.device.swt.SwtImmutableImage import SwtImmutableImage
from org.microemu.device.swt.SwtMutableImage import SwtMutableImage


