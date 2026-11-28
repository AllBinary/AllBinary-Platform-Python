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
# package org.allbinary.graphics.paint

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.paint.InitUpdatePaintable import InitUpdatePaintable


@java_inherited_overloads
class AnimationCompositePaintable(InitUpdatePaintable):
    def _java_defaults(self):
        vars(self).setdefault("animationInterface", None)

    def _init_fields(self) -> None:
        if "animationInterface" not in vars(self): self.animationInterface: Animation = None
    

    def __init__(self, animationInterface: Animation) -> None:
        __class__._java_defaults(self)
        from org.allbinary.animation.Animation import Animation
        super().__init__()
        __class__._init_fields(self)
        self.animationInterface = animationInterface
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.animationInterface.paintXY(graphics, 0, 0)
    

    def paintThreed(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.animationInterface.paintThreedXYZ(graphics, 0, 0, 0)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.animation.Animation import Animation


