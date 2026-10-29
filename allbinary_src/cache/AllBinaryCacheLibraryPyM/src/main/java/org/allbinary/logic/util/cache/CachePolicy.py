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
# package org.allbinary.logic.util.cache

from __future__ import annotations



class CachePolicy:

    def _init_fields(self) -> None:
        self.name: str = None
        self.maxTime: int = 0
        self.maxSize: int = 0
    

    def __init__(self, name: str, maxTime: int, maxSize: int) -> None:
        self._init_fields()
        self.name = name
        self.setMaxTime(maxTime)
        self.setMaxSize(maxSize)
    

    def getMaxTime(self) -> int:
        return self.maxTime
    

    def setMaxTime(self, maxTime: int) -> None:
        self.maxTime = maxTime
    

    def getMaxSize(self) -> int:
        return self.maxSize
    

    def setMaxSize(self, maxSize: int) -> None:
        self.maxSize = maxSize
    

    def getName(self) -> str:
        return self.name


