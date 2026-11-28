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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.animation.Animation import Animation


@java_inherited_overloads
class CaptionAnimation(Animation):
    def _java_defaults(self):
        vars(self).setdefault("animationInterface", None)
        vars(self).setdefault("overlayAnimationInterface", None)
        vars(self).setdefault("captionDx", 0)
        vars(self).setdefault("captionDy", 0)
        vars(self).setdefault("dx", 0)
        vars(self).setdefault("dy", 0)

    def _init_fields(self) -> None:
        if "animationInterface" not in vars(self): self.animationInterface: Animation = None
        if "overlayAnimationInterface" not in vars(self): self.overlayAnimationInterface: Animation = None
        if "captionDx" not in vars(self): self.captionDx: int = 0
        if "captionDy" not in vars(self): self.captionDy: int = 0
        if "dx" not in vars(self): self.dx: int = 0
        if "dy" not in vars(self): self.dy: int = 0
    

    def __init__(self, animationInterface: Animation, overlayAnimationInterface: Animation, captionDx: int, captionDy: int, dx: int, dy: int) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
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
        from javax.microedition.lcdui.Graphics import Graphics
        self.animationInterface.paintXY(graphics, x + self.captionDx, y + self.captionDy)
        self.overlayAnimationInterface.paintXY(graphics, x + self.captionDx + self.dx, y + self.captionDy + self.dy)
    

    def paintThreedXYZ(self, graphics: Graphics, x: int, y: int, z: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.animationInterface.paintThreedXYZ(graphics, x + self.captionDx, y + self.captionDy, z)
        self.overlayAnimationInterface.paintThreedXYZ(graphics, x + self.captionDx + self.dx, y + self.captionDy + self.dy, z)
# from javax.microedition.lcdui.Graphics import Graphics


