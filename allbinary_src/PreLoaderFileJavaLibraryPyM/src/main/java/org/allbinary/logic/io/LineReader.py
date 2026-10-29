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
# package org.allbinary.logic.io

from __future__ import annotations



class LineReader:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.fileName: str = None
        self.string: str = None
        self.index: int = 0
        self.idFile: AbFileInputStream = None
        self.idData: DataInputStream = None
    

    def __init__(self, fileName: str) -> None:
        from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
        self._init_fields()
        try:
            bytes: list[int] = [0] * (100000)
            self.fileName = fileName
            self.idFile = AbFileInputStream(fileName)
            self.idFile.read(bytes)
            self.string = bytes(bytes).decode()
        except Exception as e:
            self.logUtil.put("File: " + fileName, self, "LineReader", e)
            if True:
                pass
    

    def hasNext(self) -> bool:
        try:
            nextIndex: int = self.string.find(CommonSeps.getInstance().NEW_LINE, self.index)
            if nextIndex == -1:
                return False
            return True
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "hasNext", e)
            if True:
                pass
            return False
    

    # throws Exception
    def next(self) -> str:
        try:
            nextIndex: int = self.string.find(CommonSeps.getInstance().NEW_LINE, self.index)
            if nextIndex == -1:
                raise Exception("next() should have been called first")
            temp: str = self.string[self.index:nextIndex]
            self.index = nextIndex + 1
            return temp
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "next", e)
            if True:
                pass
            raise e
# from java.io.DataInputStream import DataInputStream
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings


