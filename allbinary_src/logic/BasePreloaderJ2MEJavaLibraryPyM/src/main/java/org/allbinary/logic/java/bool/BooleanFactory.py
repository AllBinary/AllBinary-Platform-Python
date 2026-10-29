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
# package org.allbinary.logic.java.bool

from __future__ import annotations



class BooleanFactory:
    instance: BooleanFactory = None

    def _init_fields(self) -> None:
        self.TRUE: bool = True
        self.FALSE: bool = False
        self.TRUE_STRING: str = str(self.TRUE)
        self.FALSE_STRING: str = str(self.FALSE)
        self.YES: str = "yes"
        self.NO: str = "no"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BooleanFactory:
        return BooleanFactory.instance
    

    def toStringb(self, bool: bool) -> str:
        if bool:
            return self.TRUE_STRING
        else:
            return self.FALSE_STRING


BooleanFactory.instance = BooleanFactory()

