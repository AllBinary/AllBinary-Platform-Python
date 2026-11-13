# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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

from java.lang.JavaRuntimeStatic import lazy_static


class ItemIndexPaintable:
    instance: ItemIndexPaintable = None
    

    @staticmethod
    def getInstance() -> ItemIndexPaintable:
        return ItemIndexPaintable.instance
    

    # throws Exception
    def paint(self, graphics: Graphics, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
        return 0
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem


def _ItemIndexPaintable_instance() -> object:
    return ItemIndexPaintable()

lazy_static(ItemIndexPaintable, "instance", _ItemIndexPaintable_instance)

