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
# package org.allbinary.game

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class GameMode:
    NONE: GameMode = None
    SERVER: GameMode = None
    CLIENT: GameMode = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.name: str = StringUtil.getInstance().EMPTY_STRING
    

    def __init__(self, name: str) -> None:
        self._init_fields()
        self.setName(name)
    

    def setName(self, name: str) -> None:
        self.name = name
    

    def getName(self) -> str:
        return self.name
    

    def toString(self) -> str:
        return self.getName()

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.logic.string.StringUtil import StringUtil


def _GameMode_NONE() -> object:
    from org.allbinary.logic.string.StringUtil import StringUtil
    return GameMode(StringUtil.getInstance().NULL_STRING)

lazy_static(GameMode, "NONE", _GameMode_NONE)

def _GameMode_SERVER() -> object:
    return GameMode("Server")

lazy_static(GameMode, "SERVER", _GameMode_SERVER)

def _GameMode_CLIENT() -> object:
    return GameMode("Client")

lazy_static(GameMode, "CLIENT", _GameMode_CLIENT)

