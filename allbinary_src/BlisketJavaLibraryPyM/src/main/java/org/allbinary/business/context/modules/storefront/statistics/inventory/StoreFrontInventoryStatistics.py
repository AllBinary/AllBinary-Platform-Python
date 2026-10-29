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
# package org.allbinary.business.context.modules.storefront.statistics.inventory

from __future__ import annotations

from org.allbinary.business.context.modules.storefront.statistics.inventory.StoreFrontInventoryStatisticsInterface import StoreFrontInventoryStatisticsInterface


class StoreFrontInventoryStatistics(StoreFrontInventoryStatisticsInterface):

    def _init_fields(self) -> None:
        self.totalNumberOfItems: int = 0
        self.totalInventorySaleValueMoney: Money = None
    

    def __init__(self, storeFrontInterface: StoreFrontInterface) -> None:
        self._init_fields()
        self.totalInventorySaleValueMoney = Money()
        inventoryEntityInterface: InventoryEntityInterface = InventoryEntityFactory.getInstance().getInventoryEntityInstance()
        itemVector: BasicArrayList = inventoryEntityInterface.getItems(storeFrontInterface)
        size: int = itemVector.size()
        for index in range(0, size):
            itemInterface: ItemInterface = itemVector.get(index)
            numberInStock: int = int(str(itemInterface.getNumber()))
            self.totalNumberOfItems = self.totalNumberOfItems + numberInStock
            itemPriceMoney: Money = itemInterface.getPrice()
            itemPriceMoney.multiply(numberInStock)
            self.totalInventorySaleValueMoney.add(str(itemPriceMoney))
    

    def getNumber(self) -> int:
        return int(self.totalNumberOfItems)
    

    def getTotal(self) -> Money:
        return self.totalInventorySaleValueMoney
    

    def toHashMap(self) -> dict:
        from org.allbinary.business.context.modules.storefront.statistics.inventory.StoreFrontInventoryStatisticsData import StoreFrontInventoryStatisticsData
        from org.allbinary.business.context.modules.storefront.statistics.inventory.StoreFrontInventoryStatisticsData import StoreFrontInventoryStatisticsData
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(StoreFrontInventoryStatisticsData.getInstance().NUMBEROFITEMS, str(self.getNumber()))
        hashMap.put(StoreFrontInventoryStatisticsData.getInstance().TOTALVALUE, str(self.getTotal()))
        return hashMap
    

    def toVector(self) -> BasicArrayList:
        return None
    

    def getKey(self) -> object:
        return None
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
from org.allbinary.business.user.commerce.money.Money import Money
from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityInterface import InventoryEntityInterface
from org.allbinary.logic.StdUtil import StdUtil


