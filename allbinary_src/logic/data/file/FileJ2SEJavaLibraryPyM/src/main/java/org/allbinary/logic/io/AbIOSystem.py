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
# package org.allbinary.logic.io

from __future__ import annotations



class AbIOSystem:
    instance: AbIOSystem = None

    def _init_fields(self) -> None:
        self.type_: str = "java.io"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> AbIOSystem:
        return AbIOSystem.instance
    

    def getType(self) -> str:
        return self.type_
    

    def isType(self, type_: str) -> bool:
        if ((self.type_ > type_) - (self.type_ < type_)) == 0:
            return True
        else:
            return False


AbIOSystem.instance = AbIOSystem()

