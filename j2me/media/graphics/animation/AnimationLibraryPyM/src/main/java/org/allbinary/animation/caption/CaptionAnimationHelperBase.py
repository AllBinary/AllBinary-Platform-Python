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
# package org.allbinary.animation.caption

from __future__ import annotations

from org.allbinary.animation.Animation import Animation


class CaptionAnimationHelperBase(Animation):
    INSTANCE: CaptionAnimationHelperBase = None

    def __init__(self) -> None:
        super().__init__()
    

    def isShowing(self) -> bool:
        return False
    

    def tick(self) -> None:
        pass
    

    def update(self, message: str, basicColor: BasicColor) -> None:
        pass
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        pass
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColor import BasicColor


CaptionAnimationHelperBase.INSTANCE = CaptionAnimationHelperBase()

