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

from java.lang.JavaRuntimeStatic import lazy_static


class SubDirectory:
    instance: SubDirectory = None

    def _init_fields(self) -> None:
        self.directory: Directory = Directory.getInstance()
    

    @staticmethod
    def getInstance() -> SubDirectory:
        return SubDirectory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def search_j2_1(self, fileFilter: FileFilter, file: AbFile) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.directory.search(fileFilter, file, True)
    

    def search_j1(self, file: AbFile) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.directory.search(file, True)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def search_j2_2(self, searchValue: str, file: AbFile) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.directory.search(searchValue, file, True)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def search_j2_3(self, level: int, file: AbFile) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.directory.search(level, file, True)

    def search(self, *args):
        if len(args) == 2 and True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)):
            return self.search_j2_1(*args)
        if len(args) == 2 and True and (args[0] is None or isinstance(args[0], str)) and not isinstance(args[1], (str, list, int, float)):
            return self.search_j2_2(*args)
        if len(args) == 2:
            return self.search_j2_3(*args)
        return getattr(self, "search_j" + str(len(args)))(*args)
    

    @staticmethod
    def toString(files: BasicArrayList) -> str:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.allbinary.util.BasicArrayList import BasicArrayList
        stringBuffer: StringMaker = StringMaker()
        NEW_LINE: str = CommonSeps.getInstance().NEW_LINE
        size: int = files.size()
        for index in range(0, size):
            file: AbFile = files.get(index)
            stringBuffer.append(file.getPath())
            stringBuffer.append(NEW_LINE)
        return str(stringBuffer)
# from java.io.FileFilter import FileFilter
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.logic.io.file.directory.Directory import Directory


def _SubDirectory_instance() -> object:
    return SubDirectory()

lazy_static(SubDirectory, "instance", _SubDirectory_instance)

