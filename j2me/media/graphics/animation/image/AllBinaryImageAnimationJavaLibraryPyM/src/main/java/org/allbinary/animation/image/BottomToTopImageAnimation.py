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
class BottomToTopImageAnimation(ImageSegmentAnimation):
    def _java_defaults(self):
        vars(self).setdefault("startHeight", 0)
        vars(self).setdefault("currentHeight", 0)
        vars(self).setdefault("anchor", 0)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.Anchor import Anchor
        if "startHeight" not in vars(self): self.startHeight: int = 0
        if "currentHeight" not in vars(self): self.currentHeight: int = 0
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
        self.startHeight = java_divide(self.getDrawHeight() * self.getFrame(), self.getSize())
            
        self.currentHeight = self.getDrawHeight() - self.startHeight
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        from javax.microedition.lcdui.game.Sprite import Sprite
        graphics.drawRegion(self.getImage(), self.getStartX(), self.startHeight, self.getDrawWidth(), self.currentHeight, Sprite.TRANS_NONE, x, y + self.startHeight, self.anchor)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
# from org.allbinary.animation.AnimationBehavior import AnimationBehavior
# from org.allbinary.graphics.Anchor import Anchor
# from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil


