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
# package org.allbinary.data.tables.user

from __future__ import annotations

from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.user.UserEntityInterface import UserEntityInterface


class UserEntity(AbSqlBean, UserEntityInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tableName: str = "user"
        self.COMMAND_SUCCESS_FOR_USER: str = "Command Success for user: "
        self.PASSWORD_LABEL: str = " Password: "
        self.EQUALS: str = "=="
        self.COMMAND_SUCCESS_BUT_LOGIN_FAILED: str = "Command Success but login failed for user: "
        self.INVALID_PASSWORD_LABEL: str = " Password: \n\""
        self.NOT_EQUAL: str = "\"!=\""
        self.END_QUOTES: str = CommonSeps.getInstance().QUOTE
    

    def __init__(self) -> None:
        super().__init__(UserDbInitInfo())
        self._init_fields()
        self.setTableName(self.tableName)
    

    def insert(self, values: BasicArrayList) -> None:
        try:
            super().insert(values)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.INSERT)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.INSERT, e)
    

    # throws Exception
    def getAdministrators(self) -> BasicArrayList:
        return self.getUsersWithRole(UserRoleFactory.getInstance().ADMINISTRATOR)
    

    # throws Exception
    def getStoreManagers(self, storeFrontInterface: StoreFrontInterface) -> BasicArrayList:
        keysAndValues: dict = StdUtil.getInstance().createHashMap()
        usersVector: BasicArrayList = BasicArrayListD()
        keysAndValues.put(str(UserRoleData.NAME), str(UserRoleFactory.getInstance().STOREMANAGER))
        keysAndValues.put(UserData.PERMISSIONS, storeFrontInterface.getName())
        usersHashMapVector: BasicArrayList = super().getRows(keysAndValues)
        size: int = usersHashMapVector.size()
        for i in range(0, size):
            userHashMap: dict = usersHashMapVector.get(i)
            if userHashMap is not None:
                usersVector.add(User(userHashMap))
        return usersVector
    

    # throws Exception
    def getCustomers(self) -> BasicArrayList:
        return self.getUsersWithRole(UserRoleFactory.getInstance().CUSTOMER)
    

    # throws Exception
    def getUsersWithRole(self, userRole: UserRole) -> BasicArrayList:
        keysAndValues: dict = StdUtil.getInstance().createHashMap()
        usersVector: BasicArrayList = BasicArrayListD()
        keysAndValues.put(str(UserRoleData.NAME), str(userRole))
        usersHashMapVector: BasicArrayList = super().getRows(keysAndValues)
        size: int = usersHashMapVector.size()
        for index in range(0, size):
            userHashMap: dict = usersHashMapVector.get(index)
            if userHashMap is not None:
                usersVector.add(User(userHashMap))
        return usersVector
    

    # throws Exception
    def getUsers(self, storeFrontInterface: StoreFrontInterface) -> BasicArrayList:
        keysAndValues: dict = StdUtil.getInstance().createHashMap()
        usersVector: BasicArrayList = BasicArrayListD()
        keysAndValues.put(StoreFrontData.getInstance().NAME, storeFrontInterface.getName())
        usersHashMapVector: BasicArrayList = super().getRows(keysAndValues)
        size: int = usersHashMapVector.size()
        for index in range(0, size):
            userHashMap: dict = usersHashMapVector.get(index)
            if userHashMap is not None:
                usersVector.add(User(userHashMap))
        return usersVector
    

    # throws Exception
    def getUser(self, userName: str) -> UserInterface:
        row: dict = StdUtil.getInstance().createHashMap()
        row.put(UserData.USERNAME, userName)
        userHashMap: dict = super().getRow(row)
        if userHashMap is not None:
            return CreateUserFactory.getInstance(userHashMap)
        else:
            return None
    

    def deleteWhere(self, key: str, value: str) -> None:
        try:
            super().deleteWhere(key, value)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "deleteWhere")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "deleteWhere", e)
    

    def login(self, userName: str, password: str) -> str:
        try:
            isUserNameAndPasswordCorrect: int = 0
            result: str = super().getField(UserData.USERNAME, userName, UserData.PASSWORD)
            encryption: str = super().getField(UserData.USERNAME, userName, EntryData.getInstance().ENCRYPTION)
            if encryption is not None and ((encryption > self.stringUtil.EMPTY_STRING) - (encryption < self.stringUtil.EMPTY_STRING)) != 0:
                isUserNameAndPasswordCorrect = ((result > SuperCrypt(int(int(encryption))).encrypt(password)) - (result < SuperCrypt(int(int(encryption))).encrypt(password)))
            else:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF("Command Success but login failed for user: " + userName + " because user did not exist", self, "login")
                return self.GLOBALS2.LOGINFAILED
            if isUserNameAndPasswordCorrect == 0:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append(self.COMMAND_SUCCESS_FOR_USER)
                    stringBuffer.append(userName)
                    stringBuffer.append(self.PASSWORD_LABEL)
                    stringBuffer.append(password)
                    stringBuffer.append(self.EQUALS)
                    stringBuffer.append(result)
                    self.logUtil.putF(str(stringBuffer), self, "login")
                return self.GLOBALS2.LOGINSUCCESS
            else:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append(self.COMMAND_SUCCESS_BUT_LOGIN_FAILED)
                    stringBuffer.append(userName)
                    stringBuffer.append(self.INVALID_PASSWORD_LABEL)
                    stringBuffer.append(SuperCrypt(int(int(encryption))).encrypt(password))
                    stringBuffer.append(self.NOT_EQUAL)
                    stringBuffer.append(result)
                    stringBuffer.append(self.END_QUOTES)
                    self.logUtil.putF(str(stringBuffer), self, "login")
                return self.GLOBALS2.LOGINFAILED
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "login", e)
            return "Error"
    

    def update(self, userName: str, updatedValues: dict) -> None:
        super().updateWhere(UserData.USERNAME, userName, updatedValues)
    

    def dropTables(self) -> str:
        return super().dropTable()
    

    def createTableStatement(self) -> str:
        entryData: EntryData = EntryData.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE).append(self.tableName).append(self.sqlStrings.START).append(UserData.USERNAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(UserData.PREFIXNAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(UserData.FIRSTNAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(UserData.LASTNAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(UserData.MIDDLENAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(UserData.SUFFIXNAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(UserData.COMPANY).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(UserData.POSITIONATCOMPANY).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(UserData.MAINEMAIL).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(UserData.SECONDARYEMAIL).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(UserData.HOMEPHONE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(UserData.CELLPHONE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(UserData.WORKPHONE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(UserData.OTHERCONTACT).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(UserData.ELECTRONICDEVICE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(UserData.FAX).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(str(UserRoleData.NAME)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(UserData.CONFIGURATION).append(self.sqlTypeStrings.BLOB_NOT_NULL).append(UserData.PERMISSIONS).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(entryData.ENCRYPTION).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(UserData.SECRET).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(UserData.PASSWORD).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(entryData.ENABLE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(entryData.TIMECREATED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(entryData.LASTMODIFIED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(UserData.USERNAME).append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return super().createTable(self.createTableStatement())
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
from org.allbinary.business.user.CreateUserFactory import CreateUserFactory
from org.allbinary.business.user.UserData import UserData
from org.allbinary.business.user.UserInterface import UserInterface
from org.allbinary.business.user.modules.User import User
from org.allbinary.business.user.role.UserRole import UserRole
from org.allbinary.business.user.role.UserRoleData import UserRoleData
from org.allbinary.business.user.role.UserRoleFactory import UserRoleFactory
from org.allbinary.globals.GLOBALS2 import GLOBALS2
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.crypt.SuperCrypt import SuperCrypt
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps


