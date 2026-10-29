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
# package org.allbinary.game.identification

from __future__ import annotations



class CompositeGroup:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.groupInterface: Group = None
        self.list_: BasicArrayList = BasicArrayListD()
    

    def __init__(self, groupInterface: Group) -> None:
        self._init_fields()
        self.groupInterface = groupInterface
    

    def clear(self) -> None:
        self.list_.clear()
    

    def add(self, groupInterface: Group) -> None:
        from org.allbinary.game.identification.GroupCommonFactory import GroupCommonFactory
        commonStrings: CommonStrings = CommonStrings.getInstance()
        groupCommonFactory: GroupCommonFactory = GroupCommonFactory.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(groupCommonFactory.ADDING_LABEL)
        stringBuffer.append(str(groupInterface))
        stringBuffer.append(groupCommonFactory.TO_LABEL)
        stringBuffer.append(StringUtil.getInstance().toString(self.groupInterface))
        self.logUtil.putF(str(stringBuffer), self, commonStrings.ADD)
        self.list_.add(groupInterface)
    

    def isInGroup(self, groupInterface: Group) -> bool:
        if self.list_.contains(groupInterface):
            return True
        else:
            return False
    

    def getGroup(self) -> Group:
        return self.groupInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


