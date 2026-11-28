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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.workflow.WorkFlowEntityInterface import WorkFlowEntityInterface


@java_inherited_overloads
class WorkFlowEntity(*java_bases(AbSqlBean, WorkFlowEntityInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("abeClientInformation", None)
        vars(self).setdefault("tableName", None)
        vars(self).setdefault("METHOD_GET", None)
        vars(self).setdefault("METHOD_UPDATE", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        self.tableName: str = "workflows"
        self.METHOD_GET: str = "get()"
        self.METHOD_UPDATE: str = "update"
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
        super().__init__(UserDbInitInfo())
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
    

    def delete(self, name: str, storeName: str) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.control.workflow.WorkFlowData import WorkFlowData
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            keysAndValues: HashMap = StdUtil.getInstance().createHashMap()
            keysAndValues.put(WorkFlowData.getInstance().NAME, name)
            keysAndValues.put(StoreFrontData.getInstance().NAME, storeName)
            java_super_call(super(), "deleteWhere", keysAndValues)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.commonStrings.delete)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.delete, e)
    

    # throws Exception, LicensingException
    def get_j2(self, name: str, storeName: str) -> WorkFlowInterface:
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.control.workflow.DbWorkFlowFactory import DbWorkFlowFactory
        from org.allbinary.logic.control.workflow.WorkFlowData import WorkFlowData
        from org.allbinary.logic.control.workflow.WorkFlowInterface import WorkFlowInterface
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            keysAndValues: HashMap = StdUtil.getInstance().createHashMap()
            keysAndValues.put(WorkFlowData.getInstance().NAME, name)
            keysAndValues.put(StoreFrontData.getInstance().NAME, storeName)
            hashMap: HashMap = java_super_call(super(), "getRow", keysAndValues)
            return DbWorkFlowFactory.getInstance().getInstance(self.abeClientInformation, hashMap)
        except LicensingException as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.METHOD_GET, e)
            raise e
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.METHOD_GET, e)
            raise e
    

    def get_j1(self, storeName: str) -> BasicArrayList:
        from java.util.HashMap import HashMap
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.control.workflow.DbWorkFlowFactory import DbWorkFlowFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            workFlowsVector: BasicArrayList = BasicArrayListD()
            keysAndValues: HashMap = StdUtil.getInstance().createHashMap()
            keysAndValues.put(StoreFrontData.getInstance().NAME, storeName)
            hashMapVector: BasicArrayList = java_super_call(super(), "getRows", keysAndValues)
            size: int = hashMapVector.size()
            for i in range(0, size):
                workFlowHashMap: HashMap = hashMapVector.get(i)
                if workFlowHashMap is not None:
                    workFlowsVector.add(DbWorkFlowFactory.getInstance().getInstance(self.abeClientInformation, workFlowHashMap))
            return workFlowsVector
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.METHOD_GET, e)
            return None

    def get(self, *args):
        implementation = __class__.__dict__.get("get_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().get(*args)
    

    def update(self, updatedValues: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.control.workflow.WorkFlowData import WorkFlowData
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            wherekeysAndValues: HashMap = StdUtil.getInstance().createHashMap()
            wherekeysAndValues.put(WorkFlowData.getInstance().NAME, updatedValues.get(WorkFlowData.getInstance().NAME))
            wherekeysAndValues.put(StoreFrontData.getInstance().NAME, updatedValues.get(StoreFrontData.getInstance().NAME))
            java_super_call(super(), "updateWhere", wherekeysAndValues, updatedValues)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.METHOD_UPDATE, e)
    

    def createTableStatement(self) -> str:
        from org.allbinary.business.DynamicObjectData import DynamicObjectData
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.logic.control.workflow.WorkFlowData import WorkFlowData
        from org.allbinary.logic.string.StringMaker import StringMaker
        workFlowData: WorkFlowData = WorkFlowData.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE).append(self.tableName).append(self.sqlStrings.START).append(workFlowData.NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(StoreFrontData.getInstance().NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(DynamicObjectData.NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(workFlowData.DATA).append(self.sqlTypeStrings.BLOB_NOT_NULL).append(EntryData.getInstance().TIMECREATED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(EntryData.getInstance().LASTMODIFIED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(workFlowData.NAME).append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return java_super_call(super(), "createTable", self.createTableStatement())
    

    def dropTable(self) -> str:
        return java_super_call(super(), "dropTable")
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.DynamicObjectData import DynamicObjectData
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.control.workflow.DbWorkFlowFactory import DbWorkFlowFactory
# from org.allbinary.logic.control.workflow.WorkFlowData import WorkFlowData
# from org.allbinary.logic.control.workflow.WorkFlowInterface import WorkFlowInterface
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


