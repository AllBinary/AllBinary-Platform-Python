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
# package org.allbinary.logic.util.event

from __future__ import annotations

from org.allbinary.logic.util.cache.BaseCircularPool import BaseCircularPool


class AllBinaryEventCircularPool(BaseCircularPool):
    

    def __init__(self, max: int) -> None:
        super().__init__()
        self.OBJECT_ARRAY = [None] * (max)
        self.circularIndexUtil = CircularIndexUtil.createInstance(max)
    

    def initAllBinaryEventCircularPool(self, allBinaryEventObjectFactoryInterface: AllBinaryEventObjectFactoryInterface) -> None:
        self.circularIndexUtil.setIndex(0)
        size: int = self.circularIndexUtil.getSize()
        for index in range(0, size):
            self.OBJECT_ARRAY[index] = allBinaryEventObjectFactoryInterface.getInstance()
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


