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



class MethodUtil:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def viewAll(myClass: type, lineBreak: str) -> str:
        from org.allbinary.logic.java.anyType.ParamsUtil import ParamsUtil
        stringBuffer: StringMaker = StringMaker()
        method: list[Method] = myClass.getMethods()
        stringBuffer.append("Methods: ")
        stringBuffer.append(lineBreak)
        for index in range(0, len(method)):
            stringBuffer.append(method[index].getReturnType().getName())
            stringBuffer.append(" ")
            stringBuffer.append(method[index].getName())
            stringBuffer.append("(")
            ParamsUtil.viewParams(method[index].getParameterTypes())
            stringBuffer.append(")")
            stringBuffer.append(lineBreak)
        return str(stringBuffer)
# from java.lang.reflect.Method import Method
from org.allbinary.logic.string.StringMaker import StringMaker


