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
# package org.allbinary.logic.communication.xmlrpc

from __future__ import annotations



class XmlRpcAbeClient:
    isOnline: bool = True

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.remoteMethod: str = None
        self.clientInfo: AbeClientInformationInterface = None
        self.client: XmlRpcHandler = NullXmlRpcHandler.NULL_XML_RPC_HANDLER
        self.server: int = None
        self.start: int = 0
        self.maxServers: int = 0
        self.isDone: bool = None
        self.START_SERVER: str = "Start With Server #"
        self.TRYING: str = "Trying Server #"
        self.SEP: str = CommonLabels.getInstance().COLON_SEP
        self.CLIENT_INFO: str = "Client Info: \n"
        self.RESULT: str = CommonLabels.getInstance().RESULT_ + CommonSeps.getInstance().NEW_LINE
        self.INVALID: str = "License data is Invalid Trying Other Servers"
        self.EXCEPTION_IN_CLIENT: str = "Exception in client"
        self.SERVER_REPORTED_ERROR: str = "Server reported error"
        self.UNKNOWN_ERROR: str = "Unknown License Retrieval Failure"
        self.TRYING_OTHER_SERVERS: str = "IOException Trying Other Servers"
        self.HOST_NOT_RESOLVED_MSG: str = "Not Trying Again Since Host Unresolved"
        self.HOST_NOT_RESOLVED: str = "Host is unresolved"
        self.myRandomFactory: MyRandomFactory = MyRandomFactory.getInstance()
    

    def __init__(self, clientInfo: AbeClientInformationInterface, remoteMethod: str) -> None:
        self._init_fields()
        self.remoteMethod = remoteMethod
        self.clientInfo = clientInfo
        if clientInfo.getNumberOfLicenseServers() > 1:
            self.maxServers = clientInfo.getNumberOfLicenseServers() - 2
            self.start = self.myRandomFactory.getAbsoluteNextInt(self.maxServers) + 1
        elif clientInfo.getNumberOfLicenseServers() == 1:
            self.maxServers = 0
            self.start = 0
        self.isDone = False
        self.server = self.start
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.START_SERVER)
        stringBuffer.appendint(self.getServer())
        stringBuffer.append(self.SEP)
        stringBuffer.append(clientInfo.getLicenseServer(self.getServer()))
        self.logUtil.putF(str(stringBuffer), self, self.commonStrings.CONSTRUCTOR)
    

    # throws Exception
    def get(self, anyType: object) -> object:
        ForcedLogUtil.log(self.commonStrings.NOT_IMPLEMENTED, self)
        return NullUtil.getInstance().NULL_OBJECT
    

    # throws Exception
    def tryAnother(self, anyType: object) -> object:
        if self.getServer() < self.getMaxServers():
            self.setServer(self.getServer() + 1)
        else:
            self.setServer(0)
        if self.getServer() != self.getStart() and not self.isIsDone():
            return self.get(anyType)
        else:
            self.setIsDone(True)
        raise Exception("Tried All Servers But Still Failed")
    

    def getClientInfo(self) -> AbeClientInformationInterface:
        return self.clientInfo
    

    def getClient(self) -> XmlRpcHandler:
        return self.client
    

    def setClient(self, client: XmlRpcClient) -> None:
        self.client = client
    

    def getServer(self) -> int:
        return self.server
    

    def setServer(self, server: int) -> None:
        self.server = server
    

    def getStart(self) -> int:
        return self.start
    

    def setStart(self, start: int) -> None:
        self.start = start
    

    def getMaxServers(self) -> int:
        return self.maxServers
    

    def setMaxServers(self, maxServers: int) -> None:
        self.maxServers = maxServers
    

    def isIsDone(self) -> bool:
        return self.isDone
    

    def setIsDone(self, isDone: bool) -> None:
        self.isDone = isDone
    

    def getRemoteMethod(self) -> str:
        return self.remoteMethod
from org.allbinary.game.rand.MyRandomFactory import MyRandomFactory
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.apache.xmlrpc.NullXmlRpcHandler import NullXmlRpcHandler
from org.apache.xmlrpc.XmlRpcClient import XmlRpcClient
from org.apache.xmlrpc.XmlRpcHandler import XmlRpcHandler


