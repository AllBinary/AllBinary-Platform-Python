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
# package org.allbinary.business.context.modules.storefront

from __future__ import annotations

from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface


# Java interface
class StoreFrontInterface(TableMappingInterface):
    

    def isNameValid(self) -> bool:
        raise NotImplementedError()
    

    def isValid(self) -> bool:
        raise NotImplementedError()
    

    def nameValidationInfo(self) -> str:
        raise NotImplementedError()
    

    def validationInfo(self) -> str:
        raise NotImplementedError()
    

    def getTestHtmlPath(self) -> str:
        raise NotImplementedError()
    

    def getCurrentHostName(self) -> str:
        raise NotImplementedError()
    

    def getCurrentHostNamePath(self) -> str:
        raise NotImplementedError()
    

    def getCurrentHomeHostName(self) -> str:
        raise NotImplementedError()
    

    def getCurrentHomeHostNamePath(self) -> str:
        raise NotImplementedError()
    

    def getName(self) -> str:
        raise NotImplementedError()
    

    def getBasketName(self) -> str:
        raise NotImplementedError()
    

    def getHomeHostName(self) -> str:
        raise NotImplementedError()
    

    def getHomeHostNamePath(self) -> str:
        raise NotImplementedError()
    

    def getHostName(self) -> str:
        raise NotImplementedError()
    

    def getHostNamePath(self) -> str:
        raise NotImplementedError()
    

    def getTestHomeHostName(self) -> str:
        raise NotImplementedError()
    

    def getTestHomeHostNamePath(self) -> str:
        raise NotImplementedError()
    

    def getTestHostName(self) -> str:
        raise NotImplementedError()
    

    def getTestHostNamePath(self) -> str:
        raise NotImplementedError()
    

    def getStaticPath(self) -> str:
        raise NotImplementedError()
    

    def getCategoryPath(self) -> str:
        raise NotImplementedError()
    

    # throws Exception
    def getSubStores(self) -> BasicArrayList:
        raise NotImplementedError()
    

    def getTagLocation(self) -> str:
        raise NotImplementedError()
    

    def getPackageLocation(self) -> str:
        raise NotImplementedError()
    

    def getInventoryControl(self) -> str:
        raise NotImplementedError()
    

    def getContextConfigurationInterface(self) -> ContextConfigurationInterface:
        raise NotImplementedError()
    

    def setContextConfigurationInterface(self, contextConfigurationInterface: ContextConfigurationInterface) -> None:
        raise NotImplementedError()
    

    def getFtp(self) -> str:
        raise NotImplementedError()
    

    def getFtpPath(self) -> str:
        raise NotImplementedError()
    

    def getFtpUserName(self) -> str:
        raise NotImplementedError()
    

    def getFtpPassword(self) -> str:
        raise NotImplementedError()
    

    def getTestFtp(self) -> str:
        raise NotImplementedError()
    

    def getTestFtpPath(self) -> str:
        raise NotImplementedError()
    

    def getTestFtpUserName(self) -> str:
        raise NotImplementedError()
    

    def getTestFtpPassword(self) -> str:
        raise NotImplementedError()
    

    def getTimeCreated(self) -> str:
        raise NotImplementedError()
    

    def getLastModified(self) -> str:
        raise NotImplementedError()
    

    def setName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setBasketName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setHomeHostName(self, value: str) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def setHomeHostNamePath(self, value: str) -> None:
        raise NotImplementedError()
    

    def setHostName(self, value: str) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def setHostNamePath(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTestHomeHostName(self, value: str) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def setTestHomeHostNamePath(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTestHostName(self, value: str) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def setTestHostNamePath(self, value: str) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def setImagePath(self, value: str) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def setStaticPath(self, value: str) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def setCategoryPath(self, value: str) -> None:
        raise NotImplementedError()
    

    def setPackageLocation(self, value: str) -> None:
        raise NotImplementedError()
    

    def setInventoryControl(self, value: str) -> None:
        raise NotImplementedError()
    

    def setFtp(self, value: str) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def setFtpPath(self, value: str) -> None:
        raise NotImplementedError()
    

    def setFtpUserName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setFtpPassword(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTestFtp(self, value: str) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def setTestFtpPath(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTestFtpUserName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTestFtpPassword(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTimeCreated(self, value: str) -> None:
        raise NotImplementedError()
    

    def setLastModified(self, value: str) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def install(self, current: int, total: int) -> None:
        raise NotImplementedError()
from org.allbinary.business.context.configuration.ContextConfigurationInterface import ContextConfigurationInterface
from org.allbinary.util.BasicArrayList import BasicArrayList


