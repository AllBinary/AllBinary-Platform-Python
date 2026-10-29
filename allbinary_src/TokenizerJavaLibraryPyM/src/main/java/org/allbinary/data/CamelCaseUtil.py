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
# package org.allbinary.data

from __future__ import annotations



class CamelCaseUtil:
    instance: CamelCaseUtil = None

    def _init_fields(self) -> None:
        self.commonSeps: CommonSeps = CommonSeps.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CamelCaseUtil:
        return CamelCaseUtil.instance
    

    # throws Exception
    def getAsCamelCase(self, string: str, stringBuilder: StringMaker) -> str:
        if string is None:
            return StringUtil.getInstance().EMPTY_STRING
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        stringBuilder.delete(0, stringBuilder.length())
        list_: BasicArrayList = BasicArrayListD()
        tokenizer: Tokenizer = Tokenizer(self.commonSeps.UNDERSCORE)
        tokenizer.getTokensFromString(string, list_)
        size: int = list_.size()
        word: str = None
        for i in range(0, size):
            word = list_.get(i)
            word = (word if stringValidationUtil.isEmpty(word) else str(StringMaker().appendchar(word[0].upper()).append(word[1:].lower())))
            stringBuilder.append(word)
        return str(stringBuilder)
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.string.tokens.Tokenizer import Tokenizer
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


CamelCaseUtil.instance = CamelCaseUtil()

