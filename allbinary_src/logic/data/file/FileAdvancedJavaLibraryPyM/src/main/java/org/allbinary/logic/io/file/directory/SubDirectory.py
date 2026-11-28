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
        __class__._init_fields(self)
    

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
        if len(args) == 2 and True and (args[0] is None or any(base.__name__ == "FileFilter" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "AbFile" for base in type(args[1]).__mro__)):
            return __class__.__dict__["search_j2_1"].__get__(self, __class__)(*args)
        if len(args) == 2 and True and (args[0] is None or isinstance(args[0], str)) and (args[1] is None or any(base.__name__ == "AbFile" for base in type(args[1]).__mro__)):
            return __class__.__dict__["search_j2_2"].__get__(self, __class__)(*args)
        if len(args) == 2:
            return __class__.__dict__["search_j2_3"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("search_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().search(*args)
    

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

