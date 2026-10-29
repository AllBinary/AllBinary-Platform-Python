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



class Directory:
    instance: Directory = None
    

    @staticmethod
    def getInstance() -> Directory:
        return Directory.instance
    

    def __init__(self) -> None:
        pass
    

    def create(self, directoryAbPath: AbPath) -> bool:
        return self.create(directoryAbPath.toFileSystemString())
    

    # throws Exception
    def remove(self, existingDirectoryAbPath: AbPath) -> None:
        self.remove(existingDirectoryAbPath.toFileSystemString())
    

    # Java overloaded method: Python keeps the last definition
    def create(self, directory: str) -> bool:
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
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def remove(self, existingDirectory: str) -> None:
        existingDirectoryFile: AbFile = FileFactory.getInstance().getInstance(existingDirectory)
        if existingDirectoryFile.isDirectory():
            if len(existingDirectoryFile.list_()) > 0:
                raise Exception("Did not remove category: " + existingDirectory + " because files exist")
            elif existingDirectoryFile.delete():
                PreLogUtil.put("Successfully Removed: " + existingDirectory, "Directory", "remove")
        else:
            raise Exception("Category Directory Is Missing:" + existingDirectory)
    

    def search(self, fileFilter: FileFilter, file: AbFile) -> BasicArrayList:
        return self.search(fileFilter, file, False)
    

    # Java overloaded method: Python keeps the last definition
    def search(self, fileFilter: FileFilter, file: AbFile, isRecursiveSearch: bool) -> BasicArrayList:
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
    

    # Java overloaded method: Python keeps the last definition
    def search(self, file: AbFile) -> BasicArrayList:
        return self.search(file, False)
    

    # Java overloaded method: Python keeps the last definition
    def search(self, file: AbFile, isRecursiveSearch: bool) -> BasicArrayList:
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
    

    # Java overloaded method: Python keeps the last definition
    def search(self, searchValue: str, file: AbFile) -> BasicArrayList:
        return self.search(searchValue, file, False)
    

    # Java overloaded method: Python keeps the last definition
    def search(self, searchValue: str, file: AbFile, isRecursiveSearch: bool) -> BasicArrayList:
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
    

    # Java overloaded method: Python keeps the last definition
    def search(self, level: int, file: AbFile) -> BasicArrayList:
        return self.search(level, file, False)
    

    # Java overloaded method: Python keeps the last definition
    def search(self, level: int, file: AbFile, isRecursiveSearch: bool) -> BasicArrayList:
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
# from java.io.FileFilter import FileFilter
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.FileFactory import FileFactory
from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


Directory.instance = Directory()

