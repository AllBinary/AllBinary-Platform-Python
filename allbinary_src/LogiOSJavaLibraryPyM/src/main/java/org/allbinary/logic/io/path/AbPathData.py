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



class AbPathData:
    instance: AbPathData = None

    def _init_fields(self) -> None:
        self.EXTENSION_SEP: str = CommonSeps.getInstance().PERIOD
        self.SEPARATORCHAR: str = '/'
        self.SEPARATOR: str = CommonSeps.getInstance().FORWARD_SLASH
    

    @staticmethod
    def getInstance() -> AbPathData:
        return AbPathData.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getExtensionIndex(self, filePath: str) -> int:
        indexOfFileExtensionDelmiter: int = filePath.rfind(self.EXTENSION_SEP)
        indexOfLatDelimiter: int = filePath.rfind(self.SEPARATORCHAR)
        if indexOfFileExtensionDelmiter < 0:
            return -1
        if indexOfFileExtensionDelmiter < indexOfLatDelimiter:
            return -1
        return indexOfFileExtensionDelmiter
    

    def getExtensionWithDot(self, filePath: str) -> str:
        indexOfFileExtensionDelmiter: int = self.getExtensionIndex(filePath)
        extension: str = StringUtil.getInstance().EMPTY_STRING
        if indexOfFileExtensionDelmiter >= 0:
            extension = filePath[indexOfFileExtensionDelmiter:]
        return extension
    

    def getExtension(self, filePath: str) -> str:
        indexOfFileExtensionDelmiter: int = self.getExtensionIndex(filePath)
        extension: str = StringUtil.getInstance().EMPTY_STRING
        if indexOfFileExtensionDelmiter >= 0:
            extension = filePath[indexOfFileExtensionDelmiter + 1:]
        return extension
    

    def getNameFromPath(self, path: str) -> str:
        endIndex: int = path.rfind(self.SEPARATORCHAR)
        if endIndex < 0:
            endIndex = path.rfind(FilePathData.getInstance().SEPARATORCHAR)
        if endIndex < 0:
            return path
        if len(path) == endIndex + 1:
            categoryName: str = path[0:endIndex]
            return self.getNameFromPath(categoryName)
        else:
            categoryName: str = path[endIndex + 1:]
            return categoryName
    

    def removeNameFromPath(self, path: str) -> str:
        endIndex: int = path.rfind(self.SEPARATORCHAR)
        if endIndex < 0:
            endIndex = path.rfind(FilePathData.getInstance().SEPARATORCHAR)
        if endIndex < 0:
            return StringUtil.getInstance().EMPTY_STRING
        if len(path) == endIndex + 1:
            return self.removeNameFromPath(path[0:endIndex - 1])
        else:
            pathWithoutName: str = path[0:endIndex]
            return pathWithoutName
from org.allbinary.logic.io.file.FilePathData import FilePathData
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonSeps import CommonSeps


AbPathData.instance = AbPathData()

