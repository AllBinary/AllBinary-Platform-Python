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


class ColorLessVectorAnimation(VectorAnimation):
    

    def __init__(self, currentPoints: list[list[list[int]]], animationBehavior: AnimationBehavior) -> None:
        super().__init__(currentPoints, BasicColorFactory.getInstance().WHITE, animationBehavior)
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.paintVectors(graphics, x, y)
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory


