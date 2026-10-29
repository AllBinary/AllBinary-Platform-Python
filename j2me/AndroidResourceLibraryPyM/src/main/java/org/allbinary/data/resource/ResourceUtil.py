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



#Android
class ResourceUtil:
    instance: ResourceUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.context: object = NullUtil.getInstance().NULL_OBJECT
        self.resources: object = NullUtil.getInstance().NULL_OBJECT
        self.hashMap: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
    

    @staticmethod
    def getInstance() -> ResourceUtil:
        return ResourceUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def setLoadingPaths(self, path: str, ext: str) -> None:
        self.logUtil.putF(CommonStrings.getInstance().NOT_IMPLEMENTED, self, "setLoadingPaths")
    

    def getContext(self) -> Context:
        return self.context
    

    def setContextFromActivity(self, activity: Activity) -> None:
        self.context = activity
    

    def setContext(self, aContext: Context) -> None:
        self.context = aContext
    

    def getResourceId(self, resource: str) -> int:
        value: int = self.hashMap.get(resource)
        if DebugFactory.getInstance() != NoDebug.getInstance():
            PreLogUtil.put(str(StringMaker().append(resource).append(CommonSeps.getInstance().COLON).append(str(value))), self, "getResourceId")
        return value
    

    def addResource(self, resource: str, value: int) -> None:
        if DebugFactory.getInstance() != NoDebug.getInstance():
            PreLogUtil.put(str(StringMaker().append(resource).append(CommonSeps.getInstance().COLON).append(str(value))), self, "addResource")
            if self.containsDuplicate(resource, value):
                ForcedLogUtil.log(str(StringMaker().append("Found Duplicate Resource: ").append(resource)), self)
        self.hashMap.put(resource, value)
    

    def containsDuplicate(self, resource: str, value: int) -> bool:
        objectArray: list[object] = HashtableUtil.getInstance().getKeysAsArray(self.hashMap)
        index = len(objectArray)
        while (index := index - 1) >= 0:
            integer: int = self.hashMap.get(objectArray[index])
            if resource != objectArray[index]:
                if value != integer:
                    if int(value) == int(integer):
                        return True
        return False
    

    def setResources(self, resources: Resources) -> None:
        self.logUtil.putF(str(StringMaker().append("Resource Loader: ").append(type(resources).__module__ + "." + type(resources).__qualname__)), self, "setResources")
        self.resources = resources
    

    # throws Exception
    def getResourceAsStream(self, resource: str) -> InputStream:
        integer: int = self.hashMap.get(resource)
        id: int = int(integer)
        resources: Resources = (self.resources)
        inputStream: InputStream = resources.openRawResource(id)
        if inputStream is not None:
            return inputStream
        return inputStream
# from java.io.InputStream import InputStream
from android.app.Activity import Activity
from android.content.Context import Context
from android.content.res.Resources import Resources
from org.allbinary.debug.DebugFactory import DebugFactory
from org.allbinary.debug.NoDebug import NoDebug
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.HashtableUtil import HashtableUtil


ResourceUtil.instance = ResourceUtil()

