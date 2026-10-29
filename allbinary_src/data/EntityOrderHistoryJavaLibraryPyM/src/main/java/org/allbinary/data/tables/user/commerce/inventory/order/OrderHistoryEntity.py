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
# package org.allbinary.data.tables.user.commerce.inventory.order

from __future__ import annotations

import random
import datetime
from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityInterface import OrderHistoryEntityInterface


class OrderHistoryEntity(AbSqlBean, OrderHistoryEntityInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tableName: str = "orderhistory"
    

    def __init__(self) -> None:
        super().__init__(HistoryDbInitInfo())
        self._init_fields()
        self.setTableName(self.tableName)
    

    def insert(self, userName: str, order: Order) -> None:
        vector: BasicArrayList = BasicArrayListD()
        try:
            paymentInterface: PaymentInterface = PaymentEntity().getDefault(userName)
            billingAddress: StreetAddress = BillingAddressesEntity(userName).getDefault()
            shippingAddress: StreetAddress = ShippingAddressesEntity(userName).getDefault()
            abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
            storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(order.getStoreName())
            shippingInterface: ShippingInterface = ShippingMethods(abeClientInformation, storeFrontInterface).getShippingInterface(order.getShippingMethod())
            shippingCost: Money = shippingInterface.getCost(order)
            basketInterface: BasketInterface = order.getBasket()
            subTotal: Money = basketInterface.getSubTotal()
            taxRate: float = TaxFactory.getInstance().getInstance(abeClientInformation, storeFrontInterface).getTaxRate(shippingAddress, storeFrontInterface)
            tax: Money = Money()
            total: Money = Money()
            total.add(str(shippingCost))
            total.add(str(subTotal))
            tax.add(str(total))
            tax.multiply(taxRate)
            total.add(str(tax))
            empty: str = StringUtil.getInstance().EMPTY_STRING
            vector.add(OrderHistoryIdGenerator().getNext())
            ZERO: str = TableDataFactory.getInstance().ZERO_STRING
            vector.add(order.getId())
            vector.add(userName)
            vector.add(order.getStoreName())
            calendar: datetime.datetime = datetime.datetime.now()
            time: str = str(str(int(calendar.getTimeInMillis())))
            vector.add(ZERO)
            vector.add(time)
            vector.add(ZERO)
            vector.add(ZERO)
            vector.add(OrderHistoryData.PREPROCESSING)
            vector.add(order.getPaymentMethod())
            if paymentInterface is not None:
                vector.add(paymentInterface.getName())
                vector.add(paymentInterface.getType())
                vector.add(paymentInterface.getExpiration())
                random: int = random.Random().nextInt(SuperCrypt.KEYMAX)
                vector.add(SuperCrypt(random).encrypt(paymentInterface.getNumber()))
                vector.add(str(int(random)))
            else:
                vector.add(empty)
                vector.add(empty)
                vector.add(empty)
                vector.add(empty)
                vector.add(ZERO)
            if billingAddress is not None:
                vector.add(billingAddress.getName())
                vector.add(billingAddress.getStreet())
                vector.add(billingAddress.getCity())
                vector.add(billingAddress.getState())
                vector.add(billingAddress.getCode())
                vector.add(billingAddress.getCountry())
            else:
                vector.add(empty)
                vector.add(empty)
                vector.add(empty)
                vector.add(empty)
                vector.add(empty)
                vector.add(empty)
            if shippingAddress is not None:
                vector.add(shippingAddress.getName())
                vector.add(shippingAddress.getStreet())
                vector.add(shippingAddress.getCity())
                vector.add(shippingAddress.getState())
                vector.add(shippingAddress.getCode())
                vector.add(shippingAddress.getCountry())
            else:
                vector.add(empty)
                vector.add(empty)
                vector.add(empty)
                vector.add(empty)
                vector.add(empty)
                vector.add(empty)
            vector.add(order.getShippingMethod())
            vector.add(str(subTotal))
            vector.add(str(shippingCost))
            vector.add(str(tax))
            vector.add(str(total))
            vector.add(order.getSpecial())
            vector.add(order.getUserComments())
            vector.add(order.getUserCancelComments())
            vector.add(order.getStoreComments())
            vector.add(order.getStoreCancelComments())
            self.insert(vector)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.INSERT)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put("Command Failed: " + str(vector), self, self.INSERT, e)
    

    # Java overloaded method: Python keeps the last definition
    def insert(self, values: BasicArrayList) -> None:
        try:
            super().insert(values)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.INSERT)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.INSERT, e)
    

    def setStatus(self, orderId: str, status: str) -> None:
        try:
            calendar: datetime.datetime = datetime.datetime.now()
            time: str = str(str(int(calendar.getTimeInMillis())))
            updateHashMap: dict = StdUtil.getInstance().createHashMap()
            updateHashMap.put(OrderHistoryData.STATUS, status)
            if ((status > OrderHistoryData.CANCELLED) - (status < OrderHistoryData.CANCELLED)) == 0:
                updateHashMap.put(OrderHistoryData.CANCELDATE, time)
            elif ((status > OrderHistoryData.SHIPPED) - (status < OrderHistoryData.SHIPPED)) == 0:
                updateHashMap.put(OrderHistoryData.SHIPPEDDATE, time)
            super().updateWhere(OrderData.ID, orderId, updateHashMap)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "setStatus", e)
    

    def setPaymentMethod(self, orderId: str, paymentMethod: str) -> None:
        try:
            calendar: datetime.datetime = datetime.datetime.now()
            time: str = str(str(int(calendar.getTimeInMillis())))
            updateHashMap: dict = StdUtil.getInstance().createHashMap()
            updateHashMap.put(PaymentData.METHOD, paymentMethod)
            updateHashMap.put(OrderHistoryData.TRANSDATE, time)
            super().updateWhere(OrderData.ID, orderId, updateHashMap)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "setPaymentMethod", e)
    

    # throws Exception
    def getStoreOrders(self, storeFrontInterface: StoreFrontInterface) -> BasicArrayList:
        orderReviewVector: BasicArrayList = BasicArrayListD()
        whereHashMap: dict = StdUtil.getInstance().createHashMap()
        whereHashMap.put(StoreFrontData.getInstance().NAME, storeFrontInterface.getName())
        orderHashMapVector: BasicArrayList = super().getRows(whereHashMap)
        size: int = orderHashMapVector.size()
        for i in range(0, size):
            orderReviewHashMap: dict = orderHashMapVector.get(i)
            orderReview: OrderHistory = OrderHistory(Basket(), orderReviewHashMap)
            orderReviewVector.add(orderReview)
        return orderReviewVector
    

    # throws Exception
    def getOrders(self, userName: str) -> BasicArrayList:
        orderReviewVector: BasicArrayList = BasicArrayListD()
        whereHashMap: dict = StdUtil.getInstance().createHashMap()
        whereHashMap.put(UserData.USERNAME, userName)
        orderHashMapVector: BasicArrayList = super().getRows(whereHashMap)
        size: int = orderHashMapVector.size()
        for index in range(0, size):
            orderReviewHashMap: dict = orderHashMapVector.get(index)
            orderReview: OrderHistory = OrderHistory(Basket(), orderReviewHashMap)
            orderReviewVector.add(orderReview)
        return orderReviewVector
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getOrders(self, status: str, fromDate: str, toDate: str) -> BasicArrayList:
        orderReviewVector: BasicArrayList = BasicArrayListD()
        whereHashMap: dict = StdUtil.getInstance().createHashMap()
        whereHashMap.put(OrderHistoryData.STATUS, status)
        orderHashMapVector: BasicArrayList = super().getRowsWhereBetween(whereHashMap, OrderHistoryData.ORDERDATE, fromDate, toDate)
        size: int = orderHashMapVector.size()
        for index in range(0, size):
            orderReviewHashMap: dict = orderHashMapVector.get(index)
            orderReview: OrderHistory = OrderHistory(Basket(), orderReviewHashMap)
            orderReviewVector.add(orderReview)
        return orderReviewVector
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getOrders(self, fromDate: str, toDate: str) -> BasicArrayList:
        orderReviewVector: BasicArrayList = BasicArrayListD()
        orderHashMapVector: BasicArrayList = super().getRowsWhereBetween(OrderHistoryData.ORDERDATE, fromDate, toDate)
        size: int = orderHashMapVector.size()
        for index in range(0, size):
            orderReviewHashMap: dict = orderHashMapVector.get(index)
            orderReview: OrderHistory = OrderHistory(Basket(), orderReviewHashMap)
            orderReviewVector.add(orderReview)
        return orderReviewVector
    

    # throws Exception
    def getOrder(self, id: str) -> OrderHistory:
        whereHashMap: dict = StdUtil.getInstance().createHashMap()
        whereHashMap.put(OrderData.ID, id)
        orderReviewHashMap: dict = super().getRow(whereHashMap)
        if orderReviewHashMap is not None:
            orderHistory: OrderHistory = OrderHistory(Basket(), orderReviewHashMap)
            return orderHistory
        else:
            return None
    

    def createTableStatement(self) -> str:
        entryData: EntryData = EntryData.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("CREATE TABLE ")
        stringBuffer.append(self.tableName)
        stringBuffer.append(" (")
        stringBuffer.append(entryData.ID)
        stringBuffer.append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL)
        stringBuffer.append(OrderData.ID)
        stringBuffer.append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL)
        stringBuffer.append(UserData.USERNAME)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(StoreFrontData.getInstance().NAME)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(OrderHistoryData.SHIPPEDDATE)
        stringBuffer.append(" BIGINT(19) UNSIGNED ,")
        stringBuffer.append(OrderHistoryData.ORDERDATE)
        stringBuffer.append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL)
        stringBuffer.append(OrderHistoryData.TRANSDATE)
        stringBuffer.append(" BIGINT(19) UNSIGNED ,")
        stringBuffer.append(OrderHistoryData.CANCELDATE)
        stringBuffer.append(" BIGINT(19) UNSIGNED ,")
        stringBuffer.append(OrderHistoryData.STATUS)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(PaymentData.METHOD)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(PaymentData.NAME)
        stringBuffer.append(" VARCHAR(255) ,")
        stringBuffer.append(PaymentData.TYPE)
        stringBuffer.append(" VARCHAR(255) ,")
        stringBuffer.append(PaymentData.EXPIRATION)
        stringBuffer.append(" VARCHAR(255) ,")
        stringBuffer.append(PaymentData.NUMBER)
        stringBuffer.append(" VARCHAR(255) ,")
        stringBuffer.append(entryData.ENCRYPTION)
        stringBuffer.append(" BIGINT(19) UNSIGNED ,")
        stringBuffer.append(BillingAddressData.NAME)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(BillingAddressData.STREET)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(BillingAddressData.CITY)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(BillingAddressData.STATE)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(BillingAddressData.CODE)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(BillingAddressData.COUNTRY)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(ShippingAddressData.NAME)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(ShippingAddressData.STREET)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(ShippingAddressData.CITY)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(ShippingAddressData.STATE)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(ShippingAddressData.CODE)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(ShippingAddressData.COUNTRY)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(ShippingMethodData.NAME)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(OrderHistoryData.SUBTOTAL)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(OrderHistoryData.SHIPPINGCOST)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(OrderHistoryData.TAX)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(OrderHistoryData.TOTAL)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(entryData.SPECIAL)
        stringBuffer.append(" VARCHAR(255) ,")
        stringBuffer.append(OrderData.CUSTOMERCOMMENT)
        stringBuffer.append(self.sqlTypeStrings.BLOB_NOT_NULL)
        stringBuffer.append(OrderData.CUSTOMERCANCELCOMMENT)
        stringBuffer.append(self.sqlTypeStrings.BLOB_NOT_NULL)
        stringBuffer.append(OrderData.STORECOMMENT)
        stringBuffer.append(self.sqlTypeStrings.BLOB_NOT_NULL)
        stringBuffer.append(OrderData.STORECANCELCOMMENT)
        stringBuffer.append(self.sqlTypeStrings.BLOB_NOT_NULL)
        stringBuffer.append("PRIMARY KEY(")
        stringBuffer.append(entryData.ID)
        stringBuffer.append(") )")
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return super().createTable(self.createTableStatement())
    

    def dropTable(self) -> str:
        return super().dropTable()
    

    # throws Exception
    def update(self, whereHashMap: dict, orderHashMap: dict) -> None:
        try:
            self.updateWhere(whereHashMap, orderHashMap)
        except Exception as e:
            raise e
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
# from java.util.Random import Random
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.init.db.HistoryDbInitInfo import HistoryDbInitInfo
from org.allbinary.business.user.UserData import UserData
from org.allbinary.business.user.address.BillingAddressData import BillingAddressData
from org.allbinary.business.user.address.ShippingAddressData import ShippingAddressData
from org.allbinary.business.user.address.StreetAddress import StreetAddress
from org.allbinary.business.user.commerce.inventory.basket.Basket import Basket
from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface
from org.allbinary.business.user.commerce.inventory.order.Order import Order
from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
from org.allbinary.business.user.commerce.inventory.order.OrderHistory import OrderHistory
from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
from org.allbinary.business.user.commerce.money.Money import Money
from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
from org.allbinary.business.user.commerce.money.payment.PaymentInterface import PaymentInterface
from org.allbinary.business.user.commerce.money.tax.TaxFactory import TaxFactory
from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
from org.allbinary.business.user.commerce.shipping.ShippingMethods import ShippingMethods
from org.allbinary.business.user.commerce.shipping.modules.ShippingInterface import ShippingInterface
from org.allbinary.data.generator.OrderHistoryIdGenerator import OrderHistoryIdGenerator
from org.allbinary.data.tables.TableDataFactory import TableDataFactory
from org.allbinary.data.tables.user.address.billing.BillingAddressesEntity import BillingAddressesEntity
from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntity import ShippingAddressesEntity
from org.allbinary.data.tables.user.commerce.money.payment.PaymentEntity import PaymentEntity
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.crypt.SuperCrypt import SuperCrypt
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory


