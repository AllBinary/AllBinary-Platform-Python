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

import datetime
from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.user.address.StreetAddressesEntityInterface import StreetAddressesEntityInterface


class StreetAddressesEntity(AbSqlBean, StreetAddressesEntityInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.userName: str = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        super().__init__(UserDbInitInfo())
        self._init_fields()
    

    def _constructor1(self, userName: str) -> None:
        super().__init__(UserDbInitInfo())
        self._init_fields()
        self.userName = userName
    

    def remove(self, index: int) -> None:
        try:
            whereHashMap: dict = StdUtil.getInstance().createHashMap()
            whereHashMap.put(UserData.USERNAME, self.userName)
            whereHashMap.put(StreetAddressData.ID, str(index))
            super().deleteWhere(whereHashMap)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "remove")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "remove", e)
    

    def add(self, address: StreetAddress) -> None:
        self.add(address, TableDataFactory.getInstance().INTEGER_MAX_VALUE_STRING)
    

    # Java overloaded method: Python keeps the last definition
    def add(self, address: StreetAddress, index: str) -> None:
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
            super().insert(values)
            self.setDefault(self.getLastId())
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "add")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "add", e)
    

    def update(self, address: StreetAddress) -> None:
        try:
            addressHashMap: dict = address.toHashMap()
            whereKeyValuePairs: dict = StdUtil.getInstance().createHashMap()
            whereKeyValuePairs.put(StreetAddressData.ID, address.getId())
            whereKeyValuePairs.put(UserData.USERNAME, self.userName)
            super().updateWhere(whereKeyValuePairs, addressHashMap)
            self.setDefault(address.getId())
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "update")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "add", e)
    

    def getLastId(self) -> str:
        return super().getLargestIntegerInColumnWhere(StreetAddressData.ID, UserData.USERNAME, self.userName)
    

    def get(self) -> BasicArrayList:
        try:
            streetAddressVector: BasicArrayList = BasicArrayListD()
            keyAndValue: dict = StdUtil.getInstance().createHashMap()
            keyAndValue.put(UserData.USERNAME, self.userName)
            addressList: BasicArrayList = super().getRows(keyAndValue)
            size: int = addressList.size()
            for index in range(0, size):
                addressHashMap: dict = addressList.get(index)
                streetAddress: StreetAddress = StreetAddress(addressHashMap)
                if streetAddress is not None:
                    streetAddressVector.add(streetAddress)
            return streetAddressVector
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.GET, e)
            return None
    

    # Java overloaded method: Python keeps the last definition
    def get(self, index: int) -> StreetAddress:
        try:
            keyAndValue: dict = StdUtil.getInstance().createHashMap()
            keyAndValue.put(UserData.USERNAME, self.userName)
            keyAndValue.put(StreetAddressData.ID, str(index))
            addressHashMap: dict = super().getRow(keyAndValue)
            if addressHashMap is not None:
                return StreetAddress(addressHashMap)
            else:
                return None
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.GET, e)
            return None
    

    def getDefault(self) -> StreetAddress:
        try:
            addressHashMap: dict = StdUtil.getInstance().createHashMap()
            updateKeyAndValue: dict = StdUtil.getInstance().createHashMap()
            updateKeyAndValue.put(StreetAddressData.DEFAULT, StreetAddressData.DEFAULT)
            updateKeyAndValue.put(UserData.USERNAME, self.userName)
            addressHashMap = super().getRow(updateKeyAndValue)
            if addressHashMap is not None:
                streetAddress: StreetAddress = StreetAddress(addressHashMap)
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF(self.commonStrings.SUCCESS, self, "getDefault")
                return streetAddress
            else:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF("No Default Address Found", self, "getDefault")
                return None
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "getDefault", e)
            return None
    

    def setDefault(self, value: str) -> None:
        try:
            updateKeyAndValue: dict = StdUtil.getInstance().createHashMap()
            whereKeyAndValue: dict = StdUtil.getInstance().createHashMap()
            whereKeyAndValue.put(UserData.USERNAME, self.userName)
            streetAddress: StreetAddress = self.getDefault()
            if streetAddress is not None:
                updateKeyAndValue.put(StreetAddressData.DEFAULT, StringUtil.getInstance().EMPTY_STRING)
                whereKeyAndValue.put(StreetAddressData.ID, streetAddress.getId())
                super().updateWhere(whereKeyAndValue, updateKeyAndValue)
            whereKeyAndValue.put(StreetAddressData.ID, value)
            updateKeyAndValue.put(StreetAddressData.DEFAULT, StreetAddressData.DEFAULT)
            super().updateWhere(whereKeyAndValue, updateKeyAndValue)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "setDefault")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "setShippingAddress", e)
    

    def getUserName(self) -> str:
        return self.userName
    

    def createTableStatement(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE).append(self.getTableName()).append(self.sqlStrings.START).append(StreetAddressData.ID).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_AUTO_INCREMENT_NOT_NULL).append(UserData.USERNAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(StreetAddressData.DEFAULT).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(StreetAddressData.NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(StreetAddressData.STREET).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(StreetAddressData.CITY).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(StreetAddressData.STATE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(StreetAddressData.CODE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(StreetAddressData.COUNTRY).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(EntryData.getInstance().TIMECREATED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(StreetAddressData.ID).append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return super().createTable(self.createTableStatement())
    

    def drop(self) -> str:
        return super().dropTable()
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
from org.allbinary.business.user.UserData import UserData
from org.allbinary.business.user.address.StreetAddress import StreetAddress
from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
from org.allbinary.data.tables.TableDataFactory import TableDataFactory
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil


