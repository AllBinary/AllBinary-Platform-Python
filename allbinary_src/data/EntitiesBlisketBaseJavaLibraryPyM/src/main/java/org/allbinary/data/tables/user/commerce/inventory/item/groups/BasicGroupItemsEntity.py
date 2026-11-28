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
# package org.allbinary.data.tables.user.commerce.inventory.item.groups

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.user.commerce.inventory.item.groups.BasicGroupItemsEntityInterface import BasicGroupItemsEntityInterface


@java_inherited_overloads
class BasicGroupItemsEntity(*java_bases(AbSqlBean, BasicGroupItemsEntityInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("basicItemData", None)
        vars(self).setdefault("tableName", None)

    def _init_fields(self) -> None:
        from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        self.tableName: str = "basicgroupeditems"
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.init.db.InventoryDbInitInfo import InventoryDbInitInfo
        super().__init__(InventoryDbInitInfo())
        __class__._init_fields(self)
        self.setTableName(self.tableName)
    

    def insert(self, values: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            java_super_call(super(), "insert", values)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.INSERT)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.INSERT, e)
    

    def delete(self, value: str) -> None:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            java_super_call(super(), "deleteWhere", self.basicItemData.ID, value)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.commonStrings.delete)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.delete, e)
    

    def createTableStatement(self) -> str:
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.user.commerce.inventory.item.group.BasicGroupItemData import BasicGroupItemData
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE).append(self.tableName).append(self.sqlStrings.START).append(self.basicItemData.ID).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(BasicGroupItemData.ITEM_ONE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(BasicGroupItemData.ITEM_TWO).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(BasicGroupItemData.ITEM_THREE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(BasicGroupItemData.ITEM_FOUR).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(BasicGroupItemData.ITEM_FIVE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(BasicGroupItemData.ITEM_SIX).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(BasicGroupItemData.ITEM_SEVEN).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(BasicGroupItemData.ITEM_EIGHT).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(BasicGroupItemData.ITEM_NINE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(BasicGroupItemData.ITEM_TEN).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(EntryData.getInstance().TIMECREATED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(EntryData.getInstance().LASTMODIFIED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(self.basicItemData.ID).append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return java_super_call(super(), "createTable", self.createTableStatement())
    

    def update(self, updatedValues: HashMap) -> None:
        from java.util.HashMap import HashMap
        java_super_call(super(), "updateWhere", self.basicItemData.ID, updatedValues.get(self.basicItemData.ID), updatedValues)
    

    def dropTable(self) -> str:
        return java_super_call(super(), "dropTable")
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.init.db.InventoryDbInitInfo import InventoryDbInitInfo
# from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
# from org.allbinary.business.user.commerce.inventory.item.group.BasicGroupItemData import BasicGroupItemData
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


