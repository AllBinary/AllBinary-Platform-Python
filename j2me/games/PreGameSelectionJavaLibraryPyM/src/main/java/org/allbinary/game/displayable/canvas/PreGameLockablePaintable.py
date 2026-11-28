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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_divide
from org.allbinary.graphics.form.LockablePaintable import LockablePaintable


@java_inherited_overloads
class PreGameLockablePaintable(LockablePaintable):
    def _java_defaults(self):
        vars(self).setdefault("halfWidth", 0)
        vars(self).setdefault("paintableForm", None)

    def _init_fields(self) -> None:
        if "halfWidth" not in vars(self): self.halfWidth: int = 0
        if "paintableForm" not in vars(self): self.paintableForm: ScrollCurrentSelectionForm = None
    

    def __init__(self, paintableForm: ScrollCurrentSelectionForm, lockedIndex: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.image.GameFeatureImageCacheFactory import GameFeatureImageCacheFactory
        from org.allbinary.logic.system.security.licensing.LockedResources import LockedResources
        from org.allbinary.graphics.form.ScrollCurrentSelectionForm import ScrollCurrentSelectionForm
        super().__init__(lockedIndex)
        __class__._init_fields(self)
        self.paintableForm = paintableForm
        self.halfWidth = java_divide(GameFeatureImageCacheFactory.getInstance().getWithKey(LockedResources.getInstance().LOCKED_DEMO_GAME_FEATURE_RESOURCE).getWidth(), 2)
            
    

    def paint(self, graphics: Graphics, currentIndex: int, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.logic.system.security.licensing.LockedUtil import LockedUtil
        if java_predicate(LockedUtil.getInstance(), "isLocked") and self.getPaintableForm().getSelectedIndex() >= self.getLockedIndex():
            self.getAnimation().paintXY(graphics, self.getPaintableForm().getDx() - self.halfWidth, self.getPaintableForm().getDy() + 34)
    

    def getPaintableForm(self) -> ScrollCurrentSelectionForm:
        from org.allbinary.graphics.form.ScrollCurrentSelectionForm import ScrollCurrentSelectionForm
        return self.paintableForm
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.image.GameFeatureImageCacheFactory import GameFeatureImageCacheFactory
# from org.allbinary.logic.system.security.licensing.LockedResources import LockedResources
# from org.allbinary.logic.system.security.licensing.LockedUtil import LockedUtil
# from org.allbinary.graphics.form.ScrollCurrentSelectionForm import ScrollCurrentSelectionForm


