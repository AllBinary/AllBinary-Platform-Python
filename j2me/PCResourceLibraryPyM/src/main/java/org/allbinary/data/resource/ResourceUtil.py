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
# package org.allbinary.data.resource

from __future__ import annotations



#J2SE - PC
class ResourceUtil:
    instance: ResourceUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.path: str = StringUtil.getInstance().EMPTY_STRING
        self.ext: str = StringUtil.getInstance().EMPTY_STRING
    

    @staticmethod
    def getInstance() -> ResourceUtil:
        return ResourceUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def setLoadingPaths(self, path: str, ext: str) -> None:
        self.path = path
        self.ext = ext
    

    def setClassLoader(self, classLoader: ClassLoader) -> None:
        pass
    

    # throws Exception
    def getResourceAsStream(self, resource: str) -> InputStream:
        inputStream: InputStream = self.getResourceAsStreamAtStart(resource, 2)
        if inputStream is None:
            inputStream = self.getResourceAsStreamAtStart(resource, 1)
            if inputStream is None:
                raise Exception(str(StringMaker().append("Unable to obtain: ").append(resource)))
        return inputStream
    

    # throws Exception
    def getResourceAsStreamAtStart(self, resource: str, startIndex: int) -> InputStream:
        inputStream: InputStream = FileInputStream(str(StringMaker().append(self.path).append(resource).append(self.ext)))
        if inputStream is not None:
            byteArray: list[int] = [0] * (inputStream.available())
            StreamUtil.getInstance().getByteArray(inputStream, ByteArrayOutputStream(), byteArray)
            return ByteArrayInputStream(byteArray)
        return inputStream
    

    def addResource(self, resource: str, value: int) -> None:
        pass
# from java.io.ByteArrayInputStream import ByteArrayInputStream
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.FileInputStream import FileInputStream
# from java.io.InputStream import InputStream
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.StreamUtil import StreamUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil


ResourceUtil.instance = ResourceUtil()

