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
# package views

from __future__ import annotations

from org.allbinary.logic.visual.transform.TransformInterface import TransformInterface


class CustomUriTransformView(TransformInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        self.transformInfoInterface: TransformInfoInterface = None
        self.transformDocumentInterface: TransformDocumentInterface = None
        self.NO_TYPE: int = 0
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("View Name: " + transformInfoInterface.getName(), self, self.commonStrings.CONSTRUCTOR)
        self.setTransformInfoInterface(transformInfoInterface)
        self.setTransformDocumentInterface(TransformDocumentFactory.getInstance())
    

    def getTypeId(self) -> int:
        return self.NO_TYPE
    

    def getTransformInfoInterface(self) -> TransformInfoInterface:
        return self.transformInfoInterface
    

    def setTransformInfoInterface(self, transformInfoInterface: TransformInfoInterface) -> None:
        self.transformInfoInterface = transformInfoInterface
    

    def getTransformDocumentInterface(self) -> TransformDocumentInterface:
        return self.transformDocumentInterface
    

    def setTransformDocumentInterface(self, transformDocumentInterface: TransformDocumentInterface) -> None:
        self.transformDocumentInterface = transformDocumentInterface
    

    def toXmlDoc(self) -> Document:
        return self.transformDocumentInterface.getDoc()
    

    # throws Exception
    def getDoc(self) -> Document:
        document: Document = self.getTransformInfoInterface().getDataDocument()
        dataNode: Node = self.getTransformDocumentInterface().getDoc().importNode(document.getFirstChild(), True)
        if dataNode is not None:
            self.getTransformDocumentInterface().getBaseNode().appendChild(dataNode)
        return self.getTransformDocumentInterface().getDoc()
    

    # throws Exception
    def view(self) -> str:
        try:
            success: str = XmlDocumentHelper.toString(self.getDoc())
            result: str = TransformInfoCustomUriTransformer(self.abeClientInformation, self.getTransformInfoInterface()).translate(success)
            return result
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
from org.allbinary.logic.visual.transform.TransformInfoCustomUriTransformer import TransformInfoCustomUriTransformer
from org.allbinary.logic.visual.transform.data.TransformDocumentFactory import TransformDocumentFactory
from org.allbinary.logic.visual.transform.data.TransformDocumentInterface import TransformDocumentInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


