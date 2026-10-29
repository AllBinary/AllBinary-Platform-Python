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



class ConstructorUtil:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def viewAll(myClass: type, lineBreak: str) -> str:
        stringBuffer: StringMaker = StringMaker()
        constructor: list[Constructor] = myClass.getConstructors()
        stringBuffer.append("Constructors: ")
        stringBuffer.append(lineBreak)
        for index in range(0, len(constructor)):
            stringBuffer.append(ConstructorUtil.view(constructor[index], lineBreak))
        return str(stringBuffer)
    

    @staticmethod
    def view(constructor: Constructor, lineBreak: str) -> str:
        if constructor is not None:
            commonSeps: CommonSeps = CommonSeps.getInstance()
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(constructor.getName())
            classes: list[type] = constructor.getParameterTypes()
            for index in range(0, len(classes)):
                stringBuffer.append(commonSeps.SPACE)
                stringBuffer.append(classes[index].getName())
                stringBuffer.append(commonSeps.COLON)
                stringBuffer.appendint(index)
            stringBuffer.append(lineBreak)
            return str(stringBuffer)
        else:
            return "Constructor Null"
# from java.lang.reflect.Constructor import Constructor
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps


