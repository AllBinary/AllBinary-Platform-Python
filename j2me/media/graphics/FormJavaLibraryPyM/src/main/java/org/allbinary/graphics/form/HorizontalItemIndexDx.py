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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.form.ItemIndexDx import ItemIndexDx


@java_inherited_overloads
class HorizontalItemIndexDx(ItemIndexDx):
    def _java_defaults(self):
        vars(self).setdefault("scrollCurrentSelectionForm", None)

    def _init_fields(self) -> None:
        if "scrollCurrentSelectionForm" not in vars(self): self.scrollCurrentSelectionForm: ScrollCurrentSelectionForm = None
    

    def __init__(self, scrollCurrentSelectionForm: ScrollCurrentSelectionForm) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.scrollCurrentSelectionForm = scrollCurrentSelectionForm
    

    # throws Exception
    def getDx(self, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
        from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
        return self.scrollCurrentSelectionForm.getXHorizontalForm(index, item, dx, dy)
# from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem


