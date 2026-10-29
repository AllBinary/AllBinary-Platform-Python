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
# package org.allbinary.animation.text

from __future__ import annotations

from org.allbinary.animation.text.CustomTextAnimation import CustomTextAnimation


class AdjustCustomTextAnimation(CustomTextAnimation):

    def _init_fields(self) -> None:
        self.dx: int = None
        self.dy: int = None
    

    def __init__(self, text: str, fontSize: int, dx: int, dy: int, animationBehavior: AnimationBehavior) -> None:
        super().__init__(text, fontSize, animationBehavior)
        self._init_fields()
        self.dx = dx
        self.dy = dy
    

    def getDx(self) -> int:
        return self.dx
    

    def setDx(self, dx: int) -> None:
        self.dx = dx
    

    def getDy(self) -> int:
        return self.dy
    

    def setDy(self, dy: int) -> None:
        self.dy = dy
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        super().paintXY(graphics, x + self.dx, y + self.dy)
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.AnimationBehavior import AnimationBehavior


