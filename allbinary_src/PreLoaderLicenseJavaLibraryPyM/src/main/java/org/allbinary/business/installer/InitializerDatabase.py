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
# package org.allbinary.business.installer

from __future__ import annotations



class InitializerDatabase:
    MAXDB: int = 30
    MAX: int = 16
    MIN: int = 4
    MINPASSWORD: int = 0

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.adminDbUserName: str = None
        self.adminDbPassword: str = None
        self.adminJdbcDriver: str = None
        self.adminSchema: str = None
        self.adminServer: str = None
        self.adminPort: str = None
        self.initDb: DynamicInitDb = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self.__jconstructor2(*args)

    def __jconstructor2(self, *args) -> None:
        if True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)):
            self._constructor2_1(*args)
        else:
            self._constructor2_2(*args)
    

    def _constructor2_1(self, abeClientInformation: AbeClientInformationInterface, map: Map) -> None:
        from java.util.HashMap import HashMap
        from java.util.Map import Map
        from java.util.Set import Set
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        self._init_fields()
        stringBuffer: StringMaker = StringMaker()
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        keys: Set = map.keySet()
        keyArray: list[object] = keys.toArray()
        size: int = len(keyArray)
        for index in range(0, size):
            key: str = keyArray[index]
            values: list[str] = map.get(key)
            hashMap.put(str(key), str(values[0]))
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append("key: ")
            stringBuffer.append(key)
            stringBuffer.append(" Value: ")
            stringBuffer.append(values[0])
            self.logUtil.putF(str(stringBuffer), self, "getFormData()")
        self.getFormData(abeClientInformation, hashMap)
    

    def _constructor2_2(self, abeClientInformation: AbeClientInformationInterface, initHashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        self._init_fields()
        self.getFormData(abeClientInformation, initHashMap)
    

    def getFormData(self, abeClientInformation: AbeClientInformationInterface, hashMap: HashMap) -> None:
        from org.allbinary.business.installer.InitializerData import InitializerData
        from org.allbinary.business.installer.DynamicInitDb import DynamicInitDb
        from java.util.HashMap import HashMap
        from org.allbinary.business.init.db.DatabaseConnectionInfoInterface import DatabaseConnectionInfoInterface
        from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        try:
            initializerData: InitializerData = InitializerData.getInstance()
            self.setAdminDbUserName(hashMap.get(initializerData.DBUSER))
            self.setAdminDbPassword(hashMap.get(initializerData.DBPASSWORD))
            self.setAdminJdbcDriver(hashMap.get(initializerData.ADMINJDBCDRIVER))
            self.setAdminSchema(hashMap.get(initializerData.ADMINSCHEMA))
            self.setAdminServer(hashMap.get(initializerData.ADMINSERVER))
            self.setAdminPort(hashMap.get(initializerData.ADMINPORT))
            dbConnectionInfo: DbConnectionInfo = DbConnectionInfo()
            adminDbName: str = StringUtil.getInstance().EMPTY_STRING
            dbConnectionInfo.setJdbcDriver(self.getAdminJdbcDriver())
            dbConnectionInfo.setName(adminDbName)
            dbConnectionInfo.setUserName(self.getAdminDbUserName())
            dbConnectionInfo.setPassword(self.getAdminDbPassword())
            dbConnectionInfo.setSchema(self.getAdminSchema())
            dbConnectionInfo.setServer(self.getAdminServer())
            dbConnectionInfo.setPort(self.getAdminPort())
            self.initDb = DynamicInitDb(abeClientInformation, dbConnectionInfo)
        except Exception as e:
            self.logUtil.put("Unable to get form data", self, "getFormData()", e)
    

    def isJdbcDriverValid(self, jdbcDriverClassPathString: str) -> bool:
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            (lambda jname: getattr(__import__(jname, fromlist=["*"]), jname.rsplit(".", 1)[-1]))(jdbcDriverClassPathString).newInstance()
            return True
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.IS_VALID, e)
            return False
    

    def isValid(self) -> bool:
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        isValid: bool = True
        if not self.isJdbcDriverValid(self.adminJdbcDriver):
            isValid = False
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if not stringValidationUtil.isValidRequired(self.adminDbUserName, InitializerDatabase.MIN, InitializerDatabase.MAX):
            isValid = False
        if not stringValidationUtil.isValidNotRequired(self.adminDbPassword, InitializerDatabase.MINPASSWORD, InitializerDatabase.MAX):
            isValid = False
        return isValid
    

    def getJdbcDriverValidationInfo(self, jdbcDriver: str) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("The JDBC driver (")
        stringBuffer.append(jdbcDriver)
        stringBuffer.append(") you have provided is not valid.<br/>")
        return str(stringBuffer)
    

    def getInvalidInfo(self) -> str:
        from org.allbinary.business.installer.InitializerData import InitializerData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        isValid: bool = True
        isJdbcDriversValid: bool = True
        stringBuffer: StringMaker = StringMaker()
        if not self.isJdbcDriverValid(self.adminJdbcDriver):
            isJdbcDriversValid = False
            stringBuffer.append(self.getJdbcDriverValidationInfo(self.getAdminJdbcDriver()))
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if not stringValidationUtil.isValidRequired(self.adminDbUserName, InitializerDatabase.MIN, InitializerDatabase.MAX):
            stringBuffer.append("Admin username should be < " + str(InitializerDatabase.MAX) + " and > " + str(InitializerDatabase.MIN) + " characters in length.<br />")
        if not stringValidationUtil.isValidNotRequired(self.adminDbPassword, InitializerDatabase.MINPASSWORD, InitializerDatabase.MAX):
            stringBuffer.append("Admin password should be < " + str(InitializerDatabase.MAX) + " and > " + str(InitializerDatabase.MINPASSWORD) + " characters in length.<br />")
        if not isJdbcDriversValid:
            stringBuffer.append(InitializerData.getInstance().getJdbcDriverSolutionInfo())
        return str(stringBuffer)
    

    def createUsers(self) -> bool:
        try:
            self.initDb.addUsers()
            return True
        except Exception as e:
            self.logUtil.put("Unable to Create Users", self, "createUsers()", e)
            return False
    

    def createDatabases(self) -> bool:
        try:
            self.initDb.addDatabases()
            return True
        except Exception as e:
            self.logUtil.put("Unable to Create Databases", self, "createDatabases()", e)
            return False
    

    def createTables(self) -> bool:
        try:
            self.initDb.addTables()
            return True
        except Exception as e:
            self.logUtil.put("Unable to Create Tables", self, "createTables()", e)
            return False
    

    def getAdminDbUserName(self) -> str:
        return self.adminDbUserName
    

    def setAdminDbUserName(self, adminDbUserName: str) -> None:
        self.adminDbUserName = adminDbUserName
    

    def getAdminDbPassword(self) -> str:
        return self.adminDbPassword
    

    def setAdminDbPassword(self, adminDbPassword: str) -> None:
        self.adminDbPassword = adminDbPassword
    

    def getAdminJdbcDriver(self) -> str:
        return self.adminJdbcDriver
    

    def setAdminJdbcDriver(self, adminJdbcDriver: str) -> None:
        self.adminJdbcDriver = adminJdbcDriver
    

    def getAdminSchema(self) -> str:
        return self.adminSchema
    

    def setAdminSchema(self, adminSchema: str) -> None:
        self.adminSchema = adminSchema
    

    def getAdminServer(self) -> str:
        return self.adminServer
    

    def setAdminServer(self, adminServer: str) -> None:
        self.adminServer = adminServer
    

    def getAdminPort(self) -> str:
        return self.adminPort
    

    def setAdminPort(self, adminPort: str) -> None:
        self.adminPort = adminPort
# from java.util.HashMap import HashMap
# from java.util.Map import Map
# from java.util.Set import Set
# from org.allbinary.business.init.db.DatabaseConnectionInfoInterface import DatabaseConnectionInfoInterface
# from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


