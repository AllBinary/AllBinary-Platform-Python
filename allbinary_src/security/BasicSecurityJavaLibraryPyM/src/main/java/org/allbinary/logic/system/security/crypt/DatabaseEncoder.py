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
# package org.allbinary.logic.system.security.crypt

from __future__ import annotations



class DatabaseEncoder:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def encode(value: list[int]) -> str:
        try:
            array: list[int] = value
            stringBuffer: StringMaker = StringMaker()
            for index in range(0, len(array)):
                stringBuffer.append(str(int(array[index])))
                if index < len(array) - 1:
                    stringBuffer.append(CommonSeps.getInstance().SPACE)
            return str(stringBuffer)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            PreLogUtil.putOE(commonStrings.EXCEPTION, "DatabaseEncoder", "decode", e)
            return StringUtil.getInstance().EMPTY_STRING
    

    @staticmethod
    def decode(value: str) -> list[int]:
        try:
            tokenizer: Tokenizer = Tokenizer(CommonSeps.getInstance().SPACE)
            vector: BasicArrayList = tokenizer.getTokensFromString(value, BasicArrayListD())
            byteVector: BasicArrayList = BasicArrayListD()
            size: int = vector.size()
            byteOfData: str = None
            for index in range(0, size):
                byteOfData = vector.objectArray[index]
                byteVector.add(int(byteOfData))
            decode: list[int] = [0] * (byteVector.size())
            decodeIndex: int = 0
            aByte: int = None
            for index in range(0, size):
                aByte = byteVector.objectArray[index]
                decode[decodeIndex] = int(aByte)
                decodeIndex += 1
            return decode
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            PreLogUtil.putSE(commonStrings.EXCEPTION, "DatabaseEncoder", "decode", e)
            return NullUtil.getInstance().NULL_BYTE_ARRAY
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.tokens.Tokenizer import Tokenizer
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


