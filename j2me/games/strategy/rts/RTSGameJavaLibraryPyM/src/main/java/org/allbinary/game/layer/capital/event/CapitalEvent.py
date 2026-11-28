# 
# AllBinary Open License Version 1 
# Copyright (c) 2002 AllBinary 
#  
# By agreeing to this license you and any business entity you represent are 
# legally bound to the AllBinary Open License Version 1 legal agreement. 
#  
# You may obtain the AllBinary Open License Version 1 legal agreement from 
# AllBinary or the root directory of AllBinary's AllBinary Platform repository. 
#  
# Created By: Travis Berthelot  
# Generated Code Do Not Modify
# package org.allbinary.game.layer.capital.event

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


@java_inherited_overloads
class CapitalEvent(AllBinaryEventObject):
    def _java_defaults(self):
        vars(self).setdefault("value", 0)

    def _init_fields(self) -> None:
        if "value" not in vars(self): self.value: int = 0
    

    def __init__(self, anyType: object) -> None:
        __class__._java_defaults(self)
        super().__init__(anyType)
        __class__._init_fields(self)
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("CapitalEvent: Value: \n")
        stringBuffer.appendint(self.getValue())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def getValue(self) -> int:
        return self.value
    

    def setValue(self, value: int) -> None:
        self.value = value
# from org.allbinary.logic.string.StringMaker import StringMaker


