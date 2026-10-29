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
# package org.allbinary.logic.system.security.licensing

from __future__ import annotations



class LockableFeatureFactory:
    instance: LockableFeatureFactory = None

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListD()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> LockableFeatureFactory:
        return LockableFeatureFactory.instance
    

    def getList(self) -> BasicArrayList:
        return self.list_
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


LockableFeatureFactory.instance = LockableFeatureFactory()

