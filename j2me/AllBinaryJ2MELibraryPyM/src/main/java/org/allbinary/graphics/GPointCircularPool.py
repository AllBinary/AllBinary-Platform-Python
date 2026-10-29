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
# package org.allbinary.graphics

from __future__ import annotations

from org.allbinary.logic.util.cache.BaseCircularPool import BaseCircularPool


class GPointCircularPool(BaseCircularPool):
    

    def __init__(self, size: int) -> None:
        from org.allbinary.graphics.CustomGPoint import CustomGPoint
        super().__init__()
        self.circularIndexUtil = CircularIndexUtil.createInstance(size)
        self.OBJECT_ARRAY = [None] * (size)
        for index in range(size - 1, 0 - 1, -1):
            self.OBJECT_ARRAY[index] = CustomGPoint.getInstance3(0, 0)
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


