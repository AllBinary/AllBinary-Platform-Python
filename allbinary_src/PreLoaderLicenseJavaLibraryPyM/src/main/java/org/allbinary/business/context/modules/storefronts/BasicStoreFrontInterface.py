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
# package org.allbinary.business.context.modules.storefronts

from __future__ import annotations



# Java interface
class BasicStoreFrontInterface:
    

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
    

    def getUserName(self) -> str:
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
from org.allbinary.util.BasicArrayList import BasicArrayList


