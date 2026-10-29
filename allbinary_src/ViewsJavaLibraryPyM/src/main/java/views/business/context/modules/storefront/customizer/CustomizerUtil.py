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
# package views.business.context.modules.storefront.customizer

from __future__ import annotations



class CustomizerUtil:
    instance: CustomizerUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> CustomizerUtil:
        return CustomizerUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getTransformInfoInterfaceToCustomize(self, customizerTransformInfoInterface: TransformInfoInterface, transformInfoInterface: TransformInfoInterface) -> TransformInfoInterface:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("View Name: " + customizerTransformInfoInterface.getName(), self, "getTransformInfoInterfaceToCustomize()")
        transformInfoEntityInterface: TransformInfoEntity = TransformInfoEntityBuilder.getInstance()
        viewName: str = transformInfoInterface.getName()
        httpTransformInfoInterface: TransformInfoHttpInterface = customizerTransformInfoInterface
        customizedTransformInfoInterface: TransformInfoInterface = transformInfoEntityInterface.get(viewName, httpTransformInfoInterface.getPropertiesHashMap(), httpTransformInfoInterface.getPageContext())
        return customizedTransformInfoInterface
    

    # throws Exception
    def getTransformInfoObjectConfigComponentNodesToCustomize(self, customizerTransformInfoInterface: TransformInfoInterface, transformInfoInterface: TransformInfoInterface) -> BasicArrayList:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("View Name: " + customizerTransformInfoInterface.getName(), self, "getTransformInfoObjectConfigComponentNodesToCustomize()")
        transformInfoEntityInterface: TransformInfoEntity = TransformInfoEntityBuilder.getInstance()
        viewName: str = transformInfoInterface.getName()
        httpTransformInfoInterface: TransformInfoHttpInterface = customizerTransformInfoInterface
        customizedTransformInfoInterface: TransformInfoInterface = transformInfoEntityInterface.get(viewName, httpTransformInfoInterface.getPropertiesHashMap(), httpTransformInfoInterface.getPageContext())
        return self.getTransformInfoObjectConfigComponentNodes(customizedTransformInfoInterface)
    

    # throws Exception
    def getTransformInfoObjectConfigComponentNodes(self, transformInfoInterface: TransformInfoInterface) -> BasicArrayList:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("View Name: " + transformInfoInterface.getName(), self, "getTransformInfoObjectConfigComponentNodes()")
        transformInfoObjectConfigInterface: TransformInfoObjectConfigInterface = transformInfoInterface.getObjectConfigInterface()
        return transformInfoObjectConfigInterface.getTransforms()
    

    # throws Exception
    def getTransformInfoObjectConfigGroupComponentNodes(self, transformInfoInterface: TransformInfoInterface) -> BasicArrayList:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("View Name: " + transformInfoInterface.getName(), self, "getTransformInfoObjectConfigComponentNodes()")
        transformInfoObjectConfigInterface: TransformInfoObjectConfigInterface = transformInfoInterface.getObjectConfigInterface()
        return transformInfoObjectConfigInterface.getGroupTransforms()
    

    # throws Exception
    def insert(self, transformInfoInterface: TransformInfoInterface, domNodeInterface: DomNodeInterface) -> None:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("View Name: " + transformInfoInterface.getName(), self, "insert()")
        transformInfoEntityInterface: TransformInfoEntity = TransformInfoEntityBuilder.getInstance()
        allViewsToBeModified: BasicArrayList = self.getTransformInfoObjectConfigGroupComponentNodes(transformInfoInterface)
        document: Document = DomDocumentHelper.create()
        document.appendChild(domNodeInterface.toXmlNode(document))
        documentString: str = XmlDocumentHelper.toString(document)
        stringBuffer: StringMaker = StringMaker()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            stringBuffer.append("Total Views For Modification: ")
            stringBuffer.appendint(allViewsToBeModified.size())
            stringBuffer.append(" New Xml/Data: ")
            stringBuffer.append(documentString)
            self.logUtil.putF(str(stringBuffer), self, "insert()")
        transformInfoInterface.setData(documentString)
        size: int = allViewsToBeModified.size()
        for index in range(0, size):
            transformInfo: TransformInfo = allViewsToBeModified.get(index)
            viewNameOfViewToBeModified: str = transformInfo.getName()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append(transformInfoInterface.getName())
                stringBuffer.append(" is modifying view: ")
                stringBuffer.append(viewNameOfViewToBeModified)
                self.logUtil.putF(str(stringBuffer), self, "insert()")
            httpTransformInfoInterface: TransformInfoHttpInterface = transformInfoInterface
            specifiedTransformInfoInterface: TransformInfoInterface = transformInfoEntityInterface.get(viewNameOfViewToBeModified, httpTransformInfoInterface.getPropertiesHashMap(), httpTransformInfoInterface.getPageContext())
            if specifiedTransformInfoInterface is None:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    stringBuffer.delete(0, stringBuffer.length())
                    stringBuffer.append(transformInfoInterface.getName())
                    stringBuffer.append(" is unable to add data to view: ")
                    stringBuffer.append(viewNameOfViewToBeModified)
                    stringBuffer.append(" since it does not exist")
                    self.logUtil.putF(str(stringBuffer), self, "insert()")
            else:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF(transformInfoInterface.getName() + " is adding data to view: " + viewNameOfViewToBeModified, self, "insert()")
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    stringBuffer.delete(0, stringBuffer.length())
                    stringBuffer.append(viewNameOfViewToBeModified)
                    stringBuffer.append(" is changing data in ")
                    stringBuffer.append(str(specifiedTransformInfoInterface.getDataFilePath()))
                    stringBuffer.append(" to the following data:\n")
                    stringBuffer.append(documentString)
                    self.logUtil.putF(str(stringBuffer), self, "insert()")
                self.write(specifiedTransformInfoInterface, documentString)
    

    # throws Exception
    def write(self, specifiedTransformInfoInterface: TransformInfoInterface, documentString: str) -> None:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("View Name: " + specifiedTransformInfoInterface.getName(), self, "write()")
        transformInfoEntityInterface: TransformInfoEntity = TransformInfoEntityBuilder.getInstance()
        specifiedTransformInfoInterface.setData(documentString)
        transformInfoEntityInterface.update(specifiedTransformInfoInterface.toHashMap())
    

    # throws Exception
    def getViewDataForComponentsInObjectConfig(self, transformInfoInterface: TransformInfoInterface) -> Document:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("View Name: " + transformInfoInterface.getName(), self, "getViewDataForComponentsInObjectConfig()")
        transformInfoObjectConfigInterface: TransformInfoObjectConfigInterface = transformInfoInterface.getObjectConfigInterface()
        allViewsToBeModified: BasicArrayList = transformInfoObjectConfigInterface.getGroupTransforms()
        transformInfoEntityInterface: TransformInfoEntity = TransformInfoEntityBuilder.getInstance()
        size: int = allViewsToBeModified.size()
        for index in range(0, size):
            nextTransformInfoInterface: TransformInfo = allViewsToBeModified.get(index)
            viewNameOfViewToBeModified: str = nextTransformInfoInterface.getName()
            httpTransformInfoInterface: TransformInfoHttpInterface = transformInfoInterface
            specifiedTransformInfoInterface: TransformInfoInterface = transformInfoEntityInterface.get(viewNameOfViewToBeModified, httpTransformInfoInterface.getPropertiesHashMap(), httpTransformInfoInterface.getPageContext())
            return specifiedTransformInfoInterface.getDataDocument()
        raise Exception("No Components Specified in ObjectConfig")
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.data.tables.transform.info.TransformInfoEntity import TransformInfoEntity
from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigInterface import TransformInfoObjectConfigInterface
from org.w3c.dom.Document import Document


CustomizerUtil.instance = CustomizerUtil()

