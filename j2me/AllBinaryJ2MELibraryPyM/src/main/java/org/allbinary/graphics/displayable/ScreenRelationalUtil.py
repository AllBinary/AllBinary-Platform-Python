# Generated Code Do Not Modify
# package org.allbinary.graphics.displayable

from __future__ import annotations



class ScreenRelationalUtil:
    instance: ScreenRelationalUtil = None
    

    @staticmethod
    def getInstance() -> ScreenRelationalUtil:
        return ScreenRelationalUtil.instance
    

    def getScaleImage(self, image: Image) -> float:
        return self.getScaleWH(image.getWidth(), image.getHeight())
    

    def getScaleWH(self, aWidth: int, aHeight: int) -> float:
        return self.getScaleWHA(aWidth, aHeight, 20)
    

    def getScaleWHA(self, aWidth: int, aHeight: int, add: int) -> float:
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        last: list[int] = displayInfoSingleton.getLast()
        width: float = float(last[displayInfoSingleton.WIDTH])
        height: float = float(last[displayInfoSingleton.HEIGHT])
        largestSize: float = width
        if largestSize < height:
            largestSize = height
        scale: float = (largestSize) / float(aWidth)
        return scale
    

    def getScaledHeight(self, aWidth: int, aHeight: int) -> int:
        return int((self.getScaleWH(aWidth, aHeight) * float(aHeight)))
    

    def getScaledHeightAdd(self, aWidth: int, aHeight: int, add: int) -> int:
        return int((self.getScaleWHA(aWidth, aHeight, add) * float(aHeight)))
# from javax.microedition.lcdui.Image import Image


ScreenRelationalUtil.instance = ScreenRelationalUtil()

