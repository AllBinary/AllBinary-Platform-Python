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
# package org.allbinary.business.user.commerce.inventory.order

from __future__ import annotations



class OrderProcessorUtil:
    instance: OrderProcessorUtil = None

    def _init_fields(self) -> None:
        self.ORDER_PROCESSED: str = "Order Processed"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> OrderProcessorUtil:
        return OrderProcessorUtil.instance
    

    # throws Exception
    def process(self, userName: str, order: Order) -> str:
        orderItems: OrderItemsEntity = OrderItemsEntity()
        orderHistory: OrderHistoryEntity = OrderHistoryEntity()
        order.setId(OrderIdGenerator().getNext())
        orderItems.insert(userName, order)
        orderHistory.insert(userName, order)
        return self.ORDER_PROCESSED
from org.allbinary.data.generator.OrderIdGenerator import OrderIdGenerator
from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntity import OrderHistoryEntity
from org.allbinary.data.tables.user.commerce.inventory.order.OrderItemsEntity import OrderItemsEntity


OrderProcessorUtil.instance = OrderProcessorUtil()

