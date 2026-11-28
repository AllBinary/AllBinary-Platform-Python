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
from org.allbinary.graphics.form.ItemPaintableFactory import ItemPaintableFactory


@java_inherited_overloads
class PreGameLockableFormPaintableFactory(ItemPaintableFactory):
    def _java_defaults(self):
        vars(self).setdefault("lockedIndex", 0)

    def _init_fields(self) -> None:
        if "lockedIndex" not in vars(self): self.lockedIndex: int = 0
    

    def __init__(self, lockedIndex: int) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.lockedIndex = lockedIndex
    

    # throws Exception
    def getInstanceItemPaintable(self, paintableForm: PaintableForm) -> ItemPaintable:
        from org.allbinary.game.displayable.canvas.PreGameLockablePaintable import PreGameLockablePaintable
        from org.allbinary.graphics.form.ItemPaintable import ItemPaintable
        from org.allbinary.graphics.form.PaintableForm import PaintableForm
        from org.allbinary.graphics.form.ScrollCurrentSelectionForm import ScrollCurrentSelectionForm
        return PreGameLockablePaintable(paintableForm, self.lockedIndex)
# from org.allbinary.graphics.form.ItemPaintable import ItemPaintable
# from org.allbinary.graphics.form.PaintableForm import PaintableForm
# from org.allbinary.graphics.form.ScrollCurrentSelectionForm import ScrollCurrentSelectionForm


