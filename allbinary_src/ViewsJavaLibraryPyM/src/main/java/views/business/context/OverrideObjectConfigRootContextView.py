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

from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class OverrideObjectConfigRootContextView(HttpStoreComponentView):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("View Name: " + transformInfoInterface.getName(), self, "OverrideObjectRootContextView()")
    

    # throws Exception
    def view(self) -> str:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("View Name: " + self.getTransformInfoInterface().getName(), self, "view()")
            rootTransformInfoInterface: TransformInfoInterface = TransformInfoHttp(self.getTransformInfoInterface())
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.getTransformInfoInterface().getStoreName())
            stringBuffer.append(CommonSeps.getInstance().SPACE)
            nameStart: str = str(stringBuffer)
            if self.getTransformInfoInterface().getName().indexOf(GeneratorTransformInfoData.NAME) > 0:
                rootTransformInfoInterface.setName(nameStart + str(GeneratorTransformInfoData.NAME))
            elif self.getTransformInfoInterface().getName().indexOf(RootTransformInfoData.NAME) > 0:
                rootTransformInfoInterface.setName(nameStart + str(RootTransformInfoData.NAME))
            else:
                raise Exception("Override Currently Not Supported")
            overrideObjectConfigDocument: Document = self.getTransformInfoInterface().getObjectConfigInterface().toXmlDoc()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Retrieved OverrideObjectConfig: " + XmlDocumentHelper.toString(overrideObjectConfigDocument), self, "view()")
            transformFactory: TransformFactory = TransformFactory.getInstance()
            rootComponentInterface: TransformInterface = transformFactory.getInstance(self.abeClientInformation, rootTransformInfoInterface.getName(), rootTransformInfoInterface)
            transformTemplateInterface: TransformTemplateInterface = rootComponentInterface
            componentInterface: TransformInterface = transformFactory.getInstance(self.abeClientInformation, transformTemplateInterface.getName(), rootComponentInterface.getTransformInfoInterface())
            transformInfoObjectConfigInterface: TransformInfoObjectConfigInterface = TransformInfoObjectConfigAndManipulatorFactory.getInstance().getInstance(self.abeClientInformation, componentInterface.getTransformInfoInterface(), overrideObjectConfigDocument)
            componentInterface.getTransformInfoInterface().setObjectConfigInterface(transformInfoObjectConfigInterface)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Set OverrideObjectConfig: " + str(componentInterface.getTransformInfoInterface().getObjectConfigInterface()), self, "view()")
            return componentInterface.view()
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.visual.transform.TransformFactory import TransformFactory
from org.allbinary.logic.visual.transform.TransformInterface import TransformInterface
from org.allbinary.logic.visual.transform.info.GeneratorTransformInfoData import GeneratorTransformInfoData
from org.allbinary.logic.visual.transform.info.RootTransformInfoData import RootTransformInfoData
from org.allbinary.logic.visual.transform.info.TransformInfoHttp import TransformInfoHttp
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigAndManipulatorFactory import TransformInfoObjectConfigAndManipulatorFactory
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigInterface import TransformInfoObjectConfigInterface
from org.allbinary.logic.visual.transform.template.TransformTemplateInterface import TransformTemplateInterface
from org.allbinary.string.CommonSeps import CommonSeps
from org.w3c.dom.Document import Document


