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
# package org.allbinary.logic.java.number

from __future__ import annotations



class LongUtil:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def fillIn(end: str) -> str:
        from org.allbinary.logic.java.number.LongData import LongData
        from org.allbinary.logic.java.number.LongData import LongData
        frameStringBuffer: StringMaker = StringMaker()
        if frameStringBuffer.length() < LongData.MAX_LONG_LENGTH:
            commonPhoneStrings: CommonPhoneStrings = CommonPhoneStrings.getInstance()
            size: int = LongData.MAX_LONG_LENGTH - frameStringBuffer.length()
            for index in range(0, size):
                frameStringBuffer.append(commonPhoneStrings.ZERO)
        frameStringBuffer.append(end)
        return str(frameStringBuffer)
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings


