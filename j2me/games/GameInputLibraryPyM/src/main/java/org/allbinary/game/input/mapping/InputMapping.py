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
# package org.allbinary.game.input.mapping

from __future__ import annotations



class InputMapping:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        self.mappedList: BasicArrayList = BasicArrayListD()
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getTotalMapped(self) -> int:
        return self.hashtable.size()
    

    def isDefaultNew(self) -> bool:
        return False
    

    def getDefault(self) -> InputToGameKeyMapping:
        from org.allbinary.game.input.mapping.InputToGameKeyMapping import InputToGameKeyMapping
        return InputToGameKeyMapping.getNullInstance()
    

    def removeAll(self) -> None:
        self.hashtable.clear()
        self.mappedList.clear()
    

    def remove(self, input: Input, mappedToInput: Input) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringUtil: StringUtil = StringUtil.getInstance()
        stringBuffer.append(CommonLabels.getInstance().START_LABEL)
        stringBuffer.append(stringUtil.toString(input))
        stringBuffer.append(" == ")
        stringBuffer.append(stringUtil.toString(mappedToInput))
        self.logUtil.putF(str(stringBuffer), self, "InputMapping::remove")
        list_: BasicArrayList = self.getMappedInput(input)
        if list_.contains(mappedToInput):
            list_.remove(mappedToInput)
            self.mappedList.remove(mappedToInput)
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append("Removed: ")
            stringBuffer.append(stringUtil.toString(input))
            stringBuffer.append(" == ")
            stringBuffer.append(stringUtil.toString(mappedToInput))
            self.logUtil.putF(str(stringBuffer), self, "InputMapping::remove")
        else:
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append("Not Deleted: ")
            stringBuffer.append(stringUtil.toString(input))
            stringBuffer.append(" == ")
            stringBuffer.append(stringUtil.toString(mappedToInput))
            self.logUtil.putF(str(stringBuffer), self, "InputMapping::remove")
    

    # throws Exception
    def addMapping(self, inputToGameKeyMapping: InputToGameKeyMapping) -> None:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    def add(self, input: Input, mappedToInput: Input) -> None:
        list_: BasicArrayList = self.getMappedInput(input)
        if not list_.contains(mappedToInput):
            list_.add(mappedToInput)
            self.mappedList.add(mappedToInput)
    

    def isMapped(self, input: Input) -> bool:
        return self.mappedList.contains(input)
    

    def getMappedInput(self, id: Input) -> BasicArrayList:
        mappingInputCanBeNullList: object = self.hashtable.get(id)
        if mappingInputCanBeNullList is None:
            list_: BasicArrayList = BasicArrayListD()
            self.hashtable.put(id, list_)
            return list_
        return mappingInputCanBeNullList
    

    def getHashtable(self) -> ABHashtable[object, object]:
        return self.hashtable
from org.allbinary.game.input.Input import Input
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.ABHashtable import ABHashtable


