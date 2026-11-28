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
class RightToLeftImageAnimation(ImageSegmentAnimation):
    def _java_defaults(self):
        vars(self).setdefault("startWidth", 0)
        vars(self).setdefault("currentWidth", 0)
        vars(self).setdefault("anchor", 0)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.Anchor import Anchor
        if "startWidth" not in vars(self): self.startWidth: int = 0
        if "currentWidth" not in vars(self): self.currentWidth: int = 0
        self.anchor: int = Anchor.TOP_LEFT
    

    def __init__(self, image: Image, animationBehavior: AnimationBehavior) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
        super().__init__(image, PrimitiveIntUtil.getArrayInstance(), animationBehavior)
        __class__._init_fields(self)
        self.setFrame(self.getSize() - 1)
    

    def nextFrame(self) -> None:
        java_super_call(super(), "previousFrame")
        self.update()
    

    def previousFrame(self) -> None:
        java_super_call(super(), "nextFrame")
        self.update()
    

    def setFrame(self, index: int) -> None:
        java_super_call(super(), "setFrame", index)
        self.update()
    

    def update(self) -> None:
        self.startWidth = java_divide(self.getDrawWidth() * self.getFrame(), self.getSize())
        self.currentWidth = self.getDrawWidth() - self.startWidth
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        from javax.microedition.lcdui.game.Sprite import Sprite
        graphics.drawRegion(self.getImage(), self.startWidth, self.getStartY(), self.currentWidth, self.getDrawHeight(), Sprite.TRANS_NONE, x + self.startWidth, y, self.anchor)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
# from org.allbinary.animation.AnimationBehavior import AnimationBehavior
# from org.allbinary.graphics.Anchor import Anchor
# from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil


