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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from admin.taghelpers.ModifyTable import ModifyTable


@java_inherited_overloads
class DownloadItemsRequestHelper(ModifyTable):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("downloadableItem", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "downloadableItem" not in vars(self): self.downloadableItem: DownloadableItem = None
    

    def __init__(self, hashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from admin.taghelpers.InventoryItemViewParentTagHelper import InventoryItemViewParentTagHelper
        from java.util.HashMap import HashMap
        from admin.tags.AbTagData import AbTagData
        from tags.HelperTag import HelperTag
        from views.admin.inventory.download.DownloadableInventoryItemView import DownloadableInventoryItemView
        super().__init__()
        __class__._init_fields(self)
        inventoryTag: HelperTag = hashMap.get(AbTagData.PARENT)
        inventoryItemViewParentTagHelper: InventoryItemViewParentTagHelper = InventoryItemViewParentTagHelper.getInstance()
        downloadableInventoryItemView: DownloadableInventoryItemView = inventoryItemViewParentTagHelper.getDownloadableInventoryItemView(inventoryTag)
        self.downloadableItem = downloadableInventoryItemView.getDownloadableItem()
    

    def insert(self) -> str:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.data.tables.user.commerce.inventory.item.downloads.DownloadItemsEntityFactory import DownloadItemsEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            vector: BasicArrayList = self.downloadableItem.toVector()
            DownloadItemsEntityFactory.getInstance().getDownloadItemsEntityInstance().insert(vector)
            success: str = "Successfully inserted " + str(self.downloadableItem.getId()) + " into downloaditems table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "insert()")
            return success
        except Exception as e:
            error: str = "Failed to insert " + str(self.downloadableItem.getId()) + " into downloaditems table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "inserts()", e)
            return error
    

    def delete(self) -> str:
        from org.allbinary.data.tables.user.commerce.inventory.item.downloads.DownloadItemsEntityFactory import DownloadItemsEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            DownloadItemsEntityFactory.getInstance().getDownloadItemsEntityInstance().delete(self.downloadableItem.getId())
            success: str = "Successfully deleted"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "delete()")
            return success
        except Exception as e:
            error: str = "Failed to delete"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "delete()", e)
            return error
    

    def update(self) -> str:
        from java.util.HashMap import HashMap
        from org.allbinary.data.tables.user.commerce.inventory.item.downloads.DownloadItemsEntityFactory import DownloadItemsEntityFactory
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Update Successful"
            values: HashMap = self.downloadableItem.toHashMap()
            DownloadItemsEntityFactory.getInstance().getDownloadItemsEntityInstance().update(values)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(str(self.downloadableItem.getId() + CommonSeps.getInstance().SPACE) + success, self, "update()")
            return success
        except Exception as e:
            error: str = "Failed to update: " + str(self.downloadableItem.getId())
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.jsp.PageContext import PageContext
# from admin.tags.AbTagData import AbTagData
# from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItem import DownloadableItem
# from org.allbinary.data.tables.user.commerce.inventory.item.downloads.DownloadItemsEntityFactory import DownloadItemsEntityFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonSeps import CommonSeps
# from tags.HelperTag import HelperTag
# from views.admin.inventory.download.DownloadableInventoryItemView import DownloadableInventoryItemView
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


