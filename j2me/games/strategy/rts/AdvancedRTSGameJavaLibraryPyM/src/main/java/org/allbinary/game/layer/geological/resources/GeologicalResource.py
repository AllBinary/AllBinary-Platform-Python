# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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
# package org.allbinary.game.layer.geological.resources

from __future__ import annotations



class GeologicalResource:

    def _init_fields(self) -> None:
        self.total: int = 0
        self.initTotal: int = None
    

    def __init__(self, initTotal: int) -> None:
        self._init_fields()
        self.initTotal = initTotal
        self.init()
    

    def init(self) -> None:
        self.setTotal(self.initTotal)
    

    def add(self, value: int) -> None:
        max: int = 2147483647
        if self.getTotal() + value > max:
            self.setTotal(max)
        else:
            self.setTotal(self.getTotal() + value)
    

    def remove(self, value: int) -> None:
        if self.getTotal() - value < 0:
            self.setTotal(0)
        else:
            self.setTotal(self.getTotal() - value)
    

    def getTotal(self) -> int:
        return self.total
    

    def setTotal(self, total: int) -> None:
        self.total = total


