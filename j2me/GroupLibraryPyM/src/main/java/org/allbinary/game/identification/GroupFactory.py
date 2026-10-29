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



class GroupFactory:
    instance: GroupFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.NULL_GROUP_ARRAY: list[Group] = [None] * (0)
        self.list_: BasicArrayList = BasicArrayListD()
        self.index: int = 0

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GroupFactory:
        return GroupFactory.instance
    

    def getNextGroup(self) -> Group:
        group: Group = self.list_.objectArray[self.index]
        self.index += 1
        return group
    

    def getNextGroupByName(self, name: str) -> Group:
        group: Group = self.getNextGroup()
        group.setName(name)
        return group
    

    def init(self, groups: int, nameArray: list[str]) -> None:
        from org.allbinary.game.identification.Group import Group
        stringMaker: StringMaker = StringMaker()
        stringUtil: StringUtil = StringUtil.getInstance()
        TEAM: str = "Team "
        self.list_.clear()
        self.index = 0
        size: int = self.list_.size()
        while size < groups:
            name: str = stringUtil.EMPTY_STRING
            if size < len(nameArray):
                name = nameArray[size]
            else:
                stringMaker.delete(0, stringMaker.length())
                name = str(stringMaker.append(TEAM).appendint(size))
            self.list_.add(Group(name, ((int((size + 3)) + 32768) % 65536 - 32768)))
            size += 1
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


GroupFactory.instance = GroupFactory()

