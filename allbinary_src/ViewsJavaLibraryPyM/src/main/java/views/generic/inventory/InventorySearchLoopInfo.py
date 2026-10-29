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
# package views.generic.inventory

from __future__ import annotations



class InventorySearchLoopInfo:

    def _init_fields(self) -> None:
        self.lastPage: int = -1
        self.currentPage: int = -1
        self.numberOfResultsOnCurrentPage: int = 0
        self.numberOfResults: int = 0
        self.CURRENT: str = "current: "
        self.NUM: str = " num: "
        self.LAST: str = " last: "

    def __init__(self) -> None:
        self._init_fields()
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.CURRENT)
        stringBuffer.appendint(self.currentPage)
        stringBuffer.append(self.NUM)
        stringBuffer.appendint(self.numberOfResults)
        stringBuffer.append(self.LAST)
        stringBuffer.appendint(self.lastPage)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker


