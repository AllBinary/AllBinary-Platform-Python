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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.data.tables.BasicDataTableInterface import BasicDataTableInterface


# Java interface
@java_inherited_overloads
class OrderItemsEntityInterface(BasicDataTableInterface):
    

    def setStatus(self, orderId: str, groupId: str, status: str) -> None:
        raise NotImplementedError()
    

    def isEverythingShipped(self, orderId: str) -> bool:
        raise NotImplementedError()
    

    def getBasketReview(self, orderId: str) -> BasketReview:
        from org.allbinary.business.user.commerce.inventory.basket.BasketReview import BasketReview
        raise NotImplementedError()
    

    def insert_j2(self, userName: str, order: OrderInterface) -> None:
        from org.allbinary.business.user.commerce.inventory.order.OrderInterface import OrderInterface
        raise NotImplementedError()
    

    def insert_j1(self, values: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise NotImplementedError()

    def insert(self, *args):
        implementation = __class__.__dict__.get("insert_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().insert(*args)
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.user.commerce.inventory.basket.BasketReview import BasketReview
# from org.allbinary.business.user.commerce.inventory.order.OrderInterface import OrderInterface


