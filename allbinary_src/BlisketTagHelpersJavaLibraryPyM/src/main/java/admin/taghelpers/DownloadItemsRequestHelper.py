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
# package admin.taghelpers

from __future__ import annotations

from admin.taghelpers.ModifyTable import ModifyTable


class DownloadItemsRequestHelper(ModifyTable):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.downloadableItem: DownloadableItem = None
    

    def __init__(self, hashMap: dict, pageContext: PageContext) -> None:
        from admin.taghelpers.InventoryItemViewParentTagHelper import InventoryItemViewParentTagHelper
        super().__init__()
        self._init_fields()
        inventoryTag: HelperTag = hashMap.get(AbTagData.PARENT)
        inventoryItemViewParentTagHelper: InventoryItemViewParentTagHelper = InventoryItemViewParentTagHelper.getInstance()
        downloadableInventoryItemView: DownloadableInventoryItemView = inventoryItemViewParentTagHelper.getDownloadableInventoryItemView(inventoryTag)
        self.downloadableItem = downloadableInventoryItemView.getDownloadableItem()
    

    def insert(self) -> str:
        try:
            vector: BasicArrayList = self.downloadableItem.toVector()
            DownloadItemsEntityFactory.getInstance().getDownloadItemsEntityInstance().insert(vector)
            success: str = "Successfully inserted " + str(self.downloadableItem.getId()) + " into downloaditems table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "insert()")
            return success
        except Exception as e:
            error: str = "Failed to insert " + str(self.downloadableItem.getId()) + " into downloaditems table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "inserts()", e)
            return error
    

    def delete(self) -> str:
        try:
            DownloadItemsEntityFactory.getInstance().getDownloadItemsEntityInstance().delete(self.downloadableItem.getId())
            success: str = "Successfully deleted"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "delete()")
            return success
        except Exception as e:
            error: str = "Failed to delete"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "delete()", e)
            return error
    

    def update(self) -> str:
        try:
            success: str = "Update Successful"
            values: dict = self.downloadableItem.toHashMap()
            DownloadItemsEntityFactory.getInstance().getDownloadItemsEntityInstance().update(values)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(str(self.downloadableItem.getId() + CommonSeps.getInstance().SPACE) + success, self, "update()")
            return success
        except Exception as e:
            error: str = "Failed to update: " + str(self.downloadableItem.getId())
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.jsp.PageContext import PageContext
from admin.tags.AbTagData import AbTagData
from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItem import DownloadableItem
from org.allbinary.data.tables.user.commerce.inventory.item.downloads.DownloadItemsEntityFactory import DownloadItemsEntityFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonSeps import CommonSeps
from tags.HelperTag import HelperTag
from views.admin.inventory.download.DownloadableInventoryItemView import DownloadableInventoryItemView


