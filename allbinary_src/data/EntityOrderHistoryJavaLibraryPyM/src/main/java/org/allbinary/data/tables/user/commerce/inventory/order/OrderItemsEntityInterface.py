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
class OrderItemsEntityInterface(BasicDataTableInterface):
    

    def setStatus(self, orderId: str, groupId: str, status: str) -> None:
        raise NotImplementedError()
    

    def isEverythingShipped(self, orderId: str) -> bool:
        raise NotImplementedError()
    

    def getBasketReview(self, orderId: str) -> BasketReview:
        raise NotImplementedError()
    

    def insert(self, userName: str, order: OrderInterface) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def insert(self, values: BasicArrayList) -> None:
        raise NotImplementedError()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.user.commerce.inventory.basket.BasketReview import BasketReview
from org.allbinary.business.user.commerce.inventory.order.OrderInterface import OrderInterface


