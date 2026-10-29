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
# package org.allbinary.business.user.commerce.money.payment.gateway

from __future__ import annotations

from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface


# Java interface
class PaymentGatewayInterface(TableMappingInterface):
    

    def getEnable(self) -> str:
        raise NotImplementedError()
    

    def getStoreName(self) -> str:
        raise NotImplementedError()
    

    def getName(self) -> str:
        raise NotImplementedError()
    

    def getPaymentMethod(self) -> str:
        raise NotImplementedError()
    

    def getMode(self) -> str:
        raise NotImplementedError()
    

    def getTestProtocol(self) -> str:
        raise NotImplementedError()
    

    def getTestServer(self) -> str:
        raise NotImplementedError()
    

    def getTestPort(self) -> str:
        raise NotImplementedError()
    

    def getTestPath(self) -> str:
        raise NotImplementedError()
    

    def getServerProtocol(self) -> str:
        raise NotImplementedError()
    

    def getServer(self) -> str:
        raise NotImplementedError()
    

    def getServerPort(self) -> str:
        raise NotImplementedError()
    

    def getServerPath(self) -> str:
        raise NotImplementedError()
    

    def getUserName(self) -> str:
        raise NotImplementedError()
    

    def getPassword(self) -> str:
        raise NotImplementedError()
    

    def getProxyProtocol(self) -> str:
        raise NotImplementedError()
    

    def getProxyServer(self) -> str:
        raise NotImplementedError()
    

    def getProxyPath(self) -> str:
        raise NotImplementedError()
    

    def getProxyPort(self) -> str:
        raise NotImplementedError()
    

    def getProxyUserName(self) -> str:
        raise NotImplementedError()
    

    def getProxyPassword(self) -> str:
        raise NotImplementedError()
    

    def getTimeout(self) -> str:
        raise NotImplementedError()
    

    def getProxyTimeout(self) -> str:
        raise NotImplementedError()
    

    def getSpecial1(self) -> str:
        raise NotImplementedError()
    

    def getSpecial2(self) -> str:
        raise NotImplementedError()
    

    def getSpecial3(self) -> str:
        raise NotImplementedError()
    

    def getSpecial4(self) -> str:
        raise NotImplementedError()
    

    def getSpecial5(self) -> str:
        raise NotImplementedError()
    

    def getSpecial6(self) -> str:
        raise NotImplementedError()
    

    def getSpecial7(self) -> str:
        raise NotImplementedError()
    

    def getSpecial8(self) -> str:
        raise NotImplementedError()
    

    def getSpecial9(self) -> str:
        raise NotImplementedError()
    

    def getLastModified(self) -> str:
        raise NotImplementedError()
    

    def getTimeEntered(self) -> str:
        raise NotImplementedError()
    

    def setEnable(self, value: str) -> None:
        raise NotImplementedError()
    

    def setStoreName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setPaymentMethod(self, value: str) -> None:
        raise NotImplementedError()
    

    def setMode(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTestProtocol(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTestServer(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTestPort(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTestPath(self, value: str) -> None:
        raise NotImplementedError()
    

    def setServerProtocol(self, value: str) -> None:
        raise NotImplementedError()
    

    def setServer(self, value: str) -> None:
        raise NotImplementedError()
    

    def setServerPort(self, value: str) -> None:
        raise NotImplementedError()
    

    def setServerPath(self, value: str) -> None:
        raise NotImplementedError()
    

    def setUserName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setPassword(self, value: str) -> None:
        raise NotImplementedError()
    

    def setProxyProtocol(self, value: str) -> None:
        raise NotImplementedError()
    

    def setProxyServer(self, value: str) -> None:
        raise NotImplementedError()
    

    def setProxyPath(self, value: str) -> None:
        raise NotImplementedError()
    

    def setProxyPort(self, value: str) -> None:
        raise NotImplementedError()
    

    def setProxyUserName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setProxyPassword(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTimeout(self, value: str) -> None:
        raise NotImplementedError()
    

    def setProxyTimeout(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSpecial1(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSpecial2(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSpecial3(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSpecial4(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSpecial5(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSpecial6(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSpecial7(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSpecial8(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSpecial9(self, value: str) -> None:
        raise NotImplementedError()
    

    def setLastModified(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTimeEntered(self, value: str) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def toHashMap(self, isEncrypted: bool) -> dict:
        raise NotImplementedError()
    

    def toVector(self, isEncrypted: bool) -> BasicArrayList:
        raise NotImplementedError()
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


