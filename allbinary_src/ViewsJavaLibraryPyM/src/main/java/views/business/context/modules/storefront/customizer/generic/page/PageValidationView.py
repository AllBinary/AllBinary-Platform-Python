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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.business.context.modules.storefront.customizer.generic.page.PageView import PageView


@java_inherited_overloads
class PageValidationView(*java_bases(PageView, ValidationComponentInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__(transformInfoInterface)
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("View Name: " + transformInfoInterface.getName(), self, "PageViewValidation()")
    

    def isValid(self) -> bool:
        from java.util.HashMap import HashMap
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.data.tables.transform.info.TransformInfoEntity import TransformInfoEntity
        from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigInterface import TransformInfoObjectConfigInterface
        from org.allbinary.logic.visual.transform.template.customizer.page.PageValidation import PageValidation
        from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleData import TitleData
        from org.w3c.dom.Document import Document
        from views.business.context.modules.storefront.customizer.CustomizerUtil import CustomizerUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            isValid: bool = True
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.IS_VALID)
            transformInfoEntityInterface: TransformInfoEntity = TransformInfoEntityBuilder.getInstance()
            pageObjectConfigInterface: TransformInfoObjectConfigInterface = self.getTransformInfoInterface().getObjectConfigInterface()
            allViewsToBeModifiedVector: BasicArrayList = pageObjectConfigInterface.getGroupTransforms()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Views To Be Modified: " + str(allViewsToBeModifiedVector.size()), self, "get(transformInfoInterface)")
            size: int = allViewsToBeModifiedVector.size()
            for index in range(0, size):
                transformInfoInterface: TransformInfo = allViewsToBeModifiedVector.get(index)
                viewNameOfViewToBeModified: str = transformInfoInterface.getName()
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append(self.getTransformInfoInterface().getName())
                    stringBuffer.append(" is modifying view: ")
                    stringBuffer.append(viewNameOfViewToBeModified)
                    self.logUtil.putF(str(stringBuffer), self, "insert()")
                httpTransformInfoInterface: TransformInfoHttpInterface = self.getTransformInfoInterface()
                specifiedTransformInfoInterface: TransformInfoInterface = transformInfoEntityInterface.get(viewNameOfViewToBeModified, httpTransformInfoInterface.getPropertiesHashMap(), httpTransformInfoInterface.getPageContext())
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append(self.getTransformInfoInterface().getName())
                    stringBuffer.append(" is adding data to view: ")
                    stringBuffer.append(viewNameOfViewToBeModified)
                    self.logUtil.putF(str(stringBuffer), self, "insert()")
                hashMap: HashMap = StdUtil.getInstance().createHashMap()
                title: str = specifiedTransformInfoInterface.getName().substring(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.getTransformInfoInterface().getStoreName()))
                if ((title > "index") - (title < "index")) == 0:
                    hashMap.put(TitleData.getInstance().TEXT, str(self.getTransformInfoInterface().getStoreName()) + " - Home Page")
                else:
                    hashMap.put(TitleData.getInstance().TEXT, str(self.getTransformInfoInterface().getStoreName()) + " -" + title)
                pageValidation: PageValidation = PageValidation(hashMap)
                if java_predicate(pageValidation, "isValid") == False:
                    isValid = False
                if isValid == True:
                    document: Document = DomDocumentHelper.create()
                    document.appendChild(pageValidation.toXmlNode(document))
                    documentString: str = XmlDocumentHelper.toString(document)
                    if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
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
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to validate", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        from java.util.HashMap import HashMap
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.data.tables.transform.info.TransformInfoEntity import TransformInfoEntity
        from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigInterface import TransformInfoObjectConfigInterface
        from org.allbinary.logic.visual.transform.template.customizer.page.PageValidation import PageValidation
        from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleData import TitleData
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
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
                hashMap: HashMap = StdUtil.getInstance().createHashMap()
                title: str = specifiedTransformInfoInterface.getName().substring(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.getTransformInfoInterface().getStoreName()))
                if ((title > "index") - (title < "index")) == 0:
                    hashMap.put(TitleData.getInstance().TEXT, str(self.getTransformInfoInterface().getStoreName()) + " - Home Page")
                else:
                    hashMap.put(TitleData.getInstance().TEXT, str(self.getTransformInfoInterface().getStoreName()) + " -" + title)
                pageValidation: PageValidation = PageValidation(hashMap)
                if java_predicate(pageValidation, "isValid") == False:
                    stringBuffer.append("TransformInfo Name for PageValidation:" + specifiedTransformInfoInterface.getName())
                    stringBuffer.append("PageValidation:" + str(hashMap))
                    stringBuffer.append("PageValidation Info:" + str(pageValidation.validationInfo()))
            return str(stringBuffer)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "An auto generated page name was invalid."
    

    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return None
    

    # throws Exception
    def getTransformInfoInterface(self) -> TransformInfoInterface:
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        return java_super_call(super(), "getTransformInfoInterface")
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.data.tables.transform.info.TransformInfoEntity import TransformInfoEntity
# from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
# from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
# from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
# from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigInterface import TransformInfoObjectConfigInterface
# from org.allbinary.logic.visual.transform.template.customizer.page.PageValidation import PageValidation
# from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleData import TitleData
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from views.business.context.modules.storefront.customizer.CustomizerUtil import CustomizerUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


