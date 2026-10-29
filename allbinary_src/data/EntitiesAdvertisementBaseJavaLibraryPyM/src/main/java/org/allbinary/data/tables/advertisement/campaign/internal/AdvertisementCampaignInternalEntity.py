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
# package org.allbinary.data.tables.advertisement.campaign.internal

from __future__ import annotations

from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.advertisement.campaign.internal.AdvertisementCampaignInternalEntityInterface import AdvertisementCampaignInternalEntityInterface


class AdvertisementCampaignInternalEntity(AbSqlBean, AdvertisementCampaignInternalEntityInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tableName: str = "adCampaignInternal"
    

    def __init__(self) -> None:
        super().__init__(UserDbInitInfo())
        self._init_fields()
        self.setTableName(self.tableName)
    

    def delete(self, value: str) -> None:
        try:
            super().deleteWhere(StoreFrontData.getInstance().NAME, value)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.commonStrings.delete)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.delete, e)
    

    def getCampaignsInStore(self, storeName: str) -> AdvertisementCampaignsInterface:
        keysAndValues: dict = StdUtil.getInstance().createHashMap()
        keysAndValues.put(StoreFrontData.getInstance().NAME, storeName)
        hashMapVector: BasicArrayList = super().getRows(keysAndValues)
        vector: BasicArrayList = BasicArrayListD()
        size: int = hashMapVector.size()
        for index in range(0, size):
            hashMap: dict = hashMapVector.get(index)
            if hashMap is not None:
                vector.add(AdvertisementCampaign(hashMap))
        return AdvertisementCampaigns(vector)
    

    def get(self, storeName: str, name: str) -> AdvertisementCampaignInterface:
        keysAndValues: dict = StdUtil.getInstance().createHashMap()
        keysAndValues.put(StoreFrontData.getInstance().NAME, storeName)
        keysAndValues.put(AdvertisementCampaignData.getInstance().NAME, name)
        hashMap: dict = super().getRow(keysAndValues)
        if hashMap is not None:
            return AdvertisementCampaign(hashMap)
        else:
            return None
    

    def update(self, updatedValues: dict) -> None:
        super().updateWhere(EntryData.getInstance().getInstance().ID, updatedValues.get(EntryData.getInstance().getInstance().ID), updatedValues)
    

    def createTableStatement(self) -> str:
        entryData: EntryData = EntryData.getInstance().getInstance()
        advertisementCampaignData: AdvertisementCampaignData = AdvertisementCampaignData.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE)
        stringBuffer.append(self.getTableName())
        stringBuffer.append(self.sqlStrings.START)
        stringBuffer.append(entryData.ID).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(StoreFrontData.getInstance().NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(advertisementCampaignData.NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(advertisementCampaignData.DESCRIPTION).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(advertisementCampaignData.CONFIG).append(self.sqlTypeStrings.BLOB_NOT_NULL).append(TimeData.getInstance().START).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(TimeData.getInstance().END).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(entryData.TIMECREATED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(entryData.LASTMODIFIED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(entryData.ID).append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        returnStr: str = super().createTable(self.createTableStatement())
        return returnStr
    

    def dropTable(self) -> str:
        return super().dropTable()
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.advertisement.campaign.AdvertisementCampaign import AdvertisementCampaign
from org.allbinary.business.advertisement.campaign.AdvertisementCampaignData import AdvertisementCampaignData
from org.allbinary.business.advertisement.campaign.AdvertisementCampaignInterface import AdvertisementCampaignInterface
from org.allbinary.business.advertisement.campaign.AdvertisementCampaigns import AdvertisementCampaigns
from org.allbinary.business.advertisement.campaign.AdvertisementCampaignsInterface import AdvertisementCampaignsInterface
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
from org.allbinary.business.time.TimeData import TimeData
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker


