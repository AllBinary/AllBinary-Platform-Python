# Generated Code Do Not Modify
# package org.allbinary.animation

from __future__ import annotations

from org.allbinary.animation.IndexedAnimation import IndexedAnimation


class FillAnimation(IndexedAnimation):

    def _init_fields(self) -> None:
        self.pixelBuffer: list[int] = None
        self.width: int = None
        self.height: int = None
    

    def __init__(self, pixelBuffer: list[int], width: int, height: int, animationBehavior: AnimationBehavior) -> None:
        super().__init__(animationBehavior)
        self._init_fields()
        self.width = 100
        self.height = 100
        self.pixelBuffer = pixelBuffer
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        changed: bool = False
        if self.getBasicColorP() is None or int(self.getBasicColorP()) != int(basicColor):
            changed = True
        super().setBasicColorP(basicColor)
        if changed:
            self.updateModifiers()
    

    def changeBasicColor(self, basicColor: BasicColor) -> None:
        changed: bool = False
        if self.getChangeBasicColor() is None or int(self.getChangeBasicColor()) != int(basicColor):
            changed = True
        super().changeBasicColor(basicColor)
        if changed:
            self.updateModifiers()
    

    def setAlpha(self, alpha: int) -> None:
        changed: bool = False
        if self.alphaP != alpha:
            changed = True
        super().setAlpha(alpha)
        if changed:
            self.updateModifiers()
    

    def setScale(self, scaleX: float, scaleY: float) -> None:
        pass
    

    def setMaxScale(self, maxScaleX: float, maxScaleY: float) -> None:
        pass
    

    def updateModifiers(self) -> None:
        pass
    

    def paint(self, g: Graphics) -> None:
        g.drawRGB(self.pixelBuffer, 0, self.width, 0, 0, self.width, self.height, True)
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColor import BasicColor


