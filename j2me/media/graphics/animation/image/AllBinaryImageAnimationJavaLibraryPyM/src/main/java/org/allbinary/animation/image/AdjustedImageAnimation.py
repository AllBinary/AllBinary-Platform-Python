# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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

from org.allbinary.animation.image.ImageAnimation import ImageAnimation


class AdjustedImageAnimation(ImageAnimation):

    def _init_fields(self) -> None:
        self.dx: int = 0
        self.dy: int = 0
    

    def __init__(self, image: Image, dx: int, dy: int, animationBehavior: AnimationBehavior) -> None:
        super().__init__(image, animationBehavior)
        self._init_fields()
        self.init(dx, dy)
    

    # throws Exception
    def init(self, dx: int, dy: int) -> None:
        self.setDx(dx)
        self.setDy(dy)
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        super().paintXY(graphics, x + self.dx, y + self.dy)
    

    def setDx(self, dx: int) -> None:
        self.dx = dx
    

    def getDx(self) -> int:
        return self.dx
    

    def setDy(self, dy: int) -> None:
        self.dy = dy
    

    def getDy(self) -> int:
        return self.dy
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.AnimationBehavior import AnimationBehavior


