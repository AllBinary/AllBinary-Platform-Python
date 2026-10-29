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
# package views.compound.objectConfig

from __future__ import annotations

from org.allbinary.logic.visual.transform.info.objectConfig.GenericStoreTransformInfoObjectConfig import GenericStoreTransformInfoObjectConfig


class CompoundContextTransformInfoObjectConfig(GenericStoreTransformInfoObjectConfig):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 3:
            self._constructor3(*args)
        elif len(args) == 4:
            self._constructor4(*args)
    

    def _constructor2(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(abeClientInformation, transformInfoInterface)
        self._init_fields()
    

    def _constructor3(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, document: Document) -> None:
        super().__init__(abeClientInformation, transformInfoInterface, document)
        self._init_fields()
        self.setDocument(self.generate(self.toXmlDoc()))
    

    def _constructor4(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, name: str, type_: str) -> None:
        super().__init__(abeClientInformation, transformInfoInterface, name, type_)
        self._init_fields()
        self.setDocument(self.generate(self.toXmlDoc()))
    

    # throws Exception
    def get(self) -> str:
        storeName: str = self.getTransformInfoInterface().getStoreName()
        httpTransformInfoInterface: TransformInfoHttpInterface = self.getTransformInfoInterface()
        templateNameOverride: str = StringUtil.getInstance().getNonNull(httpTransformInfoInterface.getPropertiesHashMap().get(TransformInfoData.getInstance().PARTIAL))
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(storeName)
        stringBuffer.append(templateNameOverride)
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(RootTransformInfoData.NAME)
        rootComponentInterface: TransformInterface = TransformFactory.getInstance().getInstance(self.abeClientInformation, str(stringBuffer), self.getTransformInfoInterface())
        viewVector: BasicArrayList = self.getTransformDomNodes()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Root View Called with: " + str(viewVector.size()), self, "get(transformInfoInterface)")
        rootView: str = rootComponentInterface.view()
        startXMLHeader: str = "<xsl:text disable-output-escaping=\"yes\" ><![CDATA["
        endXMLHeader: str = "]]></xsl:text>"
        size: int = viewVector.size()
        for index in range(0, size):
            objectConfigTransformInfoDomNode: TransformInfoDomNode = viewVector.get(index)
            templateKey: str = objectConfigTransformInfoDomNode.getReplaceKey()
            componentInterface: TransformInterface = TransformFactory.getInstance().getInstance(self.abeClientInformation, objectConfigTransformInfoDomNode.getTransformInfoInterface().getName(), self.getTransformInfoInterface())
            replacementViewString: str = componentInterface.view()
            replacementViewString = DocumentToNode.convertDocumentToNodeString(replacementViewString)
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append(startXMLHeader)
            stringBuffer.append(replacementViewString)
            stringBuffer.append(endXMLHeader)
            templateValue: str = str(stringBuffer)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append("Replacing: ")
                stringBuffer.append(templateKey)
                stringBuffer.append(" with ")
                stringBuffer.append(templateValue)
                self.logUtil.putF(str(stringBuffer), self, "get()")
            replace: Replace = Replace(templateKey, templateValue)
            rootView = replace.all(rootView)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("End: Result of a compound view: " + rootView, self, "get()")
        return rootView
    

    # throws Exception
    def createInputStream(self) -> InputStream:
        completeTemplateViewBytes: list[int] = self.get().getBytes()
        bais: ByteArrayInputStream = ByteArrayInputStream(completeTemplateViewBytes)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Template: " + str(bytes(completeTemplateViewBytes).decode()), self, "createInputStream()")
        return bais
# from java.io.ByteArrayInputStream import ByteArrayInputStream
# from java.io.InputStream import InputStream
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.data.tree.dom.document.DocumentToNode import DocumentToNode
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.regex.replace.Replace import Replace
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.visual.transform.TransformFactory import TransformFactory
from org.allbinary.logic.visual.transform.TransformInterface import TransformInterface
from org.allbinary.logic.visual.transform.info.RootTransformInfoData import RootTransformInfoData
from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
from org.allbinary.logic.visual.transform.info.TransformInfoDomNode import TransformInfoDomNode
from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.string.CommonSeps import CommonSeps
from org.w3c.dom.Document import Document


