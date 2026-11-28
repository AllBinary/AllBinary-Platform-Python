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

from org.allbinary.business.context.modules.storefront.statistics.StoreFrontStatisticsInterface import StoreFrontStatisticsInterface


class RealTimeStoreFrontStatistics(StoreFrontStatisticsInterface):

    def _init_fields(self) -> None:
        if "storeFrontAdvertisementsStatisticsInterface" not in vars(self): self.storeFrontAdvertisementsStatisticsInterface: StoreFrontAdvertisementsStatisticsInterface = None
        if "storeFrontUsersStatisticsInterface" not in vars(self): self.storeFrontUsersStatisticsInterface: StoreFrontUsersStatisticsInterface = None
        if "storeFrontInventoryStatisticsInterface" not in vars(self): self.storeFrontInventoryStatisticsInterface: StoreFrontInventoryStatisticsInterface = None
        if "storeFrontOrderHistoryStatisticsInterface" not in vars(self): self.storeFrontOrderHistoryStatisticsInterface: StoreFrontOrdersHistoryStatisticsInterface = None
    

    def __init__(self, storeFrontInterface: StoreFrontInterface) -> None:
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.business.context.modules.storefront.statistics.advertisements.StoreFrontAdvertisementsStatistics import StoreFrontAdvertisementsStatistics
        from org.allbinary.business.context.modules.storefront.statistics.advertisements.StoreFrontAdvertisementsStatisticsInterface import StoreFrontAdvertisementsStatisticsInterface
        from org.allbinary.business.context.modules.storefront.statistics.inventory.StoreFrontInventoryStatistics import StoreFrontInventoryStatistics
        from org.allbinary.business.context.modules.storefront.statistics.inventory.StoreFrontInventoryStatisticsInterface import StoreFrontInventoryStatisticsInterface
        from org.allbinary.business.context.modules.storefront.statistics.orders.history.StoreFrontOrdersHistoryStatistics import StoreFrontOrdersHistoryStatistics
        from org.allbinary.business.context.modules.storefront.statistics.orders.history.StoreFrontOrdersHistoryStatisticsInterface import StoreFrontOrdersHistoryStatisticsInterface
        from org.allbinary.business.context.modules.storefront.statistics.users.StoreFrontUsersStatistics import StoreFrontUsersStatistics
        from org.allbinary.business.context.modules.storefront.statistics.users.StoreFrontUsersStatisticsInterface import StoreFrontUsersStatisticsInterface
        __class__._init_fields(self)
        self.storeFrontAdvertisementsStatisticsInterface = StoreFrontAdvertisementsStatistics(storeFrontInterface)
        self.storeFrontUsersStatisticsInterface = StoreFrontUsersStatistics(storeFrontInterface)
        self.storeFrontInventoryStatisticsInterface = StoreFrontInventoryStatistics(storeFrontInterface)
        self.storeFrontOrderHistoryStatisticsInterface = StoreFrontOrdersHistoryStatistics(storeFrontInterface)
    

    def getAdvertisements(self) -> StoreFrontAdvertisementsStatisticsInterface:
        from org.allbinary.business.context.modules.storefront.statistics.advertisements.StoreFrontAdvertisementsStatisticsInterface import StoreFrontAdvertisementsStatisticsInterface
        return self.storeFrontAdvertisementsStatisticsInterface
    

    def getUsers(self) -> StoreFrontUsersStatisticsInterface:
        from org.allbinary.business.context.modules.storefront.statistics.users.StoreFrontUsersStatisticsInterface import StoreFrontUsersStatisticsInterface
        return self.storeFrontUsersStatisticsInterface
    

    def getInventory(self) -> StoreFrontInventoryStatisticsInterface:
        from org.allbinary.business.context.modules.storefront.statistics.inventory.StoreFrontInventoryStatisticsInterface import StoreFrontInventoryStatisticsInterface
        return self.storeFrontInventoryStatisticsInterface
    

    def getOrders(self) -> StoreFrontOrdersHistoryStatisticsInterface:
        from org.allbinary.business.context.modules.storefront.statistics.orders.history.StoreFrontOrdersHistoryStatisticsInterface import StoreFrontOrdersHistoryStatisticsInterface
        return self.storeFrontOrderHistoryStatisticsInterface
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.business.context.modules.storefront.statistics.advertisements.StoreFrontAdvertisementsStatistics import StoreFrontAdvertisementsStatistics
# from org.allbinary.business.context.modules.storefront.statistics.advertisements.StoreFrontAdvertisementsStatisticsInterface import StoreFrontAdvertisementsStatisticsInterface
# from org.allbinary.business.context.modules.storefront.statistics.inventory.StoreFrontInventoryStatistics import StoreFrontInventoryStatistics
# from org.allbinary.business.context.modules.storefront.statistics.inventory.StoreFrontInventoryStatisticsInterface import StoreFrontInventoryStatisticsInterface
# from org.allbinary.business.context.modules.storefront.statistics.orders.history.StoreFrontOrdersHistoryStatistics import StoreFrontOrdersHistoryStatistics
# from org.allbinary.business.context.modules.storefront.statistics.orders.history.StoreFrontOrdersHistoryStatisticsInterface import StoreFrontOrdersHistoryStatisticsInterface
# from org.allbinary.business.context.modules.storefront.statistics.users.StoreFrontUsersStatistics import StoreFrontUsersStatistics
# from org.allbinary.business.context.modules.storefront.statistics.users.StoreFrontUsersStatisticsInterface import StoreFrontUsersStatisticsInterface


