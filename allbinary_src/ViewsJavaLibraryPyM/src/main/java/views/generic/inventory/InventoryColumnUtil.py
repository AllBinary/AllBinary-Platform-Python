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
# package views.generic.inventory

from __future__ import annotations



class InventoryColumnUtil:
    instance: InventoryColumnUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> InventoryColumnUtil:
        return InventoryColumnUtil.instance
    

    def getColumnWhereLike(self, inventoryEntity: InventoryEntity, category: str, column: str) -> BasicArrayList:
        self.logUtil.putF("Start Category: " + category, self, "getKeywords")
        keywords: BasicArrayList = BasicArrayListD()
        vectorOfHashMaps: BasicArrayList = inventoryEntity.getAllRows()
        size: int = vectorOfHashMaps.size()
        for index in range(0, size):
            hashMap: dict = vectorOfHashMaps.get(index)
            categoryName: str = hashMap.get(self.basicItemData.CATEGORY)
            if not StringValidationUtil.getInstance().isEmpty(categoryName) and categoryName.startswith(category):
                keywords.add(hashMap.get(column))
        return keywords
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntity import InventoryEntity
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil


InventoryColumnUtil.instance = InventoryColumnUtil()

