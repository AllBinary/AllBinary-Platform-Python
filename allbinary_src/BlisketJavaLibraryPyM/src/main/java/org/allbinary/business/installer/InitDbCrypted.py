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

from org.allbinary.logic.communication.sql.AbDatabaseManagement import AbDatabaseManagement


#Warning you must have sql root access
class InitDbCrypted(AbDatabaseManagement):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.userDbInitInfo: UserDbInitInfo = None
        self.inventoryDbInitInfo: InventoryDbInitInfo = None
        self.historyDbInitInfo: HistoryDbInitInfo = None
        self.staticpagesDbInitInfo: StaticPagesDbInitInfo = None
        self.logDbInitInfo: LogDbInitInfo = None
        self.SQL_FILE: str = "initWeblisket.sql"
    

    def __init__(self, databaseConnectionInfoInterface: DatabaseConnectionInfoInterface) -> None:
        super().__init__(databaseConnectionInfoInterface)
        self._init_fields()
    

    def addUsers(self) -> bool:
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.METHOD_ADD_USERS)
            self.userDbInitInfo = UserDbInitInfo()
            self.inventoryDbInitInfo = InventoryDbInitInfo()
            self.historyDbInitInfo = HistoryDbInitInfo()
            self.staticpagesDbInitInfo = StaticPagesDbInitInfo()
            self.logDbInitInfo = LogDbInitInfo()
            CUSTOMERDB: str = self.userDbInitInfo.getName()
            CUSTOMERDBUSER: str = self.userDbInitInfo.getUserName()
            CUSTOMERDBPASSWORD: str = self.userDbInitInfo.getPassword()
            if not self.addDbUser(CUSTOMERDB, CUSTOMERDBUSER, CUSTOMERDBPASSWORD):
                self.logUtil.putF(str(self.UNABLE_TO_CREATE_USER) + CUSTOMERDBUSER, self, self.METHOD_ADD_USERS)
                return False
            INVENTORYDB: str = self.inventoryDbInitInfo.getName()
            INVENTORYDBUSER: str = self.inventoryDbInitInfo.getUserName()
            INVENTORYDBPASSWORD: str = self.inventoryDbInitInfo.getPassword()
            if not self.addDbUser(INVENTORYDB, INVENTORYDBUSER, INVENTORYDBPASSWORD):
                self.logUtil.putF(str(self.UNABLE_TO_CREATE_USER) + INVENTORYDBUSER, self, self.METHOD_ADD_USERS)
                return False
            HISTORYDB: str = self.historyDbInitInfo.getName()
            HISTORYDBUSER: str = self.historyDbInitInfo.getUserName()
            HISTORYDBPASSWORD: str = self.historyDbInitInfo.getPassword()
            if not self.addDbUser(HISTORYDB, HISTORYDBUSER, HISTORYDBPASSWORD):
                self.logUtil.putF(str(self.UNABLE_TO_CREATE_USER) + HISTORYDBUSER, self, self.METHOD_ADD_USERS)
                return False
            STATICPAGESDB: str = self.staticpagesDbInitInfo.getName()
            STATICPAGESDBUSER: str = self.staticpagesDbInitInfo.getUserName()
            STATICPAGESDBPASSWORD: str = self.staticpagesDbInitInfo.getPassword()
            if not self.addDbUser(STATICPAGESDB, STATICPAGESDBUSER, STATICPAGESDBPASSWORD):
                self.logUtil.putF(str(self.UNABLE_TO_CREATE_USER) + STATICPAGESDBUSER, self, self.METHOD_ADD_USERS)
                return False
            LOGDB: str = self.logDbInitInfo.getName()
            LOGDBUSER: str = self.logDbInitInfo.getUserName()
            LOGDBPASSWORD: str = self.logDbInitInfo.getPassword()
            if not self.addDbUser(LOGDB, LOGDBUSER, LOGDBPASSWORD):
                self.logUtil.putF(str(self.UNABLE_TO_CREATE_USER) + LOGDBUSER, self, self.METHOD_ADD_USERS)
                return False
            self.logUtil.putF(self.commonStrings.END, self, self.METHOD_ADD_USERS)
            return True
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.METHOD_ADD_USERS, e)
            return True
    

    def addDatabases(self) -> bool:
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.METHOD_ADD_DATABASES)
            self.userDbInitInfo = UserDbInitInfo()
            self.inventoryDbInitInfo = InventoryDbInitInfo()
            self.historyDbInitInfo = HistoryDbInitInfo()
            self.staticpagesDbInitInfo = StaticPagesDbInitInfo()
            self.logDbInitInfo = LogDbInitInfo()
            CUSTOMERDB: str = self.userDbInitInfo.getName()
            if not self.addDb(CUSTOMERDB):
                self.logUtil.putF(str(self.UNABLE_TO_CREATE_DATABASE) + CUSTOMERDB, self, self.METHOD_ADD_DATABASES)
                return False
            INVENTORYDB: str = self.inventoryDbInitInfo.getName()
            if not self.addDb(INVENTORYDB):
                self.logUtil.putF(str(self.UNABLE_TO_CREATE_DATABASE) + INVENTORYDB, self, self.METHOD_ADD_DATABASES)
                return False
            HISTORYDB: str = self.historyDbInitInfo.getName()
            if not self.addDb(HISTORYDB):
                self.logUtil.putF(str(self.UNABLE_TO_CREATE_DATABASE) + HISTORYDB, self, self.METHOD_ADD_DATABASES)
                return False
            STATICPAGESDB: str = self.staticpagesDbInitInfo.getName()
            if not self.addDb(STATICPAGESDB):
                self.logUtil.putF(str(self.UNABLE_TO_CREATE_DATABASE) + STATICPAGESDB, self, self.METHOD_ADD_DATABASES)
                return False
            LOGDB: str = self.logDbInitInfo.getName()
            if not self.addDb(LOGDB):
                self.logUtil.putF(str(self.UNABLE_TO_CREATE_DATABASE) + LOGDB, self, self.METHOD_ADD_DATABASES)
                return False
            file: AbFile = FileFactory.getInstance().getInstance(self.SQL_FILE)
            file.createNewFile()
            idOutData: AbDataOutputStream = DataOutputStreamFactory.getInstance().getInstanceForAbFile(file)
            idOutData.writeBytes(str(self.sqlCommandLog))
            return True
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.METHOD_ADD_DATABASES, e)
            return True
    

    def addTables(self) -> bool:
        try:
            stringBuffer: StringMaker = StringMaker()
            self.logUtil.putF(self.commonStrings.START, self, self.METHOD_ADD_TABLES)
            stringBuffer.append(UserEntityFactory.getInstance().createTable())
            stringBuffer.append(StoreFrontsEntityFactory.getInstance().getStoreFrontsEntityInstance().createTable())
            stringBuffer.append(BillingAddressesEntityFactory.getInstance().getInstance(self.stringUtil.EMPTY_STRING).createTable())
            stringBuffer.append(ShippingAddressesEntityFactory.getInstance().getInstance(self.stringUtil.EMPTY_STRING).createTable())
            stringBuffer.append(PaymentEntityFactory.getInstance().getPaymentEntityInstance().createTable())
            stringBuffer.append(QuoteRequestEntityFactory.getInstance().getQuoteRequestEntityInstance().createTable())
            stringBuffer.append(OrderHistoryEntityFactory.getInstance().createTable())
            stringBuffer.append(OrderItemsEntityFactory.getInstance().createTable())
            stringBuffer.append(TransactionEntityFactory.getInstance().getTransactionEntityInstance().createTable())
            stringBuffer.append(TransactionResultEntityFactory.getInstance().getTransactionResultEntityInstance().createTable())
            stringBuffer.append(PaymentGatewayEntityFactory.getInstance().createTable())
            stringBuffer.append(InventoryEntityFactory.getInstance().getInventoryEntityInstance().createTable())
            stringBuffer.append(InitInfoEntity().createTable())
            stringBuffer.append(LogTableEntityFactory.getInstance().getLogTableEntityInstance().createTable())
            stringBuffer.append(StaticPagesEntityFactory.getInstance().getStaticPagesEntityInstance().createTable())
            stringBuffer.append(TransformInfoEntityBuilder.getInstance().createTable())
            self.logUtil.putF(str(self.ADD_TABLES_RESULTS_LABEL) + str(stringBuffer), self, self.METHOD_ADD_TABLES)
            return True
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.METHOD_ADD_TABLES, e)
            return False
from org.allbinary.business.init.InitInfoEntity import InitInfoEntity
from org.allbinary.business.init.db.DatabaseConnectionInfoInterface import DatabaseConnectionInfoInterface
from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo
from org.allbinary.business.init.db.HistoryDbInitInfo import HistoryDbInitInfo
from org.allbinary.business.init.db.InventoryDbInitInfo import InventoryDbInitInfo
from org.allbinary.business.init.db.LogDbInitInfo import LogDbInitInfo
from org.allbinary.business.init.db.StaticPagesDbInitInfo import StaticPagesDbInitInfo
from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
from org.allbinary.data.tables.context.module.storefronts.StoreFrontsEntityFactory import StoreFrontsEntityFactory
from org.allbinary.data.tables.log.LogTableEntityFactory import LogTableEntityFactory
from org.allbinary.data.tables.staticpages.StaticPagesEntityFactory import StaticPagesEntityFactory
from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
from org.allbinary.data.tables.user.address.billing.BillingAddressesEntityFactory import BillingAddressesEntityFactory
from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntityFactory import ShippingAddressesEntityFactory
from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityFactory import OrderHistoryEntityFactory
from org.allbinary.data.tables.user.commerce.inventory.order.OrderItemsEntityFactory import OrderItemsEntityFactory
from org.allbinary.data.tables.user.commerce.money.payment.PaymentEntityFactory import PaymentEntityFactory
from org.allbinary.data.tables.user.commerce.money.payment.gateway.PaymentGatewayEntityFactory import PaymentGatewayEntityFactory
from org.allbinary.data.tables.user.commerce.money.payment.transaction.TransactionEntityFactory import TransactionEntityFactory
from org.allbinary.data.tables.user.commerce.money.payment.transaction.TransactionResultEntityFactory import TransactionResultEntityFactory
from org.allbinary.data.tables.user.quoterequest.QuoteRequestEntityFactory import QuoteRequestEntityFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
from org.allbinary.logic.io.DataOutputStreamFactory import DataOutputStreamFactory
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.FileFactory import FileFactory
from org.allbinary.logic.string.StringMaker import StringMaker


