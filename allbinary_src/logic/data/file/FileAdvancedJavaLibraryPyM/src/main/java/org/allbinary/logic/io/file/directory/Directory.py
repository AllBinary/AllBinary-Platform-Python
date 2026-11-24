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


class Directory:
    instance: Directory = None
    

    @staticmethod
    def getInstance() -> Directory:
        return Directory.instance
    

    def __init__(self) -> None:
        pass
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def create_j1_1(self, directoryAbPath: AbPath) -> bool:
        from org.allbinary.logic.io.path.AbPath import AbPath
        return self.create(directoryAbPath.toFileSystemString())
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def remove_j1_1(self, existingDirectoryAbPath: AbPath) -> None:
        from org.allbinary.logic.io.path.AbPath import AbPath
        self.remove(existingDirectoryAbPath.toFileSystemString())
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def create_j1_2(self, directory: str) -> bool:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.FileFactory import FileFactory
        try:
            directoryFile: AbFile = FileFactory.getInstance().getInstance(directory)
            if not directoryFile.isDirectory():
                PreLogUtil.put("Creating Directories: " + directory, self, "create")
                if not directoryFile.mkdirs():
                    return False
            return True
        except Exception as e:
            PreLogUtil.putOE("Error Creating Directories: " + directory, self, "create", e)
            return False

    def create(self, *args):
        if len(args) == 1 and True and not isinstance(args[0], (str, list, int, float)):
            return self.create_j1_1(*args)
        if len(args) == 1:
            return self.create_j1_2(*args)
        return getattr(self, "create_j" + str(len(args)))(*args)
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def remove_j1_2(self, existingDirectory: str) -> None:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.FileFactory import FileFactory
        existingDirectoryFile: AbFile = FileFactory.getInstance().getInstance(existingDirectory)
        if existingDirectoryFile.isDirectory():
            if len(existingDirectoryFile.list_()) > 0:
                raise Exception("Did not remove category: " + existingDirectory + " because files exist")
            elif existingDirectoryFile.delete():
                PreLogUtil.put("Successfully Removed: " + existingDirectory, "Directory", "remove")
        else:
            raise Exception("Category Directory Is Missing:" + existingDirectory)

    def remove(self, *args):
        if len(args) == 1 and True and not isinstance(args[0], (str, list, int, float)):
            return self.remove_j1_1(*args)
        if len(args) == 1:
            return self.remove_j1_2(*args)
        return getattr(self, "remove_j" + str(len(args)))(*args)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def search_j2_1(self, fileFilter: FileFilter, file: AbFile) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.search(fileFilter, file, False)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def search_j3_1(self, fileFilter: FileFilter, file: AbFile, isRecursiveSearch: bool) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        fileList: BasicArrayList = BasicArrayListD()
        recursiveFileList: BasicArrayList = None
        if file.isDirectory():
            fileArray: list[object] = file.listFilesFileFilter(fileFilter)
            if fileArray is None:
                return fileList
            files: list[AbFile] = FileWrapperUtil.wrapFiles(fileArray)
            if files is None:
                return fileList
            size: int = len(files)
            for index in range(0, size):
                fileList.add(files[index])
                if isRecursiveSearch:
                    recursiveFileList = self.search(fileFilter, files[index], isRecursiveSearch)
                    fileList.addAllList(recursiveFileList)
        return fileList
    

    def search_j1(self, file: AbFile) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.search(file, False)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def search_j2_2(self, file: AbFile, isRecursiveSearch: bool) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        fileList: BasicArrayList = BasicArrayListD()
        recursiveFileList: BasicArrayList = None
        if file.isDirectory():
            fileArray: list[object] = file.listFiles()
            if fileArray is None:
                return fileList
            files: list[AbFile] = FileWrapperUtil.wrapFiles(fileArray)
            if files is None:
                return fileList
            for index in range(0, len(files)):
                fileList.add(files[index])
                if isRecursiveSearch:
                    recursiveFileList = self.search(files[index], isRecursiveSearch)
                    fileList.addAllList(recursiveFileList)
        return fileList
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def search_j2_3(self, searchValue: str, file: AbFile) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.search(searchValue, file, False)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def search_j3_2(self, searchValue: str, file: AbFile, isRecursiveSearch: bool) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        fileList: BasicArrayList = BasicArrayListD()
        recursiveFileList: BasicArrayList = None
        if file.isDirectory():
            fileArray: list[object] = file.listFiles()
            if fileArray is None:
                return fileList
            files: list[AbFile] = FileWrapperUtil.wrapFiles(fileArray)
            if files is None:
                return fileList
            for index in range(0, len(files)):
                if files[index].getPath().indexOf(searchValue) >= 0:
                    fileList.add(files[index])
                if isRecursiveSearch:
                    recursiveFileList = self.search(searchValue, files[index], isRecursiveSearch)
                    fileList.addAllList(recursiveFileList)
        return fileList
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def search_j2_4(self, level: int, file: AbFile) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.search(level, file, False)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def search_j3_3(self, level: int, file: AbFile, isRecursiveSearch: bool) -> BasicArrayList:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        fileList: BasicArrayList = BasicArrayListD()
        recursiveFileList: BasicArrayList = None
        if file.isDirectory():
            fileArray: list[object] = file.listFiles()
            if fileArray is None:
                return fileList
            files: list[AbFile] = FileWrapperUtil.wrapFiles(fileArray)
            if files is None:
                return fileList
            for index in range(0, len(files)):
                fileList.add(files[index])
                if level <= 0:
                    return fileList
                recursiveFileList = self.search(level - 1, files[index], isRecursiveSearch)
                fileList.addAllList(recursiveFileList)
        return fileList

    def search(self, *args):
        if len(args) == 2 and True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)):
            return self.search_j2_1(*args)
        if len(args) == 3 and True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)) and isinstance(args[2], bool):
            return self.search_j3_1(*args)
        if len(args) == 2 and True and not isinstance(args[0], (str, list, int, float)) and isinstance(args[1], bool):
            return self.search_j2_2(*args)
        if len(args) == 2 and True and (args[0] is None or isinstance(args[0], str)) and not isinstance(args[1], (str, list, int, float)):
            return self.search_j2_3(*args)
        if len(args) == 3 and True and (args[0] is None or isinstance(args[0], str)) and not isinstance(args[1], (str, list, int, float)) and isinstance(args[2], bool):
            return self.search_j3_2(*args)
        if len(args) == 2:
            return self.search_j2_4(*args)
        if len(args) == 3:
            return self.search_j3_3(*args)
        return getattr(self, "search_j" + str(len(args)))(*args)
# from java.io.FileFilter import FileFilter
# from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.io.file.FileFactory import FileFactory
# from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


def _Directory_instance() -> object:
    return Directory()

lazy_static(Directory, "instance", _Directory_instance)

