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
# package org.allbinary.animation

from __future__ import annotations

from org.allbinary.animation.VectorAnimation import VectorAnimation


class AdjustedVectorAnimation(VectorAnimation):

    def _init_fields(self) -> None:
        self.dx: int = None
        self.dy: int = None
    

    def __init__(self, currentPoints: list[list[list[int]]], basicColor: BasicColor, dx: int, dy: int, animationBehavior: AnimationBehavior) -> None:
        super().__init__(currentPoints, basicColor, animationBehavior)
        self._init_fields()
        self.dx = dx
        self.dy = dy
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        super().paintXY(graphics, x + self.dx, y + self.dy)
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColor import BasicColor


