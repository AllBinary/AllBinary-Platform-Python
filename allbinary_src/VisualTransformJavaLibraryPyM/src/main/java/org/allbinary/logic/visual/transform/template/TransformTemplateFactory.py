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



class TransformTemplateFactory:
    instance: TransformTemplateFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> TransformTemplateFactory:
        return TransformTemplateFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, abeClientInformation: AbeClientInformationInterface, templateName: str, propertiesHashMap: dict, pageContext: PageContext) -> TransformTemplateInterface:
        try:
            transformInfoEntity: TransformInfoEntity = TransformInfoEntityBuilder.getInstance()
            transformInfoInterface: TransformInfoInterface = transformInfoEntity.get(templateName, propertiesHashMap, pageContext)
            return TransformInfoObjectFactory.getInstance().getInstance(abeClientInformation, transformInfoInterface)
        except Exception as e:
            error: str = "Failed To Get Instance"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                self.logUtil.put(error + templateName + "->TemplateFactory", self, "getInstance(viewName, HashMap, PageContext)", e)
            raise e
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.data.tables.transform.info.TransformInfoEntity import TransformInfoEntity
from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.info.TransformInfoObjectFactory import TransformInfoObjectFactory


TransformTemplateFactory.instance = TransformTemplateFactory()

