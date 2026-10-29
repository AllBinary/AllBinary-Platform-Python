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
# package org.allbinary.data.tables.advertisement.areas

from __future__ import annotations

from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.advertisement.areas.AdvertisementAreasEntityInterface import AdvertisementAreasEntityInterface


class AdvertisementAreasEntity(AbSqlBean, AdvertisementAreasEntityInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tableName: str = "advertisements"
    

    def __init__(self) -> None:
        super().__init__(UserDbInitInfo())
        self._init_fields()
        self.setTableName(self.tableName)
    

    def delete(self, value: str) -> None:
        try:
            super().deleteWhere(EntryData.getInstance().ID, value)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.commonStrings.delete)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.delete, e)
    

    # throws Exception
    def get(self, storeName: str) -> BasicArrayList:
        keysAndValues: dict = StdUtil.getInstance().createHashMap()
        keysAndValues.put(StoreFrontData.getInstance().NAME, storeName)
        hashMapVector: BasicArrayList = super().getRows(keysAndValues)
        vector: BasicArrayList = BasicArrayListD()
        size: int = hashMapVector.size()
        for index in range(0, size):
            hashMap: dict = hashMapVector.get(index)
            if hashMap is not None:
                vector.add(AdvertisementArea(hashMap))
        return vector
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def get(self, storeName: str, advertisementAreaName: str) -> AdvertisementAreaInterface:
        keysAndValues: dict = StdUtil.getInstance().createHashMap()
        keysAndValues.put(StoreFrontData.getInstance().NAME, storeName)
        keysAndValues.put(AdvertisementAreaData.getInstance().NAME, advertisementAreaName)
        hashMap: dict = super().getRow(keysAndValues)
        if hashMap is not None:
            return AdvertisementArea(hashMap)
        else:
            return None
    

    def createTableStatement(self) -> str:
        advertisementAreaData: AdvertisementAreaData = AdvertisementAreaData.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE)
        stringBuffer.append(self.getTableName())
        stringBuffer.append(self.sqlStrings.START)
        stringBuffer.append(advertisementAreaData.NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(StoreFrontData.getInstance().NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(advertisementAreaData.DESCRIPTION).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(advertisementAreaData.CONSTRAINTS).append(self.sqlTypeStrings.BLOB_NOT_NULL).append(AdvertisementCampaignData.getInstance().NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(EntryData.getInstance().TIMECREATED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(EntryData.getInstance().LASTMODIFIED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(advertisementAreaData.NAME).append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        returnStr: str = super().createTable(self.createTableStatement())
        return returnStr
    

    def update(self, updatedValues: dict) -> None:
        super().updateWhere(AdvertisementAreaData.getInstance().NAME, updatedValues.get(AdvertisementAreaData.getInstance().NAME), updatedValues)
    

    def dropTable(self) -> str:
        return super().dropTable()
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.advertisement.area.AdvertisementArea import AdvertisementArea
from org.allbinary.business.advertisement.area.AdvertisementAreaData import AdvertisementAreaData
from org.allbinary.business.advertisement.area.AdvertisementAreaInterface import AdvertisementAreaInterface
from org.allbinary.business.advertisement.campaign.AdvertisementCampaignData import AdvertisementCampaignData
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker


