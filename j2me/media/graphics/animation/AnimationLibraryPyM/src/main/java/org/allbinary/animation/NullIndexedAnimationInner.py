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

from org.allbinary.animation.NullIndexedAnimation import NullIndexedAnimation


class NullIndexedAnimationInner(NullIndexedAnimation):
    

    def __init__(self) -> None:
        from org.allbinary.animation.IndexedAnimationBehavior import IndexedAnimationBehavior
        super().__init__(IndexedAnimationBehavior(1, 250))
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
# from javax.microedition.lcdui.Graphics import Graphics


