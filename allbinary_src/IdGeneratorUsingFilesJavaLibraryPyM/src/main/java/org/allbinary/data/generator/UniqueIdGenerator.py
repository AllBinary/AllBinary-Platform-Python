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
# package org.allbinary.data.generator

from __future__ import annotations

import threading
from org.allbinary.data.generator.IdGeneratorInterface import IdGeneratorInterface


class UniqueIdGenerator(IdGeneratorInterface):
    EXT: str = ".unq"
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.newFile: AbFile = None
        self.id: int = 0
    

    def __init__(self) -> None:
        self._init_fields()
    

    def initialize(self, value: int) -> None:
        try:
            self.newFile.createNewFile()
            idData: AbDataOutputStream = DataOutputStreamFactory.getInstance().getInstanceForAbFile(self.newFile)
            idData.writeLong(value)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().IDLOGGING):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, "initialize", e)
    

    # throws Exception
    def setFile(self, filePathName: str, name: str) -> None:
        with self._lock:
            return self._setFile_unlocked(filePathName, name)

    def _setFile_unlocked(self, filePathName: str, name: str) -> None:
        self.newFile = AbFile.createAbFile(filePathName)
    

    # throws IOException
    def getNext(self) -> str:
        with self._lock:
            return self._getNext_unlocked()

    def _getNext_unlocked(self) -> str:
        idData: AbDataInputStream = None
        idOutData: AbDataOutputStream = None
        try:
            idFile: AbFileInputStream = AbFileInputStream(self.newFile)
            idData = AbDataInputStream(idFile)
            self.id = idData.readLong()
            idOutFile: AbFileOutputStream = AbFileOutputStream.createFromAbFile(self.newFile)
            idOutData = AbDataOutputStream(idOutFile)
            idOutData.writeLong(self.id + 1)
            idLong: int = int(self.id)
            return str(idLong)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().IDLOGGING):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, "getNext", e)
            return "Error"
        finally:
            StreamUtil.getInstance().close(idData)
            StreamUtil.getInstance().close(idOutData)
# from java.io.IOException import IOException
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.AbDataInputStream import AbDataInputStream
from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
from org.allbinary.logic.io.AbFileOutputStream import AbFileOutputStream
from org.allbinary.logic.io.DataOutputStreamFactory import DataOutputStreamFactory
from org.allbinary.logic.io.StreamUtil import StreamUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.string.CommonStrings import CommonStrings


