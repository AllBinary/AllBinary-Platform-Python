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
# package org.allbinary.data.tables.user.commerce.money.payment.gateway

from __future__ import annotations

import datetime
from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.user.commerce.money.payment.gateway.PaymentGatewayEntityInterface import PaymentGatewayEntityInterface


class PaymentGatewayEntity(AbSqlBean, PaymentGatewayEntityInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tableName: str = "paymentgateways"
    

    def __init__(self) -> None:
        super().__init__(UserDbInitInfo())
        self._init_fields()
        self.setTableName(self.tableName)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
            self.logUtil.putF(self.commonStrings.CONSTRUCTOR, self, self.commonStrings.CONSTRUCTOR)
    

    def add(self, paymentGatewayInterface: PaymentGatewayInterface) -> None:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.START, self, "add")
            vector: BasicArrayList = BasicArrayListD()
            vector.add(PaymentGatewayIdGenerator().getNext())
            vector.addAllList(PaymentGatewayEncryptedMapping(paymentGatewayInterface).toVector())
            calendar: datetime.datetime = datetime.datetime.now()
            time: str = str(str(int(calendar.getTimeInMillis())))
            vector.add(time)
            vector.add(time)
            super().insert(vector)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.END, self, "add")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "add", e)
    

    def update(self, paymentGatewayInterface: PaymentGatewayInterface) -> None:
        try:
            calendar: datetime.datetime = datetime.datetime.now()
            time: str = str(str(int(calendar.getTimeInMillis())))
            paymentGatewayInterface.setLastModified(time)
            whereKeyValuePairs: dict = StdUtil.getInstance().createHashMap()
            whereKeyValuePairs.put(str(StoreFrontData.getInstance().NAME), paymentGatewayInterface.getStoreName())
            whereKeyValuePairs.put(str(PaymentGatewayData.NAME), paymentGatewayInterface.getName())
            if whereKeyValuePairs.get(EntryData.getInstance().TIMECREATED) is not None:
                raise Exception("Don't update TimeCreated for update")
            updateHashMap: dict = PaymentGatewayEncryptedMapping(paymentGatewayInterface).toHashMap()
            super().updateWhere(whereKeyValuePairs, updateHashMap)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "update")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "update", e)
    

    def getPaymentGatewayInterface(self, storeName: str, paymentType: BasicPaymentType) -> PaymentGatewayInterface:
        try:
            paymentGatewayHashMap: dict = StdUtil.getInstance().createHashMap()
            whereKeyAndValue: dict = StdUtil.getInstance().createHashMap()
            whereKeyAndValue.put(str(StoreFrontData.getInstance().NAME), storeName)
            whereKeyAndValue.put(str(PaymentGatewayData.NAME), paymentType.getName())
            paymentGatewayHashMap = super().getRow(whereKeyAndValue)
            if paymentGatewayHashMap is not None:
                userName: str = paymentGatewayHashMap.get(str(UserData.USERNAME))
                password: str = paymentGatewayHashMap.get(str(UserData.PASSWORD))
                special1: str = paymentGatewayHashMap.get(str(PaymentGatewayData.SPECIAL1))
                special2: str = paymentGatewayHashMap.get(str(PaymentGatewayData.SPECIAL2))
                special3: str = paymentGatewayHashMap.get(str(PaymentGatewayData.SPECIAL3))
                special4: str = paymentGatewayHashMap.get(str(PaymentGatewayData.SPECIAL4))
                special5: str = paymentGatewayHashMap.get(str(PaymentGatewayData.SPECIAL5))
                special6: str = paymentGatewayHashMap.get(str(PaymentGatewayData.SPECIAL6))
                special7: str = paymentGatewayHashMap.get(str(PaymentGatewayData.SPECIAL7))
                special8: str = paymentGatewayHashMap.get(str(PaymentGatewayData.SPECIAL8))
                special9: str = paymentGatewayHashMap.get(str(PaymentGatewayData.SPECIAL9))
                superCrypt: SuperCrypt = SuperCrypt(PaymentGatewayData.CRYPTNUM)
                paymentGatewayHashMap.put(str(UserData.USERNAME), superCrypt.decrypt(userName))
                paymentGatewayHashMap.put(str(UserData.PASSWORD), superCrypt.decrypt(password))
                paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL1), superCrypt.decrypt(special1))
                paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL2), superCrypt.decrypt(special2))
                paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL3), superCrypt.decrypt(special3))
                paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL4), superCrypt.decrypt(special4))
                paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL5), superCrypt.decrypt(special5))
                paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL6), superCrypt.decrypt(special6))
                paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL7), superCrypt.decrypt(special7))
                paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL8), superCrypt.decrypt(special8))
                paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL9), superCrypt.decrypt(special9))
                paymentGatewayInterface: PaymentGatewayInterface = PaymentGatewayInterfaceFactory().getInstance(paymentGatewayHashMap)
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF(self.commonStrings.SUCCESS, self, "getPaymentGatewayInterface()")
                return paymentGatewayInterface
            else:
                return PaymentGatewayInterfaceFactory().getInstance(paymentType)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put("Command Failed for paymentType: " + paymentType.getName(), self, "getPaymentGatewayInterface", e)
            return None
    

    def findPaymentTypeVectorByStore(self, storeName: str) -> BasicArrayList:
        try:
            paymentGatewayNameVector: BasicArrayList = BasicArrayListD()
            paymentGatewayNameVector = super().getColumnWhere(str(PaymentGatewayData.NAME), str(StoreFrontData.getInstance().NAME), storeName)
            if paymentGatewayNameVector is not None:
                paymentGatewayVector: BasicArrayList = BasicArrayListD()
                size: int = paymentGatewayNameVector.size()
                for i in range(0, size):
                    paymentTypeString: str = paymentGatewayNameVector.get(i)
                    paymentType: BasicPaymentType = BasicPaymentTypeUtil.getInstance().get(paymentTypeString)
                    paymentGatewayVector.add(paymentType)
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF(self.commonStrings.SUCCESS, self, "findPaymentTypeVectorByStore()")
                return paymentGatewayVector
            else:
                return BasicArrayListD()
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "findPaymentTypeVectorByStore", e)
            return None
    

    def remove(self, storeName: str, paymentType: BasicPaymentType) -> None:
        try:
            whereHashMap: dict = StdUtil.getInstance().createHashMap()
            whereHashMap.put(str(StoreFrontData.getInstance().NAME), storeName)
            whereHashMap.put(str(PaymentGatewayData.NAME), paymentType.getName())
            super().deleteWhere(whereHashMap)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "remove")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "remove", e)
    

    def createTableStatement(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE)
        stringBuffer.append(self.tableName)
        stringBuffer.append(self.sqlStrings.START)
        stringBuffer.append(str(PaymentGatewayData.ID))
        stringBuffer.append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_AUTO_INCREMENT_NOT_NULL)
        stringBuffer.append(EntryData.getInstance().ENABLE)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(StoreFrontData.getInstance().NAME)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.NAME))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(PaymentData.METHOD)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.MODE))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.TESTPROTOCOL))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.TESTSERVER))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.TESTPORT))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.TESTPATH))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.SERVERPROTOCOL))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.SERVER))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.SERVERPORT))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.SERVERPATH))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(UserData.USERNAME)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(UserData.PASSWORD)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.TIMEOUT))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.PROXYPROTOCOL))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.PROXYSERVER))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.PROXYPORT))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.PROXYPATH))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.PROXYUSERNAME))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.PROXYPASSWORD))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.PROXYTIMEOUT))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.SPECIAL1))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.SPECIAL2))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.SPECIAL3))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.SPECIAL4))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.SPECIAL5))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.SPECIAL6))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.SPECIAL7))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.SPECIAL8))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(str(PaymentGatewayData.SPECIAL9))
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(EntryData.getInstance().LASTMODIFIED)
        stringBuffer.append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL)
        stringBuffer.append(EntryData.getInstance().TIMECREATED)
        stringBuffer.append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL)
        stringBuffer.append(self.sqlStrings.PRIMARY_KEY)
        stringBuffer.append(str(PaymentGatewayData.ID))
        stringBuffer.append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return super().createTable(self.createTableStatement())
    

    def dropTable(self) -> str:
        return super().dropTable()
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
from org.allbinary.business.user.UserData import UserData
from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayEncryptedMapping import PaymentGatewayEncryptedMapping
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayInterface import PaymentGatewayInterface
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayInterfaceFactory import PaymentGatewayInterfaceFactory
from org.allbinary.business.user.commerce.money.payment.types.BasicPaymentType import BasicPaymentType
from org.allbinary.business.user.commerce.money.payment.types.BasicPaymentTypeUtil import BasicPaymentTypeUtil
from org.allbinary.data.generator.PaymentGatewayIdGenerator import PaymentGatewayIdGenerator
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.crypt.SuperCrypt import SuperCrypt
from org.allbinary.logic.string.StringMaker import StringMaker


