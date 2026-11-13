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
# package org.allbinary.logic.java.bool

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class BooleanUtil:
    instance: BooleanUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.TsUtil import TsUtil
        self.tsUtil: TsUtil = TsUtil.getInstance()
    

    @staticmethod
    def getInstance() -> BooleanUtil:
        return BooleanUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getFromString(self, booleanString: str) -> bool:
        from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        booleanFactory: BooleanFactory = BooleanFactory.getInstance()
        if stringValidationUtil.isEmpty(booleanString):
            return False
        booleanStringLowerCase: str = booleanString.lower()
        if ((booleanStringLowerCase > booleanFactory.TRUE_STRING) - (booleanStringLowerCase < booleanFactory.TRUE_STRING)) == 0:
            return True
        elif ((booleanStringLowerCase > booleanFactory.FALSE_STRING) - (booleanStringLowerCase < booleanFactory.FALSE_STRING)) == 0:
            return False
        else:
            raise Exception("Invalid booleanString - Must be true or false")
    

    # throws Exception
    def isStringBoolean(self, booleanString: str) -> bool:
        from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
        booleanFactory: BooleanFactory = BooleanFactory.getInstance()
        booleanStringLowerCase: str = booleanString.lower()
        if ((booleanStringLowerCase > booleanFactory.TRUE_STRING) - (booleanStringLowerCase < booleanFactory.TRUE_STRING)) == 0 or ((booleanStringLowerCase > booleanFactory.FALSE_STRING) - (booleanStringLowerCase < booleanFactory.FALSE_STRING)) == 0:
            return True
        return False
    

    def toStringFromBooleanArray(self, booleanArray: list[bool]) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringMaker: StringMaker = StringMaker()
        size: int = len(booleanArray)
        for index in range(0, size):
            stringMaker.appendboolean(booleanArray[index])
        return str(stringMaker)
# from org.allbinary.TsUtil import TsUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil


def _BooleanUtil_instance() -> object:
    return BooleanUtil()

lazy_static(BooleanUtil, "instance", _BooleanUtil_instance)

