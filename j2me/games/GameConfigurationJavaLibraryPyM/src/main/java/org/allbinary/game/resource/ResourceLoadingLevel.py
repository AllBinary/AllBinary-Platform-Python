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
# package org.allbinary.game.resource

from __future__ import annotations



class ResourceLoadingLevel:

    def _init_fields(self) -> None:
        self.name: str = None
        self.level: int = None
    

    def __init__(self, name: str, level: int) -> None:
        self._init_fields()
        self.name = name
        self.level = level
    

    def getLevel(self) -> int:
        return self.level
    

    def getName(self) -> str:
        return self.name


