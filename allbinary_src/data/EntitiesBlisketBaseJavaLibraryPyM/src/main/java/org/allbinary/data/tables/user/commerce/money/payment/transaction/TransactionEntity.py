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
# package org.allbinary.data.tables.user.commerce.money.payment.transaction

from __future__ import annotations

import datetime
from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.user.commerce.money.payment.transaction.TransactionEntityInterface import TransactionEntityInterface


class TransactionEntity(AbSqlBean, TransactionEntityInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tableName: str = "vtrans"
    

    def __init__(self) -> None:
        super().__init__(UserDbInitInfo())
        self._init_fields()
        self.setTableName(self.tableName)
    

    def remove(self, userName: str, orderNumber: str) -> None:
        try:
            whereHashMap: dict = StdUtil.getInstance().createHashMap()
            whereHashMap.put(OrderData.ID, orderNumber)
            whereHashMap.put(UserData.USERNAME, userName)
            super().deleteWhere(whereHashMap)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "remove")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "remove", e)
    

    def add(self, userName: str, orderNumber: str, paymentTransactionInterface: PaymentTransactionInterface) -> None:
        try:
            values: BasicArrayList = BasicArrayListD()
            values.add(orderNumber)
            values.add(userName)
            values.addAllList(paymentTransactionInterface.toVector())
            calendar: datetime.datetime = datetime.datetime.now()
            time: str = str(str(int(calendar.getTimeInMillis())))
            values.add(time)
            values.add(time)
            super().insert(values)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "add")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "add", e)
    

    def createTableStatement(self) -> str:
        paymentTransactionKeysFactory: PaymentTransactionKeysFactory = PaymentTransactionKeysFactory.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE)
        stringBuffer.append(self.tableName)
        stringBuffer.append(self.sqlStrings.START)
        stringBuffer.append(OrderData.ID).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(UserData.USERNAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.TRXTYPE)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.TENDER)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.ACCT)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.EXPDATE)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.AMT)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.AUTHCODE)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.MICR)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.CHECKNUM)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.NAME)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.STREET)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.CITY)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.STATE)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.ZIP)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.DL)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.EMAIL)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.COMMENT1)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.COMMENT2)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.ORIGID)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.PONUM)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.DESC)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.DESC1TO4)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.INVNUM)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.SHIPTOZIP)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.SWIPE)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.TAXAMT)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.COMMCARD)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.DUTYAMT)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.FREIGHTAMT)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.ORDERDATE)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.TAXEXEMPT)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.COUNTRYCODE)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.CUSTCODE)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.CVV2)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.ABA)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.ACCTTYPE)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.DISCOUNT)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.FIRSTNAME)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.LASTNAME)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.SHIPFROMZIP)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.PRENOTE)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.CHKTYPE)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.DOB)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.PHONENUM)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.SS)).append(" VARCHAR(30) NOT NULL,").append(str(paymentTransactionKeysFactory.COMPANYNAME)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.COUNTRY)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.SHIPTOCITY)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.SHIPTOFIRSTNAME)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.SHIPTOLASTNAME)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.SHIPTOSTATE)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.SHIPTOSTREET)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.SPECIAL1)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.SPECIAL2)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.SPECIAL3)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(EntryData.getInstance().LASTMODIFIED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(EntryData.getInstance().TIMECREATED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(OrderData.ID).append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return super().createTable(self.createTableStatement())
    

    def dropTable(self) -> str:
        return super().dropTable()
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
from org.allbinary.business.user.UserData import UserData
from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionInterface import PaymentTransactionInterface
from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker


