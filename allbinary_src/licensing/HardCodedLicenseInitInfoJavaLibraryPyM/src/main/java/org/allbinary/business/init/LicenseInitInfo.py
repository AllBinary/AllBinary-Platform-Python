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
# package org.allbinary.business.init

from __future__ import annotations



class LicenseInitInfo:

    def _init_fields(self) -> None:
        self.id: str = StringUtil.getInstance().EMPTY_STRING
        self.serverList: BasicArrayList = BasicArrayListD()
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getLicenseId(self) -> str:
        return self.id
    

    def getServer(self, index: int) -> str:
        return self.serverList.get(index)
    

    def getNumberOfServers(self) -> int:
        return self.serverList.size()
    

    def setLicenseId(self, value: str) -> None:
        self.id = value
    

    def clearServers(self) -> None:
        self.serverList.clear()
    

    def setServer(self, value: str, index: int) -> None:
        self.serverList.addAt(index, value)
    

    def addServer(self, value: str) -> None:
        self.serverList.add(value)
    

    def getServerList(self) -> BasicArrayList:
        return self.serverList
    

    def setServerList(self, servers: BasicArrayList) -> None:
        if DebugFactory.getInstance() == NoDebug.getInstance():
            self.serverList = servers
from org.allbinary.debug.DebugFactory import DebugFactory
from org.allbinary.debug.NoDebug import NoDebug
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


