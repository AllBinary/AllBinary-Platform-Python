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
# package org.allbinary.business.context.modules.storefront.statistics

from __future__ import annotations



# Java interface
class StoreFrontStatisticsInterface:
    

    def getAdvertisements(self) -> StoreFrontAdvertisementsStatisticsInterface:
        raise NotImplementedError()
    

    def getUsers(self) -> StoreFrontUsersStatisticsInterface:
        raise NotImplementedError()
    

    def getInventory(self) -> StoreFrontInventoryStatisticsInterface:
        raise NotImplementedError()
    

    def getOrders(self) -> StoreFrontOrdersHistoryStatisticsInterface:
        raise NotImplementedError()
from org.allbinary.business.context.modules.storefront.statistics.advertisements.StoreFrontAdvertisementsStatisticsInterface import StoreFrontAdvertisementsStatisticsInterface
from org.allbinary.business.context.modules.storefront.statistics.inventory.StoreFrontInventoryStatisticsInterface import StoreFrontInventoryStatisticsInterface
from org.allbinary.business.context.modules.storefront.statistics.orders.history.StoreFrontOrdersHistoryStatisticsInterface import StoreFrontOrdersHistoryStatisticsInterface
from org.allbinary.business.context.modules.storefront.statistics.users.StoreFrontUsersStatisticsInterface import StoreFrontUsersStatisticsInterface


