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
# package org.allbinary.business.context.modules.storefront.statistics.orders.history

from __future__ import annotations

from org.allbinary.business.context.modules.storefront.statistics.orders.history.StoreFrontOrdersHistoryStatisticsInterface import StoreFrontOrdersHistoryStatisticsInterface


class StoreFrontOrdersHistoryStatistics(StoreFrontOrdersHistoryStatisticsInterface):

    def _init_fields(self) -> None:
        self.numberOfOrdersLong: int = None
        self.subTotalMoney: Money = None
        self.shippingCostMoney: Money = None
        self.taxesMoney: Money = None
        self.totalMoney: Money = None
    

    def __init__(self, storeFrontInterface: StoreFrontInterface) -> None:
        self._init_fields()
        self.subTotalMoney = Money()
        self.shippingCostMoney = Money()
        self.taxesMoney = Money()
        self.totalMoney = Money()
        orderHistoryEntityInterface: OrderHistoryEntityInterface = OrderHistoryEntityFactory.getInstance()
        orderHistoryInterfaceVector: BasicArrayList = orderHistoryEntityInterface.getStoreOrders(storeFrontInterface)
        numberOfOrders: int = 0
        orderHistoryInterface: OrderHistoryInterface = None
        size: int = orderHistoryInterfaceVector.size()
        for index in range(0, size):
            orderHistoryInterface = orderHistoryInterfaceVector.get(index)
            numberOfOrders = numberOfOrders + 1
            self.subTotalMoney.add(orderHistoryInterface.getSubTotal())
            self.shippingCostMoney.add(orderHistoryInterface.getShippingCost())
            self.taxesMoney.add(orderHistoryInterface.getTaxes())
            self.totalMoney.add(orderHistoryInterface.getTotal())
        self.numberOfOrdersLong = int(numberOfOrders)
    

    def getNumberOfOrders(self) -> int:
        return self.numberOfOrdersLong
    

    def getSubTotal(self) -> Money:
        return self.subTotalMoney
    

    def getShippingCost(self) -> Money:
        return self.shippingCostMoney
    

    def getTaxes(self) -> Money:
        return self.taxesMoney
    

    def getTotal(self) -> Money:
        return self.totalMoney
    

    def toHashMap(self) -> dict:
        from org.allbinary.business.context.modules.storefront.statistics.orders.history.StoreFrontOrdersHistoryStatisticsData import StoreFrontOrdersHistoryStatisticsData
        hashMap: dict = StdUtil.getInstance().createHashMap()
        storeFrontOrdersHistoryStatisticsData: StoreFrontOrdersHistoryStatisticsData = StoreFrontOrdersHistoryStatisticsData.getInstance()
        hashMap.put(storeFrontOrdersHistoryStatisticsData.NUMBEROFORDERS, str(self.getNumberOfOrders()))
        hashMap.put(storeFrontOrdersHistoryStatisticsData.SUBTOTAL, str(self.getSubTotal()))
        hashMap.put(storeFrontOrdersHistoryStatisticsData.SHIPPINGCOST, str(self.getShippingCost()))
        hashMap.put(storeFrontOrdersHistoryStatisticsData.TAXES, str(self.getTaxes()))
        hashMap.put(storeFrontOrdersHistoryStatisticsData.TOTAL, str(self.getTotal()))
        return hashMap
    

    def toVector(self) -> BasicArrayList:
        return None
    

    def getKey(self) -> object:
        return None
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.commerce.inventory.order.OrderHistoryInterface import OrderHistoryInterface
from org.allbinary.business.user.commerce.money.Money import Money
from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityFactory import OrderHistoryEntityFactory
from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityInterface import OrderHistoryEntityInterface
from org.allbinary.logic.StdUtil import StdUtil


