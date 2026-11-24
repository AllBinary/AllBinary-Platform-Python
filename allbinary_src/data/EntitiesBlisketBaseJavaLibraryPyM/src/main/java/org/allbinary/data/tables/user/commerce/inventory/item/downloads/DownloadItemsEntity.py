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
# package org.allbinary.data.tables.user.commerce.inventory.item.downloads

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.user.commerce.inventory.item.downloads.DownloadItemsEntityInterface import DownloadItemsEntityInterface


class DownloadItemsEntity(*java_bases(AbSqlBean, DownloadItemsEntityInterface)):

    def _init_fields(self) -> None:
        from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        self.tableName: str = "downloaditems"
    

    def __init__(self) -> None:
        from org.allbinary.business.init.db.InventoryDbInitInfo import InventoryDbInitInfo
        super().__init__(InventoryDbInitInfo())
        self._init_fields()
        self.setTableName(self.tableName)
    

    def insert(self, values: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            super().insert(values)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.INSERT)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.INSERT, e)
    

    def delete(self, value: str) -> None:
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            super().deleteWhere(DownloadItemData.ID, value)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.commonStrings.delete)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.delete, e)
    

    def update(self, updatedValues: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        super().updateWhere(DownloadItemData.ID, updatedValues.get(DownloadItemData.ID), updatedValues)
    

    def getForItem_j1(self, id: str) -> BasicArrayList:
        from java.util.HashMap import HashMap
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItem import DownloadableItem
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        returnVector: BasicArrayList = BasicArrayListD()
        keysAndValues: HashMap = StdUtil.getInstance().createHashMap()
        keysAndValues.put(self.basicItemData.ID, id)
        vector: BasicArrayList = super().getRows(keysAndValues)
        size: int = vector.size()
        for index in range(0, size):
            hashMap: HashMap = vector.get(index)
            returnVector.add(DownloadableItem(hashMap))
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
            self.logUtil.putF("Found: " + str(size), self, "getForItem")
        return returnVector
    

    def getForItem_j2(self, id: str, downloadItemId: str) -> BasicArrayList:
        from java.util.HashMap import HashMap
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItem import DownloadableItem
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        returnVector: BasicArrayList = BasicArrayListD()
        keysAndValues: HashMap = StdUtil.getInstance().createHashMap()
        keysAndValues.put(self.basicItemData.ID, id)
        keysAndValues.put(DownloadItemData.ID, downloadItemId)
        vector: BasicArrayList = super().getRows(keysAndValues)
        size: int = vector.size()
        for index in range(0, size):
            hashMap: HashMap = vector.get(index)
            returnVector.add(DownloadableItem(hashMap))
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
            self.logUtil.putF("Found: " + str(size), self, "getForItem")
        return returnVector

    def getForItem(self, *args):
        return getattr(self, "getForItem_j" + str(len(args)))(*args)
    

    def createTableStatement(self) -> str:
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE).append(self.tableName).append(self.sqlStrings.START).append(DownloadItemData.ID).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.basicItemData.ID).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(EntryData.getInstance().ENABLE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(DownloadItemData.SPECIAL_NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(DownloadItemData.VERSION).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(DownloadItemData.CHANGES).append(self.sqlTypeStrings.BLOB_NOT_NULL).append(DownloadItemData.SYSTEM).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(DownloadItemData.PLATFORM).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(DownloadItemData.LICENSE_FILE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(DownloadItemData.FILE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(DownloadItemData.SIZE).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(DownloadItemData.VALID_TIME).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(DownloadItemData.RETRIES).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(EntryData.getInstance().TIMECREATED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(EntryData.getInstance().LASTMODIFIED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(DownloadItemData.ID).append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return super().createTable(self.createTableStatement())
    

    def dropTable(self) -> str:
        return super().dropTable()
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.init.db.InventoryDbInitInfo import InventoryDbInitInfo
# from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
# from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
# from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItem import DownloadableItem
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


