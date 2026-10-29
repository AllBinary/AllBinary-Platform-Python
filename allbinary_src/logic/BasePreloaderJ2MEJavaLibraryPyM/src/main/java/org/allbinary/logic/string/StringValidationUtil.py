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
# package org.allbinary.logic.string

from __future__ import annotations



class StringValidationUtil:
    instance: StringValidationUtil = None

    def _init_fields(self) -> None:
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.tsUtil: TsUtil = TsUtil.getInstance()
    

    @staticmethod
    def getInstance() -> StringValidationUtil:
        return StringValidationUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def containsSpaces(self, value: str) -> bool:
        if value.find(' ') >= 0:
            return True
        return False
    

    def isNumber(self, value: str) -> bool:
        numberOfDecimalPoints: int = 0
        for index in range(0, len(value)):
            digit: str = value[index]
            if not self.isNumberFromChar(digit) and digit != '.':
                return False
            if digit == '.':
                numberOfDecimalPoints += 1
                if numberOfDecimalPoints > 1:
                    return False
        return True
    

    def isNumberFromChar(self, digit: str) -> bool:
        if digit != '0' and digit != '1' and digit != '2' and digit != '3' and digit != '4' and digit != '5' and digit != '6' and digit != '7' and digit != '8' and digit != '9':
            return False
        return True
    

    def isValidRequired(self, value: str, min: int, max: int) -> bool:
        if value is None or len(value) < min or len(value) > max:
            return False
        return True
    

    def isValidRequiredNumber(self, value: str, min: int, max: int) -> bool:
        if self.isEmpty(value) or len(value) < min or len(value) > max:
            return False
        if not self.isNumber(value):
            return False
        return True
    

    def isValidNotRequired(self, value: str, min: int, max: int) -> bool:
        if value is not None:
            if len(value) < min or len(value) > max:
                return False
        return True
    

    def isValidNotRequiredNumber(self, value: str, min: int, max: int) -> bool:
        if value is not None:
            if ((value > self.stringUtil.NULL_STRING) - (value < self.stringUtil.NULL_STRING)) == 0 or len(value) < min or len(value) > max:
                return False
            if not self.isNumber(value):
                return False
        return True
    

    def isEmpty(self, string: str) -> bool:
        if string is not None and ((string > self.stringUtil.NULL_STRING) - (string < self.stringUtil.NULL_STRING)) != 0 and ((string > self.stringUtil.EMPTY_STRING) - (string < self.stringUtil.EMPTY_STRING)) != 0:
            return False
        else:
            return True
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.string.StringUtil import StringUtil


StringValidationUtil.instance = StringValidationUtil()

