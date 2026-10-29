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
# package org.allbinary.data.tables.staticpages

from __future__ import annotations

from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.staticpages.StaticPagesEntityInterface import StaticPagesEntityInterface


class StaticPagesEntity(AbSqlBean, StaticPagesEntityInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        self.TABLENAME: str = "staticpages"
    

    def __init__(self) -> None:
        super().__init__(StaticPagesDbInitInfo())
        self._init_fields()
        self.setTableName(self.TABLENAME)
    

    def insert(self, values: BasicArrayList) -> None:
        try:
            super().insert(values)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.INSERT)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.INSERT, e)
    

    def getFile(self, store: str, keywords: str) -> str:
        whereHashMap: dict = StdUtil.getInstance().createHashMap()
        whereHashMap.put(StoreFrontData.getInstance().NAME, store)
        whereHashMap.put(self.basicItemData.KEYWORDS, keywords)
        file: str = super().getField(whereHashMap, SearchData.PAGE)
        return file
    

    def delete(self, keywords: str) -> None:
        super().deleteWhere(self.basicItemData.KEYWORDS, keywords)
    

    def dropTable(self) -> str:
        returnStr: str = super().dropTable()
        return returnStr
    

    def update(self, updatedValues: dict) -> None:
        super().updateWhere(self.basicItemData.KEYWORDS, updatedValues.get(self.basicItemData.KEYWORDS), updatedValues)
    

    def createTableStatement(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE).append(self.TABLENAME).append(self.sqlStrings.START).append(StoreFrontData.getInstance().NAME).append(self.sqlTypeStrings.SIXTY_CHAR_COLUMN_NOT_NULL).append(self.basicItemData.KEYWORDS).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(SearchData.PAGE).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(StoreFrontData.getInstance().NAME).append(CommonSeps.getInstance().COMMA_SEP).append(self.basicItemData.KEYWORDS).append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return super().createTable(self.createTableStatement())
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.init.db.StaticPagesDbInitInfo import StaticPagesDbInitInfo
from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.search.SearchData import SearchData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps


