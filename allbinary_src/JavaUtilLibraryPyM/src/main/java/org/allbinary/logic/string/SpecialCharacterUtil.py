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



class SpecialCharacterUtil:
    

    @staticmethod
    def getHashMap() -> dict:
        from org.allbinary.logic.string.StringUtil import StringUtil
        commonSeps: CommonSeps = CommonSeps.getInstance()
        commonPhoneStrings: CommonPhoneStrings = CommonPhoneStrings.getInstance()
        stringUtil: StringUtil = StringUtil.getInstance()
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put("!", stringUtil.EMPTY_STRING)
        hashMap.put("@", stringUtil.EMPTY_STRING)
        hashMap.put(commonPhoneStrings.POUND, stringUtil.EMPTY_STRING)
        hashMap.put("$", stringUtil.EMPTY_STRING)
        hashMap.put("%", stringUtil.EMPTY_STRING)
        hashMap.put("^", stringUtil.EMPTY_STRING)
        hashMap.put(commonSeps.AMPERSAND, stringUtil.EMPTY_STRING)
        hashMap.put(commonPhoneStrings.STAR, stringUtil.EMPTY_STRING)
        hashMap.put(commonSeps.PARENTHESIS_OPEN, stringUtil.EMPTY_STRING)
        hashMap.put(commonSeps.PARENTHESIS_CLOSE, stringUtil.EMPTY_STRING)
        hashMap.put(commonSeps.DASH, stringUtil.EMPTY_STRING)
        hashMap.put(commonSeps.UNDERSCORE, stringUtil.EMPTY_STRING)
        hashMap.put(MathData.getInstance().PLUS, stringUtil.EMPTY_STRING)
        hashMap.put(commonSeps.EQUALS, stringUtil.EMPTY_STRING)
        hashMap.put("\\", stringUtil.EMPTY_STRING)
        hashMap.put("|", stringUtil.EMPTY_STRING)
        hashMap.put(AbPathData.getInstance().EXTENSION_SEP, stringUtil.EMPTY_STRING)
        hashMap.put(",", stringUtil.EMPTY_STRING)
        hashMap.put("<", stringUtil.EMPTY_STRING)
        hashMap.put(">", stringUtil.EMPTY_STRING)
        hashMap.put("?", stringUtil.EMPTY_STRING)
        hashMap.put(AbPathData.getInstance().SEPARATOR, stringUtil.EMPTY_STRING)
        hashMap.put("~", stringUtil.EMPTY_STRING)
        hashMap.put("`", stringUtil.EMPTY_STRING)
        return hashMap
# from java.util.HashMap import HashMap
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.math.MathData import MathData
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
from org.allbinary.string.CommonSeps import CommonSeps


