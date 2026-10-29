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



class SmallInsert:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.fileName: str = None
        self.string: str = None
    

    def __init__(self, fileName: str) -> None:
        self._init_fields()
        self.fileName = fileName
        self.string = AbFileSystem.getInstance().readAsString(fileName)
    

    def atBeginning(self, text: str) -> bool:
        try:
            idFile: FileOutputStream = FileOutputStream(self.fileName)
            idOutData: DataOutputStream = DataOutputStream(idFile)
            idOutData.writeBytes(text + self.string)
            return True
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().IDLOGGING):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "insertAtBeginning", e)
            return False
    

    def after(self, text: str, after: str) -> bool:
        try:
            index: int = self.string.find(after)
            if index < 0:
                print("No such start: " + after + " in: " + self.string)
                return False
            index = index + len(after)
            start: str = self.string[0:index]
            end: str = self.string[index + 1:len(self.string)]
            idFile: FileOutputStream = FileOutputStream(self.fileName)
            idOutData: DataOutputStream = DataOutputStream(idFile)
            idOutData.writeBytes(start + text + end)
            idOutData.close()
            idFile.close()
            return True
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().IDLOGGING):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "after", e)
            return False
    

    def atEnd(self, text: str) -> bool:
        try:
            idFile: FileOutputStream = FileOutputStream(self.fileName)
            idOutData: DataOutputStream = DataOutputStream(idFile)
            idOutData.writeBytes(self.string + text)
            return True
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().IDLOGGING):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "insertAtEnd", e)
            return False
# from java.io.DataOutputStream import DataOutputStream
# from java.io.FileOutputStream import FileOutputStream
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.file.AbFileSystem import AbFileSystem
from org.allbinary.string.CommonStrings import CommonStrings


