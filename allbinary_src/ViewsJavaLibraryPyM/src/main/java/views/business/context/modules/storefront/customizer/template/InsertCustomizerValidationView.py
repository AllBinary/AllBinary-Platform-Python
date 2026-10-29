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
# package views.business.context.modules.storefront.customizer.template

from __future__ import annotations

from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


#Sets Template Type
class InsertCustomizerValidationView(HttpStoreComponentView, ValidationComponentInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.viewName: str = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("View Name: " + transformInfoInterface.getName(), self, self.commonStrings.CONSTRUCTOR)
        requestHashMap: dict = RequestParams(self.getPageContext()).toHashMap()
        self.viewName = requestHashMap.get(TransformInfoData.getInstance().NAME)
    

    def isValid(self) -> bool:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Started Validation", self, self.commonStrings.IS_VALID)
            isValid: bool = True
            if StringValidationUtil.getInstance().isEmpty(self.viewName):
                isValid = False
            else:
                objectConfig: NoTemplateTransformInfoObjectConfig = NoTemplateTransformInfoObjectConfig(self.getTransformInfoInterface(), self.getTransformInfoInterface().getObjectConfigInterface().toXmlDoc())
                componentVector: BasicArrayList = objectConfig.getGroupTransforms()
                size: int = componentVector.size()
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append("Pointing ")
                    stringBuffer.appendint(componentVector.size())
                    stringBuffer.append(" Components")
                    self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
                for index in range(0, size):
                    transformInfo: TransformInfo = componentVector.get(index)
                    transformInfoName: str = transformInfo.getName()
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                        self.logUtil.putF("Setting Template Component with ViewName: " + transformInfoName, self, self.commonStrings.IS_VALID)
                    componentInterface: TransformInterface = TransformFactory.getInstance().getInstance(self.abeClientInformation, transformInfoName, self.getTransformInfoInterface())
                    templateViewObjectConfig: InsertTemplateCustomizerTransformInfoObjectConfig = InsertTemplateCustomizerTransformInfoObjectConfig(componentInterface.getTransformInfoInterface(), componentInterface.getTransformInfoInterface().getObjectConfigInterface().toXmlDoc())
                    storeName: str = self.getTransformInfoInterface().getStoreName()
                    endIndex: int = self.viewName.find(storeName) + len(storeName)
                    storePrepend: str = self.viewName[0:endIndex]
                    viewNamePostfix: str = self.viewName[endIndex:len(self.viewName)]
                    newViewNameStringBuffer: StringMaker = StringMaker()
                    newViewNameStringBuffer.append(storePrepend)
                    commonSeps: CommonSeps = CommonSeps.getInstance()
                    transformInfosData: TransformInfosData = TransformInfosData.getInstance()
                    if transformInfoName.find(transformInfosData.SMALL_PREVIEW) >= 0:
                        newViewNameStringBuffer.append(commonSeps.SPACE)
                        newViewNameStringBuffer.append(transformInfosData.SMALL_PREVIEW)
                    elif transformInfoName.find(transformInfosData.PREVIEW) >= 0:
                        newViewNameStringBuffer.append(commonSeps.SPACE)
                        newViewNameStringBuffer.append(transformInfosData.PREVIEW)
                    newViewNameStringBuffer.append(commonSeps.SPACE)
                    newViewNameStringBuffer.append(viewNamePostfix)
                    if transformInfoName.find(GeneratorTransformInfoData.NAME) >= 0:
                        newViewNameStringBuffer.append(commonSeps.SPACE)
                        newViewNameStringBuffer.append(GeneratorTransformInfoData.NAME)
                    newViewName: str = str(newViewNameStringBuffer)
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                        stringBuffer: StringMaker = StringMaker()
                        stringBuffer.append("Template Component: ")
                        stringBuffer.append(transformInfoName)
                        stringBuffer.append("\n Now Pointing To View Name: ")
                        stringBuffer.append(newViewName)
                        self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
                    templateViewObjectConfig.set(newViewName)
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                        stringBuffer: StringMaker = StringMaker()
                        stringBuffer.append("Template Component: ")
                        stringBuffer.append(transformInfoName)
                        stringBuffer.append("\n with ObjectConfig: ")
                        stringBuffer.append(str(templateViewObjectConfig))
                        self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
                    componentInterface.getTransformInfoInterface().setObjectConfigInterface(templateViewObjectConfig)
                    updatedTransformInfoHashMap: dict = componentInterface.getTransformInfoInterface().toHashMap()
                    TransformInfoEntityBuilder.getInstance().update(updatedTransformInfoHashMap)
            return isValid
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to validate", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Error: Template Name Is Empty.")
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Getting Validation Info"
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    # throws Exception
    def view(self) -> str:
        return self.views.ValidationOnlyTempUtil.getInstance().view(self)
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.visual.transform.TransformFactory import TransformFactory
from org.allbinary.logic.visual.transform.TransformInterface import TransformInterface
from org.allbinary.logic.visual.transform.info.GeneratorTransformInfoData import GeneratorTransformInfoData
from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.info.TransformInfosData import TransformInfosData
from org.allbinary.string.CommonSeps import CommonSeps
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from views.business.context.modules.storefront.customizer.template.objectConfig.InsertTemplateCustomizerTransformInfoObjectConfig import InsertTemplateCustomizerTransformInfoObjectConfig
from views.business.context.modules.storefront.customizer.template.objectConfig.NoTemplateTransformInfoObjectConfig import NoTemplateTransformInfoObjectConfig


