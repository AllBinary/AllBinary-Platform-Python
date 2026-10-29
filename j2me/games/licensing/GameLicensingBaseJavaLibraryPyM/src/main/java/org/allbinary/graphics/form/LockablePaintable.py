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
# package org.allbinary.graphics.form

from __future__ import annotations

from org.allbinary.graphics.form.ItemPaintable import ItemPaintable


class LockablePaintable(ItemPaintable):

    def _init_fields(self) -> None:
        self.animation: Animation = FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().get(LockedResources.getInstance().LOCKED_DEMO_GAME_FEATURE_RESOURCE).getInstance(0)
        self.lockedIndex: int = None
    

    def __init__(self, lockedIndex: int) -> None:
        super().__init__()
        self._init_fields()
        self.lockedIndex = lockedIndex
    

    def paint(self, graphics: Graphics, currentIndex: int, x: int, y: int) -> None:
        if LockedUtil.getInstance().isLocked() and currentIndex >= self.getLockedIndex():
            self.getAnimation().paintXY(graphics, x, y)
    

    def getLockedIndex(self) -> int:
        return self.lockedIndex
    

    def getAnimation(self) -> Animation:
        return self.animation
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.FeaturedAnimationInterfaceFactoryInterfaceFactory import FeaturedAnimationInterfaceFactoryInterfaceFactory
from org.allbinary.logic.system.security.licensing.LockedResources import LockedResources
from org.allbinary.logic.system.security.licensing.LockedUtil import LockedUtil


