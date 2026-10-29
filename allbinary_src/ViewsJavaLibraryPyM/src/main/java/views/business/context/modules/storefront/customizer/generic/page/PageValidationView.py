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
# package views.business.context.modules.storefront.customizer.generic.page

from __future__ import annotations

from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.business.context.modules.storefront.customizer.generic.page.PageView import PageView


class PageValidationView(PageView, ValidationComponentInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("View Name: " + transformInfoInterface.getName(), self, "PageViewValidation()")
    

    def isValid(self) -> bool:
        try:
            isValid: bool = True
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.IS_VALID)
            transformInfoEntityInterface: TransformInfoEntity = TransformInfoEntityBuilder.getInstance()
            pageObjectConfigInterface: TransformInfoObjectConfigInterface = self.getTransformInfoInterface().getObjectConfigInterface()
            allViewsToBeModifiedVector: BasicArrayList = pageObjectConfigInterface.getGroupTransforms()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Views To Be Modified: " + str(allViewsToBeModifiedVector.size()), self, "get(transformInfoInterface)")
            size: int = allViewsToBeModifiedVector.size()
            for index in range(0, size):
                transformInfoInterface: TransformInfo = allViewsToBeModifiedVector.get(index)
                viewNameOfViewToBeModified: str = transformInfoInterface.getName()
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append(self.getTransformInfoInterface().getName())
                    stringBuffer.append(" is modifying view: ")
                    stringBuffer.append(viewNameOfViewToBeModified)
                    self.logUtil.putF(str(stringBuffer), self, "insert()")
                httpTransformInfoInterface: TransformInfoHttpInterface = self.getTransformInfoInterface()
                specifiedTransformInfoInterface: TransformInfoInterface = transformInfoEntityInterface.get(viewNameOfViewToBeModified, httpTransformInfoInterface.getPropertiesHashMap(), httpTransformInfoInterface.getPageContext())
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append(self.getTransformInfoInterface().getName())
                    stringBuffer.append(" is adding data to view: ")
                    stringBuffer.append(viewNameOfViewToBeModified)
                    self.logUtil.putF(str(stringBuffer), self, "insert()")
                hashMap: dict = StdUtil.getInstance().createHashMap()
                title: str = specifiedTransformInfoInterface.getName().substring(self.getTransformInfoInterface().getStoreName().length())
                if ((title > "index") - (title < "index")) == 0:
                    hashMap.put(TitleData.getInstance().TEXT, str(self.getTransformInfoInterface().getStoreName()) + " - Home Page")
                else:
                    hashMap.put(TitleData.getInstance().TEXT, str(self.getTransformInfoInterface().getStoreName()) + " -" + title)
                pageValidation: PageValidation = PageValidation(hashMap)
                if pageValidation.isValid() == False:
                    isValid = False
                if isValid == True:
                    document: Document = DomDocumentHelper.create()
                    document.appendChild(pageValidation.toXmlNode(document))
                    documentString: str = XmlDocumentHelper.toString(document)
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                        stringBuffer: StringMaker = StringMaker()
                        stringBuffer.append(viewNameOfViewToBeModified)
                        stringBuffer.append(" is changing data in ")
                        stringBuffer.append(str(specifiedTransformInfoInterface.getDataFilePath()))
                        stringBuffer.append(" to the following data:\n")
                        stringBuffer.append(documentString)
                        self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
                    CustomizerUtil.getInstance().write(specifiedTransformInfoInterface, documentString)
            return isValid
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to validate", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            transformInfoEntityInterface: TransformInfoEntity = TransformInfoEntityBuilder.getInstance()
            objectConfig: TransformInfoObjectConfigInterface = self.getTransformInfoInterface().getObjectConfigInterface()
            httpTransformInfoInterface: TransformInfoHttpInterface = self.getTransformInfoInterface()
            allViewsToBeModifiedVector: BasicArrayList = objectConfig.getGroupTransforms()
            size: int = allViewsToBeModifiedVector.size()
            for index in range(0, size):
                transformInfoInterface: TransformInfo = allViewsToBeModifiedVector.get(index)
                viewNameOfViewToBeModified: str = transformInfoInterface.getName()
                specifiedTransformInfoInterface: TransformInfoInterface = transformInfoEntityInterface.get(viewNameOfViewToBeModified, httpTransformInfoInterface.getPropertiesHashMap(), httpTransformInfoInterface.getPageContext())
                hashMap: dict = StdUtil.getInstance().createHashMap()
                title: str = specifiedTransformInfoInterface.getName().substring(self.getTransformInfoInterface().getStoreName().length())
                if ((title > "index") - (title < "index")) == 0:
                    hashMap.put(TitleData.getInstance().TEXT, str(self.getTransformInfoInterface().getStoreName()) + " - Home Page")
                else:
                    hashMap.put(TitleData.getInstance().TEXT, str(self.getTransformInfoInterface().getStoreName()) + " -" + title)
                pageValidation: PageValidation = PageValidation(hashMap)
                if pageValidation.isValid() == False:
                    stringBuffer.append("TransformInfo Name for PageValidation:" + specifiedTransformInfoInterface.getName())
                    stringBuffer.append("PageValidation:" + str(hashMap))
                    stringBuffer.append("PageValidation Info:" + str(pageValidation.validationInfo()))
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "An auto generated page name was invalid."
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.data.tables.transform.info.TransformInfoEntity import TransformInfoEntity
from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigInterface import TransformInfoObjectConfigInterface
from org.allbinary.logic.visual.transform.template.customizer.page.PageValidation import PageValidation
from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleData import TitleData
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from views.business.context.modules.storefront.customizer.CustomizerUtil import CustomizerUtil


