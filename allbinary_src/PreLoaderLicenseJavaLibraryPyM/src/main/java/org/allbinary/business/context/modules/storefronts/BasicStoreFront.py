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

from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.business.context.modules.storefronts.BasicStoreFrontInterface import BasicStoreFrontInterface


class BasicStoreFront(BasicStoreFrontInterface):

    def _init_fields(self) -> None:
        if "name" not in vars(self): self.name: str = None
        if "userName" not in vars(self): self.userName: str = None
        if "basketName" not in vars(self): self.basketName: str = None
        if "homeHostName" not in vars(self): self.homeHostName: str = None
        if "homeHostNamePath" not in vars(self): self.homeHostNamePath: str = None
        if "hostName" not in vars(self): self.hostName: str = None
        if "hostNamePath" not in vars(self): self.hostNamePath: str = None
        if "testHomeHostName" not in vars(self): self.testHomeHostName: str = None
        if "testHomeHostNamePath" not in vars(self): self.testHomeHostNamePath: str = None
        if "testHostName" not in vars(self): self.testHostName: str = None
        if "testHostNamePath" not in vars(self): self.testHostNamePath: str = None
        if "imagePath" not in vars(self): self.imagePath: str = None
        if "staticPath" not in vars(self): self.staticPath: str = None
        if "categoryPath" not in vars(self): self.categoryPath: str = None
        if "inventoryControl" not in vars(self): self.inventoryControl: str = None
        if "subStores" not in vars(self): self.subStores: str = None
        if "tagLocation" not in vars(self): self.tagLocation: str = None
        if "packageLocation" not in vars(self): self.packageLocation: str = None
        if "ftp" not in vars(self): self.ftp: str = None
        if "ftpPath" not in vars(self): self.ftpPath: str = None
        if "ftpUserName" not in vars(self): self.ftpUserName: str = None
        if "ftpPassword" not in vars(self): self.ftpPassword: str = None
        if "testFtp" not in vars(self): self.testFtp: str = None
        if "testFtpPath" not in vars(self): self.testFtpPath: str = None
        if "testFtpUserName" not in vars(self): self.testFtpUserName: str = None
        if "testFtpPassword" not in vars(self): self.testFtpPassword: str = None
        if "timeCreated" not in vars(self): self.timeCreated: str = None
        if "lastModified" not in vars(self): self.lastModified: str = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 1:
            __class__._constructor1(self, *args)
    

    def _constructor0(self) -> None:
        __class__._init_fields(self)
    

    def _constructor1(self, storeHashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.user.UserData import UserData
        __class__._init_fields(self)
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
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        return URLGLOBALS.getTestHtmlPath() + self.getCurrentHostNamePath()
    

    def getCurrentHostName(self) -> str:
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        location: str = None
        if java_predicate(URLGLOBALS, "isTestingMode"):
            location = self.getTestHostName()
        else:
            location = self.getHostName()
        return location
    

    def getCurrentHostNamePath(self) -> str:
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        location: str = None
        if java_predicate(URLGLOBALS, "isTestingMode"):
            location = self.getTestHostNamePath()
        else:
            location = self.getHostNamePath()
        return location
    

    def getCurrentHomeHostName(self) -> str:
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        location: str = None
        if java_predicate(URLGLOBALS, "isTestingMode"):
            location = self.getTestHomeHostName()
        else:
            location = self.getHomeHostName()
        return location
    

    def getCurrentHomeHostNamePath(self) -> str:
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        location: str = None
        if java_predicate(URLGLOBALS, "isTestingMode"):
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
        from org.allbinary.logic.string.tokens.Tokenizer import Tokenizer
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
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
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.user.UserData import UserData
# from org.allbinary.logic.string.tokens.Tokenizer import Tokenizer
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS


