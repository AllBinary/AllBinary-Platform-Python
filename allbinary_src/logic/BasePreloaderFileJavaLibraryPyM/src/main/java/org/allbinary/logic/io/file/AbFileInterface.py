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



# Java interface
class AbFileInterface:
    

    def canRead(self) -> bool:
        raise NotImplementedError()
    

    def canWrite(self) -> bool:
        raise NotImplementedError()
    

    # throws IOException
    def createNewFile(self) -> bool:
        raise NotImplementedError()
    

    # throws IOException
    def delete(self) -> bool:
        raise NotImplementedError()
    

    def deleteOnExit(self) -> None:
        raise NotImplementedError()
    

    def exists(self) -> bool:
        raise NotImplementedError()
    

    def getAbsolutePath(self) -> str:
        raise NotImplementedError()
    

    # throws IOException
    def getCanonicalPath(self) -> str:
        raise NotImplementedError()
    

    def getParent(self) -> str:
        raise NotImplementedError()
    

    def getPath(self) -> str:
        raise NotImplementedError()
    

    def isAbsolute(self) -> bool:
        raise NotImplementedError()
    

    def isDirectory(self) -> bool:
        raise NotImplementedError()
    

    def isFile(self) -> bool:
        raise NotImplementedError()
    

    def isHidden(self) -> bool:
        raise NotImplementedError()
    

    def lastModified(self) -> int:
        raise NotImplementedError()
    

    def length(self) -> int:
        raise NotImplementedError()
    

    def list_(self) -> list[str]:
        raise NotImplementedError()
    

    def listWithFilter(self, filter: FilenameFilter) -> list[str]:
        raise NotImplementedError()
    

    def mkdir(self) -> bool:
        raise NotImplementedError()
    

    def mkdirs(self) -> bool:
        raise NotImplementedError()
    

    def setLastModified(self, time: int) -> bool:
        raise NotImplementedError()
    

    def setReadOnly(self) -> bool:
        raise NotImplementedError()
    

    def toString(self) -> str:
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.toString()
    

    def toURI(self) -> URI:
        raise NotImplementedError()
# from java.io.FilenameFilter import FilenameFilter
# from java.io.IOException import IOException
# from java.net.URI import URI


