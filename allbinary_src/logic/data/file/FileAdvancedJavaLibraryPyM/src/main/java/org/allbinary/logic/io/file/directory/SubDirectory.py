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
# package org.allbinary.logic.io.file.directory

from __future__ import annotations



class SubDirectory:
    instance: SubDirectory = None

    def _init_fields(self) -> None:
        self.directory: Directory = Directory.getInstance()
    

    @staticmethod
    def getInstance() -> SubDirectory:
        return SubDirectory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def search(self, fileFilter: FileFilter, file: AbFile) -> BasicArrayList:
        return self.directory.search(fileFilter, file, True)
    

    # Java overloaded method: Python keeps the last definition
    def search(self, file: AbFile) -> BasicArrayList:
        return self.directory.search(file, True)
    

    # Java overloaded method: Python keeps the last definition
    def search(self, searchValue: str, file: AbFile) -> BasicArrayList:
        return self.directory.search(searchValue, file, True)
    

    # Java overloaded method: Python keeps the last definition
    def search(self, level: int, file: AbFile) -> BasicArrayList:
        return self.directory.search(level, file, True)
    

    @staticmethod
    def toString(files: BasicArrayList) -> str:
        stringBuffer: StringMaker = StringMaker()
        NEW_LINE: str = CommonSeps.getInstance().NEW_LINE
        size: int = files.size()
        for index in range(0, size):
            file: AbFile = files.get(index)
            stringBuffer.append(file.getPath())
            stringBuffer.append(NEW_LINE)
        return str(stringBuffer)
# from java.io.FileFilter import FileFilter
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.logic.io.file.directory.Directory import Directory


SubDirectory.instance = SubDirectory()

