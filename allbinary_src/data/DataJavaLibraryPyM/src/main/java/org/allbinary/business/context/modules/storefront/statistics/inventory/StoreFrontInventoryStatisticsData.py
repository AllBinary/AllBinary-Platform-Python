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



class StoreFrontInventoryStatisticsData:
    instance: StoreFrontInventoryStatisticsData = None

    def _init_fields(self) -> None:
        self.NAME: str = "STOREFRONT_INVENTORY_STATISTICS_NAME"
        self.NUMBEROFITEMS: str = "STOREFRONT_INVENTORY_STATISTICS_NUMBER_OF_ITEMS"
        self.TOTALVALUE: str = "STOREFRONT_INVENTORY_STATISTICS_TOTAL_VALUE"
    

    @staticmethod
    def getInstance() -> StoreFrontInventoryStatisticsData:
        return StoreFrontInventoryStatisticsData.instance
    

    def __init__(self) -> None:
        self._init_fields()


StoreFrontInventoryStatisticsData.instance = StoreFrontInventoryStatisticsData()

