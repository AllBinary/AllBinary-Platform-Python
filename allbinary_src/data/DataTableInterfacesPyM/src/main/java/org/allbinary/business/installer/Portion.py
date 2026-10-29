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
# package org.allbinary.business.installer

from __future__ import annotations



class Portion:

    def _init_fields(self) -> None:
        self.current: int = None
        self.total: int = None
    

    def __init__(self, hashMap: dict) -> None:
        self._init_fields()
        self.current = hashMap.get("current")
        self.total = hashMap.get("total")
    

    def getCurrent(self) -> int:
        return self.current
    

    def getTotal(self) -> int:
        return self.total
# from java.util.HashMap import HashMap


