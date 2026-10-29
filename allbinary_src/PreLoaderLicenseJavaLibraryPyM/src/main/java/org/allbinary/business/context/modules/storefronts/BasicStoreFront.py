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

from org.allbinary.business.context.modules.storefronts.BasicStoreFrontInterface import BasicStoreFrontInterface


class BasicStoreFront(BasicStoreFrontInterface):

    def _init_fields(self) -> None:
        self.name: str = None
        self.userName: str = None
        self.basketName: str = None
        self.homeHostName: str = None
        self.homeHostNamePath: str = None
        self.hostName: str = None
        self.hostNamePath: str = None
        self.testHomeHostName: str = None
        self.testHomeHostNamePath: str = None
        self.testHostName: str = None
        self.testHostNamePath: str = None
        self.imagePath: str = None
        self.staticPath: str = None
        self.categoryPath: str = None
        self.inventoryControl: str = None
        self.subStores: str = None
        self.tagLocation: str = None
        self.packageLocation: str = None
        self.ftp: str = None
        self.ftpPath: str = None
        self.ftpUserName: str = None
        self.ftpPassword: str = None
        self.testFtp: str = None
        self.testFtpPath: str = None
        self.testFtpUserName: str = None
        self.testFtpPassword: str = None
        self.timeCreated: str = None
        self.lastModified: str = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
    

    def _constructor1(self, storeHashMap: dict) -> None:
        self._init_fields()
        storeFrontData: StoreFrontData = StoreFrontData.getInstance()
        self.name = storeHashMap.get(storeFrontData.NAME)
        self.userName = storeHashMap.get(UserData.USERNAME)
        self.basketName = storeHashMap.get(storeFrontData.NAME)
        self.homeHostName = storeHashMap.get(storeFrontData.HOMEHOSTNAME)
        self.homeHostNamePath = storeHashMap.get(storeFrontData.HOMEHOSTNAMEPATH)
        self.hostName = storeHashMap.get(storeFrontData.HOSTNAME)
        self.hostNamePath = storeHashMap.get(storeFrontData.HOSTNAMEPATH)
        self.testHomeHostName = storeHashMap.get(storeFrontData.TESTHOMEHOSTNAME)
        self.testHomeHostNamePath = storeHashMap.get(storeFrontData.TESTHOMEHOSTNAMEPATH)
        self.testHostName = storeHashMap.get(storeFrontData.TESTHOSTNAME)
        self.testHostNamePath = storeHashMap.get(storeFrontData.TESTHOSTNAMEPATH)
        self.imagePath = storeHashMap.get(storeFrontData.IMAGEPATH)
        self.staticPath = storeHashMap.get(storeFrontData.STATICPATH)
        self.categoryPath = storeHashMap.get(storeFrontData.CATEGORYPATH)
        self.inventoryControl = storeHashMap.get(storeFrontData.INVENTORYCONTROL)
        self.subStores = storeHashMap.get(storeFrontData.SUBSTORES)
        self.tagLocation = storeHashMap.get(storeFrontData.TAGLOCATION)
        self.packageLocation = storeHashMap.get(storeFrontData.PACKAGELOCATION)
        self.ftp = storeHashMap.get(storeFrontData.FTP)
        self.ftpPath = storeHashMap.get(storeFrontData.FTPPATH)
        self.ftpUserName = storeHashMap.get(storeFrontData.FTPUSERNAME)
        self.ftpPassword = storeHashMap.get(storeFrontData.FTPPASSWORD)
        self.testFtp = storeHashMap.get(storeFrontData.TESTFTP)
        self.testFtpPath = storeHashMap.get(storeFrontData.TESTFTPPATH)
        self.testFtpUserName = storeHashMap.get(storeFrontData.TESTFTPUSERNAME)
        self.testFtpPassword = storeHashMap.get(storeFrontData.TESTFTPPASSWORD)
        self.timeCreated = storeHashMap.get(EntryData.getInstance().TIMECREATED)
        self.lastModified = storeHashMap.get(EntryData.getInstance().LASTMODIFIED)
    

    def getTestHtmlPath(self) -> str:
        return org.allbinary.globals.URLGLOBALS.getTestHtmlPath() + self.getCurrentHostNamePath()
    

    def getCurrentHostName(self) -> str:
        location: str = None
        if org.allbinary.globals.URLGLOBALS.isTestingMode():
            location = self.getTestHostName()
        else:
            location = self.getHostName()
        return location
    

    def getCurrentHostNamePath(self) -> str:
        location: str = None
        if org.allbinary.globals.URLGLOBALS.isTestingMode():
            location = self.getTestHostNamePath()
        else:
            location = self.getHostNamePath()
        return location
    

    def getCurrentHomeHostName(self) -> str:
        location: str = None
        if org.allbinary.globals.URLGLOBALS.isTestingMode():
            location = self.getTestHomeHostName()
        else:
            location = self.getHomeHostName()
        return location
    

    def getCurrentHomeHostNamePath(self) -> str:
        location: str = None
        if org.allbinary.globals.URLGLOBALS.isTestingMode():
            location = self.getTestHomeHostNamePath()
        else:
            location = self.getHomeHostNamePath()
        return location
    

    def getName(self) -> str:
        return self.name
    

    def getUserName(self) -> str:
        return self.userName
    

    def getBasketName(self) -> str:
        return self.basketName
    

    def getHomeHostName(self) -> str:
        return self.homeHostName
    

    def getHomeHostNamePath(self) -> str:
        return self.homeHostNamePath
    

    def getHostName(self) -> str:
        return self.hostName
    

    def getHostNamePath(self) -> str:
        return self.hostNamePath
    

    def getTestHomeHostName(self) -> str:
        return self.testHomeHostName
    

    def getTestHomeHostNamePath(self) -> str:
        return self.testHomeHostNamePath
    

    def getTestHostName(self) -> str:
        return self.testHostName
    

    def getTestHostNamePath(self) -> str:
        return self.testHostNamePath
    

    def getStaticPath(self) -> str:
        return self.staticPath
    

    def getCategoryPath(self) -> str:
        return self.categoryPath
    

    def getInventoryControl(self) -> str:
        return self.inventoryControl
    

    # throws Exception
    def getSubStores(self) -> BasicArrayList:
        try:
            tokenizer: Tokenizer = Tokenizer(CommonSeps.getInstance().SEMICOLON)
            subStoreVector: BasicArrayList = tokenizer.getTokensFromString(self.subStores, BasicArrayListD())
            return subStoreVector
        except Exception as e:
            raise e
    

    def getTagLocation(self) -> str:
        return self.tagLocation
    

    def getPackageLocation(self) -> str:
        return self.packageLocation
    

    def getFtp(self) -> str:
        return self.ftp
    

    def getFtpUserName(self) -> str:
        return self.ftpUserName
    

    def getFtpPassword(self) -> str:
        return self.ftpPassword
    

    def getTestFtp(self) -> str:
        return self.testFtp
    

    def getTestFtpUserName(self) -> str:
        return self.testFtpUserName
    

    def getTestFtpPassword(self) -> str:
        return self.testFtpPassword
    

    def getFtpPath(self) -> str:
        return self.ftpPath
    

    def getTestFtpPath(self) -> str:
        return self.testFtpPath
    

    def getTimeCreated(self) -> str:
        return self.timeCreated
    

    def getLastModified(self) -> str:
        return self.lastModified
# from java.util.HashMap import HashMap
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.user.UserData import UserData
from org.allbinary.logic.string.tokens.Tokenizer import Tokenizer
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


