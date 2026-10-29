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
# package views.business.context.modules.storefront.generator

from __future__ import annotations

from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class GeneratorStoreFrontContextView(HttpStoreComponentView):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("View Name: " + transformInfoInterface.getName(), self, self.commonStrings.CONSTRUCTOR)
    

    # throws Exception
    def view(self, group: str) -> str:
        result: str = TransformsGeneratorUtil.getInstance().generateComponentsFromObjectConfig(self.abeClientInformation, self.getTransformInfoInterface(), group)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPEXTRAOUTPUT):
            return result
        else:
            return StringUtil.getInstance().EMPTY_STRING
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def view(self) -> str:
        try:
            return self.view(TransformInfosData.getInstance().ALL)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.visual.transform.generator.TransformsGeneratorUtil import TransformsGeneratorUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.info.TransformInfosData import TransformInfosData


