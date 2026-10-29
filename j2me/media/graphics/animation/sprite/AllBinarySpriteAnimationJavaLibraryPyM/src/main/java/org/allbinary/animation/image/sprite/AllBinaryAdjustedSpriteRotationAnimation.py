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

from org.allbinary.animation.image.sprite.AllBinarySpriteRotationAnimation import AllBinarySpriteRotationAnimation


class AllBinaryAdjustedSpriteRotationAnimation(AllBinarySpriteRotationAnimation):

    def _init_fields(self) -> None:
        self.dx: int = None
        self.dy: int = None
    

    def __init__(self, sprite: Sprite, image: Image, dx: int, dy: int, animationBehavior: AnimationBehavior) -> None:
        super().__init__(sprite, image, animationBehavior)
        self._init_fields()
        self.dx = dx
        self.dy = dy
    

    def paintXY(self, g: Graphics, x: int, y: int) -> None:
        self.sprite.setPosition(x + self.dx, y + self.dy)
        self.paint(g)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
from org.allbinary.animation.AnimationBehavior import AnimationBehavior


