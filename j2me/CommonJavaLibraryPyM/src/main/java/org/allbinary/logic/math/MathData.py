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
# package org.allbinary.logic.math

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class MathData:
    instance: MathData = None

    def _init_fields(self) -> None:
        if "EQUALS" not in vars(self): self.EQUALS: str = None
        self.PLUS: str = "+"
        self.GREATER_THAN: str = ">"
        if "MINUS" not in vars(self): self.MINUS: str = None
        if "DIVIDE" not in vars(self): self.DIVIDE: str = None
        if "MULTIPLY" not in vars(self): self.MULTIPLY: str = None
    

    @staticmethod
    def getInstance() -> MathData:
        return MathData.instance
    

    def __init__(self) -> None:
        from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
        from org.allbinary.string.CommonSeps import CommonSeps
        __class__._init_fields(self)
        commonSeps: CommonSeps = CommonSeps.getInstance()
        self.EQUALS = commonSeps.EQUALS
        self.MINUS = commonSeps.DASH
        self.DIVIDE = commonSeps.FORWARD_SLASH
        self.MULTIPLY = CommonPhoneStrings.getInstance().STAR
# from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
# from org.allbinary.string.CommonSeps import CommonSeps


def _MathData_instance() -> object:
    return MathData()

lazy_static(MathData, "instance", _MathData_instance)

