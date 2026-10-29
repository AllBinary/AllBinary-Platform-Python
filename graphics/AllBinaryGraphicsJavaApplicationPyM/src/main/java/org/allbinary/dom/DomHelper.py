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
# package org.allbinary.dom

from __future__ import annotations



class DomHelper:
    instance: DomHelper = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> DomHelper:
        return DomHelper.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def createDocument(self) -> Document:
        try:
            factory: DocumentBuilderFactory = DocumentBuilderFactory.newInstance()
            builder: DocumentBuilder = factory.newDocumentBuilder()
            document: Document = builder.newDocument()
            return document
        except Exception as e:
            return None
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def createDocument(self, xmlFile: File) -> Document:
        try:
            factory: DocumentBuilderFactory = DocumentBuilderFactory.newInstance()
            builder: DocumentBuilder = factory.newDocumentBuilder()
            document: Document = builder.parse(xmlFile)
            return document
        except Exception as e:
            raise e
    

    # throws Exception
    def toString(self, document: Document) -> str:
        try:
            domSource: DOMSource = DOMSource(document)
            byteArrayOutputStream: ByteArrayOutputStream = ByteArrayOutputStream()
            streamResult: StreamResult = StreamResult(byteArrayOutputStream)
            copyTransformerFactory: TransformerFactory = TransformerFactory.newInstance()
            copyTransformer: Transformer = copyTransformerFactory.newTransformer()
            copyTransformer.transform(domSource, streamResult)
            return str(byteArrayOutputStream)
        except Exception as e:
            raise e
    

    # throws Exception
    def save(self, file: File, document: Document) -> None:
        try:
            copyTransformerFactory: TransformerFactory = TransformerFactory.newInstance()
            copyTransformer: Transformer = copyTransformerFactory.newTransformer()
            domSource: DOMSource = DOMSource(document)
            file.createNewFile()
            streamResult: StreamResult = StreamResult(file)
            copyTransformer.transform(domSource, streamResult)
        except Exception as e:
            raise e
    

    # throws Exception
    def getChildNodeList(self, nodeName: str, nodeList: NodeList) -> NodeList:
        numberOfNodes: int = nodeList.getLength()
        for index in range(0, numberOfNodes):
            node: Node = nodeList.item(index)
            if node.getNodeName().compareTo(nodeName) == 0:
                return node.getChildNodes()
        raise Exception(nodeName + " Node Not Found")
    

    # throws Exception
    def getChildrenWithoutTextNodes(self, nodeName: str, nodeList: NodeList) -> BasicArrayList:
        list_: BasicArrayList = BasicArrayListD()
        childNodeList: NodeList = self.getChildNodeList(nodeName, nodeList)
        numberOfChildren: int = childNodeList.getLength()
        for index in range(0, numberOfChildren):
            node: Node = childNodeList.item(index)
            if node.getNodeType() != Node.TEXT_NODE:
                list_.add(node)
        return list_
    

    # throws Exception
    def getWithoutTextNodes(self, nodeList: NodeList) -> BasicArrayList:
        list_: BasicArrayList = BasicArrayListD()
        numberOfChildren: int = nodeList.getLength()
        for index in range(0, numberOfChildren):
            node: Node = nodeList.item(index)
            if node.getNodeType() != Node.TEXT_NODE:
                list_.add(node)
        return list_
    

    # throws Exception
    def searchNodeList(self, nodeName: str, nodeList: NodeList) -> Node:
        numberOfNodes: int = nodeList.getLength()
        for index in range(0, numberOfNodes):
            node: Node = nodeList.item(index)
            self.logUtil.putF("NodeName: " + str(node.getNodeName()), self, "searchNodeList")
            if node.getNodeName().compareTo(nodeName) == 0:
                return node
        raise Exception(nodeName + " Node Not Found in search")
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def searchNodeList(self, nodeName: str, nodeList: BasicArrayList) -> Node:
        numberOfNodes: int = nodeList.size()
        for index in range(0, numberOfNodes):
            node: Node = nodeList.get(index)
            self.logUtil.putF("NodeName: " + str(node.getNodeName()), self, "searchNodeList")
            if node.getNodeName().compareTo(nodeName) == 0:
                return node
        raise Exception(nodeName + " Node Not Found in search")
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.File import File
# from javax.xml.parsers.DocumentBuilder import DocumentBuilder
# from javax.xml.parsers.DocumentBuilderFactory import DocumentBuilderFactory
# from javax.xml.transform.Transformer import Transformer
# from javax.xml.transform.TransformerFactory import TransformerFactory
# from javax.xml.transform.dom.DOMSource import DOMSource
# from javax.xml.transform.stream.StreamResult import StreamResult
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


DomHelper.instance = DomHelper()

