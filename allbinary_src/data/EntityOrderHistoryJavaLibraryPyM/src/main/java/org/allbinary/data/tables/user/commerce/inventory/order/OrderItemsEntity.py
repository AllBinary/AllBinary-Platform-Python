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

from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.user.commerce.inventory.order.OrderItemsEntityInterface import OrderItemsEntityInterface


class OrderItemsEntity(AbSqlBean, OrderItemsEntityInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        self.tableName: str = "orderitems"
    

    def __init__(self) -> None:
        super().__init__(HistoryDbInitInfo())
        self._init_fields()
        self.setTableName(self.tableName)
    

    def insert(self, userName: str, order: OrderInterface) -> None:
        vector: BasicArrayList = BasicArrayListD()
        try:
            basket: BasketInterface = order.getBasket()
            items: Set = basket.getIds()
            ZERO_STRING: str = TableDataFactory.getInstance().ZERO_STRING
            EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
            inventoryEntity: InventoryEntity = InventoryEntityFactory.getInstance().getInventoryEntityInstance()
            itemsArray: list[object] = items.toArray()
            itemsSize: int = len(itemsArray)
            for i in range(0, itemsSize):
                item: str = itemsArray[i]
                itemInterface: ItemInterface = inventoryEntity.getItem(item)
                vector = BasicArrayListD()
                vector.add(OrderItemIdGenerator().getNext())
                vector.add(order.getId())
                vector.add(TableDataFactory.getInstance().INTEGER_MAX_VALUE_STRING)
                vector.add(userName)
                vector.add(order.getStoreName())
                vector.add(itemInterface.getId())
                vector.add(str(basket.getNumberOf(item)))
                vector.add(itemInterface.getNewOrUsed())
                vector.add(itemInterface.getSummary())
                vector.add(itemInterface.getDistributor())
                vector.add(itemInterface.getIdUsedByDistributor())
                vector.add(itemInterface.getProducedBy())
                vector.add(itemInterface.getProductionDate())
                vector.add(itemInterface.getStartProductionDate())
                vector.add(itemInterface.getDescription())
                vector.add(itemInterface.getKeywords())
                vector.add(itemInterface.getCategory())
                vector.add(itemInterface.getType())
                vector.add(itemInterface.getSmallImage())
                vector.add(itemInterface.getMediumImage())
                vector.add(itemInterface.getLargeImage())
                vector.add(itemInterface.getWeight())
                vector.add(str(itemInterface.getPrice()))
                vector.add(itemInterface.getComment())
                vector.add(itemInterface.getCustoms())
                vector.add(itemInterface.getDownloads())
                vector.add(EMPTY_STRING)
                vector.add(EMPTY_STRING)
                vector.add(EMPTY_STRING)
                vector.add(EMPTY_STRING)
                vector.add(EMPTY_STRING)
                vector.add(EMPTY_STRING)
                vector.add(EMPTY_STRING)
                vector.add(EMPTY_STRING)
                vector.add(EMPTY_STRING)
                vector.add(EMPTY_STRING)
                vector.add(EMPTY_STRING)
                vector.add(EMPTY_STRING)
                vector.add(EMPTY_STRING)
                vector.add(ZERO_STRING)
                vector.add(ZERO_STRING)
                vector.add(ZERO_STRING)
                vector.add(ZERO_STRING)
                self.insert(vector)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF("Command Success Added: " + str(items.size()), self, self.INSERT)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put("Command Failed: " + str(vector), self, self.INSERT, e)
    

    def setStatus(self, orderId: str, groupId: str, status: str) -> None:
        try:
            whereHashMap: dict = StdUtil.getInstance().createHashMap()
            updateHashMap: dict = StdUtil.getInstance().createHashMap()
            whereHashMap.put(OrderData.ID, orderId)
            whereHashMap.put(ShippingMethodData.GROUP, groupId)
            updateHashMap.put(OrderHistoryData.STATUS, status)
            super().updateWhere(whereHashMap, updateHashMap)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "setStatus", e)
    

    def isEverythingShipped(self, orderId: str) -> bool:
        try:
            itemStatusVector: BasicArrayList = super().getColumnWhere(OrderHistoryData.STATUS, OrderData.ID, orderId)
            size: int = itemStatusVector.size()
            for index in range(0, size):
                status: str = itemStatusVector.get(index)
                if ((status > OrderHistoryData.SHIPPED) - (status < OrderHistoryData.SHIPPED)) != 0:
                    return False
            return True
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "isEverythingShipped", e)
            return False
    

    def getBasketReview(self, orderId: str) -> BasketReview:
        try:
            basketReview: BasketReview = BasketReview()
            keyValues: dict = StdUtil.getInstance().createHashMap()
            keyValues.put(OrderData.ID, orderId)
            items: BasicArrayList = super().getRows(keyValues)
            entryData: EntryData = EntryData.getInstance()
            if items is not None and items.size() > 0:
                EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
                itemsArray: list[object] = items.toArray()
                itemsSize: int = len(itemsArray)
                for i in range(0, itemsSize):
                    itemHashMap: dict = itemsArray[i]
                    itemHashMap.put(self.basicItemData.INBASKETS, EMPTY_STRING)
                    itemHashMap.put(entryData.ENABLE, EMPTY_STRING)
                    itemHashMap.put(entryData.TIMECREATED, EMPTY_STRING)
                    itemHashMap.put(entryData.LASTMODIFIED, EMPTY_STRING)
                    itemHashMap.put(self.basicItemData.GROUPS, EMPTY_STRING)
                    itemHashMap.put(self.basicItemData.OPTIONS, EMPTY_STRING)
                    itemHashMap.put(self.basicItemData.PERMISSIONS, EMPTY_STRING)
                    itemHashMap.put(self.basicItemData.SPECIALS, EMPTY_STRING)
                    item: Item = Item(itemHashMap)
                    basketReview.addItem(item)
                return basketReview
            else:
                return None
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "getBasketReview", e)
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
        stringBuffer.append(ShippingMethodData.GROUP)
        stringBuffer.append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL)
        stringBuffer.append(UserData.USERNAME)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(StoreFrontData.getInstance().NAME)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.basicItemData.ID)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.basicItemData.NUMBER)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.basicItemData.NEWORUSED)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.basicItemData.SUMMARY)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.basicItemData.DISTRIBUTOR)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.basicItemData.IDUSEDBYDISTRIBUTOR)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.basicItemData.PRODUCEDBY)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.basicItemData.PRODUCTIONDATE)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.basicItemData.STARTPRODUCTIONDATE)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.basicItemData.DESCRIPTION)
        stringBuffer.append(self.sqlTypeStrings.BLOB_NOT_NULL)
        stringBuffer.append(self.basicItemData.KEYWORDS)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.basicItemData.CATEGORY)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.basicItemData.TYPE)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.basicItemData.SMALLIMAGE)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.basicItemData.MEDIUMIMAGE)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.basicItemData.LARGEIMAGE)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.basicItemData.WEIGHT)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.basicItemData.PRICE)
        stringBuffer.append(" VARCHAR(20) NOT NULL,")
        stringBuffer.append(self.basicItemData.COMMENT)
        stringBuffer.append(self.sqlTypeStrings.BLOB_NOT_NULL)
        stringBuffer.append(self.basicItemData.CUSTOMS)
        stringBuffer.append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL)
        stringBuffer.append(self.basicItemData.DOWNLOADS)
        stringBuffer.append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL)
        stringBuffer.append(ShippingMethodData.COST)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(OrderHistoryData.TAX)
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
        stringBuffer.append(entryData.SPECIAL)
        stringBuffer.append(" VARCHAR(255) ,")
        stringBuffer.append(OrderHistoryData.STATUS)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(OrderHistoryData.CANCELINFO)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(OrderHistoryData.CANCELTYPE)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(OrderHistoryData.SHIPPEDDATE)
        stringBuffer.append(" BIGINT(19) UNSIGNED ,")
        stringBuffer.append(OrderHistoryData.ORDERDATE)
        stringBuffer.append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL)
        stringBuffer.append(OrderHistoryData.TRANSDATE)
        stringBuffer.append(" BIGINT(19) UNSIGNED ,")
        stringBuffer.append(OrderHistoryData.CANCELDATE)
        stringBuffer.append(" BIGINT(19) UNSIGNED ,")
        stringBuffer.append("PRIMARY KEY(")
        stringBuffer.append(entryData.ID)
        stringBuffer.append(") )")
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return super().createTable(self.createTableStatement())
    

    def dropTable(self) -> str:
        return super().dropTable()
# from java.util.HashMap import HashMap
# from java.util.ListIterator import ListIterator
# from java.util.Set import Set
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.init.db.HistoryDbInitInfo import HistoryDbInitInfo
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.business.user.UserData import UserData
from org.allbinary.business.user.address.ShippingAddressData import ShippingAddressData
from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface
from org.allbinary.business.user.commerce.inventory.basket.BasketReview import BasketReview
from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
from org.allbinary.business.user.commerce.inventory.item.Item import Item
from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
from org.allbinary.business.user.commerce.inventory.order.OrderInterface import OrderInterface
from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
from org.allbinary.data.generator.OrderItemIdGenerator import OrderItemIdGenerator
from org.allbinary.data.tables.TableDataFactory import TableDataFactory
from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntity import InventoryEntity
from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil


