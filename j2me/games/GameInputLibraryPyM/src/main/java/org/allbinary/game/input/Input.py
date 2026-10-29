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
# package org.allbinary.game.input

from __future__ import annotations



class Input:

    def _init_fields(self) -> None:
        self.id: int = 0
        self.name: str = StringUtil.getInstance().EMPTY_STRING
    

    def __init__(self, id: int, name: str) -> None:
        self._init_fields()
        self.setId(id)
        self.setName(name)
    

    def getId(self) -> int:
        return self.id
    

    def setId(self, key: int) -> None:
        self.id = key
    

    def getName(self) -> str:
        return self.name
    

    def setName(self, keyName: str) -> None:
        self.name = keyName
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Name: ")
        stringBuffer.append(self.getName())
        stringBuffer.append(" Id: ")
        stringBuffer.appendint(self.getId())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil


