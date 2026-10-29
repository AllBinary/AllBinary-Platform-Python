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

from org.allbinary.graphics.form.ScrollCurrentSelectionForm import ScrollCurrentSelectionForm


class PreGameScrollSelectionForm(ScrollCurrentSelectionForm):
    

    def __init__(self, title: str, items: list[ABCustomItem], formPaintableFactory: ItemPaintableFactory, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(title, items, formPaintableFactory, 0, 3, False, backgroundBasicColor, foregroundBasicColor)
    

    # throws Exception
    def init(self, rectangle: Rectangle) -> None:
        super().init(rectangle, FormTypeFactory.getInstance().TEMP_HORIZONTAL_FORM)
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.form.FormTypeFactory import FormTypeFactory
from org.allbinary.graphics.form.ItemPaintableFactory import ItemPaintableFactory


