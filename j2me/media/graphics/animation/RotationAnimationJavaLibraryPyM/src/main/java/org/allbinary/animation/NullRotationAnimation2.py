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

from org.allbinary.animation.NullRotationAnimation import NullRotationAnimation


class NullRotationAnimation2(NullRotationAnimation):
    

    def __init__(self) -> None:
        from org.allbinary.animation.IndexedAnimationBehavior import IndexedAnimationBehavior
        from org.allbinary.math.AngleFactory import AngleFactory
        from org.allbinary.math.AngleInfo import AngleInfo
        from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
        super().__init__(AngleInfo.getInstance(AngleFactory.getInstance().QUARTER_TOTAL_ANGLE), CircularIndexUtil.createInstance(4), IndexedAnimationBehavior(1, 250))
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.math.AngleFactory import AngleFactory
# from org.allbinary.math.AngleInfo import AngleInfo
# from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


