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
# package org.allbinary.logic.io.path

from __future__ import annotations



#Used to correct user input for paths
class PathUtil:
    instance: PathUtil = None

    def _init_fields(self) -> None:
        self.abPathData: AbPathData = AbPathData.getInstance()
        self.filePathData: FilePathData = FilePathData.getInstance()
    

    @staticmethod
    def getInstance() -> PathUtil:
        return PathUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getExtensionWithAbFilePath(self, abFilePath: AbFilePath) -> str:
        return self.abPathData.getExtension(str(abFilePath))
    

    def getExtensionWithAbPath(self, abPath: AbPath) -> str:
        return self.abPathData.getExtension(str(abPath))
    

    # throws Exception
    def getWithoutExtensionWithAbFilePath(self, abFilePath: AbFilePath) -> str:
        return self.getWithoutExtension(str(abFilePath))
    

    # throws Exception
    def getWithoutExtensionWithAbPath(self, abPath: AbPath) -> str:
        return self.getWithoutExtension(str(abPath))
    

    # throws Exception
    def getWithoutExtension(self, filePath: str) -> str:
        indexOfFileExtensionDelmiter: int = self.abPathData.getExtensionIndex(filePath)
        pathWithoutExtension: str = filePath
        if indexOfFileExtensionDelmiter >= 0:
            pathWithoutExtension = filePath[0:indexOfFileExtensionDelmiter]
        return pathWithoutExtension
    

    def isValid(self, path: str) -> bool:
        if self.isValidStart(path):
            if self.isValidEnd(path):
                return True
        return False
    

    def isValidStart(self, path: str) -> bool:
        if path[0] == self.abPathData.SEPARATORCHAR or path[0] == '.':
            return True
        else:
            return False
    

    def isValidEnd(self, path: str) -> bool:
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if stringValidationUtil.isEmpty(path):
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
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if stringValidationUtil.isEmpty(path):
            return self.abPathData.SEPARATOR
        if path.find("\\") >= 0:
            path = path.replace('\\', self.abPathData.SEPARATORCHAR)
        return path
    

    # throws Exception
    def removeNameFromPath(self, path: str) -> AbPath:
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.io.path.AbPath import AbPath
        endIndex: int = path.rfind(self.abPathData.SEPARATOR)
        if endIndex < 0:
            endIndex = path.rfind(self.filePathData.SEPARATORCHAR)
        if endIndex < 0:
            return AbPath.createAbPath()
        if len(path) == endIndex + 1:
            return self.removeNameFromPath(path[0:endIndex - 1])
        else:
            pathWithoutName: str = path[0:endIndex]
            return AbPath(pathWithoutName, StringUtil.getInstance().EMPTY_STRING)
from org.allbinary.logic.io.file.FilePathData import FilePathData
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.io.path.AbPathData import AbPathData


PathUtil.instance = PathUtil()

