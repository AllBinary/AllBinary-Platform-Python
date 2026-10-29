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

from org.allbinary.graphics.form.ItemPaintableFactory import ItemPaintableFactory


class PreGameLockableFormPaintableFactory(ItemPaintableFactory):

    def _init_fields(self) -> None:
        self.lockedIndex: int = None
    

    def __init__(self, lockedIndex: int) -> None:
        super().__init__()
        self._init_fields()
        self.lockedIndex = lockedIndex
    

    # throws Exception
    def getInstanceItemPaintable(self, paintableForm: PaintableForm) -> ItemPaintable:
        from org.allbinary.game.displayable.canvas.PreGameLockablePaintable import PreGameLockablePaintable
        return PreGameLockablePaintable(paintableForm, self.lockedIndex)
from org.allbinary.graphics.form.ItemPaintable import ItemPaintable
from org.allbinary.graphics.form.PaintableForm import PaintableForm
from org.allbinary.graphics.form.ScrollCurrentSelectionForm import ScrollCurrentSelectionForm


