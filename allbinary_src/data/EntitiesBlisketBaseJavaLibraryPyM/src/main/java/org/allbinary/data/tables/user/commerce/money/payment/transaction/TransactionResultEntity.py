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
from org.allbinary.data.tables.user.commerce.money.payment.transaction.TransactionResultEntityInterface import TransactionResultEntityInterface


class TransactionResultEntity(AbSqlBean, TransactionResultEntityInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tableName: str = "vresults"
    

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
    

    def add(self, userName: str, orderNumber: str, transactionResultInterface: TransactionResultInterface) -> None:
        try:
            values: BasicArrayList = BasicArrayListD()
            values.add(orderNumber)
            values.add(userName)
            values.addAllList(transactionResultInterface.getValues())
            calendar: datetime.datetime = datetime.datetime.now()
            time: str = str(int(calendar.getTimeInMillis()))
            values.add(time)
            values.add(time)
            super().insert(values)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "add")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "add", e)
    

    def getTransactionResultInterface(self, orderNumber: str) -> TransactionResultInterface:
        try:
            resultHashMap: dict = StdUtil.getInstance().createHashMap()
            updateKeyAndValue: dict = StdUtil.getInstance().createHashMap()
            updateKeyAndValue.put(OrderData.ID, orderNumber)
            resultHashMap = super().getRow(updateKeyAndValue)
            if resultHashMap is not None:
                transactionResult: TransactionResult = TransactionResult(resultHashMap)
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF(self.commonStrings.SUCCESS, self, "getTransactionResultInterface")
                return transactionResult
            else:
                return None
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "getTransactionResultInterface", e)
            return None
    

    def createTableStatement(self) -> str:
        paymentTransactionKeysFactory: PaymentTransactionKeysFactory = PaymentTransactionKeysFactory.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE).append(self.tableName).append(self.sqlStrings.START).append(OrderData.ID).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(UserData.USERNAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(paymentTransactionKeysFactory.RESULT)).append(self.sqlTypeStrings.MAX_INT_NOT_NULL).append(str(paymentTransactionKeysFactory.PNREF)).append(self.sqlTypeStrings.TWELVE_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(paymentTransactionKeysFactory.RESPMSG)).append(self.sqlTypeStrings.BLOB_NOT_NULL).append(str(paymentTransactionKeysFactory.AUTHCODE)).append(self.sqlTypeStrings.SIX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.AVSADDR)).append(self.sqlTypeStrings.ONE_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(paymentTransactionKeysFactory.AVSZIP)).append(self.sqlTypeStrings.ONE_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.ORIGRESULT)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(str(paymentTransactionKeysFactory.STATUS)).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(paymentTransactionKeysFactory.FRAUDCODE)).append(self.sqlTypeStrings.TWO_INT_NOT_NULL)
        stringBuffer.append(str(paymentTransactionKeysFactory.FRAUDMSG)).append(self.sqlTypeStrings.MAX_INT_NOT_NULL)
        stringBuffer.append(str(paymentTransactionKeysFactory.ERRCODE)).append(self.sqlTypeStrings.MAX_INT_NOT_NULL)
        stringBuffer.append(str(paymentTransactionKeysFactory.SCORE)).append(self.sqlTypeStrings.THREE_INT_NOT_NULL)
        stringBuffer.append(str(paymentTransactionKeysFactory.REASON1)).append(self.sqlTypeStrings.FOUR_INT_NOT_NULL).append(str(paymentTransactionKeysFactory.REASON2)).append(self.sqlTypeStrings.FOUR_INT_NOT_NULL).append(str(paymentTransactionKeysFactory.REASON3))
        stringBuffer.append(self.sqlTypeStrings.FOUR_INT_NOT_NULL).append(str(paymentTransactionKeysFactory.EXCEPTION1)).append(self.sqlTypeStrings.FOUR_INT_NOT_NULL).append(str(paymentTransactionKeysFactory.EXCEPTION2)).append(self.sqlTypeStrings.FOUR_INT_NOT_NULL).append(str(paymentTransactionKeysFactory.EXCEPTION3)).append(self.sqlTypeStrings.FOUR_INT_NOT_NULL).append(str(paymentTransactionKeysFactory.EXCEPTION4)).append(self.sqlTypeStrings.FOUR_INT_NOT_NULL).append(str(paymentTransactionKeysFactory.EXCEPTION5)).append(self.sqlTypeStrings.FOUR_INT_NOT_NULL).append(str(paymentTransactionKeysFactory.EXCEPTION6)).append(self.sqlTypeStrings.FOUR_INT_NOT_NULL).append(str(paymentTransactionKeysFactory.EXCEPTION7)).append(self.sqlTypeStrings.FOUR_INT_NOT_NULL).append(EntryData.getInstance().LASTMODIFIED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(EntryData.getInstance().TIMECREATED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(OrderData.ID).append(self.sqlStrings.END)
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
from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
from org.allbinary.business.user.commerce.money.payment.gateway.transaction.TransactionResult import TransactionResult
from org.allbinary.business.user.commerce.money.payment.gateway.transaction.TransactionResultInterface import TransactionResultInterface
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker


