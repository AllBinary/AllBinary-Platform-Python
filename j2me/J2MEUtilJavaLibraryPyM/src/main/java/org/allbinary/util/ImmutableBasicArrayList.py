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
# package org.allbinary.util

from __future__ import annotations

from org.allbinary.util.BasicArrayListS import BasicArrayListS


class ImmutableBasicArrayList(BasicArrayListS):

    def _init_fields(self) -> None:
        self.name: str = None
    

    def __init__(self, name: str, size: int) -> None:
        super().__init__(size)
        self._init_fields()
        self.name = name
    

    def add(self, e: object) -> bool:
        ForcedLogUtil.log(self.name, self)
        return True
    

    def addAt(self, index: int, element: object) -> None:
        ForcedLogUtil.log(self.name, self)
    

    def toString(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil


