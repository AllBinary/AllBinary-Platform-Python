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
# package views.business.context

from __future__ import annotations

from org.allbinary.logic.visual.transform.template.TransformTemplateInterface import TransformTemplateInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class RootContextView(HttpStoreComponentView, TransformTemplateInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("View Name: " + transformInfoInterface.getName(), self, "RootContextView()")
    

    # throws Exception
    def view(self) -> str:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("View Name: " + self.getTransformInfoInterface().getName(), self, "view()")
            viewName: str = self.getName()
            componentInterface: TransformInterface = TransformFactory.getInstance().getInstance(self.abeClientInformation, viewName, self.getTransformInfoInterface())
            return componentInterface.view()
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
    

    # throws Exception
    def getName(self) -> str:
        try:
            objectConfig: NoTemplateTransformInfoObjectConfig = NoTemplateTransformInfoObjectConfig(self.getTransformInfoInterface(), self.getTransformInfoInterface().getObjectConfigInterface().toXmlDoc())
            componentsVector: BasicArrayList = objectConfig.getTransforms()
            if componentsVector.size() == 0:
                raise Exception("Template View Not Set - No Components")
            if componentsVector.size() > 1:
                raise Exception("To Many Root Template Views: " + str(componentsVector.size()))
            transformInfoInterface: TransformInfo = componentsVector.get(0)
            viewName: str = transformInfoInterface.getName()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Root Template With View Name: " + viewName, self, "getName()")
            if StringValidationUtil.getInstance().isEmpty(viewName):
                raise Exception("Template View Not Set - No View Name")
            return viewName
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getName()", e)
            raise e
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.visual.transform.TransformFactory import TransformFactory
from org.allbinary.logic.visual.transform.TransformInterface import TransformInterface
from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from views.business.context.modules.storefront.customizer.template.objectConfig.NoTemplateTransformInfoObjectConfig import NoTemplateTransformInfoObjectConfig


