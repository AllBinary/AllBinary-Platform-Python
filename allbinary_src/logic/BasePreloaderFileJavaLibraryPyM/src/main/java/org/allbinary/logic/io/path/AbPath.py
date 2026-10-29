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



class AbPath:
    NETWORK_SEP: str = ":/"

    def _init_fields(self) -> None:
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.abPathData: AbPathData = AbPathData.getInstance()
        self.abPathUtil: PathUtil = PathUtil.getInstance()
        self.EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
        self.schema: str = self.EMPTY_STRING
        self.path: str = self.EMPTY_STRING
        self.nameP: str = self.EMPTY_STRING
        self.hasSchemaP: bool = False
        self.numberOfSeps: int = 0
    

    @staticmethod
    def createAbPath() -> AbPath:
        try:
            EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
            return AbPath(EMPTY_STRING, EMPTY_STRING)
        except Exception as ex:
            raise RuntimeError()
    

    def __init__(self, aPath: str, name: str) -> None:
        self._init_fields()
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if not stringValidationUtil.isEmpty(aPath):
            self.schema = self.getSchema(aPath)
            self.nameP = name
            self.path = self.abPathUtil.adjustEnd(self.abPathUtil.adjust(self.getPathFromPath(aPath)))
        else:
            self.init()
            if not stringValidationUtil.isEmpty(name):
                self.nameP = name
    

    def init(self) -> None:
        self.schema = self.EMPTY_STRING
        self.setPath(self.abPathData.SEPARATOR)
        self.nameP = self.EMPTY_STRING
    

    def getSchema(self, aPath: str) -> str:
        beginIndex: int = aPath.find(self.commonSeps.COLON)
        if beginIndex >= 0:
            self.hasSchemaP = True
            return aPath[0:beginIndex]
        self.hasSchemaP = False
        return self.EMPTY_STRING
    

    def hasSchema(self) -> bool:
        return self.hasSchemaP
    

    # throws Exception
    def getPathFromPath(self, aPath: str) -> str:
        filePathData: FilePathData = FilePathData.getInstance()
        tempPath: str = aPath
        if not self.hasSchema():
            tempPath = self.abPathUtil.adjustStart(tempPath)
        else:
            beginIndex: int = tempPath.find(self.commonSeps.COLON)
            if beginIndex >= 0:
                beginIndex += 1
                while tempPath[beginIndex] == self.abPathData.SEPARATORCHAR or tempPath[beginIndex] == filePathData.SEPARATORCHAR:
                    beginIndex += 1
                    self.numberOfSeps += 1
                    if self.numberOfSeps > 2:
                        raise Exception("Should Not Have More Than Two Seps")
                tempPath = tempPath[beginIndex:len(tempPath)]
        return tempPath
    

    def setName(self, name: str) -> None:
        self.nameP = name
    

    def getName(self) -> str:
        return self.nameP
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        if self.hasSchema():
            stringBuffer.append(self.schema)
            stringBuffer.append(AbPath.NETWORK_SEP)
        stringBuffer.append(self.getPath())
        stringBuffer.append(self.nameP)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def toFileSystemString(self) -> str:
        if self.hasSchema():
            filePathData: FilePathData = FilePathData.getInstance()
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.schema)
            stringBuffer.append(self.commonSeps.COLON)
            stringBuffer.append(filePathData.PATH_START)
            stringBuffer.append(FilePathUtil.adjust(self.getPath()))
            stringBuffer.append(self.nameP)
            return str(stringBuffer)
        else:
            return str(FilePathUtil.adjust(self.getPath())) + self.nameP
    

    def getPath(self) -> str:
        return self.path
    

    def setPath(self, path: str) -> None:
        self.path = path
from org.allbinary.logic.io.file.FilePathData import FilePathData
from org.allbinary.logic.io.file.FilePathUtil import FilePathUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.io.path.PathUtil import PathUtil


