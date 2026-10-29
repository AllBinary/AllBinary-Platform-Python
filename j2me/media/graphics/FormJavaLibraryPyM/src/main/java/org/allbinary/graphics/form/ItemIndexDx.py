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



class ItemIndexDx:
    instance: ItemIndexDx = None
    

    @staticmethod
    def getInstance() -> ItemIndexDx:
        return ItemIndexDx.instance
    

    # throws Exception
    def getDx(self, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
        return 0
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem


ItemIndexDx.instance = ItemIndexDx()

