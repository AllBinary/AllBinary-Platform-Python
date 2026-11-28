# Generated Code Do Not Modify
# package org.allbinary.animation

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.animation.IndexedAnimation import IndexedAnimation


@java_inherited_overloads
class FillAnimation(IndexedAnimation):
    def _java_defaults(self):
        vars(self).setdefault("pixelBuffer", None)
        vars(self).setdefault("width", 0)
        vars(self).setdefault("height", 0)

    def _init_fields(self) -> None:
        if "pixelBuffer" not in vars(self): self.pixelBuffer: list[int] = None
        if "width" not in vars(self): self.width: int = 0
        if "height" not in vars(self): self.height: int = 0
    

    def __init__(self, pixelBuffer: list[int], width: int, height: int, animationBehavior: AnimationBehavior) -> None:
        __class__._java_defaults(self)
        super().__init__(animationBehavior)
        __class__._init_fields(self)
        self.width = 100
        self.height = 100
        self.pixelBuffer = pixelBuffer
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        changed: bool = False
        if self.getBasicColorP() is None or int(self.getBasicColorP()) != int(basicColor):
            changed = True
        java_super_call(super(), "setBasicColorP", basicColor)
        if changed:
            self.updateModifiers()
    

    def changeBasicColor(self, basicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        changed: bool = False
        if self.getChangeBasicColor() is None or int(self.getChangeBasicColor()) != int(basicColor):
            changed = True
        java_super_call(super(), "changeBasicColor", basicColor)
        if changed:
            self.updateModifiers()
    

    def setAlpha(self, alpha: int) -> None:
        changed: bool = False
        if self.alphaP != alpha:
            changed = True
        java_super_call(super(), "setAlpha", alpha)
        if changed:
            self.updateModifiers()
    

    def setScale(self, scaleX: float, scaleY: float) -> None:
        pass
    

    def setMaxScale(self, maxScaleX: float, maxScaleY: float) -> None:
        pass
    

    def updateModifiers(self) -> None:
        pass
    

    def paint(self, g: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        g.drawRGB(self.pixelBuffer, 0, self.width, 0, 0, self.width, self.height, True)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.color.BasicColor import BasicColor


