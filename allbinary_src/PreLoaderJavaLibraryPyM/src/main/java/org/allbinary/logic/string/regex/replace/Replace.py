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
# package org.allbinary.logic.string.regex.replace

from __future__ import annotations



class Replace:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.j2seUtil: J2SEUtil = J2SEUtil.getInstance()
        self.REPLACERS_: str = "Replacers: "
        self.ALL: str = "all"
        self.FOUND_KEY: str = "found key total: "
        self.hashMap: dict = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor2(self, key: str, value: str) -> None:
        self._init_fields()
        self.hashMap = StdUtil.getInstance().createHashMap()
        self.hashMap.put([key], [value])
    

    def _constructor2(self, keys: list[str], values: list[str]) -> None:
        self._init_fields()
        self.hashMap = StdUtil.getInstance().createHashMap()
        self.hashMap.put(keys, values)
    

    def _constructor1(self, hashMap: dict) -> None:
        self._init_fields()
        self.hashMap = hashMap
    

    def all(self, replace: str) -> str:
        return self.upTo(replace, -2147483648)
    

    def upTo(self, replace: str, total: int) -> str:
        newStringBuffer: StringMaker = StringMaker()
        totalNumberOfReplaces: int = 0
        keys: list[str] = None
        values: list[str] = None
        keyArray: list[object] = self.j2seUtil.getHashMapAsArray(self.hashMap)
        size: int = len(keyArray)
        for index2 in range(0, size):
            keys = keyArray[index2]
            values = self.hashMap.get(keys)
            foundTotal: int = 0
            index: int = 0
            nextKey: str = None
            end: int = 0
            nextSecondKey: str = None
            begin2: int = 0
            while index < len(replace):
                begin: int = replace.find(keys[0], index)
                if begin != -1:
                    foundTotal += 1
                    if foundTotal % 100 == 0:
                        print(self.FOUND_KEY + str(foundTotal))
                    nextKey = keys[0]
                    end = begin + len(nextKey)
                    newStringBuffer.delete(0, newStringBuffer.length())
                    newStringBuffer.append(replace[0:begin])
                    newStringBuffer.append(values[0])
                    index = newStringBuffer.length()
                    newStringBuffer.append(replace[end:len(replace)])
                    replace = str(newStringBuffer)
                    if len(keys) > 1:
                        nextSecondKey = keys[1]
                        begin2 = replace.find(nextSecondKey, index)
                        if begin2 != -1:
                            end2: int = begin2 + len(nextSecondKey)
                            newStringBuffer.delete(0, newStringBuffer.length())
                            newStringBuffer.append(replace[0:begin2])
                            newStringBuffer.append(values[1])
                            index = newStringBuffer.length()
                            newStringBuffer.append(replace[end2:len(replace)])
                            replace = str(newStringBuffer)
                    totalNumberOfReplaces += 1
                    if total != -2147483648 and totalNumberOfReplaces >= total:
                        break
                else:
                    break
        if totalNumberOfReplaces > 0:
            if LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().REPLACE):
                self.logUtil.putF("Total Number Of Replaces: " + str(totalNumberOfReplaces), self, self.ALL)
        return replace
    

    def line(self, replace: str) -> str:
        newStringBuffer: StringMaker = StringMaker()
        totalNumberOfReplaces: int = 0
        key: str = None
        value: str = None
        keyArray: list[object] = self.j2seUtil.getHashMapAsArray(self.hashMap)
        size: int = len(keyArray)
        for index2 in range(0, size):
            key = keyArray[index2]
            value = self.hashMap.get(key)
            index: int = 0
            while index < len(replace):
                newStringBuffer.delete(0, newStringBuffer.length())
                begin: int = replace.find(key, index)
                if begin != -1:
                    print(self.FOUND_KEY)
                    end: int = replace.find('\n', begin + len(key)) + 1
                    if end >= 0:
                        newStringBuffer.append(replace[0:begin])
                        index = newStringBuffer.length()
                        newStringBuffer.append(replace[end:len(replace)])
                        replace = str(newStringBuffer)
                        totalNumberOfReplaces += 1
                else:
                    break
        if LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().REPLACE):
            self.logUtil.putF("Total Number Of Replaces: " + str(totalNumberOfReplaces), self, self.ALL)
        return replace
    

    @staticmethod
    def main(args: list[str]) -> None:
        try:
            stringUtil: StringUtil = StringUtil.getInstance()
            appUrlGlobals: AppUrlGlobals = AppUrlGlobals()
            appUrlGlobals.setWebappPath("G:/mnt/bc/mydev/work/allbinary_src/ToolsJavaLibrary/tools")
            self.URLGLOBALS.init(appUrlGlobals)
            testString: str = "\"super gun\" big tank \"goodgunriflegun"
            replace: Replace = Replace("gun", "abcdefghijklmnopqrstuxwxyzabcdefghijklmnopqrstuxwxyz")
            print("Old String: " + testString)
            testString = replace.all(testString)
            print("New String: " + testString)
            replaceCat: Replace = Replace("abcdefghijklmnopqrstuxwxyzabcdefghijklmnopqrstuxwxyz", stringUtil.EMPTY_STRING)
            testString = replaceCat.all(testString)
            print("New String: " + testString)
        except Exception as e:
            pass
# from java.util.HashMap import HashMap
from org.allbinary.J2SEUtil import J2SEUtil
from org.allbinary.globals.AppUrlGlobals import AppUrlGlobals
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


