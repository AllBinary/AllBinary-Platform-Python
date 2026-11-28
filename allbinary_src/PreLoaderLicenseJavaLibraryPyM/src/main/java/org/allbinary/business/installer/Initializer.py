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



class Initializer:
    MAXDB: int = 30
    MAX: int = 16
    MIN: int = 4
    MINPASSWORD: int = 0

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "userJdbcDriver" not in vars(self): self.userJdbcDriver: str = None
        if "userName" not in vars(self): self.userName: str = None
        if "userUserName" not in vars(self): self.userUserName: str = None
        if "userPassword" not in vars(self): self.userPassword: str = None
        if "userSchema" not in vars(self): self.userSchema: str = None
        if "userServer" not in vars(self): self.userServer: str = None
        if "userPort" not in vars(self): self.userPort: str = None
        if "historyJdbcDriver" not in vars(self): self.historyJdbcDriver: str = None
        if "historyName" not in vars(self): self.historyName: str = None
        if "historyUserName" not in vars(self): self.historyUserName: str = None
        if "historyPassword" not in vars(self): self.historyPassword: str = None
        if "historySchema" not in vars(self): self.historySchema: str = None
        if "historyServer" not in vars(self): self.historyServer: str = None
        if "historyPort" not in vars(self): self.historyPort: str = None
        if "logJdbcDriver" not in vars(self): self.logJdbcDriver: str = None
        if "logName" not in vars(self): self.logName: str = None
        if "logUserName" not in vars(self): self.logUserName: str = None
        if "logPassword" not in vars(self): self.logPassword: str = None
        if "logSchema" not in vars(self): self.logSchema: str = None
        if "logServer" not in vars(self): self.logServer: str = None
        if "logPort" not in vars(self): self.logPort: str = None
        if "inventoryJdbcDriver" not in vars(self): self.inventoryJdbcDriver: str = None
        if "inventoryName" not in vars(self): self.inventoryName: str = None
        if "inventoryUserName" not in vars(self): self.inventoryUserName: str = None
        if "inventoryPassword" not in vars(self): self.inventoryPassword: str = None
        if "inventorySchema" not in vars(self): self.inventorySchema: str = None
        if "inventoryServer" not in vars(self): self.inventoryServer: str = None
        if "inventoryPort" not in vars(self): self.inventoryPort: str = None
        if "staticPagesJdbcDriver" not in vars(self): self.staticPagesJdbcDriver: str = None
        if "staticPagesName" not in vars(self): self.staticPagesName: str = None
        if "staticPagesUserName" not in vars(self): self.staticPagesUserName: str = None
        if "staticPagesPassword" not in vars(self): self.staticPagesPassword: str = None
        if "staticPagesSchema" not in vars(self): self.staticPagesSchema: str = None
        if "staticPagesServer" not in vars(self): self.staticPagesServer: str = None
        if "staticPagesPort" not in vars(self): self.staticPagesPort: str = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__.__jconstructor1(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "Map" for base in type(args[0]).__mro__)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)
    

    def _constructor1_1(self, map: Map) -> None:
        from java.util.HashMap import HashMap
        from java.util.Map import Map
        from java.util.Set import Set
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        __class__._init_fields(self)
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
        self.getFormData(hashMap)
    

    def _constructor1_2(self, initHashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        __class__._init_fields(self)
        self.getFormData(initHashMap)
    

    def getFormData(self, hashMap: HashMap) -> None:
        from org.allbinary.business.installer.InitializerData import InitializerData
        from java.util.HashMap import HashMap
        try:
            initializerData: InitializerData = InitializerData.getInstance()
            self.userJdbcDriver = hashMap.get(initializerData.CUSTOMERJDBCDRIVER)
            self.userName = hashMap.get(initializerData.CUSTOMERNAME)
            self.userUserName = hashMap.get(initializerData.CUSTOMERUSERNAME)
            self.userPassword = hashMap.get(initializerData.CUSTOMERPASSWORD)
            self.userSchema = hashMap.get(initializerData.CUSTOMERSCHEMA)
            self.userServer = hashMap.get(initializerData.CUSTOMERSERVER)
            self.userPort = hashMap.get(initializerData.CUSTOMERPORT)
            self.historyJdbcDriver = hashMap.get(initializerData.HISTORYJDBCDRIVER)
            self.historyName = hashMap.get(initializerData.HISTORYNAME)
            self.historyUserName = hashMap.get(initializerData.HISTORYUSERNAME)
            self.historyPassword = hashMap.get(initializerData.HISTORYPASSWORD)
            self.historySchema = hashMap.get(initializerData.HISTORYSCHEMA)
            self.historyServer = hashMap.get(initializerData.HISTORYSERVER)
            self.historyPort = hashMap.get(initializerData.HISTORYPORT)
            self.logJdbcDriver = hashMap.get(initializerData.LOGJDBCDRIVER)
            self.logName = hashMap.get(initializerData.LOGNAME)
            self.logUserName = hashMap.get(initializerData.LOGUSERNAME)
            self.logPassword = hashMap.get(initializerData.LOGPASSWORD)
            self.logSchema = hashMap.get(initializerData.LOGSCHEMA)
            self.logServer = hashMap.get(initializerData.LOGSERVER)
            self.logPort = hashMap.get(initializerData.LOGPORT)
            self.inventoryJdbcDriver = hashMap.get(initializerData.INVENTORYJDBCDRIVER)
            self.inventoryName = hashMap.get(initializerData.INVENTORYNAME)
            self.inventoryUserName = hashMap.get(initializerData.INVENTORYUSERNAME)
            self.inventoryPassword = hashMap.get(initializerData.INVENTORYPASSWORD)
            self.inventorySchema = hashMap.get(initializerData.INVENTORYSCHEMA)
            self.inventoryServer = hashMap.get(initializerData.INVENTORYSERVER)
            self.inventoryPort = hashMap.get(initializerData.INVENTORYPORT)
            self.staticPagesJdbcDriver = hashMap.get(initializerData.STATICPAGESJDBCDRIVER)
            self.staticPagesName = hashMap.get(initializerData.STATICPAGESNAME)
            self.staticPagesUserName = hashMap.get(initializerData.STATICPAGESUSERNAME)
            self.staticPagesPassword = hashMap.get(initializerData.STATICPAGESPASSWORD)
            self.staticPagesSchema = hashMap.get(initializerData.STATICPAGESSCHEMA)
            self.staticPagesServer = hashMap.get(initializerData.STATICPAGESSERVER)
            self.staticPagesPort = hashMap.get(initializerData.STATICPAGESPORT)
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
        if not (self.isJdbcDriverValid(self.userJdbcDriver)):
            isValid = False
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if not (stringValidationUtil.isValidRequired(self.userName, Initializer.MIN, Initializer.MAXDB)):
            isValid = False
        if not (stringValidationUtil.isValidRequired(self.userUserName, Initializer.MIN, Initializer.MAX)):
            isValid = False
        if not (stringValidationUtil.isValidNotRequired(self.userPassword, Initializer.MINPASSWORD, Initializer.MAX)):
            isValid = False
        if not (self.isJdbcDriverValid(self.historyJdbcDriver)):
            isValid = False
        if not (stringValidationUtil.isValidRequired(self.historyName, Initializer.MIN, Initializer.MAXDB)):
            isValid = False
        if not (stringValidationUtil.isValidRequired(self.historyUserName, Initializer.MIN, Initializer.MAX)):
            isValid = False
        if not (stringValidationUtil.isValidNotRequired(self.historyPassword, Initializer.MINPASSWORD, Initializer.MAX)):
            isValid = False
        if not (self.isJdbcDriverValid(self.logJdbcDriver)):
            isValid = False
        if not (stringValidationUtil.isValidRequired(self.logName, Initializer.MIN, Initializer.MAXDB)):
            isValid = False
        if not (stringValidationUtil.isValidRequired(self.logUserName, Initializer.MIN, Initializer.MAX)):
            isValid = False
        if not (stringValidationUtil.isValidNotRequired(self.logPassword, Initializer.MINPASSWORD, Initializer.MAX)):
            isValid = False
        if not (self.isJdbcDriverValid(self.inventoryJdbcDriver)):
            isValid = False
        if not (stringValidationUtil.isValidRequired(self.inventoryName, Initializer.MIN, Initializer.MAXDB)):
            isValid = False
        if not (stringValidationUtil.isValidRequired(self.inventoryUserName, Initializer.MIN, Initializer.MAX)):
            isValid = False
        if not (stringValidationUtil.isValidNotRequired(self.inventoryPassword, Initializer.MINPASSWORD, Initializer.MAX)):
            isValid = False
        if not (self.isJdbcDriverValid(self.staticPagesJdbcDriver)):
            isValid = False
        if not (stringValidationUtil.isValidRequired(self.staticPagesName, Initializer.MIN, Initializer.MAXDB)):
            isValid = False
        if not (stringValidationUtil.isValidRequired(self.staticPagesUserName, Initializer.MIN, Initializer.MAX)):
            isValid = False
        if not (stringValidationUtil.isValidNotRequired(self.staticPagesPassword, Initializer.MINPASSWORD, Initializer.MAX)):
            isValid = False
        return isValid
    

    def getJdbcDriverValidationInfo(self, jdbcDriver: str) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("The JDBC driver (")
        stringBuffer.append(jdbcDriver)
        stringBuffer.append(") you have provided is not valid.<br/>")
        return str(stringBuffer)
    

    def getJdbcDriverSolutionInfo(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("The following describes the possible problems and solutions regarding the Jdbc Driver error(s):<p/>")
        stringBuffer.append("1. A JDBC driver you specified is not in your classpath.<br/>")
        stringBuffer.append("Solution 1: Move the JDBC driver into any directory specified in the existing classpath. <br/>")
        stringBuffer.append("Solution 2: Add the directory that contains the JDBC driver to the classpath.<br/>")
        stringBuffer.append("Solution 3: Add the JDBC driver to the WEB-INF/lib directory where you installed this webapp.<br/>")
        stringBuffer.append("2. The JDBC driver you specified does not exit.<br/>")
        stringBuffer.append("Solution: Get a JDBC driver. <br/>")
        stringBuffer.append("3. The JDBC driver you specified is not valid.<br/>")
        stringBuffer.append("Solution: Use a valid JDBC driver.<p/>")
        return str(stringBuffer)
    

    def getInvalidInfo(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        isJdbcDriversValid: bool = True
        stringBuffer: StringMaker = StringMaker()
        if not (self.isJdbcDriverValid(self.userJdbcDriver)):
            isJdbcDriversValid = False
            stringBuffer.append(self.getJdbcDriverValidationInfo(self.userJdbcDriver))
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if not (stringValidationUtil.isValidRequired(self.userName, Initializer.MIN, Initializer.MAXDB)):
            stringBuffer.append("User db name should be < " + str(Initializer.MAXDB) + " and > " + str(Initializer.MIN) + " characters in length.<br />")
        if not (stringValidationUtil.isValidRequired(self.userUserName, Initializer.MIN, Initializer.MAX)):
            stringBuffer.append("User db username should be < " + str(Initializer.MAX) + " and > " + str(Initializer.MIN) + " characters in length.<br />")
        if not (stringValidationUtil.isValidNotRequired(self.userPassword, Initializer.MINPASSWORD, Initializer.MAX)):
            stringBuffer.append("User DB password should be < " + str(Initializer.MAX) + " and > " + str(Initializer.MINPASSWORD) + " characters in length.<br />")
        if not (self.isJdbcDriverValid(self.historyJdbcDriver)):
            isJdbcDriversValid = False
            stringBuffer.append(self.getJdbcDriverValidationInfo(self.historyJdbcDriver))
        if not (stringValidationUtil.isValidRequired(self.historyName, Initializer.MIN, Initializer.MAXDB)):
            stringBuffer.append("History db should be < " + str(Initializer.MAXDB) + " and > " + str(Initializer.MIN) + " characters in length.<br />")
        if not (stringValidationUtil.isValidRequired(self.historyUserName, Initializer.MIN, Initializer.MAX)):
            stringBuffer.append("History db username should be < " + str(Initializer.MAX) + " and > " + str(Initializer.MIN) + " characters in length.<br />")
        if not (stringValidationUtil.isValidNotRequired(self.historyPassword, Initializer.MINPASSWORD, Initializer.MAX)):
            stringBuffer.append("History db password should be < " + str(Initializer.MAX) + " and > " + str(Initializer.MINPASSWORD) + " characters in length.<br />")
        if not (self.isJdbcDriverValid(self.logJdbcDriver)):
            isJdbcDriversValid = False
            stringBuffer.append(self.getJdbcDriverValidationInfo(self.logJdbcDriver))
        if not (stringValidationUtil.isValidRequired(self.logName, Initializer.MIN, Initializer.MAXDB)):
            stringBuffer.append("Log db should be < " + str(Initializer.MAXDB) + " and > " + str(Initializer.MIN) + " characters in length.<br />")
        if not (stringValidationUtil.isValidRequired(self.logUserName, Initializer.MIN, Initializer.MAX)):
            stringBuffer.append("Log db username should be < " + str(Initializer.MAX) + " and > " + str(Initializer.MIN) + " characters in length.<br />")
        if not (stringValidationUtil.isValidNotRequired(self.logPassword, Initializer.MINPASSWORD, Initializer.MAX)):
            stringBuffer.append("Log db password should be < " + str(Initializer.MAX) + " and > " + str(Initializer.MINPASSWORD) + " characters in length.<br />")
        if not (self.isJdbcDriverValid(self.inventoryJdbcDriver)):
            isJdbcDriversValid = False
            stringBuffer.append(self.getJdbcDriverValidationInfo(self.inventoryJdbcDriver))
        if not (stringValidationUtil.isValidRequired(self.inventoryName, Initializer.MIN, Initializer.MAXDB)):
            stringBuffer.append("Inventory db should be < " + str(Initializer.MAXDB) + " and > " + str(Initializer.MIN) + " characters in length.<br />")
        if not (stringValidationUtil.isValidRequired(self.inventoryUserName, Initializer.MIN, Initializer.MAX)):
            stringBuffer.append("Inventory db username should be < " + str(Initializer.MAX) + " and > " + str(Initializer.MIN) + " characters in length.<br />")
        if not (stringValidationUtil.isValidNotRequired(self.inventoryPassword, Initializer.MINPASSWORD, Initializer.MAX)):
            stringBuffer.append("Inventory DB password should be < " + str(Initializer.MAX) + " and > " + str(Initializer.MINPASSWORD) + " characters in length.<br />")
        if not (self.isJdbcDriverValid(self.staticPagesJdbcDriver)):
            isJdbcDriversValid = False
            stringBuffer.append(self.getJdbcDriverValidationInfo(self.staticPagesJdbcDriver))
        if not (stringValidationUtil.isValidRequired(self.staticPagesName, Initializer.MIN, Initializer.MAXDB)):
            stringBuffer.append("Static Pages db should be < " + str(Initializer.MAXDB) + " and > " + str(Initializer.MIN) + " characters in length.<br />")
        if not (stringValidationUtil.isValidRequired(self.staticPagesUserName, Initializer.MIN, Initializer.MAX)):
            stringBuffer.append("Static Pages db username should be < " + str(Initializer.MAX) + " and > " + str(Initializer.MIN) + " characters in length.<br />")
        if not (stringValidationUtil.isValidNotRequired(self.staticPagesPassword, Initializer.MINPASSWORD, Initializer.MAX)):
            stringBuffer.append("Static Pages DB password should be < " + str(Initializer.MAX) + " and > " + str(Initializer.MINPASSWORD) + " characters in length.<br />")
        if not (isJdbcDriversValid):
            stringBuffer.append(self.getJdbcDriverSolutionInfo())
        return str(stringBuffer)
    

    # throws Exception
    def set(self) -> None:
        from org.allbinary.business.init.db.HistoryDbInitInfo import HistoryDbInitInfo
        from org.allbinary.business.init.db.InventoryDbInitInfo import InventoryDbInitInfo
        from org.allbinary.business.init.db.LogDbInitInfo import LogDbInitInfo
        from org.allbinary.business.init.db.StaticPagesDbInitInfo import StaticPagesDbInitInfo
        from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
        self.logUtil.putF("Creating DB connection files", self, "set()")
        userDbInitInfo: UserDbInitInfo = UserDbInitInfo(False)
        userDbInitInfo.setJdbcDriver(self.userJdbcDriver)
        userDbInitInfo.setName(self.userName)
        userDbInitInfo.setUserName(self.userUserName)
        userDbInitInfo.setPassword(self.userPassword)
        userDbInitInfo.setSchema(self.userSchema)
        userDbInitInfo.setServer(self.userServer)
        userDbInitInfo.setPort(self.userPort)
        userDbInitInfo.setHasRead(True)
        userDbInitInfo.write()
        historyDbInitInfo: HistoryDbInitInfo = HistoryDbInitInfo(False)
        historyDbInitInfo.setJdbcDriver(self.historyJdbcDriver)
        historyDbInitInfo.setName(self.historyName)
        historyDbInitInfo.setUserName(self.historyUserName)
        historyDbInitInfo.setPassword(self.historyPassword)
        historyDbInitInfo.setSchema(self.historySchema)
        historyDbInitInfo.setServer(self.historyServer)
        historyDbInitInfo.setPort(self.historyPort)
        historyDbInitInfo.setHasRead(True)
        historyDbInitInfo.write()
        logDbInitInfo: LogDbInitInfo = LogDbInitInfo(False)
        logDbInitInfo.setJdbcDriver(self.logJdbcDriver)
        logDbInitInfo.setName(self.logName)
        logDbInitInfo.setUserName(self.logUserName)
        logDbInitInfo.setPassword(self.logPassword)
        logDbInitInfo.setSchema(self.logSchema)
        logDbInitInfo.setServer(self.logServer)
        logDbInitInfo.setPort(self.logPort)
        logDbInitInfo.setHasRead(True)
        logDbInitInfo.write()
        staticPagesDbInitInfo: StaticPagesDbInitInfo = StaticPagesDbInitInfo(False)
        staticPagesDbInitInfo.setJdbcDriver(self.staticPagesJdbcDriver)
        staticPagesDbInitInfo.setName(self.staticPagesName)
        staticPagesDbInitInfo.setUserName(self.staticPagesUserName)
        staticPagesDbInitInfo.setPassword(self.staticPagesPassword)
        staticPagesDbInitInfo.setSchema(self.staticPagesSchema)
        staticPagesDbInitInfo.setServer(self.staticPagesServer)
        staticPagesDbInitInfo.setPort(self.staticPagesPort)
        staticPagesDbInitInfo.setHasRead(True)
        staticPagesDbInitInfo.write()
        inventoryDbInitInfo: InventoryDbInitInfo = InventoryDbInitInfo(False)
        inventoryDbInitInfo.setJdbcDriver(self.inventoryJdbcDriver)
        inventoryDbInitInfo.setName(self.inventoryName)
        inventoryDbInitInfo.setUserName(self.inventoryUserName)
        inventoryDbInitInfo.setPassword(self.inventoryPassword)
        inventoryDbInitInfo.setSchema(self.inventorySchema)
        inventoryDbInitInfo.setServer(self.inventoryServer)
        inventoryDbInitInfo.setPort(self.inventoryPort)
        inventoryDbInitInfo.setHasRead(True)
        inventoryDbInitInfo.write()
        self.logUtil.putF("Created DB connection files", self, "set()")
# from java.util.HashMap import HashMap
# from java.util.Map import Map
# from java.util.Set import Set
# from org.allbinary.business.init.db.HistoryDbInitInfo import HistoryDbInitInfo
# from org.allbinary.business.init.db.InventoryDbInitInfo import InventoryDbInitInfo
# from org.allbinary.business.init.db.LogDbInitInfo import LogDbInitInfo
# from org.allbinary.business.init.db.StaticPagesDbInitInfo import StaticPagesDbInitInfo
# from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


