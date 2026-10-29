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

import traceback


class FileListFetcher:
    instance: FileListFetcher = None

    def _init_fields(self) -> None:
        self.subDirectory: SubDirectory = SubDirectory.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> FileListFetcher:
        return FileListFetcher.instance
    

    def getFiles(self, path: str) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        try:
            files: BasicArrayList = self.subDirectory.search(AbFile.createAbFile(path))
            return files
        except Exception as e:
            traceback.print_exception(e)
            print("Error: " + str(e) + "\nMsg: " + str(e))
        return None
    

    # Java overloaded method: Python keeps the last definition
    def getFiles(self, path: str, includeExtensions: list[str]) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
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
    

    # Java overloaded method: Python keeps the last definition
    def getFiles(self, path: str, includeExtension: str) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
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
    

    # Java overloaded method: Python keeps the last definition
    def getFiles(self, path: str, pathIncludes: str, includeExtension: str) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
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
    

    def getTrackedFiles(self, path: str, includeExtensions: list[str]) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
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
    

    # Java overloaded method: Python keeps the last definition
    def getTrackedFiles(self, path: str, includeExtension: str) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
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
    

    def getDirectories(self, path: str) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        try:
            visitorFileFilter: VisitorFileFilter = VisitorFileFilter(DirectoryBooleanFileVisitor())
            files: BasicArrayList = self.subDirectory.search(visitorFileFilter, AbFile.createAbFile(path))
            return files
        except Exception as e:
            traceback.print_exception(e)
            print("Error: " + str(e) + "\nMsg: " + str(e))
        return None
from org.allbinary.logic.io.file.directory.DirectoryBooleanFileVisitor import DirectoryBooleanFileVisitor
from org.allbinary.logic.io.file.directory.DirectoryOrIncludeFileExtensionAndTrackedBooleanFileVisitor import DirectoryOrIncludeFileExtensionAndTrackedBooleanFileVisitor
from org.allbinary.logic.io.file.directory.DirectoryOrIncludeFileExtensionBooleanFileVisitor import DirectoryOrIncludeFileExtensionBooleanFileVisitor
from org.allbinary.logic.io.file.directory.SubDirectory import SubDirectory
from org.allbinary.logic.io.file.filter.VisitorFileFilter import VisitorFileFilter
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


FileListFetcher.instance = FileListFetcher()

