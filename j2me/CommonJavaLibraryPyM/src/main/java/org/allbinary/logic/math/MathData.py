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



class MathData:
    instance: MathData = None

    def _init_fields(self) -> None:
        self.EQUALS: str = None
        self.PLUS: str = "+"
        self.GREATER_THAN: str = ">"
        self.MINUS: str = None
        self.DIVIDE: str = None
        self.MULTIPLY: str = None
    

    @staticmethod
    def getInstance() -> MathData:
        return MathData.instance
    

    def __init__(self) -> None:
        self._init_fields()
        commonSeps: CommonSeps = CommonSeps.getInstance()
        self.EQUALS = commonSeps.EQUALS
        self.MINUS = commonSeps.DASH
        self.DIVIDE = commonSeps.FORWARD_SLASH
        self.MULTIPLY = CommonPhoneStrings.getInstance().STAR
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
from org.allbinary.string.CommonSeps import CommonSeps


MathData.instance = MathData()

