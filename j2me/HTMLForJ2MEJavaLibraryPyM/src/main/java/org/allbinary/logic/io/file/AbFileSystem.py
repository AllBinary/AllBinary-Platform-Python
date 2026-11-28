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

from java.lang.JavaRuntimeStatic import lazy_static


#HTMLForJ2ME
class AbFileSystem:
    instance: AbFileSystem = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    @staticmethod
    def getInstance() -> AbFileSystem:
        return AbFileSystem.instance
    

    def isDirectoryOrFile(self, path: str) -> bool:
        return False
    

    def isDirectory(self, path: str) -> bool:
        return False
    

    def getFilesAsStringArrayForPath(self, currentDirPath: str) -> list[str]:
        from org.allbinary.logic.string.StringUtil import StringUtil
        return StringUtil.getInstance().getArrayInstance()
    

    def readAsString_j1(self, fileName: str) -> str:
        bytes: list[int] = [0] * (1000000)
        return self.readAsString(fileName, bytes)
    

    def readAsString_j2(self, fileName: str, bytes: list[int]) -> str:
        from org.allbinary.logic.string.StringUtil import StringUtil
        return StringUtil.getInstance().EMPTY_STRING

    def readAsString(self, *args):
        implementation = __class__.__dict__.get("readAsString_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().readAsString(*args)
    

    def close(self, closeable: object) -> bool:
        from java.io.InputStream import InputStream
        try:
            if closeable is not None:
                inputStream: InputStream = (closeable)
                inputStream.close()
            return True
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CLOSE, e)
            return False
# from java.io.InputStream import InputStream
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonStrings import CommonStrings


def _AbFileSystem_instance() -> object:
    return AbFileSystem()

lazy_static(AbFileSystem, "instance", _AbFileSystem_instance)

