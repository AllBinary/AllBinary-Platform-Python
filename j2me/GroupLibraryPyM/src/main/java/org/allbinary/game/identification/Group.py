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

from org.allbinary.game.identification.GroupInterface import GroupInterface


class Group(GroupInterface):

    def _init_fields(self) -> None:
        self.name: str = StringUtil.getInstance().EMPTY_STRING
        self.teamId: int = None
        self.string: str = StringUtil.getInstance().EMPTY_STRING
    

    def __init__(self, teamName: str, teamId: int) -> None:
        self._init_fields()
        self.teamId = teamId
        self.setName(teamName)
    

    def getGroupName(self) -> str:
        return self.name
    

    def setName(self, name: str) -> None:
        from org.allbinary.game.identification.GroupCommonFactory import GroupCommonFactory
        self.name = name
        groupCommonFactory: GroupCommonFactory = GroupCommonFactory.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(groupCommonFactory.GROUP_NAME_LABEL)
        stringBuffer.append(self.name)
        stringBuffer.append(groupCommonFactory.ID_LABEL)
        stringBuffer.appendshort(self.teamId)
        self.string = str(stringBuffer)
    

    def getGroupId(self) -> int:
        return self.teamId
    

    def toString(self) -> str:
        return self.string

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil


