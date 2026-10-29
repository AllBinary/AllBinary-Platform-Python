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
# package org.allbinary.business.context.modules.storefront.statistics.users

from __future__ import annotations



class StoreFrontUsersStatisticsData:
    instance: StoreFrontUsersStatisticsData = None

    def _init_fields(self) -> None:
        self.NAME: str = "STOREFRONT_USERS_STATISTICS_NAME"
        self.NUMBEROFUSERS: str = "STOREFRONT_USERS_STATISTICS_NUMBER_OF_USERS"
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> StoreFrontUsersStatisticsData:
        return StoreFrontUsersStatisticsData.instance


StoreFrontUsersStatisticsData.instance = StoreFrontUsersStatisticsData()

