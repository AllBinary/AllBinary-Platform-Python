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

from org.allbinary.graphics.form.ItemIndexPaintable import ItemIndexPaintable


class MultipleScrollSelectionFormVerticalPaintable(ItemIndexPaintable):

    def _init_fields(self) -> None:
        self.multipleScrollSelectionForm: MultipleScrollSelectionHorizontalForm = None
    

    def __init__(self, multipleScrollSelectionForm: MultipleScrollSelectionHorizontalForm) -> None:
        super().__init__()
        self._init_fields()
        self.multipleScrollSelectionForm = multipleScrollSelectionForm
    

    # throws Exception
    def paint(self, graphics: Graphics, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
        return self.multipleScrollSelectionForm.paintVertical(graphics, index, item, dx, dy)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem


