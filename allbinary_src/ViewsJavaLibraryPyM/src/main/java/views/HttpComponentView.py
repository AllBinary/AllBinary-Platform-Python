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
from org.allbinary.logic.visual.transform.info.TransformInfoHttpComposite import TransformInfoHttpComposite


class HttpComponentView(TransformInfoHttpComposite, TransformInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        self.domNodeInterfaceVector: BasicArrayList = None
        self.transformDocumentInterface: TransformDocumentInterface = None
        self.NO_TYPE: int = 0
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("View Name: " + transformInfoInterface.getName(), self, self.commonStrings.CONSTRUCTOR)
        self.domNodeInterfaceVector = BasicArrayListD()
        self.setTransformDocumentInterface(TransformHttpRequestDocumentFactory.getInstance(self.getPageContext(), self.getWeblisketSession()))
    

    def getTypeId(self) -> int:
        return self.NO_TYPE
    

    def getTransformDocumentInterface(self) -> TransformDocumentInterface:
        return self.transformDocumentInterface
    

    def setTransformDocumentInterface(self, transformDocumentInterface: TransformDocumentInterface) -> None:
        self.transformDocumentInterface = transformDocumentInterface
    

    def addDomNodeInterface(self, domNodeInterface: DomNodeInterface) -> None:
        self.domNodeInterfaceVector.add(domNodeInterface)
    

    # throws Exception
    def toXmlDoc(self) -> Document:
        try:
            size: int = self.domNodeInterfaceVector.size()
            for index in range(0, size):
                domNodeInterface: DomNodeInterface = self.domNodeInterfaceVector.get(index)
                self.transformDocumentInterface.getBaseNode().appendChild(domNodeInterface.toXmlNode(self.transformDocumentInterface.getDoc()))
            return self.getTransformDocumentInterface().getDoc()
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "toXmlDoc()", e)
            raise e
    

    # throws Exception
    def getDoc(self) -> Document:
        document: Document = self.getTransformInfoInterface().getDataDocument()
        node: Node = DomNodeHelper.getFirstChildElement(document)
        if node is not None:
            dataNode: Node = self.getTransformDocumentInterface().getDoc().importNode(node, True)
            if dataNode is not None:
                self.getTransformDocumentInterface().getBaseNode().appendChild(dataNode)
        return self.getTransformDocumentInterface().getDoc()
    

    # throws Exception
    def view(self) -> str:
        try:
            self.toXmlDoc()
            success: str = XmlDocumentHelper.toString(self.getDoc())
            result: str = BasicTransformer(self.abeClientInformation, self.getTransformInfoInterface()).translate(success)
            return result
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
from org.allbinary.logic.visual.transform.BasicTransformer import BasicTransformer
from org.allbinary.logic.visual.transform.data.TransformDocumentInterface import TransformDocumentInterface
from org.allbinary.logic.visual.transform.data.TransformHttpRequestDocumentFactory import TransformHttpRequestDocumentFactory
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


