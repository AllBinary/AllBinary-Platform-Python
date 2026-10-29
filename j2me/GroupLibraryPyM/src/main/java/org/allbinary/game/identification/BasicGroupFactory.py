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

from org.allbinary.logic.NullUtil import NullUtil


class BasicGroupFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.NAME: str = "GROUP_NAME"
        self.NO_SUCH_GROUP: str = "No Such Group: "
        self.GOOD: Group = Group("Good Guys", ((int(0) + 32768) % 65536 - 32768))
        self.ENEMY: Group = Group("Bad Guys", ((int(1) + 32768) % 65536 - 32768))
        self.ENEMY_ON_LEVEL: Group = Group("Bad Guys on Level", ((int(2) + 32768) % 65536 - 32768))
        self.NONE: Group = Group("Not On A Team", ((int(3) + 32768) % 65536 - 32768))
        self.GOOD_ARRAY: list[Group] = [self.GOOD]
        self.ENEMY_ARRAY: list[Group] = [self.ENEMY]
        self.ENEMY_ON_LEVEL_ARRAY: list[Group] = [self.ENEMY, self.ENEMY_ON_LEVEL]
        self.NONE_ARRAY: list[Group] = [self.NONE]

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BasicGroupFactory:
        if BasicGroupFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            BasicGroupFactory.instance = BasicGroupFactory()
        return BasicGroupFactory.instance
from org.allbinary.game.identification.Group import Group


