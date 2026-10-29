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
# package org.allbinary.logic.java.anyType.clazz

from __future__ import annotations



class ClassUtil:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def viewAll(anyType: object, lineBreak: str) -> str:
        if anyType is not None:
            return ClassUtil.viewAll(type(anyType), lineBreak)
        else:
            return "Object Null"
    

    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def viewAll(myClass: type, lineBreak: str) -> str:
        if myClass is not None:
            stringBuffer: StringMaker = StringMaker()
            classes: list[type] = myClass.getClasses()
            stringBuffer.append(lineBreak)
            stringBuffer.append("Class: ")
            stringBuffer.append(myClass.getName())
            stringBuffer.append(" uses ")
            stringBuffer.appendint(len(classes))
            stringBuffer.append(" other classes")
            stringBuffer.append(lineBreak)
            stringBuffer.append(lineBreak)
            stringBuffer.append("Classes: ")
            stringBuffer.append(lineBreak)
            for index in range(0, len(classes)):
                stringBuffer.append("Class: ")
                stringBuffer.append(classes[index].getName())
                stringBuffer.append(lineBreak)
            stringBuffer.append(InterfaceUtil.viewAll(myClass, lineBreak))
            stringBuffer.append(lineBreak)
            stringBuffer.append(ConstructorUtil.viewAll(myClass, lineBreak))
            stringBuffer.append(lineBreak)
            stringBuffer.append(MethodUtil.viewAll(myClass, lineBreak))
            return str(stringBuffer)
        else:
            return "Class Null"
from org.allbinary.logic.java.anyType.ConstructorUtil import ConstructorUtil
from org.allbinary.logic.java.anyType.InterfaceUtil import InterfaceUtil
from org.allbinary.logic.java.anyType.MethodUtil import MethodUtil
from org.allbinary.logic.string.StringMaker import StringMaker


