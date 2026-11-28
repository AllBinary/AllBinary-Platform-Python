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
# package org.allbinary.logic.io.file

from __future__ import annotations

from java.lang.System import System
import traceback
from java.lang.JavaRuntimeStatic import lazy_static


class FileListFetcher:
    instance: FileListFetcher = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.io.file.directory.SubDirectory import SubDirectory
        self.subDirectory: SubDirectory = SubDirectory.getInstance()

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    @staticmethod
    def getInstance() -> FileListFetcher:
        return FileListFetcher.instance
    

    def getFiles_j1(self, path: str) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.util.BasicArrayList import BasicArrayList
        try:
            files: BasicArrayList = self.subDirectory.search(AbFile.createAbFile(path))
            return files
        except Exception as e:
            traceback.print_exception(e)
            print("Error: " + str(e) + "\nMsg: " + str(e))
        return None
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getFiles_j2_1(self, path: str, includeExtensions: list[str]) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.directory.DirectoryOrIncludeFileExtensionBooleanFileVisitor import DirectoryOrIncludeFileExtensionBooleanFileVisitor
        from org.allbinary.logic.io.file.filter.VisitorFileFilter import VisitorFileFilter
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        try:
            includeExtensionBasicArrayList: BasicArrayList = BasicArrayListD()
            size: int = len(includeExtensions)
            for index in range(0, size):
                includeExtensionBasicArrayList.add(includeExtensions[index])
            visitorFileFilter: VisitorFileFilter = VisitorFileFilter(DirectoryOrIncludeFileExtensionBooleanFileVisitor(includeExtensionBasicArrayList))
            files: BasicArrayList = self.subDirectory.search(visitorFileFilter, AbFile.createAbFile(path))
            return files
        except Exception as e:
            traceback.print_exception(e)
            print("Error: " + str(e) + "\nMsg: " + str(e))
        return None
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getFiles_j2_2(self, path: str, includeExtension: str) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.directory.DirectoryOrIncludeFileExtensionBooleanFileVisitor import DirectoryOrIncludeFileExtensionBooleanFileVisitor
        from org.allbinary.logic.io.file.filter.VisitorFileFilter import VisitorFileFilter
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        try:
            includeExtensionBasicArrayList: BasicArrayList = BasicArrayListD()
            includeExtensionBasicArrayList.add(includeExtension)
            visitorFileFilter: VisitorFileFilter = VisitorFileFilter(DirectoryOrIncludeFileExtensionBooleanFileVisitor(includeExtensionBasicArrayList))
            files: BasicArrayList = self.subDirectory.search(visitorFileFilter, AbFile.createAbFile(path))
            return files
        except Exception as e:
            traceback.print_exception(e)
            print("Error: " + str(e) + "\nMsg: " + str(e))
        return None
    

    def getFiles_j3(self, path: str, pathIncludes: str, includeExtension: str) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.directory.DirectoryOrIncludeFileExtensionBooleanFileVisitor import DirectoryOrIncludeFileExtensionBooleanFileVisitor
        from org.allbinary.logic.io.file.filter.VisitorFileFilter import VisitorFileFilter
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        try:
            includeExtensionBasicArrayList: BasicArrayList = BasicArrayListD()
            includeExtensionBasicArrayList.add(includeExtension)
            visitorFileFilter: VisitorFileFilter = VisitorFileFilter(DirectoryOrIncludeFileExtensionBooleanFileVisitor(includeExtensionBasicArrayList, pathIncludes))
            files: BasicArrayList = self.subDirectory.search(visitorFileFilter, AbFile.createAbFile(path))
            return files
        except Exception as e:
            traceback.print_exception(e)
            print("Error: " + str(e) + "\nMsg: " + str(e))
        return None

    def getFiles(self, *args):
        if len(args) == 2 and True and (args[0] is None or isinstance(args[0], str)) and (args[1] is None or isinstance(args[1], list)):
            return __class__.__dict__["getFiles_j2_1"].__get__(self, __class__)(*args)
        if len(args) == 2:
            return __class__.__dict__["getFiles_j2_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("getFiles_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getFiles(*args)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getTrackedFiles_j2_1(self, path: str, includeExtensions: list[str]) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.directory.DirectoryOrIncludeFileExtensionAndTrackedBooleanFileVisitor import DirectoryOrIncludeFileExtensionAndTrackedBooleanFileVisitor
        from org.allbinary.logic.io.file.filter.VisitorFileFilter import VisitorFileFilter
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        try:
            includeExtensionBasicArrayList: BasicArrayList = BasicArrayListD()
            size: int = len(includeExtensions)
            for index in range(0, size):
                includeExtensionBasicArrayList.add(includeExtensions[index])
            visitorFileFilter: VisitorFileFilter = VisitorFileFilter(DirectoryOrIncludeFileExtensionAndTrackedBooleanFileVisitor(includeExtensionBasicArrayList))
            files: BasicArrayList = self.subDirectory.search(visitorFileFilter, AbFile.createAbFile(path))
            return files
        except Exception as e:
            traceback.print_exception(e)
            print("Error: " + str(e) + "\nMsg: " + str(e))
        return None
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getTrackedFiles_j2_2(self, path: str, includeExtension: str) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.directory.DirectoryOrIncludeFileExtensionAndTrackedBooleanFileVisitor import DirectoryOrIncludeFileExtensionAndTrackedBooleanFileVisitor
        from org.allbinary.logic.io.file.filter.VisitorFileFilter import VisitorFileFilter
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        try:
            includeExtensionBasicArrayList: BasicArrayList = BasicArrayListD()
            includeExtensionBasicArrayList.add(includeExtension)
            visitorFileFilter: VisitorFileFilter = VisitorFileFilter(DirectoryOrIncludeFileExtensionAndTrackedBooleanFileVisitor(includeExtensionBasicArrayList))
            files: BasicArrayList = self.subDirectory.search(visitorFileFilter, AbFile.createAbFile(path))
            return files
        except Exception as e:
            traceback.print_exception(e)
            print("Error: " + str(e) + "\nMsg: " + str(e))
        return None

    def getTrackedFiles(self, *args):
        if len(args) == 2 and True and (args[0] is None or isinstance(args[0], str)) and (args[1] is None or isinstance(args[1], list)):
            return __class__.__dict__["getTrackedFiles_j2_1"].__get__(self, __class__)(*args)
        if len(args) == 2:
            return __class__.__dict__["getTrackedFiles_j2_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("getTrackedFiles_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getTrackedFiles(*args)
    

    def getDirectories(self, path: str) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.directory.DirectoryBooleanFileVisitor import DirectoryBooleanFileVisitor
        from org.allbinary.logic.io.file.filter.VisitorFileFilter import VisitorFileFilter
        from org.allbinary.util.BasicArrayList import BasicArrayList
        try:
            visitorFileFilter: VisitorFileFilter = VisitorFileFilter(DirectoryBooleanFileVisitor())
            files: BasicArrayList = self.subDirectory.search(visitorFileFilter, AbFile.createAbFile(path))
            return files
        except Exception as e:
            traceback.print_exception(e)
            print("Error: " + str(e) + "\nMsg: " + str(e))
        return None
# from org.allbinary.logic.io.file.directory.DirectoryBooleanFileVisitor import DirectoryBooleanFileVisitor
# from org.allbinary.logic.io.file.directory.DirectoryOrIncludeFileExtensionAndTrackedBooleanFileVisitor import DirectoryOrIncludeFileExtensionAndTrackedBooleanFileVisitor
# from org.allbinary.logic.io.file.directory.DirectoryOrIncludeFileExtensionBooleanFileVisitor import DirectoryOrIncludeFileExtensionBooleanFileVisitor
# from org.allbinary.logic.io.file.directory.SubDirectory import SubDirectory
# from org.allbinary.logic.io.file.filter.VisitorFileFilter import VisitorFileFilter
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


def _FileListFetcher_instance() -> object:
    return FileListFetcher()

lazy_static(FileListFetcher, "instance", _FileListFetcher_instance)

