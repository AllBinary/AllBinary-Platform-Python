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

from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_divide
import datetime
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface


class StoreFront(StoreFrontInterface):
    RESOURCES: str = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.io.file.directory.Directory import Directory
        from org.allbinary.logic.io.path.AbPathUtil import AbPathUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.string.CommonStrings import CommonStrings
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
        if "contextConfigurationInterface" not in vars(self): self.contextConfigurationInterface: ContextConfigurationInterface = None
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
            __class__._constructor0(self, *args)
        elif len(args) == 1:
            __class__.__jconstructor1(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "HttpServletRequest" for base in type(args[0]).__mro__)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)
    

    def _constructor0(self) -> None:
        from org.allbinary.business.context.configuration.ContextConfiguration import ContextConfiguration
        __class__._init_fields(self)
        self.contextConfigurationInterface = ContextConfiguration()
    

    def _constructor1_1(self, request: HttpServletRequest) -> None:
        from org.allbinary.business.context.configuration.ContextConfigurationInterfaceFactory import ContextConfigurationInterfaceFactory
        from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        self.getFormData(RequestParams(request).toHashMap())
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
            self.logUtil.putF("TWB- needs update for adding and updating context configuration - currently defaults to admin context config", self, "StoreFront")
        self.setContextConfigurationInterface(ContextConfigurationInterfaceFactory.getInstance().getInstance("Admin"))
    

    def _constructor1_2(self, hashMap: HashMap) -> None:
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.configuration.ContextConfigurationInterfaceFactory import ContextConfigurationInterfaceFactory
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.w3c.dom.Document import Document
        __class__._init_fields(self)
        self.getFormData(hashMap)
        domDocumentString: str = hashMap.get(StoreFrontData.getInstance().CONFIGURATION)
        if domDocumentString is None:
            document: Document = DomDocumentHelper.create(domDocumentString)
            self.setContextConfigurationInterface(ContextConfigurationInterfaceFactory.getInstance().getInstance(document))
    

    def isColumn(self, columnName: str) -> bool:
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.business.user.UserData import UserData
        if ((columnName > StoreFrontData.getInstance().NAME) - (columnName < StoreFrontData.getInstance().NAME)) == 0 or ((columnName > UserData.MAINEMAIL) - (columnName < UserData.MAINEMAIL)) == 0:
            return True
        else:
            return False
    

    # throws Exception
    def createPath_j2(self, key: str, hashMap: HashMap) -> AbPath:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        return AbPath(self.create(self.EMPTY_STRING, key, hashMap), StringUtil.getInstance().EMPTY_STRING)
    

    # throws Exception
    def createPath_j3(self, append: str, key: str, hashMap: HashMap) -> AbPath:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        return AbPath(self.create(append, key, hashMap), StringUtil.getInstance().EMPTY_STRING)

    def createPath(self, *args):
        implementation = __class__.__dict__.get("createPath_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().createPath(*args)
    

    def get(self, key: str, hashMap: HashMap) -> str:
        from java.util.HashMap import HashMap
        return self.create(self.EMPTY_STRING, key, hashMap)
    

    def create(self, append: str, key: str, hashMap: HashMap) -> str:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        path: str = hashMap.get(key)
        if StringValidationUtil.getInstance().isEmpty(path):
            return self.EMPTY_STRING
        else:
            if self.isColumn(path):
                return str(hashMap.get(path)) + append
            else:
                return path
    

    # throws Exception
    def getFormData(self, storeHashMap: HashMap) -> None:
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from java.util.HashMap import HashMap
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.logic.io.path.AbPathData import AbPathData
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
        from java.util.HashMap import HashMap
        from org.allbinary.logic.string.SpecialCharacterUtil import SpecialCharacterUtil
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.string.regex.replace.Replace import Replace
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.apache.commons.lang3.StringEscapeUtils import StringEscapeUtils
        if not (StringValidationUtil.getInstance().isValidRequired(self.name, self.MINSTORENAMELENGTH, self.MAXCHAR)):
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
                hashMap: HashMap = SpecialCharacterUtil.getHashMap()
                hashMap.put([CommonSeps.getInstance().SPACE], self.ONE_EMPTY_STRING_ARRAY)
                self.name = Replace(hashMap).all(self.name)
        return True
    

    def isValid(self) -> bool:
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        valid: bool = True
        valid = java_predicate(self, "isNameValid")
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if not (stringValidationUtil.isValidRequired(self.basketName, self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidRequired(self.homeHostName, self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidNotRequired(str(self.homeHostNamePath), self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidRequired(self.hostName, self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidRequired(str(self.hostNamePath), self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidNotRequired(self.testHomeHostName, self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidNotRequired(str(self.testHomeHostNamePath), self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidNotRequired(self.testHostName, self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidNotRequired(str(self.testHostNamePath), self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidRequired(str(self.imagePath), self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidRequired(str(self.staticPath), self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidRequired(str(self.categoryPath), self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidRequired(self.inventoryControl, self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidNotRequired(self.subStores, self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidNotRequired(self.tagLocation, self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidRequired(self.packageLocation, self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidNotRequired(self.ftp, self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidNotRequired(str(self.ftpPath), self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidNotRequired(self.ftpUserName, self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidNotRequired(self.ftpPassword, self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidNotRequired(self.testFtp, self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidNotRequired(str(self.testFtpPath), self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidNotRequired(self.testFtpUserName, self.MINCHAR, self.MAXCHAR)):
            valid = False
        if not (stringValidationUtil.isValidNotRequired(self.testFtpPassword, self.MINCHAR, self.MAXCHAR)):
            valid = False
        if valid == True:
            return True
        else:
            return False
    

    def nameValidationInfo(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if not (stringValidationUtil.isValidRequired(self.name, self.MINCHAR, self.MAXCHAR)):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Name is invalid. Must be < ")
            stringBuffer.appendint(self.MAXCHAR)
            stringBuffer.append(" and > 0 characters.<br>")
            return str(stringBuffer)
        return self.EMPTY_STRING
    

    def validationInfo(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.nameValidationInfo())
            if not (stringValidationUtil.isValidRequired(self.basketName, self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Basket name is invalid. Must be < ")
                stringBuffer.appendint(self.MAXCHAR)
                stringBuffer.append(" and > 0 characters.<br>")
            if not (stringValidationUtil.isValidRequired(self.homeHostName, self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Home host name is invalid. Must be < ")
                stringBuffer.appendint(self.MAXCHAR)
                stringBuffer.append(" and > 0 characters.<br>")
            if not (stringValidationUtil.isValidNotRequired(str(self.homeHostNamePath), self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Home host name path is invalid. Must be < ")
                stringBuffer.appendint(self.MAXCHAR)
                stringBuffer.append(" and > 0 characters.<br>")
            if not (stringValidationUtil.isValidRequired(self.hostName, self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Host name is invalid. Must be < ")
                stringBuffer.appendint(self.MAXCHAR)
                stringBuffer.append(" and > 0 characters.<br>")
            if not (stringValidationUtil.isValidRequired(str(self.hostNamePath), self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Host name path is invalid. Must be < ")
                stringBuffer.appendint(self.MAXCHAR)
                stringBuffer.append(" and > 0 characters.<br>")
            if not (stringValidationUtil.isValidNotRequired(self.testHomeHostName, self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Test home host name is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidNotRequired(str(self.testHomeHostNamePath), self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Test home host name path is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidNotRequired(self.testHostName, self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Test host name is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidNotRequired(str(self.testHostNamePath), self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Test host name path is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidRequired(str(self.imagePath), self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Image path is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidRequired(str(self.staticPath), self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Static path is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidRequired(str(self.categoryPath), self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Category path is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidRequired(self.inventoryControl, self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Inventory control is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidNotRequired(self.subStores, self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Sub stores is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidNotRequired(self.tagLocation, self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Tag location is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidRequired(self.packageLocation, self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Package location is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidNotRequired(self.ftp, self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Ftp is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidNotRequired(str(self.ftpPath), self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Ftp path is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidNotRequired(self.ftpUserName, self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Ftp username is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidNotRequired(self.ftpPassword, self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Ftp password is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidNotRequired(self.testFtp, self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Test ftp is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidNotRequired(str(self.testFtpPath), self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Test ftp Path is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidNotRequired(self.testFtpUserName, self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Test ftp username is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            if not (stringValidationUtil.isValidNotRequired(self.testFtpPassword, self.MINCHAR, self.MAXCHAR)):
                stringBuffer.append("Test ftp password is invalid. Must be < " + str(self.MAXCHAR) + " and > 0 characters.<br>")
            return str(stringBuffer)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Validating Form"
    

    def getTestHtmlPath(self) -> str:
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        return URLGLOBALS.getTestHtmlPath() + self.getCurrentHostNamePath()
    

    def getCurrentHostName(self) -> str:
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        location: str = self.EMPTY_STRING
        if java_predicate(URLGLOBALS, "isTestingMode"):
            location = self.getTestHostName()
        else:
            location = self.getHostName()
        return location
    

    def getCurrentHostNamePath(self) -> str:
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        location: str = self.EMPTY_STRING
        if java_predicate(URLGLOBALS, "isTestingMode"):
            location = self.getTestHostNamePath()
        else:
            location = self.getHostNamePath()
        return location
    

    def getCurrentHomeHostName(self) -> str:
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        location: str = self.EMPTY_STRING
        if java_predicate(URLGLOBALS, "isTestingMode"):
            location = self.getTestHomeHostName()
        else:
            location = self.getHomeHostName()
        return location
    

    def getCurrentHomeHostNamePath(self) -> str:
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        location: str = self.EMPTY_STRING
        if java_predicate(URLGLOBALS, "isTestingMode"):
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
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
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
    

    def getPackageLocation_j0(self) -> str:
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
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.homeHostNamePath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    def setHostName(self, value: str) -> None:
        self.hostName = value
    

    # throws Exception
    def setHostNamePath(self, value: str) -> None:
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.hostNamePath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    def setTestHomeHostName(self, value: str) -> None:
        self.testHomeHostName = value
    

    # throws Exception
    def setTestHomeHostNamePath(self, value: str) -> None:
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.testHomeHostNamePath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    def setTestHostName(self, value: str) -> None:
        self.testHostName = value
    

    # throws Exception
    def setTestHostNamePath(self, value: str) -> None:
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.testHostNamePath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    # throws Exception
    def setImagePath(self, value: str) -> None:
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.imagePath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    # throws Exception
    def setStaticPath(self, value: str) -> None:
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.staticPath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    # throws Exception
    def setCategoryPath(self, value: str) -> None:
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.categoryPath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    def setSubStores(self, value: str) -> None:
        self.subStores = value
    

    def setTagLocation(self, value: str) -> None:
        self.tagLocation = value
    

    def setPackageLocation(self, value: str) -> None:
        self.packageLocation = value
    

    def setInventoryControl(self, value: str) -> None:
        self.inventoryControl = value
    

    def getPackageLocation_j1(self, value: str) -> None:
        self.packageLocation = value

    def getPackageLocation(self, *args):
        implementation = __class__.__dict__.get("getPackageLocation_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getPackageLocation(*args)
    

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
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.ftpPath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    # throws Exception
    def setTestFtpPath(self, value: str) -> None:
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.testFtpPath = AbPath(value, StringUtil.getInstance().EMPTY_STRING)
    

    # throws Exception
    def createDirectories(self) -> bool:
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        storeAbPath: AbPath = AbPath(URLGLOBALS.getWebappPath() + self.getCurrentHomeHostNamePath(), StringUtil.getInstance().EMPTY_STRING)
        if not (self.directory.create(storeAbPath)):
            return False
        if not (self.directory.create(AbPath(storeAbPath + self.getCategoryPath(), StringUtil.getInstance().EMPTY_STRING))):
            return False
        if not (self.directory.create(AbPath(storeAbPath + self.getStaticPath(), StringUtil.getInstance().EMPTY_STRING))):
            return False
        return True
    

    # throws Exception
    def install(self, current: int, total: int) -> None:
        from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if not (self.createDirectories()):
                raise Exception("Unable to create store directories")
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append(URLGLOBALS.getMainPath())
            stringBuffer.append(FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH)
            viewPath: str = str(stringBuffer)
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append(viewPath)
            stringBuffer.append(FREEBLISKET_PATH_GLOBALS.getInstance().INSTALLPATH)
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
                if not (self.directory.create(toDirectoryAbPath)):
                    raise Exception("Unable to create store view directory: " + str(toDirectoryAbPath))
            viewTotal: int = int((total * 85) / 100)
            installTotal: int = int((total * 93) / 100)
            if current < viewTotal:
                file: AbFile = AbFile.createAbFileFromAbPath(fromSpecialDirectoryAbPath)
                if java_predicate(file, "isDirectory"):
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
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "install()", e)
            raise e
    

    # throws Exception
    def installViews(self, fromDirectoryAbPath: AbPath, toDirectoryAbPath: AbPath, current: int, total: int) -> None:
        from org.allbinary.logic.io.file.FileUtil import FileUtil
        from org.allbinary.logic.io.path.AbPath import AbPath
        FileUtil.getInstance().copyDirectoryPortion(fromDirectoryAbPath, toDirectoryAbPath, True, False, current, total)
    

    # throws Exception
    def installResources(self, fromDirectoryAbPath: AbPath, current: int, total: int) -> None:
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.io.file.FileUtil import FileUtil
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(str(fromDirectoryAbPath))
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        stringBuffer.append("Resources")
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        installCategoryAbPath: AbPath = AbPath(str(stringBuffer), StringUtil.getInstance().EMPTY_STRING)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(URLGLOBALS.getMainPath())
        stringBuffer.append(self.getCurrentHomeHostNamePath())
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        stringBuffer.append(self.getCategoryPath())
        categoryAbPath: AbPath = AbPath(str(stringBuffer), StringUtil.getInstance().EMPTY_STRING)
        FileUtil.getInstance().copyDirectoryPortion(installCategoryAbPath, categoryAbPath, True, False, current, total)
    

    # throws Exception
    def installMedia(self, fromDirectoryAbPath: AbPath, current: int, total: int) -> None:
        from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.io.file.FileUtil import FileUtil
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(str(fromDirectoryAbPath))
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        stringBuffer.append(FREEBLISKET_PATH_GLOBALS.getInstance().TEMPLATEPATH)
        stringBuffer.append("images")
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        viewStoreImagesDirectoryAbPath: AbPath = AbPath(str(stringBuffer), StringUtil.getInstance().EMPTY_STRING)
        storeAbPath: AbPath = AbPath(URLGLOBALS.getWebappPath() + self.getCurrentHomeHostNamePath(), StringUtil.getInstance().EMPTY_STRING)
        FileUtil.getInstance().copyDirectoryPortion(viewStoreImagesDirectoryAbPath, storeAbPath, True, False, current, total)
    

    # throws Exception
    def toVector(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.context.configuration.ContextConfigurationDomDocumentMapping import ContextConfigurationDomDocumentMapping
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
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
    def toHashMap(self) -> HashMap:
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.configuration.ContextConfigurationDomDocumentMapping import ContextConfigurationDomDocumentMapping
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.logic.StdUtil import StdUtil
        storeFrontData: StoreFrontData = StoreFrontData.getInstance()
        dataHashMap: HashMap = StdUtil.getInstance().createHashMap()
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
        from org.allbinary.business.context.configuration.ContextConfigurationInterface import ContextConfigurationInterface
        return self.contextConfigurationInterface
    

    def setContextConfigurationInterface(self, contextConfigurationInterface: ContextConfigurationInterface) -> None:
        from org.allbinary.business.context.configuration.ContextConfigurationInterface import ContextConfigurationInterface
        self.contextConfigurationInterface = contextConfigurationInterface
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from org.allbinary.business.context.configuration.ContextConfiguration import ContextConfiguration
# from org.allbinary.business.context.configuration.ContextConfigurationDomDocumentMapping import ContextConfigurationDomDocumentMapping
# from org.allbinary.business.context.configuration.ContextConfigurationInterface import ContextConfigurationInterface
# from org.allbinary.business.context.configuration.ContextConfigurationInterfaceFactory import ContextConfigurationInterfaceFactory
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.user.UserData import UserData
# from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
# from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.io.file.FileUtil import FileUtil
# from org.allbinary.logic.io.file.directory.Directory import Directory
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.io.path.AbPathData import AbPathData
# from org.allbinary.logic.io.path.AbPathUtil import AbPathUtil
# from org.allbinary.logic.string.SpecialCharacterUtil import SpecialCharacterUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.string.regex.replace.Replace import Replace
# from org.allbinary.logic.string.tokens.Tokenizer import Tokenizer
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.apache.commons.lang3.StringEscapeUtils import StringEscapeUtils
# from org.w3c.dom.Document import Document
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _StoreFront_RESOURCES() -> object:
    from org.allbinary.logic.io.path.AbPathData import AbPathData
    return " Resources" + str(AbPathData.getInstance().SEPARATOR)

lazy_static(StoreFront, "RESOURCES", _StoreFront_RESOURCES)

