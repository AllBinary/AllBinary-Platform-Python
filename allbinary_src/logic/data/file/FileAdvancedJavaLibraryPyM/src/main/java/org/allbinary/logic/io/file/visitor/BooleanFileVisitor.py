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
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.util.BasicArrayList import BasicArrayList
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.filterStringBasicArrayList: BasicArrayList = None
    

    def __init__(self, filterStringBasicArrayList: BasicArrayList) -> None:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.util.BasicArrayList import BasicArrayList
        self._init_fields()
        self.setFilterStringBasicArrayList(filterStringBasicArrayList)
        PreLogUtil.put("Filter BasicArrayList: " + str(self.getFilterStringBasicArrayList()), self, self.commonStrings.CONSTRUCTOR)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def visit_j1_1(self, anyType: object) -> object:
        from org.allbinary.logic.io.file.AbFile import AbFile
        return self.visit(anyType)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def visit_j1_2(self, file: AbFile) -> bool:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.util.BasicArrayList import BasicArrayList
        list_: BasicArrayList = self.getFilterStringBasicArrayList()
        size: int = list_.size()
        nextFileFilterString: str = None
        for index in range(0, size):
            nextFileFilterString = list_.get(index)
            if self.visit(file, nextFileFilterString):
                return True
        return False
    

    def getFilterStringBasicArrayList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.filterStringBasicArrayList
    

    def setFilterStringBasicArrayList(self, filterStringBasicArrayList: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        self.filterStringBasicArrayList = filterStringBasicArrayList
    

    def visit_j2(self, file: AbFile, fileNameString: str) -> bool:
        from org.allbinary.logic.io.file.AbFile import AbFile
        return False

    def visit(self, *args):
        if len(args) == 1 and True:
            return self.visit_j1_1(*args)
        if len(args) == 1:
            return self.visit_j1_2(*args)
        return getattr(self, "visit_j" + str(len(args)))(*args)
# from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList


