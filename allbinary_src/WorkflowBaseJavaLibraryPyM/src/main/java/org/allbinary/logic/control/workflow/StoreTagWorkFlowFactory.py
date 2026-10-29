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
# package org.allbinary.logic.control.workflow

from __future__ import annotations



class StoreTagWorkFlowFactory:
    instance: StoreTagWorkFlowFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> StoreTagWorkFlowFactory:
        return StoreTagWorkFlowFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception, LicensingException
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, abeClientInformation: AbeClientInformationInterface, propertiesHashMap: dict, pageContext: PageContext) -> StoreWorkFlowInterface:
        try:
            workFlowClassName: str = propertiesHashMap.get(DynamicObjectData.NAME)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Creating WorkFlow: ")
                stringBuffer.append(workFlowClassName)
                stringBuffer.append("->")
                stringBuffer.append(type(StoreTagWorkFlowFactory.instance).__module__ + "." + type(StoreTagWorkFlowFactory.instance).__qualname__)
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.putF(str(stringBuffer), self, commonStrings.GET_INSTANCE)
            params: list[object] = [None] * (2)
            classes: list[type] = [None] * (2)
            classes[0] = type(propertiesHashMap)
            classes[1] = AbeFactory.getInstance().getClass(abeClientInformation, "javax.servlet.jsp.PageContext")
            params[0] = propertiesHashMap
            params[1] = pageContext
            return AbeFactory.getInstance().getInstance(abeClientInformation, workFlowClassName, classes, params)
        except LicensingException as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                workFlowClassName: str = propertiesHashMap.get(DynamicObjectData.NAME)
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Error Creating WorkFlow: ")
                stringBuffer.append(workFlowClassName)
                stringBuffer.append("->")
                stringBuffer.append(type(StoreTagWorkFlowFactory.instance).__module__ + "." + type(StoreTagWorkFlowFactory.instance).__qualname__)
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(str(stringBuffer), self, commonStrings.GET_INSTANCE, e)
            raise e
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                workFlowClassName: str = propertiesHashMap.get(DynamicObjectData.NAME)
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Error Creating WorkFlow: ")
                stringBuffer.append(workFlowClassName)
                stringBuffer.append("->")
                stringBuffer.append(type(StoreTagWorkFlowFactory.instance).__module__ + "." + type(StoreTagWorkFlowFactory.instance).__qualname__)
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(str(stringBuffer), self, commonStrings.GET_INSTANCE, e)
            raise e
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.DynamicObjectData import DynamicObjectData
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
from org.allbinary.string.CommonStrings import CommonStrings


StoreTagWorkFlowFactory.instance = StoreTagWorkFlowFactory()

