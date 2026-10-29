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
# package org.allbinary.logic.string.tokens

from __future__ import annotations



class Tokenizer:

    def _init_fields(self) -> None:
        self.sep: str = None
        self.endSep: str = StringUtil.getInstance().EMPTY_STRING
    

    def __init__(self, sep: str) -> None:
        self._init_fields()
        if sep is None or TsUtil.getInstance().compareTo(sep, StringUtil.getInstance().EMPTY_STRING) == 0:
            raise Exception("Sep provided is not valid")
        self.sep = sep
    

    def setSep(self, sep: str) -> None:
        self.sep = sep
    

    def setEndSep(self, endSep: str) -> None:
        self.endSep = endSep
    

    def getInsideSep(self, string: str) -> BasicArrayList:
        tokenList: BasicArrayList = BasicArrayListD()
        index: int = 0
        size: int = len(string)
        while index < size:
            index = string.find(self.sep, index)
            if index != -1:
                end: int = string.find(self.endSep, index + len(self.sep))
                if end != -1:
                    tokenList.add(string[index + len(self.sep):end - (len(self.endSep) - 1)])
                    index = end + len(self.endSep)
                else:
                    pass
            else:
                break
        return tokenList
    

    def getTokensFromString(self, string: str, tokenVector: BasicArrayList) -> BasicArrayList:
        index: int = 0
        end: int = 0
        while index < len(string):
            end = string.find(self.sep, index)
            if end != -1:
                tokenVector.add(string[index:end])
                index = end + len(self.sep)
            else:
                tokenVector.add(string[index:len(string)])
                break
        return tokenVector
    

    def getTokens(self, stringVector: BasicArrayList) -> ABHashtable[object, object]:
        tokenHashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        string: str = StringUtil.getInstance().EMPTY_STRING
        end: int = 0
        size: int = stringVector.size()
        for index in range(0, size):
            string = stringVector.objectArray[index]
            end = string.find(self.sep)
            if end >= 0:
                tokenHashtable.put(string[0:end], string[end + 1:len(string)])
        return tokenHashtable
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


