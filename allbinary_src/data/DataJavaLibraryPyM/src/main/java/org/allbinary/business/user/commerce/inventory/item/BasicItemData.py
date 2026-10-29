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
# package org.allbinary.business.user.commerce.inventory.item

from __future__ import annotations



class BasicItemData:
    instance: BasicItemData = None

    def _init_fields(self) -> None:
        self.ITEM: str = "BASICITEM"
        self.TOTAL: str = "BASICITEM_TOTAL"
        self.ID: str = "BASICITEM_ID"
        self.NUMBER: str = "BASICITEM_NUMBER"
        self.INBASKETS: str = "BASICITEM_IN_BASKETS"
        self.WEIGHT: str = "BASICITEM_WEIGHT"
        self.NEWORUSED: str = "BASICITEM_NEW_OR_USED"
        self.SUMMARY: str = "BASICITEM_SUMMARY"
        self.DISTRIBUTOR: str = "BASICITEM_DISTRIBUTOR"
        self.IDUSEDBYDISTRIBUTOR: str = "BASICITEM_IDUSEDBYDISTRIBUTOR"
        self.PRODUCEDBY: str = "BASICITEM_PRODUCEDBY"
        self.PRODUCTIONDATE: str = "BASICITEM_PRODUCTIONDATE"
        self.STARTPRODUCTIONDATE: str = "BASICITEM_STARTPRODUCTIONDATE"
        self.DESCRIPTION: str = "BASICITEM_DESCRIPTION"
        self.KEYWORDS: str = "BASICITEM_KEYWORDS"
        self.CATEGORY: str = "BASICITEM_CATEGORY"
        self.TYPE: str = "BASICITEM_TYPE"
        self.IMAGE: str = "BASICITEM_IMG"
        self.SMALLIMAGE: str = "BASICITEM_SMALL_IMG"
        self.MEDIUMIMAGE: str = "BASICITEM_MEDIUM_IMG"
        self.LARGEIMAGE: str = "BASICITEM_LARGE_IMG"
        self.PRICE: str = "BASICITEM_PRICE"
        self.COMMENT: str = "BASICITEM_COMMENT"
        self.CUSTOMS: str = "BASICITEM_CUSTOMS"
        self.DOWNLOADS: str = "BASICITEM_DOWNLOADS"
        self.GROUPS: str = "BASICITEM_GROUPS"
        self.OPTIONS: str = "BASICITEM_OPTIONS"
        self.PERMISSIONS: str = "BASICITEM_PERMISSIONS"
        self.SPECIALS: str = "BASICITEM_SPECIALS"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BasicItemData:
        return BasicItemData.instance


BasicItemData.instance = BasicItemData()

