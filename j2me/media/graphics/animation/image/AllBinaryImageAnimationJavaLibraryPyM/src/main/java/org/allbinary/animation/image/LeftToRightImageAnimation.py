#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
# 
# By agreeing to this license you and any business entity you represent are
# legally bound to the AllBinary Open License Version 1 legal agreement.
# 
# You may obtain the AllBinary Open License Version 1 legal agreement from
# AllBinary or the root directory of AllBinary's AllBinary Platform repository.
# 
# Created By: Travis Berthelot
#  
# Generated Code Do Not Modify
# package org.allbinary.animation.image

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_divide
from org.allbinary.animation.image.ImageSegmentAnimation import ImageSegmentAnimation


@java_inherited_overloads
class LeftToRightImageAnimation(ImageSegmentAnimation):
    def _java_defaults(self):
        vars(self).setdefault("currentWidth", 0)
        vars(self).setdefault("anchor", 0)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.Anchor import Anchor
        if "currentWidth" not in vars(self): self.currentWidth: int = 0
        self.anchor: int = Anchor.TOP_LEFT
    

    def __init__(self, image: Image, sequenceArray: list[int], animationBehavior: AnimationBehavior) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        super().__init__(image, sequenceArray, animationBehavior)
        __class__._init_fields(self)
        self.currentWidth = 0
        if self.getSequence()[0] == -1:
            self.setFrame(self.getSize() - 1)
    

    def nextFrame(self) -> None:
        if self.getSequence()[0] == -1:
            java_super_call(super(), "previousFrame")
        else:
            java_super_call(super(), "nextFrame")
        self.update()
    

    def previousFrame(self) -> None:
        if self.getSequence()[0] == -1:
            java_super_call(super(), "nextFrame")
        else:
            java_super_call(super(), "previousFrame")
        self.update()
    

    def setFrame(self, index: int) -> None:
        java_super_call(super(), "setFrame", index)
        self.update()
    

    def update(self) -> None:
        self.currentWidth = java_divide(self.getDrawWidth() * self.getFrame(), self.getSize())
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        from javax.microedition.lcdui.game.Sprite import Sprite
        graphics.drawRegion(self.getImage(), self.getStartX(), self.getStartY(), self.currentWidth, self.getDrawHeight(), Sprite.TRANS_NONE, x, y, self.anchor)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
# from org.allbinary.animation.AnimationBehavior import AnimationBehavior
# from org.allbinary.graphics.Anchor import Anchor


