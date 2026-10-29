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
# package org.allbinary.logic.visual.transform.info.objectConfig

from __future__ import annotations

from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfig import TransformInfoObjectConfig


class GenericStoreTransformInfoObjectConfig(TransformInfoObjectConfig):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 3:
            self._constructor3(*args)
        elif len(args) == 4:
            self._constructor4(*args)
    

    def _constructor2(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.abeClientInformation = abeClientInformation
    

    def _constructor3(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, document: Document) -> None:
        super().__init__(transformInfoInterface, document)
        self._init_fields()
        self.abeClientInformation = abeClientInformation
        self.setDocument(self.generate(self.toXmlDoc()))
    

    def _constructor4(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, name: str, type_: str) -> None:
        super().__init__(transformInfoInterface, name, type_)
        self._init_fields()
        self.abeClientInformation = abeClientInformation
        self.setDocument(self.generate(self.toXmlDoc()))
    

    # throws Exception
    def generate(self, objectConfigDocument: Document) -> Document:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("TransformInfo: ")
            if self.getTransformInfoInterface() is not None:
                stringBuffer.append(self.getTransformInfoInterface().getName())
            else:
                stringBuffer.append("No Owner!?#@")
            self.logUtil.putF(str(stringBuffer), self, "generate()")
        transformInfoHttpStoreInterface: TransformInfoHttp = self.getTransformInfoInterface()
        objectConfigDocumentString: str = XmlDocumentHelper.toString(objectConfigDocument)
        replaceHashMap: dict = self.createReplaceHashMap(transformInfoHttpStoreInterface, objectConfigDocumentString)
        return self.generate(objectConfigDocumentString, replaceHashMap)
    

    # throws Exception
    def createReplaceHashMap(self, transformInfoHttpStoreInterface: TransformInfoHttp, objectConfigDocumentString: str) -> dict:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
        storeName: str = transformInfoHttpStoreInterface.getStoreName()
        hashMap: dict = self.createHashMap(transformInfoHttpStoreInterface, objectConfigDocumentString)
        transformInfoObjectConfigData: TransformInfoObjectConfigData = TransformInfoObjectConfigData.getInstance()
        hashMap.put(transformInfoObjectConfigData.VARKEY + StoreFrontData.getInstance().NAME, storeName)
        pageName: str = TransformTemplateCustomizerUtil.getInstance().getPageNameHack(self.getTransformInfoInterface().getName(), storeName)
        hashMap.put(transformInfoObjectConfigData.VARKEY + TransformInfoData.getInstance().PARTIAL, pageName)
        return hashMap
    

    # throws Exception
    def createHashMap(self, transformInfoHttpStoreInterface: TransformInfoHttp, objectConfigDocumentString: str) -> dict:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
        hashMap: dict = StdUtil.getInstance().createHashMap()
        storeName: str = transformInfoHttpStoreInterface.getStoreName()
        propertiesHashMap: dict = transformInfoHttpStoreInterface.getPropertiesHashMap()
        templateNameOverride: str = StringUtil.getInstance().getNonNull(propertiesHashMap.get(TransformInfoData.getInstance().PARTIAL))
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("TemplateNameOverride: " + templateNameOverride, self, "generate()")
        templateNameStringBuffer: StringMaker = StringMaker()
        templateNameStringBuffer.append(storeName)
        templateNameStringBuffer.append(templateNameOverride)
        templateNameStringBuffer.append(CommonSeps.getInstance().SPACE)
        templateNameStringBuffer.append(RootTransformInfoData.NAME)
        templateNameKey: str = TransformInfoObjectConfigData.getInstance().VARKEY + TransformInfoData.getInstance().OWNER
        if objectConfigDocumentString.find(templateNameKey) != -1:
            templateInterface: TransformTemplateInterface = TransformTemplateFactory.getInstance().getInstance(self.abeClientInformation, str(templateNameStringBuffer), transformInfoHttpStoreInterface.getPropertiesHashMap(), transformInfoHttpStoreInterface.getPageContext())
            selectedTemplate: str = templateInterface.getName()
            hashMap.put(templateNameKey, selectedTemplate)
        return hashMap
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def generate(self, objectConfigDocumentString: str, hashMap: dict) -> Document:
        replace: Replace = Replace(hashMap)
        newObjectConfigDocument: Document = DomDocumentHelper.create(replace.all(objectConfigDocumentString))
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Final ObjectConfig: " + XmlDocumentHelper.toString(newObjectConfigDocument), self, "generate()")
        return newObjectConfigDocument
# from java.util.HashMap import HashMap
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.regex.replace.Replace import Replace
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.visual.transform.info.RootTransformInfoData import RootTransformInfoData
from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
from org.allbinary.logic.visual.transform.info.TransformInfoHttp import TransformInfoHttp
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.template.TransformTemplateFactory import TransformTemplateFactory
from org.allbinary.logic.visual.transform.template.TransformTemplateInterface import TransformTemplateInterface
from org.allbinary.logic.visual.transform.template.util.TransformTemplateCustomizerUtil import TransformTemplateCustomizerUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.w3c.dom.Document import Document


