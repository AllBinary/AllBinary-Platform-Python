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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.animation.image.ImageAnimation import ImageAnimation


@java_inherited_overloads
class AdjustedImageAnimation(ImageAnimation):
    def _java_defaults(self):
        vars(self).setdefault("dx", 0)
        vars(self).setdefault("dy", 0)

    def _init_fields(self) -> None:
        if "dx" not in vars(self): self.dx: int = 0
        if "dy" not in vars(self): self.dy: int = 0
    

    def __init__(self, image: Image, dx: int, dy: int, animationBehavior: AnimationBehavior) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        super().__init__(image, animationBehavior)
        __class__._init_fields(self)
        self.init(dx, dy)
    

    # throws Exception
    def init(self, dx: int, dy: int) -> None:
        self.setDx(dx)
        self.setDy(dy)
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        java_super_call(super(), "paintXY", graphics, x + self.dx, y + self.dy)
    

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
# from org.allbinary.animation.AnimationBehavior import AnimationBehavior


