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
# package org.allbinary.logic.java.array

from __future__ import annotations



class IntArrayUtil:
    

    def __init__(self) -> None:
        pass
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def toString_j1_1(array: list[int]) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        for index in range(0, len(array)):
            stringBuffer.appendint(array[index])
            if index < len(array):
                stringBuffer.append(", ")
        return str(stringBuffer)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def toString_j1_2(array: list[list[int]]) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        for index in range(0, len(array)):
            stringBuffer.append("{")
            for index2 in range(0, len(array[index])):
                stringBuffer.appendint(int(array[index][index2]))
                if index2 < len(array[index]) - 1:
                    stringBuffer.append(", ")
            stringBuffer.append("}")
            if index < len(array) - 1:
                stringBuffer.append(", \n")
        return str(stringBuffer)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def toString_j1_3(array: list[list[list[int]]]) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        for index in range(0, len(array)):
            stringBuffer.append("{")
            for index2 in range(0, len(array[index])):
                stringBuffer.append("{")
                for index3 in range(0, len(array[index][index2])):
                    stringBuffer.appendint(int(array[index][index2][index3]))
                    if index3 < len(array[index][index2]) - 1:
                        stringBuffer.append(", ")
                stringBuffer.append("}")
                if index2 < len(array[index]) - 1:
                    stringBuffer.append(", ")
            stringBuffer.append("}")
            if index < len(array) - 1:
                stringBuffer.append(", \n")
        return str(stringBuffer)

    @staticmethod
    def toString(*args):
        if len(args) == 1 and True and (args[0] is None or isinstance(args[0], list)):
            return IntArrayUtil.toString_j1_1(*args)
        if len(args) == 1 and True and (args[0] is None or isinstance(args[0], list)):
            return IntArrayUtil.toString_j1_2(*args)
        if len(args) == 1:
            return IntArrayUtil.toString_j1_3(*args)
        return getattr(IntArrayUtil, "toString_j" + str(len(args)))(*args)
# from org.allbinary.logic.string.StringMaker import StringMaker


