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
# package org.allbinary.animation.image.sprite

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.animation.image.sprite.SpriteIndexedAnimation import SpriteIndexedAnimation


@java_inherited_overloads
class AdjustedSpriteIndexedAnimation(SpriteIndexedAnimation):
    def _java_defaults(self):
        vars(self).setdefault("dx", 0)
        vars(self).setdefault("dy", 0)

    def _init_fields(self) -> None:
        if "dx" not in vars(self): self.dx: int = 0
        if "dy" not in vars(self): self.dy: int = 0
    

    def __init__(self, sprite: Sprite, image: Image, basicColorArray: list[BasicColor], dx: int, dy: int, animationBehavior: AnimationBehavior) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from javax.microedition.lcdui.game.Sprite import Sprite
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__(sprite, image, basicColorArray, animationBehavior)
        __class__._init_fields(self)
        self.dx = dx
        self.dy = dy
    

    def paintFrame(self, graphics: Graphics, frame: int, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.setFrame(frame)
        self.sprite.setPosition(x + self.dx, y + self.dy)
        java_super_call(super(), "paint", graphics)
    

    def paintXY(self, g: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.sprite.setPosition(x + self.dx, y + self.dy)
        java_super_call(super(), "paint", g)
    

    def paint(self, g: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.sprite.setPosition(self.dx, self.dy)
        java_super_call(super(), "paint", g)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
# from org.allbinary.animation.AnimationBehavior import AnimationBehavior
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.color.BasicColorUtil import BasicColorUtil


