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
# package org.allbinary.data.tables.user.commerce.money.payment

from __future__ import annotations

import random
import datetime
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.user.commerce.money.payment.PaymentEntityInterface import PaymentEntityInterface


class PaymentEntity(*java_bases(AbSqlBean, PaymentEntityInterface)):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tableName: str = "payment"
    

    def __init__(self) -> None:
        from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
        super().__init__(UserDbInitInfo())
        self._init_fields()
        self.setTableName(self.tableName)
    

    def getLastId(self, userName: str) -> str:
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        return super().getLargestIntegerInColumnWhere(PaymentData.ID, UserData.USERNAME, userName)
    

    def setDefault(self, userName: str, index: int) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentInterface import PaymentInterface
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            updateKeyAndValue: HashMap = StdUtil.getInstance().createHashMap()
            whereKeyAndValue: HashMap = StdUtil.getInstance().createHashMap()
            whereKeyAndValue.put(UserData.USERNAME, userName)
            paymentInterface: PaymentInterface = self.getDefault(userName)
            if paymentInterface is not None:
                updateKeyAndValue.put(EntryData.getInstance().DEFAULT, StringUtil.getInstance().EMPTY_STRING)
                whereKeyAndValue.put(PaymentData.ID, paymentInterface.getId())
                super().updateWhere(whereKeyAndValue, updateKeyAndValue)
            updateKeyAndValue.put(EntryData.getInstance().DEFAULT, EntryData.getInstance().DEFAULT)
            whereKeyAndValue.put(PaymentData.ID, str(index))
            super().updateWhere(whereKeyAndValue, updateKeyAndValue)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "setDefault")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "setDefault", e)
    

    def get(self, userName: str) -> BasicArrayList:
        from java.util.HashMap import HashMap
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.commerce.money.payment.Payment import Payment
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            paymentVector: BasicArrayList = BasicArrayListD()
            keyAndValue: HashMap = StdUtil.getInstance().createHashMap()
            keyAndValue.put(UserData.USERNAME, userName)
            paymentList: BasicArrayList = super().getRows(keyAndValue)
            size: int = paymentList.size()
            for index in range(0, size):
                paymentHashMap: HashMap = paymentList.get(index)
                payment: Payment = Payment(paymentHashMap)
                if payment is not None:
                    paymentVector.add(payment)
            return paymentVector
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.GET, e)
            return None
    

    def getDefault(self, userName: str) -> PaymentInterface:
        from java.util.HashMap import HashMap
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.commerce.money.payment.Payment import Payment
        from org.allbinary.business.user.commerce.money.payment.PaymentInterface import PaymentInterface
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            paymentHashMap: HashMap = StdUtil.getInstance().createHashMap()
            updateKeyAndValue: HashMap = StdUtil.getInstance().createHashMap()
            updateKeyAndValue.put(EntryData.getInstance().DEFAULT, EntryData.getInstance().DEFAULT)
            updateKeyAndValue.put(UserData.USERNAME, userName)
            paymentHashMap = super().getRow(updateKeyAndValue)
            if paymentHashMap is not None:
                payment: Payment = Payment(paymentHashMap)
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF(self.commonStrings.SUCCESS, self, "getDefault")
                return payment
            else:
                return None
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "getDefault", e)
            return None
    

    def remove(self, userName: str, index: int) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            whereHashMap: HashMap = StdUtil.getInstance().createHashMap()
            whereHashMap.put(UserData.USERNAME, userName)
            whereHashMap.put(PaymentData.ID, str(index))
            super().deleteWhere(whereHashMap)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "remove")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "remove", e)
    

    def add(self, userName: str, paymentInterface: PaymentInterface) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.user.commerce.money.payment.PaymentInterface import PaymentInterface
        from org.allbinary.data.generator.PaymentIdGenerator import PaymentIdGenerator
        from org.allbinary.logic.control.crypt.SuperCrypt import SuperCrypt
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            vector: BasicArrayList = BasicArrayListD()
            vector.add(PaymentIdGenerator().getNext())
            vector.add(userName)
            vector.add(StringUtil.getInstance().EMPTY_STRING)
            vector.add(paymentInterface.getName())
            vector.add(paymentInterface.getType())
            vector.add(paymentInterface.getExpiration())
            random: int = random.Random().nextInt(SuperCrypt.KEYMAX)
            vector.add(SuperCrypt(random).encrypt(paymentInterface.getNumber()))
            vector.add(str(int(random)))
            calendar: datetime.datetime = datetime.datetime.now()
            time: str = str(str(int(calendar.getTimeInMillis())))
            vector.add(time)
            super().insert(vector)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "add")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "add", e)
    

    def createTableStatement(self) -> str:
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.logic.string.StringMaker import StringMaker
        entryData: EntryData = EntryData.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE).append(self.tableName).append(self.sqlStrings.START).append(PaymentData.ID).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_AUTO_INCREMENT_NOT_NULL).append(UserData.USERNAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(entryData.DEFAULT).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(PaymentData.NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(PaymentData.TYPE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(PaymentData.EXPIRATION).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(PaymentData.NUMBER).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(entryData.ENCRYPTION).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(entryData.TIMECREATED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(PaymentData.ID).append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return super().createTable(self.createTableStatement())
    

    def drop(self) -> str:
        return super().dropTable()
    

    def insert(self, values: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        super().insert(values)
    

    def dropTable(self) -> str:
        return super().dropTable()
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
# from java.util.Random import Random
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
# from org.allbinary.business.user.UserData import UserData
# from org.allbinary.business.user.commerce.money.payment.Payment import Payment
# from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
# from org.allbinary.business.user.commerce.money.payment.PaymentInterface import PaymentInterface
# from org.allbinary.data.generator.PaymentIdGenerator import PaymentIdGenerator
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.control.crypt.SuperCrypt import SuperCrypt
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


