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
# package org.allbinary.data.tables.transform.info

from __future__ import annotations

from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.transform.info.TransformInfoEntityInterface import TransformInfoEntityInterface


class TransformInfoEntity(AbSqlBean, TransformInfoEntityInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tableName: str = "transforminfo"
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        self.transformInfoFactoryInterface: TransformInfoFactoryInterface = None
        self.transformInfoObjectConfigAndManipulatorFactoryInterface: TransformInfoObjectConfigAndManipulatorFactoryBase = None
        self.transformInfoObjectConfigGeneratorFactoryInterface: TransformInfoObjectConfigGeneratorFactoryInterface = None
    

    def __init__(self, transformInfoObjectConfigGeneratorFactoryInterface: TransformInfoObjectConfigGeneratorFactoryInterface, transformInfoObjectConfigAndManipulatorFactoryInterface: TransformInfoObjectConfigAndManipulatorFactoryBase, transformInfoFactoryInterface: TransformInfoFactoryInterface) -> None:
        super().__init__(UserDbInitInfo())
        self._init_fields()
        self.setTableName(self.tableName)
        self.transformInfoObjectConfigGeneratorFactoryInterface = transformInfoObjectConfigGeneratorFactoryInterface
        self.transformInfoObjectConfigAndManipulatorFactoryInterface = transformInfoObjectConfigAndManipulatorFactoryInterface
        self.transformInfoFactoryInterface = transformInfoFactoryInterface
    

    def insert(self, values: BasicArrayList) -> None:
        try:
            super().insert(values)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.INSERT)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.INSERT, e)
    

    def delete(self, value: str) -> None:
        try:
            super().deleteWhere(TransformInfoData.getInstance().NAME, value)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.commonStrings.delete)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.delete, e)
    

    # throws Exception
    def get(self, name: str, propertiesHashMap: dict, pageContext: PageContext) -> TransformInfoInterface:
        transformInfoData: TransformInfoData = TransformInfoData.getInstance()
        keysAndValues: dict = StdUtil.getInstance().createHashMap()
        keysAndValues.put(transformInfoData.NAME, name)
        hashMap: dict = super().getRow(keysAndValues)
        if hashMap is not None:
            anyType: object = hashMap.get(transformInfoData.OBJECTCONFIG)
            if anyType is not None:
                string: str = anyType
                hashMap.put(transformInfoData.OBJECTCONFIG, str(Encoder.decode(string)))
            objectData: object = hashMap.get(transformInfoData.DATA)
            if objectData is not None:
                string: str = objectData
                hashMap.put(transformInfoData.DATA, str(Encoder.decode(string)))
            return self.transformInfoFactoryInterface.getInstance(hashMap, propertiesHashMap, pageContext)
        else:
            return None
    

    # throws Exception
    def getObjectConfigs(self, storeName: str) -> BasicArrayList:
        objectConfigVector: BasicArrayList = BasicArrayListD()
        objectConfigColumnVector: BasicArrayList = self.getColumnWhere(TransformInfoData.getInstance().OBJECTCONFIG, StoreFrontData.getInstance().NAME, storeName)
        size: int = objectConfigColumnVector.size()
        for i in range(0, size):
            objectConfigString: str = objectConfigColumnVector.get(i)
            objectConfigString = str(Encoder.decode(objectConfigString))
            objectConfigVector.add(self.transformInfoObjectConfigAndManipulatorFactoryInterface.getInstance(self.abeClientInformation, self, DomDocumentHelper.create(objectConfigString)))
        return objectConfigVector
    

    # throws Exception
    def getNames(self, storeName: str) -> BasicArrayList:
        viewNameVector: BasicArrayList = BasicArrayListD()
        columnVector: BasicArrayList = self.getColumnWhere(TransformInfoData.getInstance().NAME, StoreFrontData.getInstance().NAME, storeName)
        size: int = columnVector.size()
        for i in range(0, size):
            viewNameString: str = columnVector.get(i)
            viewNameVector.add(viewNameString)
        return viewNameVector
    

    def createTableStatement(self) -> str:
        transformInfoData: TransformInfoData = TransformInfoData.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE)
        stringBuffer.append(self.tableName)
        stringBuffer.append(self.sqlStrings.START)
        stringBuffer.append(transformInfoData.NAME)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(StoreFrontData.getInstance().NAME)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(transformInfoData.OBJECTFILENAME)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(transformInfoData.OBJECT)
        stringBuffer.append(self.sqlTypeStrings.BLOB_NOT_NULL)
        stringBuffer.append(transformInfoData.OBJECTCONFIGFILENAME)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(transformInfoData.OBJECTCONFIG)
        stringBuffer.append(self.sqlTypeStrings.BLOB_NOT_NULL)
        stringBuffer.append(transformInfoData.TEMPLATEFILENAME)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(transformInfoData.TEMPLATE)
        stringBuffer.append(self.sqlTypeStrings.BLOB_NOT_NULL)
        stringBuffer.append(transformInfoData.DATAFILENAME)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(transformInfoData.DATA)
        stringBuffer.append(self.sqlTypeStrings.BLOB_NOT_NULL)
        stringBuffer.append(EntryData.getInstance().LASTMODIFIED)
        stringBuffer.append(EntryData.getInstance().TIMECREATED)
        stringBuffer.append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL)
        stringBuffer.append(self.sqlStrings.PRIMARY_KEY)
        stringBuffer.append(transformInfoData.NAME)
        stringBuffer.append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return super().createTable(self.createTableStatement())
    

    def update(self, updatedValues: dict) -> None:
        super().updateWhere(TransformInfoData.getInstance().NAME, updatedValues.get(TransformInfoData.getInstance().NAME), updatedValues)
    

    def dropTable(self) -> str:
        return super().dropTable()
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.crypt.Encoder import Encoder
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
from org.allbinary.logic.visual.transform.info.TransformInfoFactoryInterface import TransformInfoFactoryInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigAndManipulatorFactoryBase import TransformInfoObjectConfigAndManipulatorFactoryBase
from org.allbinary.logic.visual.transform.info.objectConfig.generator.TransformInfoObjectConfigGeneratorFactoryInterface import TransformInfoObjectConfigGeneratorFactoryInterface


