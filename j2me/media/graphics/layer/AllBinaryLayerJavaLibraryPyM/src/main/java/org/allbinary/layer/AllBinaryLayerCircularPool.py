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
# package org.allbinary.layer

from __future__ import annotations

from org.allbinary.logic.util.cache.BaseCircularPool import BaseCircularPool


class AllBinaryLayerCircularPool(BaseCircularPool):
    

    def __init__(self) -> None:
        super().__init__()
    

    # throws Exception
    def initAllBinaryLayerCircularPool(self, allbinaryLayerFactoryInterface: AllBinaryLayerFactoryInterface, total: int) -> None:
        self.circularIndexUtil = CircularIndexUtil.createInstance(total)
        self.OBJECT_ARRAY = [None] * (total)
        for localIndex in range(0, total):
            self.OBJECT_ARRAY[localIndex] = allbinaryLayerFactoryInterface.getInstance()
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


