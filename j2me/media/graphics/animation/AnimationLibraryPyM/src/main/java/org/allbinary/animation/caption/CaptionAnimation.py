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
# package org.allbinary.animation.caption

from __future__ import annotations

from org.allbinary.animation.Animation import Animation


class CaptionAnimation(Animation):

    def _init_fields(self) -> None:
        self.animationInterface: Animation = None
        self.overlayAnimationInterface: Animation = None
        self.captionDx: int = None
        self.captionDy: int = None
        self.dx: int = None
        self.dy: int = None
    

    def __init__(self, animationInterface: Animation, overlayAnimationInterface: Animation, captionDx: int, captionDy: int, dx: int, dy: int) -> None:
        super().__init__()
        self._init_fields()
        self.animationInterface = animationInterface
        self.overlayAnimationInterface = overlayAnimationInterface
        self.captionDx = captionDx
        self.captionDy = captionDy
        self.dx = dx
        self.dy = dy
    

    # throws Exception
    def nextFrame(self) -> None:
        pass
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.animationInterface.paintXY(graphics, x + self.captionDx, y + self.captionDy)
        self.overlayAnimationInterface.paintXY(graphics, x + self.captionDx + self.dx, y + self.captionDy + self.dy)
    

    def paintThreedXYZ(self, graphics: Graphics, x: int, y: int, z: int) -> None:
        self.animationInterface.paintThreedXYZ(graphics, x + self.captionDx, y + self.captionDy, z)
        self.overlayAnimationInterface.paintThreedXYZ(graphics, x + self.captionDx + self.dx, y + self.captionDy + self.dy, z)
# from javax.microedition.lcdui.Graphics import Graphics


