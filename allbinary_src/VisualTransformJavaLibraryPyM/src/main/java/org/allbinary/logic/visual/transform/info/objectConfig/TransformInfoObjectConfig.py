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

from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigInterface import TransformInfoObjectConfigInterface


class TransformInfoObjectConfig(TransformInfoObjectConfigInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.ownerTransformInfoInterface: TransformInfoInterface = None
        self.document: Document = None
        self.outputTypeName: str = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 3:
            self._constructor3(*args)
    

    def _constructor1(self, transformInfoInterface: TransformInfoInterface) -> None:
        self._init_fields()
        self.ownerTransformInfoInterface = transformInfoInterface
        self.createDocument()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("TransformInfo: ")
            if self.ownerTransformInfoInterface is not None:
                stringBuffer.append(self.ownerTransformInfoInterface.getName())
            else:
                stringBuffer.append("No Owner!?#@")
            stringBuffer.append("\nConstructed with document: ")
            stringBuffer.append(str(self))
            self.logUtil.putF(str(stringBuffer), self, "Constructor(TransformInfoInterface)")
    

    def _constructor2(self, transformInfoInterface: TransformInfoInterface, document: Document) -> None:
        self._init_fields()
        self.ownerTransformInfoInterface = transformInfoInterface
        self.document = document
        node: Node = DomSearchHelper.getNodeNoThrow(OutputTypeData.getInstance().NAME, self.getRootNode().getChildNodes())
        if node is not None:
            self.setOutputTypeName(DomNodeHelper.getTextNodeValue(node))
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("TransformInfo: ")
            if self.ownerTransformInfoInterface is not None:
                stringBuffer.append(self.ownerTransformInfoInterface.getName())
            else:
                stringBuffer.append("No Owner!?#@")
            stringBuffer.append("\nConstructed with document: ")
            stringBuffer.append(str(self))
            self.logUtil.putF(str(stringBuffer), self, "Constructor(TransformInfoInterface, Document)")
    

    def _constructor3(self, transformInfoInterface: TransformInfoInterface, name: str, type_: str) -> None:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
        self._init_fields()
        self.ownerTransformInfoInterface = transformInfoInterface
        self.createDocument()
        configNameAttr: Attr = self.document.createAttribute(TransformInfoObjectConfigData.getInstance().NAME)
        configNameAttr.setValue(name)
        objectConfigNode: Node = self.document.getElementsByTagName(TransformInfoObjectConfigData.getInstance().NAME).item(0)
        objectConfigNode.appendChild(configNameAttr)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("TransformInfo: ")
            if self.ownerTransformInfoInterface is not None:
                stringBuffer.append(self.ownerTransformInfoInterface.getName())
            else:
                stringBuffer.append("No Owner!?#@")
            stringBuffer.append("\nConstructed with document: ")
            stringBuffer.append(str(self))
            self.logUtil.putF(str(stringBuffer), self, "Constructor(TransformInfoInterface, name, type)")
    

    def createDocument(self) -> None:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
        self.document = DomDocumentHelper.create()
        objectConfigNode: Node = self.document.createElement(TransformInfoObjectConfigData.getInstance().NAME)
        self.document.appendChild(objectConfigNode)
    

    def getTransformInfoInterface(self) -> TransformInfoInterface:
        return self.ownerTransformInfoInterface
    

    # throws Exception
    def toXmlDoc(self) -> Document:
        return self.document
    

    def setDocument(self, document: Document) -> None:
        self.document = document
    

    def containsView(self, transformInfoInterface: TransformInfoInterface) -> bool:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
        objectConfigNode: Node = self.document.getElementsByTagName(TransformInfoObjectConfigData.getInstance().NAME).item(0)
        viewNodeList: NodeList = objectConfigNode.getChildNodes()
        numberOfViews: int = viewNodeList.getLength()
        for index in range(0, numberOfViews):
            viewNode: Node = viewNodeList.item(index)
            viewAttributes: NamedNodeMap = viewNode.getAttributes()
            attrNode: Attr = viewAttributes.getNamedItem(TransformInfoData.getInstance().NAME)
            if transformInfoInterface.getName().compareTo(attrNode.getValue()) == 0:
                return True
        return False
    

    # throws Exception
    def getTemplateAttributes(self) -> NamedNodeMap:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
        componentNode: Node = self.document.getElementsByTagName(TransformInfoObjectConfigData.getInstance().NAME).item(0)
        return componentNode.getAttributes()
    

    # throws Exception
    def getName(self) -> str:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
        attrNode: Attr = self.getTemplateAttributes().getNamedItem(TransformInfoObjectConfigData.getInstance().NAME)
        return attrNode.getValue()
    

    # throws Exception
    def setName(self, name: str) -> None:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
        attrNode: Attr = self.getTemplateAttributes().getNamedItem(TransformInfoObjectConfigData.getInstance().NAME)
        attrNode.setValue(name)
    

    # throws Exception
    def getNodeVector(self, nodeName: str) -> BasicArrayList:
        componentsNodeList: NodeList = self.document.getElementsByTagName(nodeName)
        if componentsNodeList is not None and componentsNodeList.getLength() > 0:
            viewNodeVector: BasicArrayList = DomSearchHelper.getAllNodes(TransformInfoData.getInstance().NAME, componentsNodeList.item(0).getChildNodes())
            numberOfViews: int = viewNodeVector.size()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Number Of ")
                stringBuffer.append(nodeName)
                stringBuffer.append(" Nodes: ")
                stringBuffer.appendint(numberOfViews)
                self.logUtil.putF(str(stringBuffer), self, "getNodeVector(nodename)")
            return viewNodeVector
        return BasicArrayListD()
    

    # throws Exception
    def getTransformDomNodes(self, nodeName: str) -> BasicArrayList:
        viewVector: BasicArrayList = BasicArrayListD()
        viewNodeVector: BasicArrayList = self.getNodeVector(nodeName)
        size: int = viewNodeVector.size()
        for index in range(0, size):
            viewNode: Node = viewNodeVector.get(index)
            viewVector.add(TransformInfoDomNode(viewNode))
        return viewVector
    

    # throws Exception
    def getTransforms(self, nodeName: str) -> BasicArrayList:
        viewVector: BasicArrayList = BasicArrayListD()
        viewNodeVector: BasicArrayList = self.getNodeVector(nodeName)
        size: int = viewNodeVector.size()
        for index in range(0, size):
            viewNode: Node = viewNodeVector.get(index)
            viewVector.add(TransformInfoDomNode(viewNode).getTransformInfoInterface())
        return viewVector
    

    # throws Exception
    def getTransformsGroup(self, group: str) -> BasicArrayList:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Started: " + group, self, "getTransformsGroup()")
        viewVector: BasicArrayList = BasicArrayListD()
        GROUP: str = TransformInfosData.getInstance().GROUP
        componentsNodeList: NodeList = self.document.getElementsByTagName(GROUP)
        if componentsNodeList is not None and componentsNodeList.getLength() > 0:
            componentsNode: Node = componentsNodeList.item(0)
            length: int = componentsNodeList.getLength()
            for index in range(0, length):
                node: Node = componentsNodeList.item(index)
                attributes: NamedNodeMap = node.getAttributes()
                attrNode: Attr = attributes.getNamedItem(GROUP)
                value: str = attrNode.getValue()
                if ((value > group) - (value < group)) == 0:
                    componentsNode = node
                    break
            viewNodeVector: BasicArrayList = DomSearchHelper.getAllNodes(TransformInfoData.getInstance().NAME, componentsNode.getChildNodes())
            numberOfViews: int = viewNodeVector.size()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Number Of Nodes: " + str(numberOfViews), self, "getTransformsGroup()")
            size: int = viewNodeVector.size()
            for index in range(0, size):
                viewNode: Node = viewNodeVector.get(index)
                viewVector.add(TransformInfoDomNode(viewNode))
        else:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                if componentsNodeList is None:
                    self.logUtil.putF("Number Of Nodes: NULL", self, "getTransformsGroup()")
                else:
                    self.logUtil.putF("Number Of Nodes: 0", self, "getTransformsGroup()")
        return viewVector
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getTransformDomNodes(self) -> BasicArrayList:
        return self.getTransformDomNodes(TransformInfosData.getInstance().GROUP)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getTransforms(self) -> BasicArrayList:
        return self.getTransforms(TransformInfosData.getInstance().NAME)
    

    # throws Exception
    def getGroupTransforms(self) -> BasicArrayList:
        return self.getTransforms(TransformInfosData.getInstance().GROUP)
    

    # throws Exception
    def getParentTransforms(self) -> BasicArrayList:
        return self.getTransforms(TransformInfoData.getInstance().PARENT)
    

    def getRootNode(self) -> Node:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
        return self.document.getElementsByTagName(TransformInfoObjectConfigData.getInstance().NAME).item(0)
    

    def setOutputTypeName(self, outputTypeName: str) -> None:
        self.outputTypeName = outputTypeName
    

    # throws Exception
    def getOutputTypeName(self) -> str:
        return self.outputTypeName
    

    # throws Exception
    def getInputOutputTypeName(self) -> str:
        node: Node = DomSearchHelper.getNode(InputOutputTypeData.getInstance().NAME, self.getRootNode().getChildNodes())
        return DomNodeHelper.getTextNodeValue(node)
    

    # throws Exception
    def getInputOutputTypeFile(self) -> str:
        node: Node = DomSearchHelper.getNode(InputOutputTypeData.getInstance().FILE, self.getRootNode().getChildNodes())
        return DomNodeHelper.getTextNodeValue(node)
    

    # throws Exception
    def getImportUriPath(self) -> str:
        node: Node = DomSearchHelper.getNode(XslData.getInstance().ROOT_IMPORT_URI, self.getRootNode().getChildNodes())
        return DomNodeHelper.getTextNodeValue(node)
    

    def toString(self) -> str:
        try:
            if self.document is not None:
                return XmlDocumentHelper.toString(self.document)
            else:
                return None
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.putF("DOM Document error", self, self.commonStrings.TOSTRING)
            return None

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.InputOutputTypeData import InputOutputTypeData
from org.allbinary.logic.io.OutputTypeData import OutputTypeData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
from org.allbinary.logic.visual.transform.info.TransformInfoDomNode import TransformInfoDomNode
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.info.TransformInfosData import TransformInfosData
from org.allbinary.logic.visual.transform.template.XslData import XslData
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Attr import Attr
from org.w3c.dom.Document import Document
from org.w3c.dom.NamedNodeMap import NamedNodeMap
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


