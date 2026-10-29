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

from org.allbinary.graphics.paint.InitUpdatePaintable import InitUpdatePaintable


class AnimationCompositePaintable(InitUpdatePaintable):

    def _init_fields(self) -> None:
        self.animationInterface: Animation = None
    

    def __init__(self, animationInterface: Animation) -> None:
        super().__init__()
        self._init_fields()
        self.animationInterface = animationInterface
    

    def paint(self, graphics: Graphics) -> None:
        self.animationInterface.paintXY(graphics, 0, 0)
    

    def paintThreed(self, graphics: Graphics) -> None:
        self.animationInterface.paintThreedXYZ(graphics, 0, 0, 0)
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.Animation import Animation


