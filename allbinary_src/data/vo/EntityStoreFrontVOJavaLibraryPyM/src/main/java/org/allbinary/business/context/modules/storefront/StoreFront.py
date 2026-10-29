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

import datetime
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface


class StoreFront(StoreFrontInterface):
    RESOURCES: str = " Resources" + str(AbPathData.getInstance().SEPARATOR)

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.directory: Directory = Directory.getInstance()
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.abPathUtil: AbPathUtil = AbPathUtil.getInstance()
        self.name: str = self.stringUtil.EMPTY_STRING
        self.basketName: str = self.stringUtil.EMPTY_STRING
        self.homeHostName: str = self.stringUtil.EMPTY_STRING
        self.homeHostNamePath: AbPath = self.abPathUtil.NO_ABPATH
        self.hostName: str = self.stringUtil.EMPTY_STRING
        self.hostNamePath: AbPath = self.abPathUtil.NO_ABPATH
        self.testHomeHostName: str = self.stringUtil.EMPTY_STRING
        self.testHomeHostNamePath: AbPath = self.abPathUtil.NO_ABPATH
        self.testHostName: str = self.stringUtil.EMPTY_STRING
        self.testHostNamePath: AbPath = self.abPathUtil.NO_ABPATH
        self.imagePath: AbPath = self.abPathUtil.NO_ABPATH
        self.staticPath: AbPath = self.abPathUtil.NO_ABPATH
        self.categoryPath: AbPath = self.abPathUtil.NO_ABPATH
        self.inventoryControl: str = self.stringUtil.EMPTY_STRING
        self.contextConfigurationInterface: ContextConfigurationInterface = None
        self.subStores: str = self.stringUtil.EMPTY_STRING
        self.tagLocation: str = self.stringUtil.EMPTY_STRING
        self.packageLocation: str = self.stringUtil.EMPTY_STRING
        self.ftp: str = self.stringUtil.EMPTY_STRING
        self.ftpPath: AbPath = self.abPathUtil.NO_ABPATH
        self.ftpUserName: str = self.stringUtil.EMPTY_STRING
        self.ftpPassword: str = self.stringUtil.EMPTY_STRING
        self.testFtp: str = self.stringUtil.EMPTY_STRING
        self.testFtpPath: AbPath = self.abPathUtil.NO_ABPATH
        self.testFtpUserName: str = self.stringUtil.EMPTY_STRING
        self.testFtpPassword: str = self.stringUtil.EMPTY_STRING
        self.timeCreated: str = self.stringUtil.EMPTY_STRING
        self.lastModified: str = self.stringUtil.EMPTY_STRING
        self.MINCHAR: int = 0
        self.MINSTORENAMELENGTH: int = 1
        self.MAXCHAR: int = 255
        self.EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
        self.ONE_EMPTY_STRING_ARRAY: list[str] = StringUtil.getInstance().ONE_EMPTY_STRING_ARRAY

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
        self.contextConfigurationInterface = ContextConfiguration()
    

    def _constructor1(self, request: HttpServletRequest) -> None:
        self._init_fields()
        self.getFormData(RequestParams(request).toHashMap())
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            self.logUtil.putF("TWB- needs update for adding and updating context configuration - currently defaults to admin context config", self, "StoreFront")
        self.setContextConfigurationInterface(ContextConfigurationInterfaceFactory.getInstance().getInstance("Admin"))
    

    def _constructor1(self, hashMap: dict) -> None:
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        self._init_fields()
        self.getFormData(hashMap)
        domDocumentString: str = hashMap.get(StoreFrontData.getInstance().CONFIGURATION)
        if domDocumentString is None:
            document: Document = DomDocumentHelper.create(domDocumentString)
            self.setContextConfigurationInterface(ContextConfigurationInterfaceFactory.getInstance().getInstance(document))
    

    def isColumn(self, columnName: str) -> bool:
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        if ((columnName > StoreFrontData.getInstance().NAME) - (columnName < StoreFrontData.getInstance().NAME)) == 0 or ((columnName > UserData.MAINEMAIL) - (columnName < UserData.MAINEMAIL)) == 0:
            return True
        else:
            return False
    

    # throws Exception
    def createPath(self, key: str, hashMap: dict) -> AbPath:
        return AbPath(self.create(self.EMPTY_STRING, key, hashMap), StringUtil.getInstance().EMPTY_STRING)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def createPath(self, append: str, key: str, hashMap: dict) -> AbPath:
        return AbPath(self.create(append, key, hashMap), StringUtil.getInstance().EMPTY_STRING)
    

    def get(self, key: str, hashMap: dict) -> str:
        return self.create(self.EMPTY_STRING, key, hashMap)
    

    def create(self, append: str, key: str, hashMap: dict) -> str:
        path: str = hashMap.get(key)
        if StringValidationUtil.getInstance().isEmpty(path):
            return self.EMPTY_STRING
        else:
            if self.isColumn(path):
                return str(hashMap.get(path)) + append
            else:
                return path
    

    # throws Exception
    def getFormData(self, storeHashMap: dict) -> None:
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        storeFrontData: StoreFrontData = StoreFrontData.getInstance()
        self.name = storeHashMap.get(storeFrontData.NAME)
        self.basketName = storeHashMap.get(storeFrontData.NAME)
        self.homeHostName = storeHashMap.get(storeFrontData.HOMEHOSTNAME)
        self.homeHostNamePath = self.createPath(storeFrontData.HOMEHOSTNAMEPATH, storeHashMap)
        self.hostName = storeHashMap.get(storeFrontData.HOSTNAME)
        self.hostNamePath = self.createPath(storeFrontData.HOSTNAMEPATH, storeHashMap)
        self.testHomeHostName = storeHashMap.get(storeFrontData.TESTHOMEHOSTNAME)
        self.testHomeHostNamePath = self.createPath(storeFrontData.TESTHOMEHOSTNAMEPATH, storeHashMap)
        self.testHostName = storeHashMap.get(storeFrontData.TESTHOSTNAME)
        self.testHostNamePath = self.createPath(storeFrontData.TESTHOSTNAMEPATH, storeHashMap)
        self.imagePath = self.createPath(StoreFront.RESOURCES, storeFrontData.IMAGEPATH, storeHashMap)
        self.staticPath = self.createPath(" Products" + str(AbPathData.getInstance().SEPARATOR), storeFrontData.STATICPATH, storeHashMap)
        self.categoryPath = self.createPath(StoreFront.RESOURCES, storeFrontData.CATEGORYPATH, storeHashMap)
        self.inventoryControl = storeHashMap.get(storeFrontData.INVENTORYCONTROL)
        self.subStores = storeHashMap.get(storeFrontData.SUBSTORES)
        self.tagLocation = storeHashMap.get(storeFrontData.TAGLOCATION)
        self.packageLocation = storeHashMap.get(storeFrontData.PACKAGELOCATION)
        self.ftp = storeHashMap.get(storeFrontData.FTP)
        self.ftpPath = self.createPath(storeFrontData.FTPPATH, storeHashMap)
        self.ftpUserName = storeHashMap.get(storeFrontData.FTPUSERNAME)
        self.ftpPassword = storeHashMap.get(storeFrontData.FTPPASSWORD)
        self.testFtp = storeHashMap.get(storeFrontData.TESTFTP)
        self.testFtpPath = self.createPath(storeFrontData.TESTFTPPATH, storeHashMap)
        self.testFtpUserName = storeHashMap.get(storeFrontData.TESTFTPUSERNAME)
        self.testFtpPassword = storeHashMap.get(storeFrontData.TESTFTPPASSWORD)
        self.timeCreated = storeHashMap.get(EntryData.getInstance().TIMECREATED)
        self.lastModified = storeHashMap.get(EntryData.getInstance().LASTMODIFIED)
    

    def isNameValid(self) -> bool:
        if not StringValidationUtil.getInstance().isValidRequired(self.name, self.MINSTORENAMELENGTH, self.MAXCHAR):
            return False
        else:
            isEscapedCharactersContained: bool = False
            storeNameEscaped: str = StringEscapeUtils.escapeHtml3(self.name)
            if ((self.name > storeNameEscaped) - (self.name < storeNameEscaped)) != 0:
                isEscapedCharactersContained = True
            stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
            isSpacesContained: bool = False
            if stringValidationUtil.containsSpaces(self.name):
                isSpacesContained = True
            if isSpacesContained or isEscapedCharactersContained:
                hashMap: dict = SpecialCharacterUtil.getHashMap()
                hashMap.put([CommonSeps.getInstance().SPACE], self.ONE_EMPTY_STRING_ARRAY)
                self.name = Replace(hashMap).all(self.name)
        return True
    

    def isValid(self) -> bool:
        valid: bool = True
        valid = self.isNameValid()
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if not stringValidationUtil.isValidRequired(self.basketName, self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidRequired(self.homeHostName, self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidNotRequired(str(self.homeHostNamePath), self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidRequired(self.hostName, self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidRequired(str(self.hostNamePath), self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidNotRequired(self.testHomeHostName, self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidNotRequired(str(self.testHomeHostNamePath), self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidNotRequired(self.testHostName, self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidNotRequired(str(self.testHostNamePath), self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidRequired(str(self.imagePath), self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidRequired(str(self.staticPath), self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidRequired(str(self.categoryPath), self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidRequired(self.inventoryControl, self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidNotRequired(self.subStores, self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidNotRequired(self.tagLocation, self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidRequired(self.packageLocation, self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidNotRequired(self.ftp, self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidNotRequired(str(self.ftpPath), self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidNotRequired(self.ftpUserName, self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidNotRequired(self.ftpPassword, self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidNotRequired(self.testFtp, self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidNotRequired(str(self.testFtpPath), self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidNotRequired(self.testFtpUserName, self.MINCHAR, self.MAXCHAR):
            valid = False
        if not stringValidationUtil.isValidNotRequired(self.testFtpPassword, self.MINCHAR, self.MAXCHAR):
            valid = False
        if valid == True:
            return True
        else:
            return False
    

    def nameValidationInfo(self) -> str:
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if not stringValidationUtil.isValidRequired(self.name, self.MINCHAR, self.MAXCHAR):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Name is invalid. Must be < ")
            stringBuffer.appendint(self.MAXCHAR)
            stringBuffer.append(" and > 0 characters.<br>")
            return str(stringBuffer)
        return self.EMPTY_STRING
    

    def validationInfo(self) -> str:
        try:
            stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.nameValidationInfo())
            if not stringValidationUtil.isValidRequired(self.basketName, self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Basket name is invalid. Must be < ")
                stringBuffer.appendint(self.MAXCHAR)
                stringBuffer.append(" and > 0 characters.<br>")
            if not stringValidationUtil.isValidRequired(self.homeHostName, self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Home host name is invalid. Must be < ")
                stringBuffer.appendint(self.MAXCHAR)
                stringBuffer.append(" and > 0 characters.<br>")
            if not stringValidationUtil.isValidNotRequired(str(self.homeHostNamePath), self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Home host name path is invalid. Must be < ")
                stringBuffer.appendint(self.MAXCHAR)
                stringBuffer.append(" and > 0 characters.<br>")
            if not stringValidationUtil.isValidRequired(self.hostName, self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Host name is invalid. Must be < ")
                stringBuffer.appendint(self.MAXCHAR)
                stringBuffer.append(" and > 0 characters.<br>")
            if not stringValidationUtil.isValidRequired(str(self.hostNamePath), self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Host name path is invalid. Must be < ")
                stringBuffer.appendint(self.MAXCHAR)
                stringBuffer.append(" and > 0 characters.<br>")
            if not stringValidationUtil.isValidNotRequired(self.testHomeHostName, self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Test home host name is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidNotRequired(str(self.testHomeHostNamePath), self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Test home host name path is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidNotRequired(self.testHostName, self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Test host name is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidNotRequired(str(self.testHostNamePath), self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Test host name path is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidRequired(str(self.imagePath), self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Image path is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidRequired(str(self.staticPath), self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Static path is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidRequired(str(self.categoryPath), self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Category path is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidRequired(self.inventoryControl, self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Inventory control is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidNotRequired(self.subStores, self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Sub stores is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidNotRequired(self.tagLocation, self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Tag location is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidRequired(self.packageLocation, self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Package location is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidNotRequired(self.ftp, self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Ftp is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidNotRequired(str(self.ftpPath), self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Ftp path is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidNotRequired(self.ftpUserName, self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Ftp username is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidNotRequired(self.ftpPassword, self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Ftp password is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidNotRequired(self.testFtp, self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Test ftp is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidNotRequired(str(self.testFtpPath), self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Test ftp Path is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidNotRequired(self.testFtpUserName, self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Test ftp username is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not stringValidationUtil.isValidNotRequired(self.testFtpPassword, self.MINCHAR, self.MAXCHAR):
                stringBuffer.append("Test ftp password is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Validating Form"
    

    def getTestHtmlPath(self) -> str:
        return org.allbinary.globals.URLGLOBALS.getTestHtmlPath() + self.getCurrentHostNamePath()
    

    def getCurrentHostName(self) -> str:
        location: str = self.EMPTY_STRING
        if org.allbinary.globals.URLGLOBALS.isTestingMode():
            location = self.getTestHostName()
        else:
            location = self.getHostName()
        return location
    

    def getCurrentHostNamePath(self) -> str:
        location: str = self.EMPTY_STRING
        if org.allbinary.globals.URLGLOBALS.isTestingMode():
            location = self.getTestHostNamePath()
        else:
            location = self.getHostNamePath()
        return location
    

    def getCurrentHomeHostName(self) -> str:
        location: str = self.EMPTY_STRING
        if org.allbinary.globals.URLGLOBALS.isTestingMode():
            location = self.getTestHomeHostName()
        else:
            location = self.getHomeHostName()
        return location
    

    def getCurrentHomeHostNamePath(self) -> str:
        location: str = self.EMPTY_STRING
        if org.allbinary.globals.URLGLOBALS.isTestingMode():
            location = self.getTestHomeHostNamePath()
        else:
            location = self.getHomeHostNamePath()
        return location
    

    def getName(self) -> str:
        return self.name
    

    def getBasketName(self) -> str:
        return self.basketName
    

    def getHomeHostName(self) -> str:
        return self.homeHostName
    

    def getHomeHostNamePath(self) -> str:
        return str(self.homeHostNamePath)
    

    def getHostName(self) -> str:
        return self.hostName
    

    def getHostNamePath(self) -> str:
        return str(self.hostNamePath)
    

    def getTestHomeHostName(self) -> str:
        return self.testHomeHostName
    

    def getTestHomeHostNamePath(self) -> str:
        return str(self.testHomeHostNamePath)
    

    def getTestHostName(self) -> str:
        return self.testHostName
    

    def getTestHostNamePath(self) -> str:
        return str(self.testHostNamePath)
    

    def getStaticPath(self) -> str:
        return str(self.staticPath)
    

    def getCategoryPath(self) -> str:
        return str(self.categoryPath)
    

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
        return str(self.ftpPath)
    

    def getTestFtpPath(self) -> str:
        return str(self.testFtpPath)
    

    def getTimeCreated(self) -> str:
        return self.timeCreated
    

    def getLastModified(self) -> str:
        return self.lastModified
    

    def setName(self, value: str) -> None:
        self.name = value
    

    def setBasketName(self, value: str) -> None:
        self.basketName = value
    

    def setHomeHostName(self, value: str) -> None:
        self.homeHostName = value
    

    # throws Exception
    def setHomeHostNamePath(self, value: str) -> None:
        self.homeHostNamePath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    def setHostName(self, value: str) -> None:
        self.hostName = value
    

    # throws Exception
    def setHostNamePath(self, value: str) -> None:
        self.hostNamePath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    def setTestHomeHostName(self, value: str) -> None:
        self.testHomeHostName = value
    

    # throws Exception
    def setTestHomeHostNamePath(self, value: str) -> None:
        self.testHomeHostNamePath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    def setTestHostName(self, value: str) -> None:
        self.testHostName = value
    

    # throws Exception
    def setTestHostNamePath(self, value: str) -> None:
        self.testHostNamePath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    # throws Exception
    def setImagePath(self, value: str) -> None:
        self.imagePath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    # throws Exception
    def setStaticPath(self, value: str) -> None:
        self.staticPath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    # throws Exception
    def setCategoryPath(self, value: str) -> None:
        self.categoryPath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    def setSubStores(self, value: str) -> None:
        self.subStores = value
    

    def setTagLocation(self, value: str) -> None:
        self.tagLocation = value
    

    def setPackageLocation(self, value: str) -> None:
        self.packageLocation = value
    

    def setInventoryControl(self, value: str) -> None:
        self.inventoryControl = value
    

    # Java overloaded method: Python keeps the last definition
    def getPackageLocation(self, value: str) -> None:
        self.packageLocation = value
    

    def setFtp(self, value: str) -> None:
        self.ftp = value
    

    def setFtpUserName(self, value: str) -> None:
        self.ftpUserName = value
    

    def setFtpPassword(self, value: str) -> None:
        self.ftpPassword = value
    

    def setTestFtp(self, value: str) -> None:
        self.testFtp = value
    

    def setTestFtpUserName(self, value: str) -> None:
        self.testFtpUserName = value
    

    def setTestFtpPassword(self, value: str) -> None:
        self.testFtpPassword = value
    

    def setTimeCreated(self, value: str) -> None:
        self.timeCreated = value
    

    def setLastModified(self, value: str) -> None:
        self.lastModified = value
    

    # throws Exception
    def setFtpPath(self, value: str) -> None:
        self.ftpPath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    # throws Exception
    def setTestFtpPath(self, value: str) -> None:
        self.testFtpPath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    # throws Exception
    def createDirectories(self) -> bool:
        storeAbPath: AbPath = AbPath(self.URLGLOBALS.getWebappPath() + self.getCurrentHomeHostNamePath(), StringUtil.getInstance().EMPTY_STRING)
        if not self.directory.create(storeAbPath):
            return False
        if not self.directory.create(AbPath(storeAbPath + self.getCategoryPath(), StringUtil.getInstance().EMPTY_STRING)):
            return False
        if not self.directory.create(AbPath(storeAbPath + self.getStaticPath(), StringUtil.getInstance().EMPTY_STRING)):
            return False
        return True
    

    # throws Exception
    def install(self, current: int, total: int) -> None:
        try:
            if not self.createDirectories():
                raise Exception("Unable to create store directories")
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append(self.URLGLOBALS.getMainPath())
            stringBuffer.append(self.FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH)
            viewPath: str = str(stringBuffer)
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append(viewPath)
            stringBuffer.append(self.FREEBLISKET_PATH_GLOBALS.getInstance().INSTALLPATH)
            fromDirectoryAbPath: AbPath = AbPath(str(stringBuffer), StringUtil.getInstance().EMPTY_STRING)
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append(viewPath)
            stringBuffer.append("special")
            stringBuffer.append(AbPathData.getInstance().SEPARATOR)
            fromSpecialDirectoryAbPath: AbPath = AbPath(str(stringBuffer), StringUtil.getInstance().EMPTY_STRING)
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append(viewPath)
            stringBuffer.append(self.getName())
            stringBuffer.append(AbPathData.getInstance().SEPARATOR)
            toDirectoryAbPath: AbPath = AbPath(str(stringBuffer), StringUtil.getInstance().EMPTY_STRING)
            if current == 0:
                if not self.directory.create(toDirectoryAbPath):
                    raise Exception("Unable to create store view directory: " + str(toDirectoryAbPath))
            viewTotal: int = int((total * 85) / 100)
            installTotal: int = int((total * 93) / 100)
            if current < viewTotal:
                file: AbFile = AbFile.createAbFileFromAbPath(fromSpecialDirectoryAbPath)
                if file.isDirectory():
                    halfViewTotal: int = int(viewTotal / 2)
                    if current < halfViewTotal:
                        self.installViews(fromSpecialDirectoryAbPath, toDirectoryAbPath, current, halfViewTotal)
                    elif current < viewTotal:
                        self.installViews(fromDirectoryAbPath, toDirectoryAbPath, current - halfViewTotal, viewTotal - halfViewTotal)
                else:
                    self.installViews(fromDirectoryAbPath, toDirectoryAbPath, current, viewTotal)
            elif current < installTotal:
                self.installResources(fromDirectoryAbPath, current - viewTotal, installTotal - viewTotal)
            else:
                self.installMedia(fromDirectoryAbPath, current - installTotal, total - installTotal)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "install()", e)
            raise e
    

    # throws Exception
    def installViews(self, fromDirectoryAbPath: AbPath, toDirectoryAbPath: AbPath, current: int, total: int) -> None:
        FileUtil.getInstance().copyDirectoryPortion(fromDirectoryAbPath, toDirectoryAbPath, True, False, current, total)
    

    # throws Exception
    def installResources(self, fromDirectoryAbPath: AbPath, current: int, total: int) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(str(fromDirectoryAbPath))
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        stringBuffer.append("Resources")
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        installCategoryAbPath: AbPath = AbPath(str(stringBuffer), StringUtil.getInstance().EMPTY_STRING)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(self.URLGLOBALS.getMainPath())
        stringBuffer.append(self.getCurrentHomeHostNamePath())
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        stringBuffer.append(self.getCategoryPath())
        categoryAbPath: AbPath = AbPath(str(stringBuffer), StringUtil.getInstance().EMPTY_STRING)
        FileUtil.getInstance().copyDirectoryPortion(installCategoryAbPath, categoryAbPath, True, False, current, total)
    

    # throws Exception
    def installMedia(self, fromDirectoryAbPath: AbPath, current: int, total: int) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(str(fromDirectoryAbPath))
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        stringBuffer.append(self.FREEBLISKET_PATH_GLOBALS.getInstance().TEMPLATEPATH)
        stringBuffer.append("images")
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        viewStoreImagesDirectoryAbPath: AbPath = AbPath(str(stringBuffer), StringUtil.getInstance().EMPTY_STRING)
        storeAbPath: AbPath = AbPath(self.URLGLOBALS.getWebappPath() + self.getCurrentHomeHostNamePath(), StringUtil.getInstance().EMPTY_STRING)
        FileUtil.getInstance().copyDirectoryPortion(viewStoreImagesDirectoryAbPath, storeAbPath, True, False, current, total)
    

    # throws Exception
    def toVector(self) -> BasicArrayList:
        dataVector: BasicArrayList = BasicArrayListD()
        dataVector.add(self.name)
        dataVector.add(self.homeHostName)
        dataVector.add(str(self.homeHostNamePath))
        dataVector.add(self.hostName)
        dataVector.add(str(self.hostNamePath))
        dataVector.add(self.testHomeHostName)
        dataVector.add(str(self.testHomeHostNamePath))
        dataVector.add(self.testHostName)
        dataVector.add(str(self.testHostNamePath))
        dataVector.add(str(self.imagePath))
        dataVector.add(str(self.staticPath))
        dataVector.add(str(self.categoryPath))
        dataVector.add(self.inventoryControl)
        contextConfigurationDomDocumentMapping: ContextConfigurationDomDocumentMapping = ContextConfigurationDomDocumentMapping(self.getContextConfigurationInterface())
        dataVector.add(contextConfigurationDomDocumentMapping.toDomDocumentString())
        dataVector.add(self.subStores)
        dataVector.add(self.tagLocation)
        dataVector.add(self.packageLocation)
        dataVector.add(self.ftp)
        dataVector.add(str(self.ftpPath))
        dataVector.add(self.ftpUserName)
        dataVector.add(self.ftpPassword)
        dataVector.add(self.testFtp)
        dataVector.add(str(self.testFtpPath))
        dataVector.add(self.testFtpUserName)
        dataVector.add(self.testFtpPassword)
        calendar: datetime.datetime = datetime.datetime.now()
        time: str = str(str(int(calendar.getTimeInMillis())))
        dataVector.add(time)
        dataVector.add(time)
        return dataVector
    

    # throws Exception
    def toHashMap(self) -> dict:
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        storeFrontData: StoreFrontData = StoreFrontData.getInstance()
        dataHashMap: dict = StdUtil.getInstance().createHashMap()
        dataHashMap.put(storeFrontData.NAME, self.name)
        dataHashMap.put(storeFrontData.HOMEHOSTNAME, self.homeHostName)
        dataHashMap.put(storeFrontData.HOMEHOSTNAMEPATH, str(self.homeHostNamePath))
        dataHashMap.put(storeFrontData.HOSTNAME, self.hostName)
        dataHashMap.put(storeFrontData.HOSTNAMEPATH, str(self.hostNamePath))
        dataHashMap.put(storeFrontData.TESTHOMEHOSTNAME, self.testHomeHostName)
        dataHashMap.put(storeFrontData.TESTHOMEHOSTNAMEPATH, str(self.testHomeHostNamePath))
        dataHashMap.put(storeFrontData.TESTHOSTNAME, self.testHostName)
        dataHashMap.put(storeFrontData.TESTHOSTNAMEPATH, str(self.testHostNamePath))
        dataHashMap.put(storeFrontData.IMAGEPATH, str(self.imagePath))
        dataHashMap.put(storeFrontData.STATICPATH, str(self.staticPath))
        dataHashMap.put(storeFrontData.CATEGORYPATH, str(self.categoryPath))
        dataHashMap.put(storeFrontData.INVENTORYCONTROL, self.inventoryControl)
        contextConfigurationDomDocumentMapping: ContextConfigurationDomDocumentMapping = ContextConfigurationDomDocumentMapping(self.getContextConfigurationInterface())
        dataHashMap.put(storeFrontData.CONFIGURATION, contextConfigurationDomDocumentMapping.toDomDocumentString())
        dataHashMap.put(storeFrontData.SUBSTORES, self.subStores)
        dataHashMap.put(storeFrontData.TAGLOCATION, self.tagLocation)
        dataHashMap.put(storeFrontData.PACKAGELOCATION, self.packageLocation)
        dataHashMap.put(storeFrontData.FTP, self.ftp)
        dataHashMap.put(storeFrontData.FTPPATH, str(self.ftpPath))
        dataHashMap.put(storeFrontData.FTPUSERNAME, self.ftpUserName)
        dataHashMap.put(storeFrontData.FTPPASSWORD, self.ftpPassword)
        dataHashMap.put(storeFrontData.TESTFTP, self.testFtp)
        dataHashMap.put(storeFrontData.TESTFTPPATH, str(self.testFtpPath))
        dataHashMap.put(storeFrontData.TESTFTPUSERNAME, self.testFtpUserName)
        dataHashMap.put(storeFrontData.TESTFTPPASSWORD, self.testFtpPassword)
        calendar: datetime.datetime = datetime.datetime.now()
        time: str = str(str(int(calendar.getTimeInMillis())))
        dataHashMap.put(EntryData.getInstance().LASTMODIFIED, time)
        return dataHashMap
    

    def getKey(self) -> object:
        return self.getName()
    

    def getContextConfigurationInterface(self) -> ContextConfigurationInterface:
        return self.contextConfigurationInterface
    

    def setContextConfigurationInterface(self, contextConfigurationInterface: ContextConfigurationInterface) -> None:
        self.contextConfigurationInterface = contextConfigurationInterface
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.business.context.configuration.ContextConfiguration import ContextConfiguration
from org.allbinary.business.context.configuration.ContextConfigurationDomDocumentMapping import ContextConfigurationDomDocumentMapping
from org.allbinary.business.context.configuration.ContextConfigurationInterface import ContextConfigurationInterface
from org.allbinary.business.context.configuration.ContextConfigurationInterfaceFactory import ContextConfigurationInterfaceFactory
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.user.UserData import UserData
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.FileUtil import FileUtil
from org.allbinary.logic.io.file.directory.Directory import Directory
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.io.path.AbPathUtil import AbPathUtil
from org.allbinary.logic.string.SpecialCharacterUtil import SpecialCharacterUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.string.regex.replace.Replace import Replace
from org.allbinary.logic.string.tokens.Tokenizer import Tokenizer
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.apache.commons.lang3.StringEscapeUtils import StringEscapeUtils
from org.w3c.dom.Document import Document


