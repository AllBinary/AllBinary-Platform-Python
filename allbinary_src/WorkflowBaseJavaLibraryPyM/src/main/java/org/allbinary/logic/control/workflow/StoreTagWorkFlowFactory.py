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

from java.lang.JavaRuntimeStatic import lazy_static


class StoreTagWorkFlowFactory:
    instance: StoreTagWorkFlowFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance_j0() -> StoreTagWorkFlowFactory:
        return StoreTagWorkFlowFactory.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws Exception, LicensingException
    def getInstance_j3(self, abeClientInformation: AbeClientInformationInterface, propertiesHashMap: HashMap, pageContext: PageContext) -> StoreWorkFlowInterface:
        from java.util.HashMap import HashMap
        from org.allbinary.business.DynamicObjectData import DynamicObjectData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            workFlowClassName: str = propertiesHashMap.get(DynamicObjectData.NAME)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Creating WorkFlow: ")
                stringBuffer.append(workFlowClassName)
                stringBuffer.append("->")
                stringBuffer.append(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(StoreTagWorkFlowFactory.instance)))
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
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                workFlowClassName: str = propertiesHashMap.get(DynamicObjectData.NAME)
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Error Creating WorkFlow: ")
                stringBuffer.append(workFlowClassName)
                stringBuffer.append("->")
                stringBuffer.append(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(StoreTagWorkFlowFactory.instance)))
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(str(stringBuffer), self, commonStrings.GET_INSTANCE, e)
            raise e
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                workFlowClassName: str = propertiesHashMap.get(DynamicObjectData.NAME)
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Error Creating WorkFlow: ")
                stringBuffer.append(workFlowClassName)
                stringBuffer.append("->")
                stringBuffer.append(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(StoreTagWorkFlowFactory.instance)))
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(str(stringBuffer), self, commonStrings.GET_INSTANCE, e)
            raise e

    def getInstance(self=None, *args):
        if self is None and not args: return __class__.getInstance_j0()
        implementation = __class__.__dict__.get("getInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getInstance(*args)
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.DynamicObjectData import DynamicObjectData
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _StoreTagWorkFlowFactory_instance() -> object:
    return StoreTagWorkFlowFactory()

lazy_static(StoreTagWorkFlowFactory, "instance", _StoreTagWorkFlowFactory_instance)

