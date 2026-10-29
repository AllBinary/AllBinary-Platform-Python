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

import threading
from org.allbinary.logic.NullUtil import NullUtil


#J2SE - J2ME
class ResourceUtil:
    classLoader: object = NullUtil.getInstance().NULL_OBJECT
    instance: ResourceUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> ResourceUtil:
        return ResourceUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def setLoadingPaths(self, path: str, ext: str) -> None:
        self.logUtil.putF(CommonStrings.getInstance().NOT_IMPLEMENTED, self, "setLoadingPaths")
    

    def setClassLoader(self, classLoader: ClassLoader) -> None:
        self.logUtil.putF(str(StringMaker().append("Resource Loader: ").append(type(classLoader).__module__ + "." + type(classLoader).__qualname__)), self, "setClassLoader")
        ResourceUtil.classLoader = classLoader
    

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
        commonSeps: CommonSeps = CommonSeps.getInstance()
        index: int = resource.find(commonSeps.COLON)
        resourcePath: str = resource[index + startIndex:]
        inputStream: InputStream = type(resource).getResourceAsStream(resourcePath)
        if inputStream is not None:
            return inputStream
        classLoader: ClassLoader = ResourceUtil.classLoader
        inputStream = classLoader.getResourceAsStream(resourcePath)
        if inputStream is not None:
            return inputStream
        inputStream = threading.current_thread().getContextClassLoader().getResourceAsStream(resourcePath)
        if inputStream is not None:
            return inputStream
        return inputStream
    

    def addResource(self, resource: str, value: int) -> None:
        pass
# from java.io.InputStream import InputStream
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings


ResourceUtil.instance = ResourceUtil()

