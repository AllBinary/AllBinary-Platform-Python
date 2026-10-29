# 
# AllBinary Open License Version 1 
# Copyright (c) 2026 AllBinary 
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



#AndroidToJ2ME
class AbFileSystem:
    instance: AbFileSystem = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> AbFileSystem:
        return AbFileSystem.instance
    

    def isDirectoryOrFile(self, path: str) -> bool:
        file: File = File(path)
        return file.isDirectory() or file.isFile()
    

    def isDirectory(self, path: str) -> bool:
        return File(path).isDirectory()
    

    def getFilesAsStringArrayForPath(self, currentDirPath: str) -> list[str]:
        file: File = File(currentDirPath)
        if file.exists():
            return file.list_()
        else:
            return StringUtil.getInstance().getArrayInstance()
    

    def readAsString(self, fileName: str) -> str:
        bytes: list[int] = [0] * (1000000)
        return self.readAsString(fileName, bytes)
    

    # Java overloaded method: Python keeps the last definition
    def readAsString(self, fileName: str, bytes: list[int]) -> str:
        closeable: object = NullUtil.getInstance().NULL_OBJECT
        try:
            idFile: InputStream = FileInputStream(fileName)
            closeable = idFile
            size: int = idFile.read(bytes)
            if size > 0:
                return bytes(bytes, 0, size).decode()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "readAsString", e)
        finally:
            self.close(closeable)
        return StringUtil.getInstance().EMPTY_STRING
    

    def close(self, closeable: object) -> bool:
        try:
            if closeable is not None:
                inputStream: InputStream = (closeable)
                inputStream.close()
            return True
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CLOSE, e)
            return False
# from java.io.File import File
# from java.io.FileInputStream import FileInputStream
# from java.io.InputStream import InputStream
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


AbFileSystem.instance = AbFileSystem()

