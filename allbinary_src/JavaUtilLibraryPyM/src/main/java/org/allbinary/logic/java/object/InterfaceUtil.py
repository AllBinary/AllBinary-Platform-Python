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



class InterfaceUtil:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def viewAll(myClass: type, lineBreak: str) -> str:
        stringBuffer: StringMaker = StringMaker()
        interfaces: list[type] = myClass.getInterfaces()
        stringBuffer.append(lineBreak)
        stringBuffer.append("Interfaces: ")
        stringBuffer.append(lineBreak)
        for index in range(0, len(interfaces)):
            stringBuffer.append("Interface: ")
            stringBuffer.append(interfaces[index].getName())
            stringBuffer.append(lineBreak)
        return str(stringBuffer)
    

    @staticmethod
    def getClass(interfaceName: str, interfaces: list[type]) -> type:
        if interfaceName is not None and interfaces is not None and len(interfaces) > 0:
            for index in range(0, len(interfaces)):
                if interfaces[index].getName().indexOf(interfaceName) >= 0:
                    return interfaces[index]
        return None
    

    @staticmethod
    def isImplemented(clazz: type, anyType: object) -> bool:
        classes: list[type] = type(anyType).getInterfaces()
        for index in range(0, len(classes)):
            if clazz.getName().compareTo(classes[index].getName()) == 0:
                return True
        return False
    

    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def isImplemented(className: str, anyType: object) -> bool:
        classes: list[type] = type(anyType).getInterfaces()
        for index in range(0, len(classes)):
            if classes[index].getName().indexOf(className) == 0:
                return True
        return False
    

    @staticmethod
    def isImplementedView(clazz: type, anyType: object) -> str:
        stringBuffer: StringMaker = StringMaker()
        classes: list[type] = type(anyType).getInterfaces()
        stringBuffer.append("isImplementedView: \n")
        for index in range(0, len(classes)):
            stringBuffer.append(clazz.getName())
            stringBuffer.append(" should be = ")
            stringBuffer.append(classes[index].getName())
            stringBuffer.append(classes[index].getName())
            stringBuffer.append(CommonSeps.getInstance().NEW_LINE)
        return str(stringBuffer)
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps


