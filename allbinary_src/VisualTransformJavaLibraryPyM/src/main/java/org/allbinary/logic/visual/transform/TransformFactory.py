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
# package org.allbinary.logic.visual.transform

from __future__ import annotations



class TransformFactory:
    instance: TransformFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    @staticmethod
    def getInstance() -> TransformFactory:
        return TransformFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, abeClientInformation: AbeClientInformationInterface, viewName: str, ownerTransformInfoInterface: TransformInfoInterface) -> TransformInterface:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                self.logUtil.putF("Creating Transform: " + viewName, self, self.commonStrings.GET_INSTANCE)
            ownerTransformInfoHttpInterface: TransformInfoHttpInterface = ownerTransformInfoInterface
            transformInfoEntity: TransformInfoEntity = TransformInfoEntityBuilder.getInstance()
            transformInfoInterface: TransformInfoInterface = transformInfoEntity.get(viewName, ownerTransformInfoHttpInterface.getPropertiesHashMap(), ownerTransformInfoHttpInterface.getPageContext())
            if transformInfoInterface is None:
                raise Exception("No Such View In DB: " + viewName)
            transformInfoInterface.setChild()
            anyType: object = TransformInfoObjectFactory.getInstance().getInstance(abeClientInformation, transformInfoInterface)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                self.logUtil.putF("Created Transform: " + viewName, self, self.commonStrings.GET_INSTANCE)
            return anyType
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.GET_INSTANCE, e)
            raise e
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, abeClientInformation: AbeClientInformationInterface, propertiesHashMap: dict, pageContext: PageContext) -> TransformInterface:
        try:
            transformInfoData: TransformInfoData = TransformInfoData.getInstance()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                self.logUtil.putF("Creating Transform: " + str(propertiesHashMap.get(transformInfoData.NAME)), self, self.commonStrings.GET_INSTANCE)
            transformInfoEntity: TransformInfoEntity = TransformInfoEntityBuilder.getInstance()
            transformInfoInterface: TransformInfoInterface = transformInfoEntity.get(propertiesHashMap.get(transformInfoData.NAME), propertiesHashMap, pageContext)
            if transformInfoInterface is not None:
                transformInfoInterface.override(propertiesHashMap)
            else:
                transformInfoInterface = TransformInfoHttpFactory.getInstance(propertiesHashMap, pageContext)
            anyType: object = TransformInfoObjectFactory.getInstance().getInstance(abeClientInformation, transformInfoInterface)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                self.logUtil.putF("Created Transform: " + str(propertiesHashMap.get(transformInfoData.NAME)), self, self.commonStrings.GET_INSTANCE)
            return anyType
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Failed To Get Instance: ")
                stringBuffer.append(propertiesHashMap.get(TransformInfoData.getInstance().NAME))
                stringBuffer.append("->TransformFactory")
                self.logUtil.put(str(stringBuffer), self, self.commonStrings.GET_INSTANCE, e)
            raise e
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface) -> TransformInterface:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                self.logUtil.putF("Creating Transform: " + transformInfoInterface.getName(), self, "getInstance(TransformInfoInterface)")
            anyType: object = TransformInfoObjectFactory.getInstance().getInstance(abeClientInformation, transformInfoInterface)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                self.logUtil.putF("Created Transform: " + transformInfoInterface.getName(), self, "getInstance(TransformInfoInterface)")
            return anyType
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(TransformInfoInterface)", e)
            raise e
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.data.tables.transform.info.TransformInfoEntity import TransformInfoEntity
from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
from org.allbinary.logic.visual.transform.info.TransformInfoHttpFactory import TransformInfoHttpFactory
from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.info.TransformInfoObjectFactory import TransformInfoObjectFactory
from org.allbinary.string.CommonStrings import CommonStrings


TransformFactory.instance = TransformFactory()

