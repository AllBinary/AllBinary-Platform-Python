# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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

from org.allbinary.logic.NullUtil import NullUtil


class GroupCommonFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.ID: int = SmallIntegerSingletonFactory.getInstance().getAt(10)
        self.GROUP_NAME_LABEL: str = "Group Name: "
        self.ID_LABEL: str = " Id: "
        self.ADDING_LABEL: str = "Adding: "
        self.TO_LABEL: str = " to: "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GroupCommonFactory:
        if GroupCommonFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            GroupCommonFactory.instance = GroupCommonFactory()
        return GroupCommonFactory.instance
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory


