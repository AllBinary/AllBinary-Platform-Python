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
# package org.allbinary.logic.io.file.path

from __future__ import annotations

import threading
from java.lang.JavaRuntimeStatic import lazy_static


#Used to correct user input for paths
class AbPathUtilOld:
    instance: AbPathUtilOld = None
    MIN: int = 4
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.io.file.FilePathData import FilePathData
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abPathData: AbPathData = AbPathData.getInstance()
        self.filePathData: FilePathData = FilePathData.getInstance()
    

    @staticmethod
    def getInstance() -> AbPathUtilOld:
        return AbPathUtilOld.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getExtension_j1_1(self, abFilePath: AbFilePath) -> str:
        from org.allbinary.logic.io.path.AbFilePath import AbFilePath
        return self.getExtension(str(abFilePath))
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getExtension_j1_2(self, abPath: AbPath) -> str:
        from org.allbinary.logic.io.path.AbPath import AbPath
        return self.getExtension(str(abPath))
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getExtension_j1_3(self, filePath: str) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if len(filePath) < AbPathUtilOld.MIN:
            raise Exception("Could not be a file path since its less that 4 characters")
        beginIndex: int = len(filePath) - AbPathUtilOld.MIN
        extension: str = filePath[beginIndex + 1:]
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("FileExtension: " + extension, self, "getExtension()")
        return extension

    def getExtension(self, *args):
        if len(args) == 1 and True and not isinstance(args[0], (str, list, int, float)):
            return self.getExtension_j1_1(*args)
        if len(args) == 1 and True and not isinstance(args[0], (str, list, int, float)):
            return self.getExtension_j1_2(*args)
        if len(args) == 1:
            return self.getExtension_j1_3(*args)
        return getattr(self, "getExtension_j" + str(len(args)))(*args)
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getWithoutExtension_j1_1(self, abFilePath: AbFilePath) -> str:
        from org.allbinary.logic.io.path.AbFilePath import AbFilePath
        return self.getWithoutExtension(str(abFilePath))
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getWithoutExtension_j1_2(self, abPath: AbPath) -> str:
        from org.allbinary.logic.io.path.AbPath import AbPath
        return self.getWithoutExtension(str(abPath))
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getWithoutExtension_j1_3(self, filePath: str) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if len(filePath) < AbPathUtilOld.MIN:
            raise Exception("Could not be a file path since its less that 4 characters")
        endIndex: int = len(filePath) - AbPathUtilOld.MIN
        pathWithoutExtension: str = filePath[0:endIndex]
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("FileWithoutExtension: " + pathWithoutExtension, self, "getWithoutExtension()")
        return pathWithoutExtension

    def getWithoutExtension(self, *args):
        if len(args) == 1 and True and not isinstance(args[0], (str, list, int, float)):
            return self.getWithoutExtension_j1_1(*args)
        if len(args) == 1 and True and not isinstance(args[0], (str, list, int, float)):
            return self.getWithoutExtension_j1_2(*args)
        if len(args) == 1:
            return self.getWithoutExtension_j1_3(*args)
        return getattr(self, "getWithoutExtension_j" + str(len(args)))(*args)
    

    def isValid(self, path: str) -> bool:
        if self.isValidStart(path):
            if self.isValidEnd(path):
                return True
        return False
    

    def isValidStart(self, path: str) -> bool:
        if path[0] == self.abPathData.SEPARATORCHAR:
            return True
        else:
            return False
    

    def isValidEnd(self, path: str) -> bool:
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        if StringValidationUtil.getInstance().isEmpty(path):
            return False
        if path[len(path) - 1] == self.abPathData.SEPARATORCHAR:
            return True
        else:
            return False
    

    def adjustStart(self, path: str) -> str:
        if not self.isValidStart(path):
            path = str(self.abPathData.SEPARATOR) + path
        return path
    

    def adjustEnd(self, path: str) -> str:
        if not self.isValidEnd(path):
            path = path + str(self.abPathData.SEPARATOR)
        return path
    

    def adjust(self, path: str) -> str:
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        if StringValidationUtil.getInstance().isEmpty(path):
            return self.abPathData.SEPARATOR
        if path.find("\\") >= 0:
            path = path.replace('\\', self.abPathData.SEPARATORCHAR)
        return path
    

    def getNameFromPath(self, categoryPath: str) -> str:
        with self._lock:
            return self._getNameFromPath_unlocked(categoryPath)

    def _getNameFromPath_unlocked(self, categoryPath: str) -> str:
        endIndex: int = categoryPath.rfind(self.abPathData.SEPARATOR)
        if endIndex < 0:
            endIndex = categoryPath.rfind(self.filePathData.SEPARATORCHAR)
        if endIndex < 0:
            return categoryPath
        if len(categoryPath) == endIndex + 1:
            categoryName: str = categoryPath[0:endIndex]
            return self.getNameFromPath(categoryName)
        else:
            categoryName: str = categoryPath[endIndex + 1:]
            return categoryName
    

    # throws Exception
    def removeNameFromPath(self, categoryPath: str) -> AbPath:
        with self._lock:
            return self._removeNameFromPath_unlocked(categoryPath)

    def _removeNameFromPath_unlocked(self, categoryPath: str) -> AbPath:
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        endIndex: int = categoryPath.rfind(self.abPathData.SEPARATOR)
        if endIndex < 0:
            endIndex = categoryPath.rfind(self.filePathData.SEPARATORCHAR)
        if endIndex < 0:
            return AbPath.createAbPath()
        if len(categoryPath) == endIndex + 1:
            return self.removeNameFromPath(categoryPath[0:endIndex - 1])
        else:
            categoryName: str = categoryPath[0:endIndex]
            return AbPath(categoryName, StringUtil.getInstance().EMPTY_STRING)
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.file.FilePathData import FilePathData
# from org.allbinary.logic.io.path.AbFilePath import AbFilePath
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.io.path.AbPathData import AbPathData
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _AbPathUtilOld_instance() -> object:
    return AbPathUtilOld()

lazy_static(AbPathUtilOld, "instance", _AbPathUtilOld_instance)

