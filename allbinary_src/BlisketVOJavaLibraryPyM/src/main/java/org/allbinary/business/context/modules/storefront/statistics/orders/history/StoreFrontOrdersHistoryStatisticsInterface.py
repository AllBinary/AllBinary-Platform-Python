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

from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface


# Java interface
class StoreFrontOrdersHistoryStatisticsInterface(TableMappingInterface):
    

    def getNumberOfOrders(self) -> int:
        raise NotImplementedError()
    

    def getSubTotal(self) -> Money:
        raise NotImplementedError()
    

    def getShippingCost(self) -> Money:
        raise NotImplementedError()
    

    def getTaxes(self) -> Money:
        raise NotImplementedError()
    

    def getTotal(self) -> Money:
        raise NotImplementedError()
from org.allbinary.business.user.commerce.money.Money import Money


