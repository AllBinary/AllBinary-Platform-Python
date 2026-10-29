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

from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.io.file.AbFileInterface import AbFileInterface


class AbFile(AbFileInterface):
    NULL_FILE: AbFile = None

    def _init_fields(self) -> None:
        self.file: File = None
    

    # throws Exception
    @staticmethod
    def createAbFileWithChild(file: AbFile, childPathName: str) -> AbFile:
        return AbFile(File(file.getFile(), childPathName))
    

    # throws Exception
    @staticmethod
    def createAbFile(filePath: str) -> AbFile:
        return AbFile(File(AbPath(filePath, StringUtil.getInstance().EMPTY_STRING).toFileSystemString()))
    

    # throws Exception
    @staticmethod
    def createAbFilePathAndName(filePath: str, fileName: str) -> AbFile:
        return AbFile(File(AbPath(filePath, StringUtil.getInstance().EMPTY_STRING).toFileSystemString(), fileName))
    

    @staticmethod
    def createAbFileFromAbPath(abPath: AbPath) -> AbFile:
        return AbFile(File(abPath.toFileSystemString()))
    

    @staticmethod
    def createAbFileFromRawPath(filePath: str) -> AbFile:
        return AbFile(File(filePath))
    

    def __init__(self, file: File) -> None:
        self._init_fields()
        self.file = file
    

    def getFile(self) -> File:
        return self.file
    

    def getName(self) -> str:
        return self.file.getName()
    

    def getParent(self) -> str:
        return self.file.getParent()
    

    def getParentFile(self) -> File:
        return self.file.getParentFile()
    

    def getPath(self) -> str:
        return self.file.getPath()
    

    def isAbsolute(self) -> bool:
        return self.file.isAbsolute()
    

    def getAbsolutePath(self) -> str:
        return self.file.getAbsolutePath()
    

    def getAbsoluteFile(self) -> File:
        return self.file.getAbsoluteFile()
    

    # throws IOException
    def getCanonicalPath(self) -> str:
        return self.file.getCanonicalPath()
    

    # throws IOException
    def getCanonicalFile(self) -> File:
        return self.file.getCanonicalFile()
    

    def toURI(self) -> URI:
        return self.file.toURI()
    

    def canRead(self) -> bool:
        return self.file.canRead()
    

    def canWrite(self) -> bool:
        return self.file.canWrite()
    

    def exists(self) -> bool:
        return self.file.exists()
    

    def isDirectory(self) -> bool:
        return self.file.isDirectory()
    

    def isFile(self) -> bool:
        return self.file.isFile()
    

    def isHidden(self) -> bool:
        return self.file.isHidden()
    

    def lastModified(self) -> int:
        return self.file.lastModified()
    

    def length(self) -> int:
        return self.file.length()
    

    # throws IOException
    def createNewFile(self) -> bool:
        return self.file.createNewFile()
    

    # throws IOException
    def delete(self) -> bool:
        return self.file.delete()
    

    def deleteOnExit(self) -> None:
        self.file.deleteOnExit()
    

    def list_(self) -> list[str]:
        return self.file.list_()
    

    def listWithFilter(self, filter: FilenameFilter) -> list[str]:
        return self.file.list_(filter)
    

    def listFiles(self) -> list[object]:
        return self.file.listFiles()
    

    def listFilesFileNameFilter(self, filter: FilenameFilter) -> list[object]:
        return self.file.listFiles(filter)
    

    def listFilesFileFilter(self, filter: FileFilter) -> list[object]:
        return self.file.listFiles(filter)
    

    def mkdir(self) -> bool:
        return self.file.mkdir()
    

    def mkdirs(self) -> bool:
        return self.file.mkdirs()
    

    def renameTo(self, dest: AbFile) -> bool:
        return self.file.renameTo(dest.getFile())
    

    def setLastModified(self, time: int) -> bool:
        return self.file.setLastModified(time)
    

    def setReadOnly(self) -> bool:
        return self.file.setReadOnly()
    

    def compareTo(self, pathname: File) -> int:
        return self.file.compareTo(pathname)
    

    def equals(self, obj: object) -> bool:
        return TsUtil.getInstance().equalsNotstring(self.file, obj)

    def __eq__(self, other: object) -> bool:
        return self.equals(other)
    

    def hashCode(self) -> int:
        return self.file.hashCode()

    def __hash__(self) -> int:
        return self.hashCode()
    

    def toString(self) -> str:
        return str(self.file)

    def __str__(self) -> str:
        return self.toString()
# from java.io.File import File
# from java.io.FileFilter import FileFilter
# from java.io.FilenameFilter import FilenameFilter
# from java.io.IOException import IOException
# from java.net.URI import URI
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.io.path.AbPath import AbPath


AbFile.NULL_FILE = AbFile.createAbFileFromRawPath(StringUtil.getInstance().EMPTY_STRING)

