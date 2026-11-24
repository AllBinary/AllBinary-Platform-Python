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
# package org.allbinary.logic.visual.transform.template

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class TransformTemplateFactory:
    instance: TransformTemplateFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance_j0() -> TransformTemplateFactory:
        return TransformTemplateFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getInstance_j4(self, abeClientInformation: AbeClientInformationInterface, templateName: str, propertiesHashMap: HashMap, pageContext: PageContext) -> TransformTemplateInterface:
        from java.util.HashMap import HashMap
        from org.allbinary.data.tables.transform.info.TransformInfoEntity import TransformInfoEntity
        from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoObjectFactory import TransformInfoObjectFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            transformInfoEntity: TransformInfoEntity = TransformInfoEntityBuilder.getInstance()
            transformInfoInterface: TransformInfoInterface = transformInfoEntity.get(templateName, propertiesHashMap, pageContext)
            return TransformInfoObjectFactory.getInstance().getInstance(abeClientInformation, transformInfoInterface)
        except Exception as e:
            error: str = "Failed To Get Instance"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                self.logUtil.put(error + templateName + "->TemplateFactory", self, "getInstance(viewName, HashMap, PageContext)", e)
            raise e

    def getInstance(self, *args):
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.data.tables.transform.info.TransformInfoEntity import TransformInfoEntity
# from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoObjectFactory import TransformInfoObjectFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _TransformTemplateFactory_instance() -> object:
    return TransformTemplateFactory()

lazy_static(TransformTemplateFactory, "instance", _TransformTemplateFactory_instance)

