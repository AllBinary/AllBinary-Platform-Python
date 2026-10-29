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
# package org.allbinary.data.tables.workflow

from __future__ import annotations

from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.workflow.WorkFlowEntityInterface import WorkFlowEntityInterface


class WorkFlowEntity(AbSqlBean, WorkFlowEntityInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        self.tableName: str = "workflows"
        self.METHOD_GET: str = "get()"
        self.METHOD_UPDATE: str = "update"
    

    def __init__(self) -> None:
        super().__init__(UserDbInitInfo())
        self._init_fields()
        self.setTableName(self.tableName)
    

    def insert(self, values: BasicArrayList) -> None:
        try:
            super().insert(values)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.INSERT)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.INSERT, e)
    

    def delete(self, name: str, storeName: str) -> None:
        try:
            keysAndValues: dict = StdUtil.getInstance().createHashMap()
            keysAndValues.put(WorkFlowData.getInstance().NAME, name)
            keysAndValues.put(StoreFrontData.getInstance().NAME, storeName)
            super().deleteWhere(keysAndValues)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.commonStrings.delete)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.delete, e)
    

    # throws Exception, LicensingException
    def get(self, name: str, storeName: str) -> WorkFlowInterface:
        try:
            keysAndValues: dict = StdUtil.getInstance().createHashMap()
            keysAndValues.put(WorkFlowData.getInstance().NAME, name)
            keysAndValues.put(StoreFrontData.getInstance().NAME, storeName)
            hashMap: dict = super().getRow(keysAndValues)
            return DbWorkFlowFactory.getInstance().getInstance(self.abeClientInformation, hashMap)
        except LicensingException as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.METHOD_GET, e)
            raise e
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.METHOD_GET, e)
            raise e
    

    # Java overloaded method: Python keeps the last definition
    def get(self, storeName: str) -> BasicArrayList:
        try:
            workFlowsVector: BasicArrayList = BasicArrayListD()
            keysAndValues: dict = StdUtil.getInstance().createHashMap()
            keysAndValues.put(StoreFrontData.getInstance().NAME, storeName)
            hashMapVector: BasicArrayList = super().getRows(keysAndValues)
            size: int = hashMapVector.size()
            for i in range(0, size):
                workFlowHashMap: dict = hashMapVector.get(i)
                if workFlowHashMap is not None:
                    workFlowsVector.add(DbWorkFlowFactory.getInstance().getInstance(self.abeClientInformation, workFlowHashMap))
            return workFlowsVector
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.METHOD_GET, e)
            return None
    

    def update(self, updatedValues: dict) -> None:
        try:
            wherekeysAndValues: dict = StdUtil.getInstance().createHashMap()
            wherekeysAndValues.put(WorkFlowData.getInstance().NAME, updatedValues.get(WorkFlowData.getInstance().NAME))
            wherekeysAndValues.put(StoreFrontData.getInstance().NAME, updatedValues.get(StoreFrontData.getInstance().NAME))
            super().updateWhere(wherekeysAndValues, updatedValues)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.METHOD_UPDATE, e)
    

    def createTableStatement(self) -> str:
        workFlowData: WorkFlowData = WorkFlowData.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE).append(self.tableName).append(self.sqlStrings.START).append(workFlowData.NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(StoreFrontData.getInstance().NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(DynamicObjectData.NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(workFlowData.DATA).append(self.sqlTypeStrings.BLOB_NOT_NULL).append(EntryData.getInstance().TIMECREATED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(EntryData.getInstance().LASTMODIFIED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(workFlowData.NAME).append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return super().createTable(self.createTableStatement())
    

    def dropTable(self) -> str:
        return super().dropTable()
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.DynamicObjectData import DynamicObjectData
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.workflow.DbWorkFlowFactory import DbWorkFlowFactory
from org.allbinary.logic.control.workflow.WorkFlowData import WorkFlowData
from org.allbinary.logic.control.workflow.WorkFlowInterface import WorkFlowInterface
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory


