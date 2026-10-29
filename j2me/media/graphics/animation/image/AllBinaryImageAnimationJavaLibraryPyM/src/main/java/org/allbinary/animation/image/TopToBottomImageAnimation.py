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

from org.allbinary.animation.image.ImageSegmentAnimation import ImageSegmentAnimation


class TopToBottomImageAnimation(ImageSegmentAnimation):

    def _init_fields(self) -> None:
        self.currentHeight: int = None
        self.anchor: int = Anchor.TOP_LEFT
    

    def __init__(self, image: Image, sequenceArray: list[int], animationBehavior: AnimationBehavior) -> None:
        super().__init__(image, sequenceArray, animationBehavior)
        self._init_fields()
        self.currentHeight = 0
        if self.getSequence()[0] == -1:
            self.setFrame(self.getSize() - 1)
    

    def nextFrame(self) -> None:
        if self.getSequence()[0] == -1:
            super().previousFrame()
        else:
            super().nextFrame()
        self.update()
    

    def previousFrame(self) -> None:
        if self.getSequence()[0] == -1:
            super().nextFrame()
        else:
            super().previousFrame()
        self.update()
    

    def setFrame(self, index: int) -> None:
        super().setFrame(index)
        self.update()
    

    def update(self) -> None:
        self.currentHeight = self.getDrawHeight() * self.getFrame() / self.getSize()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        graphics.drawRegion(self.getImage(), self.getStartX(), self.getStartY(), self.getDrawWidth(), self.currentHeight, Sprite.TRANS_NONE, x, y, self.anchor)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.graphics.Anchor import Anchor


