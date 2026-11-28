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
# package org.allbinary.data.tables.user.address

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import datetime
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.user.address.StreetAddressesEntityInterface import StreetAddressesEntityInterface


@java_inherited_overloads
class StreetAddressesEntity(*java_bases(AbSqlBean, StreetAddressesEntityInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("userName", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "userName" not in vars(self): self.userName: str = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 1:
            __class__._constructor1(self, *args)
    

    def _constructor0(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
        super().__init__(UserDbInitInfo())
        __class__._init_fields(self)
    

    def _constructor1(self, userName: str) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
        super().__init__(UserDbInitInfo())
        __class__._init_fields(self)
        self.userName = userName
    

    def remove(self, index: int) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            whereHashMap: HashMap = StdUtil.getInstance().createHashMap()
            whereHashMap.put(UserData.USERNAME, self.userName)
            whereHashMap.put(StreetAddressData.ID, str(index))
            java_super_call(super(), "deleteWhere", whereHashMap)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "remove")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "remove", e)
    

    def add_j1(self, address: StreetAddress) -> None:
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        from org.allbinary.data.tables.TableDataFactory import TableDataFactory
        self.add(address, TableDataFactory.getInstance().INTEGER_MAX_VALUE_STRING)
    

    def add_j2(self, address: StreetAddress, index: str) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            values: BasicArrayList = BasicArrayListD()
            values.add(index)
            values.add(self.userName)
            values.add(StringUtil.getInstance().EMPTY_STRING)
            values.add(address.getName())
            values.add(address.getStreet())
            values.add(address.getCity())
            values.add(address.getState())
            values.add(address.getCode())
            values.add(address.getCountry())
            calendar: datetime.datetime = datetime.datetime.now()
            time: str = str(str(int(calendar.getTimeInMillis())))
            values.add(time)
            java_super_call(super(), "insert", values)
            self.setDefault(self.getLastId())
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "add")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "add", e)

    def add(self, *args):
        implementation = __class__.__dict__.get("add_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().add(*args)
    

    def update(self, address: StreetAddress) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            addressHashMap: HashMap = address.toHashMap()
            whereKeyValuePairs: HashMap = StdUtil.getInstance().createHashMap()
            whereKeyValuePairs.put(StreetAddressData.ID, address.getId())
            whereKeyValuePairs.put(UserData.USERNAME, self.userName)
            java_super_call(super(), "updateWhere", whereKeyValuePairs, addressHashMap)
            self.setDefault(address.getId())
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "update")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "add", e)
    

    def getLastId(self) -> str:
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        return java_super_call(super(), "getLargestIntegerInColumnWhere", StreetAddressData.ID, UserData.USERNAME, self.userName)
    

    def get_j0(self) -> BasicArrayList:
        from java.util.HashMap import HashMap
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            streetAddressVector: BasicArrayList = BasicArrayListD()
            keyAndValue: HashMap = StdUtil.getInstance().createHashMap()
            keyAndValue.put(UserData.USERNAME, self.userName)
            addressList: BasicArrayList = java_super_call(super(), "getRows", keyAndValue)
            size: int = addressList.size()
            for index in range(0, size):
                addressHashMap: HashMap = addressList.get(index)
                streetAddress: StreetAddress = StreetAddress(addressHashMap)
                if streetAddress is not None:
                    streetAddressVector.add(streetAddress)
            return streetAddressVector
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.GET, e)
            return None
    

    def get_j1(self, index: int) -> StreetAddress:
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            keyAndValue: HashMap = StdUtil.getInstance().createHashMap()
            keyAndValue.put(UserData.USERNAME, self.userName)
            keyAndValue.put(StreetAddressData.ID, str(index))
            addressHashMap: HashMap = java_super_call(super(), "getRow", keyAndValue)
            if addressHashMap is not None:
                return StreetAddress(addressHashMap)
            else:
                return None
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.GET, e)
            return None

    def get(self, *args):
        implementation = __class__.__dict__.get("get_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().get(*args)
    

    def getDefault(self) -> StreetAddress:
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            addressHashMap: HashMap = StdUtil.getInstance().createHashMap()
            updateKeyAndValue: HashMap = StdUtil.getInstance().createHashMap()
            updateKeyAndValue.put(StreetAddressData.DEFAULT, StreetAddressData.DEFAULT)
            updateKeyAndValue.put(UserData.USERNAME, self.userName)
            addressHashMap = java_super_call(super(), "getRow", updateKeyAndValue)
            if addressHashMap is not None:
                streetAddress: StreetAddress = StreetAddress(addressHashMap)
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF(self.commonStrings.SUCCESS, self, "getDefault")
                return streetAddress
            else:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF("No Default Address Found", self, "getDefault")
                return None
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "getDefault", e)
            return None
    

    def setDefault(self, value: str) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            updateKeyAndValue: HashMap = StdUtil.getInstance().createHashMap()
            whereKeyAndValue: HashMap = StdUtil.getInstance().createHashMap()
            whereKeyAndValue.put(UserData.USERNAME, self.userName)
            streetAddress: StreetAddress = self.getDefault()
            if streetAddress is not None:
                updateKeyAndValue.put(StreetAddressData.DEFAULT, StringUtil.getInstance().EMPTY_STRING)
                whereKeyAndValue.put(StreetAddressData.ID, streetAddress.getId())
                java_super_call(super(), "updateWhere", whereKeyAndValue, updateKeyAndValue)
            whereKeyAndValue.put(StreetAddressData.ID, value)
            updateKeyAndValue.put(StreetAddressData.DEFAULT, StreetAddressData.DEFAULT)
            java_super_call(super(), "updateWhere", whereKeyAndValue, updateKeyAndValue)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "setDefault")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "setShippingAddress", e)
    

    def getUserName(self) -> str:
        return self.userName
    

    def createTableStatement(self) -> str:
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE).append(self.getTableName()).append(self.sqlStrings.START).append(StreetAddressData.ID).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_AUTO_INCREMENT_NOT_NULL).append(UserData.USERNAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(StreetAddressData.DEFAULT).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(StreetAddressData.NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(StreetAddressData.STREET).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(StreetAddressData.CITY).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(StreetAddressData.STATE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(StreetAddressData.CODE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(StreetAddressData.COUNTRY).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(EntryData.getInstance().TIMECREATED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(StreetAddressData.ID).append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return java_super_call(super(), "createTable", self.createTableStatement())
    

    def drop(self) -> str:
        return java_super_call(super(), "dropTable")
    

    def dropTable(self) -> str:
        return java_super_call(super(), "dropTable")
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
# from org.allbinary.business.user.UserData import UserData
# from org.allbinary.business.user.address.StreetAddress import StreetAddress
# from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
# from org.allbinary.data.tables.TableDataFactory import TableDataFactory
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


