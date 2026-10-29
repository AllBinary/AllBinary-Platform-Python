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



class CloudStreamUtil:
    instance: CloudStreamUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CloudStreamUtil:
        return CloudStreamUtil.instance
    

    # throws Exception
    def getFile(self, file: AbFile) -> InputStream:
        from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
        inputStream: InputStream = AbFileInputStream(file)
        available: int = inputStream.available()
        if available > 0:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Cloud File Bytes: " + str(available), self, "processRequest()")
        return inputStream
    

    # throws Exception
    def getFileAnyWhere(self, file: AbFile) -> InputStream:
        from org.allbinary.logic.io.AbFileLocalInputStream import AbFileLocalInputStream
        from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
        inputStream: InputStream = AbFileLocalInputStream(file)
        available: int = inputStream.available()
        if available > 0:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Local File Bytes: " + str(available), self, "processRequest()")
        else:
            inputStream = AbFileInputStream(file)
            available = inputStream.available()
            if available > 0:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                    self.logUtil.putF("Cloud File Bytes: " + str(available), self, "processRequest()")
        return inputStream
    

    # throws Exception
    def getFileLocal(self, file: AbFile) -> InputStream:
        from org.allbinary.logic.io.AbFileLocalInputStream import AbFileLocalInputStream
        inputStream: InputStream = AbFileLocalInputStream(file)
        available: int = inputStream.available()
        if available > 0:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Local File Bytes: " + str(available), self, "processRequest()")
        return inputStream
# from java.io.InputStream import InputStream
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.file.AbFile import AbFile


CloudStreamUtil.instance = CloudStreamUtil()

