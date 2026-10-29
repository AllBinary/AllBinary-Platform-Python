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

from org.allbinary.animation.image.sprite.SpriteIndexedAnimation import SpriteIndexedAnimation


class AdjustedSpriteIndexedAnimation(SpriteIndexedAnimation):

    def _init_fields(self) -> None:
        self.dx: int = None
        self.dy: int = None
    

    def __init__(self, sprite: Sprite, image: Image, basicColorArray: list[BasicColor], dx: int, dy: int, animationBehavior: AnimationBehavior) -> None:
        super().__init__(sprite, image, basicColorArray, animationBehavior)
        self._init_fields()
        self.dx = dx
        self.dy = dy
    

    def paintFrame(self, graphics: Graphics, frame: int, x: int, y: int) -> None:
        self.setFrame(frame)
        self.sprite.setPosition(x + self.dx, y + self.dy)
        super().paint(graphics)
    

    def paintXY(self, g: Graphics, x: int, y: int) -> None:
        self.sprite.setPosition(x + self.dx, y + self.dy)
        super().paint(g)
    

    def paint(self, g: Graphics) -> None:
        self.sprite.setPosition(self.dx, self.dy)
        super().paint(g)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorUtil import BasicColorUtil


