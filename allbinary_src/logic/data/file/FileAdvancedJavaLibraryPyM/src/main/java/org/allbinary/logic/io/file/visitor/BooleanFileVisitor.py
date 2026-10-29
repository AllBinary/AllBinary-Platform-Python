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
# package org.allbinary.logic.io.file.visitor

from __future__ import annotations

from org.allbinary.logic.util.visitor.VisitorInterface import VisitorInterface


class BooleanFileVisitor(VisitorInterface):

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.filterStringBasicArrayList: BasicArrayList = None
    

    def __init__(self, filterStringBasicArrayList: BasicArrayList) -> None:
        self._init_fields()
        self.setFilterStringBasicArrayList(filterStringBasicArrayList)
        PreLogUtil.put("Filter BasicArrayList: " + str(self.getFilterStringBasicArrayList()), self, self.commonStrings.CONSTRUCTOR)
    

    def visit(self, anyType: object) -> object:
        return self.visit(anyType)
    

    # Java overloaded method: Python keeps the last definition
    def visit(self, file: AbFile) -> bool:
        list_: BasicArrayList = self.getFilterStringBasicArrayList()
        size: int = list_.size()
        nextFileFilterString: str = None
        for index in range(0, size):
            nextFileFilterString = list_.get(index)
            if self.visit(file, nextFileFilterString):
                return True
        return False
    

    def getFilterStringBasicArrayList(self) -> BasicArrayList:
        return self.filterStringBasicArrayList
    

    def setFilterStringBasicArrayList(self, filterStringBasicArrayList: BasicArrayList) -> None:
        self.filterStringBasicArrayList = filterStringBasicArrayList
    

    # Java overloaded method: Python keeps the last definition
    def visit(self, file: AbFile, fileNameString: str) -> bool:
        return False
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList


