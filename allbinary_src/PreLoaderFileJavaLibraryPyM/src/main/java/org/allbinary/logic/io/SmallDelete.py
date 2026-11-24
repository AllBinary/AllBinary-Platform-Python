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



class SmallDelete:

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.fileName: str = None
        self.string: str = None
    

    def __init__(self, fileName: str) -> None:
        from org.allbinary.logic.io.file.AbFileSystem import AbFileSystem
        self._init_fields()
        self.fileName = fileName
        self.string = AbFileSystem.getInstance().readAsString(fileName)
    

    def deleteAtStart(self, start: str, end: str) -> bool:
        from java.io.DataOutputStream import DataOutputStream
        from java.io.FileOutputStream import FileOutputStream
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            beginIndex: int = 0
            endIndex: int = 0
            beginIndex = self.string.find(start)
            endIndex = self.string.find(end)
            if endIndex > beginIndex and beginIndex >= 0 and endIndex >= 0 and beginIndex < 10 and endIndex < 525:
                text: str = self.string[endIndex:len(self.string)]
                idFile: FileOutputStream = FileOutputStream(self.fileName)
                idOutData: DataOutputStream = DataOutputStream(idFile)
                idOutData.writeBytes(text)
                return True
            return False
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().IDLOGGING):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "deleteAtStart", e)
            return False
    

    def deleteBetween(self, start: str, end: str, newText: str) -> bool:
        from java.io.DataOutputStream import DataOutputStream
        from java.io.FileOutputStream import FileOutputStream
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            beginIndex: int = 0
            endIndex: int = 0
            beginIndex = self.string.find(start)
            endIndex = self.string.find(end)
            if endIndex > beginIndex and beginIndex >= 0 and endIndex >= 0 and beginIndex < 50 and endIndex < 425:
                newStart: str = self.string[0:beginIndex]
                text: str = self.string[endIndex + len(end):len(self.string)]
                idFile: FileOutputStream = FileOutputStream(self.fileName)
                idOutData: DataOutputStream = DataOutputStream(idFile)
                idOutData.writeBytes(newStart + newText + text)
                return True
            return False
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().IDLOGGING):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "deleteAtStart", e)
            return False
# from java.io.DataOutputStream import DataOutputStream
# from java.io.FileOutputStream import FileOutputStream
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.file.AbFileSystem import AbFileSystem
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


