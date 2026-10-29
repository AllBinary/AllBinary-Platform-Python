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

from org.allbinary.data.tables.BasicDataTableInterface import BasicDataTableInterface


# Java interface
class OrderHistoryEntityInterface(BasicDataTableInterface):
    

    def insert(self, userName: str, order: Order) -> None:
        raise NotImplementedError()
    

    def setStatus(self, orderId: str, status: str) -> None:
        raise NotImplementedError()
    

    def setPaymentMethod(self, orderId: str, status: str) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def getStoreOrders(self, storeFrontInterface: StoreFrontInterface) -> BasicArrayList:
        raise NotImplementedError()
    

    # throws Exception
    def getOrders(self, userName: str) -> BasicArrayList:
        raise NotImplementedError()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getOrders(self, status: str, fromDate: str, toDate: str) -> BasicArrayList:
        raise NotImplementedError()
    

    # throws Exception
    def getOrder(self, id: str) -> OrderHistory:
        raise NotImplementedError()
    

    # throws Exception
    def update(self, whereHashMap: dict, orderHashMap: dict) -> None:
        raise NotImplementedError()
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.commerce.inventory.order.Order import Order
from org.allbinary.business.user.commerce.inventory.order.OrderHistory import OrderHistory


