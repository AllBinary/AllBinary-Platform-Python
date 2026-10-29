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
# package org.allbinary.logic.java

from __future__ import annotations



class PrimitiveArrayToString:
    

    @staticmethod
    def toString(floats: list[float]) -> str:
        stringBuffer: StringMaker = StringMaker()
        for index in range(0, len(floats)):
            stringBuffer.appendfloat(floats[index])
        return str(stringBuffer)
from org.allbinary.logic.string.StringMaker import StringMaker


