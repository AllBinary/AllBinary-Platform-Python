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
# package org.allbinary.logic.java.anyType

from __future__ import annotations



class ParamsUtil:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def viewParams(params: list[type]) -> str:
        if params is not None:
            stringBuffer: StringMaker = StringMaker()
            for index in range(0, len(params)):
                stringBuffer.append(" ")
                stringBuffer.append(params[index].getName())
            return str(stringBuffer)
        else:
            return "Params Null"
from org.allbinary.logic.string.StringMaker import StringMaker


