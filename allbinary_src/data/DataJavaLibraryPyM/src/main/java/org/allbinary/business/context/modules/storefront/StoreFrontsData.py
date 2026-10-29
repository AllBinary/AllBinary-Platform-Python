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
# package org.allbinary.business.context.modules.storefront

from __future__ import annotations



class StoreFrontsData:
    instance: StoreFrontsData = None

    def _init_fields(self) -> None:
        self.TYPE: str = "STOREFRONTS_TYPE"
        self.RETAIL: str = "STOREFRONTS_RETAIL"
        self.SUBSCRIPTION: str = "STOREFRONTS_SUBSCRIPTION"
        self.AUCTION: str = "STOREFRONTS_AUCTION"
        self.NEWS: str = "STOREFRONTS_NEWS"
        self.BLOG: str = "STOREFRONTS_BLOG"
        self.FORUM: str = "STOREFRONTS_FORUM"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> StoreFrontsData:
        return StoreFrontsData.instance


StoreFrontsData.instance = StoreFrontsData()

