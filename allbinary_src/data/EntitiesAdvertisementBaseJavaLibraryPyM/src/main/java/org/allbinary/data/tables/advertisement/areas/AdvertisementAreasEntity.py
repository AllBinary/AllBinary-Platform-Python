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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.advertisement.areas.AdvertisementAreasEntityInterface import AdvertisementAreasEntityInterface


@java_inherited_overloads
class AdvertisementAreasEntity(*java_bases(AbSqlBean, AdvertisementAreasEntityInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("tableName", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tableName: str = "advertisements"
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
        super().__init__(UserDbInitInfo())
        __class__._init_fields(self)
        self.setTableName(self.tableName)
    

    def delete(self, value: str) -> None:
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            java_super_call(super(), "deleteWhere", EntryData.getInstance().ID, value)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.commonStrings.delete)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.delete, e)
    

    # throws Exception
    def get_j1(self, storeName: str) -> BasicArrayList:
        from java.util.HashMap import HashMap
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.advertisement.area.AdvertisementArea import AdvertisementArea
        from org.allbinary.business.advertisement.area.AdvertisementAreaInterface import AdvertisementAreaInterface
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.logic.StdUtil import StdUtil
        keysAndValues: HashMap = StdUtil.getInstance().createHashMap()
        keysAndValues.put(StoreFrontData.getInstance().NAME, storeName)
        hashMapVector: BasicArrayList = java_super_call(super(), "getRows", keysAndValues)
        vector: BasicArrayList = BasicArrayListD()
        size: int = hashMapVector.size()
        for index in range(0, size):
            hashMap: HashMap = hashMapVector.get(index)
            if hashMap is not None:
                vector.add(AdvertisementArea(hashMap))
        return vector
    

    # throws Exception
    def get_j2(self, storeName: str, advertisementAreaName: str) -> AdvertisementAreaInterface:
        from java.util.HashMap import HashMap
        from org.allbinary.business.advertisement.area.AdvertisementArea import AdvertisementArea
        from org.allbinary.business.advertisement.area.AdvertisementAreaData import AdvertisementAreaData
        from org.allbinary.business.advertisement.area.AdvertisementAreaInterface import AdvertisementAreaInterface
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.logic.StdUtil import StdUtil
        keysAndValues: HashMap = StdUtil.getInstance().createHashMap()
        keysAndValues.put(StoreFrontData.getInstance().NAME, storeName)
        keysAndValues.put(AdvertisementAreaData.getInstance().NAME, advertisementAreaName)
        hashMap: HashMap = java_super_call(super(), "getRow", keysAndValues)
        if hashMap is not None:
            return AdvertisementArea(hashMap)
        else:
            return None

    def get(self, *args):
        implementation = __class__.__dict__.get("get_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().get(*args)
    

    def createTableStatement(self) -> str:
        from org.allbinary.business.advertisement.area.AdvertisementAreaData import AdvertisementAreaData
        from org.allbinary.business.advertisement.campaign.AdvertisementCampaignData import AdvertisementCampaignData
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.logic.string.StringMaker import StringMaker
        advertisementAreaData: AdvertisementAreaData = AdvertisementAreaData.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE)
        stringBuffer.append(self.getTableName())
        stringBuffer.append(self.sqlStrings.START)
        stringBuffer.append(advertisementAreaData.NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(StoreFrontData.getInstance().NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(advertisementAreaData.DESCRIPTION).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(advertisementAreaData.CONSTRAINTS).append(self.sqlTypeStrings.BLOB_NOT_NULL).append(AdvertisementCampaignData.getInstance().NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(EntryData.getInstance().TIMECREATED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(EntryData.getInstance().LASTMODIFIED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(advertisementAreaData.NAME).append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        returnStr: str = java_super_call(super(), "createTable", self.createTableStatement())
        return returnStr
    

    def update(self, updatedValues: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.advertisement.area.AdvertisementAreaData import AdvertisementAreaData
        java_super_call(super(), "updateWhere", AdvertisementAreaData.getInstance().NAME, updatedValues.get(AdvertisementAreaData.getInstance().NAME), updatedValues)
    

    def dropTable(self) -> str:
        return java_super_call(super(), "dropTable")
    

    def insert(self, values: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        java_super_call(super(), "insert", values)
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.advertisement.area.AdvertisementArea import AdvertisementArea
# from org.allbinary.business.advertisement.area.AdvertisementAreaData import AdvertisementAreaData
# from org.allbinary.business.advertisement.area.AdvertisementAreaInterface import AdvertisementAreaInterface
# from org.allbinary.business.advertisement.campaign.AdvertisementCampaignData import AdvertisementCampaignData
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


