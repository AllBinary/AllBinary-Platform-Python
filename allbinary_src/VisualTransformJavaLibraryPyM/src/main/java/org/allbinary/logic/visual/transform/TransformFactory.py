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

from java.lang.JavaRuntimeStatic import lazy_static


class TransformFactory:
    instance: TransformFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    @staticmethod
    def getInstance_j0() -> TransformFactory:
        return TransformFactory.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j3_1(self, abeClientInformation: AbeClientInformationInterface, viewName: str, ownerTransformInfoInterface: TransformInfoInterface) -> TransformInterface:
        from org.allbinary.data.tables.transform.info.TransformInfoEntity import TransformInfoEntity
        from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoObjectFactory import TransformInfoObjectFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                self.logUtil.putF("Creating Transform: " + viewName, self, self.commonStrings.GET_INSTANCE)
            ownerTransformInfoHttpInterface: TransformInfoHttpInterface = ownerTransformInfoInterface
            transformInfoEntity: TransformInfoEntity = TransformInfoEntityBuilder.getInstance()
            transformInfoInterface: TransformInfoInterface = transformInfoEntity.get(viewName, ownerTransformInfoHttpInterface.getPropertiesHashMap(), ownerTransformInfoHttpInterface.getPageContext())
            if transformInfoInterface is None:
                raise Exception("No Such View In DB: " + viewName)
            transformInfoInterface.setChild()
            anyType: object = TransformInfoObjectFactory.getInstance().getInstance(abeClientInformation, transformInfoInterface)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                self.logUtil.putF("Created Transform: " + viewName, self, self.commonStrings.GET_INSTANCE)
            return anyType
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.GET_INSTANCE, e)
            raise e
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j3_2(self, abeClientInformation: AbeClientInformationInterface, propertiesHashMap: HashMap, pageContext: PageContext) -> TransformInterface:
        from java.util.HashMap import HashMap
        from org.allbinary.data.tables.transform.info.TransformInfoEntity import TransformInfoEntity
        from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpFactory import TransformInfoHttpFactory
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoObjectFactory import TransformInfoObjectFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            transformInfoData: TransformInfoData = TransformInfoData.getInstance()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                self.logUtil.putF("Creating Transform: " + str(propertiesHashMap.get(transformInfoData.NAME)), self, self.commonStrings.GET_INSTANCE)
            transformInfoEntity: TransformInfoEntity = TransformInfoEntityBuilder.getInstance()
            transformInfoInterface: TransformInfoInterface = transformInfoEntity.get(propertiesHashMap.get(transformInfoData.NAME), propertiesHashMap, pageContext)
            if transformInfoInterface is not None:
                transformInfoInterface.override(propertiesHashMap)
            else:
                transformInfoInterface = TransformInfoHttpFactory.getInstance(propertiesHashMap, pageContext)
            anyType: object = TransformInfoObjectFactory.getInstance().getInstance(abeClientInformation, transformInfoInterface)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                self.logUtil.putF("Created Transform: " + str(propertiesHashMap.get(transformInfoData.NAME)), self, self.commonStrings.GET_INSTANCE)
            return anyType
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Failed To Get Instance: ")
                stringBuffer.append(propertiesHashMap.get(TransformInfoData.getInstance().NAME))
                stringBuffer.append("->TransformFactory")
                self.logUtil.put(str(stringBuffer), self, self.commonStrings.GET_INSTANCE, e)
            raise e
    

    # throws Exception
    def getInstance_j2(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface) -> TransformInterface:
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoObjectFactory import TransformInfoObjectFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                self.logUtil.putF("Creating Transform: " + transformInfoInterface.getName(), self, "getInstance(TransformInfoInterface)")
            anyType: object = TransformInfoObjectFactory.getInstance().getInstance(abeClientInformation, transformInfoInterface)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                self.logUtil.putF("Created Transform: " + transformInfoInterface.getName(), self, "getInstance(TransformInfoInterface)")
            return anyType
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(TransformInfoInterface)", e)
            raise e

    def getInstance(self=None, *args):
        if self is None and not args: return __class__.getInstance_j0()
        if len(args) == 3 and True and (args[0] is None or any(base.__name__ == "AbeClientInformationInterface" for base in type(args[0]).__mro__)) and (args[1] is None or isinstance(args[1], str)) and (args[2] is None or any(base.__name__ == "TransformInfoInterface" for base in type(args[2]).__mro__)):
            return __class__.__dict__["getInstance_j3_1"].__get__(self, __class__)(*args)
        if len(args) == 3:
            return __class__.__dict__["getInstance_j3_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("getInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getInstance(*args)
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.data.tables.transform.info.TransformInfoEntity import TransformInfoEntity
# from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
# from org.allbinary.logic.visual.transform.info.TransformInfoHttpFactory import TransformInfoHttpFactory
# from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoObjectFactory import TransformInfoObjectFactory
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _TransformFactory_instance() -> object:
    return TransformFactory()

lazy_static(TransformFactory, "instance", _TransformFactory_instance)

