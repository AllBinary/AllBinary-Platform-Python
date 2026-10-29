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



class StoreFrontOrdersHistoryStatisticsData:
    instance: StoreFrontOrdersHistoryStatisticsData = None

    def _init_fields(self) -> None:
        self.NAME: str = "STOREFRONT_ORDERS_HISTORY_STATISTICS_NAME"
        self.NUMBEROFORDERS: str = "STOREFRONT_ORDERS_HISTORY_STATISTICS_NUMBER_OF_ORDERS"
        self.SUBTOTAL: str = "STOREFRONT_ORDERS_HISTORY_STATISTICS_SUBTOTAL"
        self.SHIPPINGCOST: str = "STOREFRONT_ORDERS_HISTORY_STATISTICS_SHIPPINGCOST"
        self.TAXES: str = "STOREFRONT_ORDERS_HISTORY_STATISTICS_TAXES"
        self.TOTAL: str = "STOREFRONT_ORDERS_HISTORY_STATISTICS_TOTAL"
    

    @staticmethod
    def getInstance() -> StoreFrontOrdersHistoryStatisticsData:
        return StoreFrontOrdersHistoryStatisticsData.instance
    

    def __init__(self) -> None:
        self._init_fields()


StoreFrontOrdersHistoryStatisticsData.instance = StoreFrontOrdersHistoryStatisticsData()

