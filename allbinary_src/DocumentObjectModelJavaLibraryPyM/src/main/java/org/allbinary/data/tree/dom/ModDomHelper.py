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
# package org.allbinary.data.tree.dom

from __future__ import annotations



class ModDomHelper:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def createTextNode(document: Document, name: str, text: str) -> Node:
        newValueNode: Node = document.createElement(name)
        newValueTextNode: Node = document.createTextNode(text)
        newValueNode.appendChild(newValueTextNode)
        return newValueNode
    

    # throws Exception
    @staticmethod
    def createValueNode(document: Document, text: str) -> Node:
        from org.allbinary.data.tree.dom.DomData import DomData
        return ModDomHelper.createTextNode(document, DomData.VALUE, text)
    

    # throws Exception
    @staticmethod
    def createNameNode(document: Document, text: str) -> Node:
        from org.allbinary.data.tree.dom.DomData import DomData
        return ModDomHelper.createTextNode(document, DomData.NAME, text)
    

    # throws Exception
    @staticmethod
    def createIndexNode(document: Document, index: int) -> Node:
        from org.allbinary.data.tree.dom.DomData import DomData
        return ModDomHelper.createTextNode(document, DomData.INDEX, str(int(index)))
    

    # throws Exception
    @staticmethod
    def createNameValueNodes(document: Document, elementName: str, nameText: str, valueText: str) -> Node:
        newNode: Node = document.createElement(elementName)
        newNode.appendChild(ModDomHelper.createNameNode(document, nameText))
        newNode.appendChild(ModDomHelper.createValueNode(document, valueText))
        return newNode
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def createNameValueNodes(document: Document, elementNameAndNameText: str, valueText: str) -> Node:
        newNode: Node = ModDomHelper.createNameValueNodes(document, elementNameAndNameText, elementNameAndNameText, valueText)
        return newNode
    

    # throws Exception
    @staticmethod
    def createNameValueIndexNodes(document: Document, elementNameAndNameText: str, index: int, valueText: str) -> Node:
        newNode: Node = ModDomHelper.createNameValueNodes(document, elementNameAndNameText, valueText)
        newNode.appendChild(ModDomHelper.createIndexNode(document, index))
        return newNode
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def createNameValueNodes(document: Document, rootNode: str, hashMap: dict) -> Node:
        node: Node = document.createElement(rootNode)
        return ModDomHelper.createNameValueNodes(document, node, hashMap)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def createNameValueNodes(document: Document, node: Node, hashMap: dict) -> Node:
        stringUtil: StringUtil = StringUtil.getInstance()
        keySet: Set = hashMap.keySet()
        keyArray: list[object] = keySet.toArray()
        size: int = len(keyArray)
        for i in range(0, size):
            objectKey: object = keyArray[i]
            name: str = objectKey
            anyType: object = hashMap.get(objectKey)
            if anyType is None:
                value: str = stringUtil.EMPTY_STRING
                node.appendChild(ModDomHelper.createNameValueNodes(document, name, value))
            elif isinstance(anyType, str):
                value: str = stringUtil.getNonNull(anyType)
                node.appendChild(ModDomHelper.createNameValueNodes(document, name, value))
            elif isinstance(anyType, dict):
                node.appendChild(ModDomHelper.createNameValueNodes(document, name, hashMap))
            else:
                raise Exception("HashMap value is the wrong instance and is: " + str(ClassUtil.viewAll(anyType, CommonSeps.getInstance().NEW_LINE)))
        return node
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def createNameValueNodes(document: Document, rootNodeName: str, duplicateNodeName: str, valueVector: BasicArrayList) -> Node:
        stringUtil: StringUtil = StringUtil.getInstance()
        node: Node = document.createElement(rootNodeName)
        size: int = valueVector.size()
        for i in range(0, size):
            value: str = stringUtil.getNonNull(valueVector.get(i))
            node.appendChild(ModDomHelper.createNameValueNodes(document, duplicateNodeName, value))
        return node
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def createNameValueIndexNodes(document: Document, rootNodeName: str, duplicateNodeName: str, valueVector: BasicArrayList) -> Node:
        stringUtil: StringUtil = StringUtil.getInstance()
        node: Node = document.createElement(rootNodeName)
        size: int = valueVector.size()
        for index in range(0, size):
            value: str = stringUtil.getNonNull(valueVector.get(index))
            node.appendChild(ModDomHelper.createNameValueIndexNodes(document, duplicateNodeName, index, value))
        return node
    

    # throws Exception
    @staticmethod
    def createNodeWithValueNodes(document: Document, rootNode: str, hashMap: dict) -> Node:
        node: Node = document.createElement(rootNode)
        return ModDomHelper.createNodeWithValueNodes(document, node, hashMap)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def createNodeWithValueNodes(document: Document, node: Node, hashMap: dict) -> Node:
        stringUtil: StringUtil = StringUtil.getInstance()
        keySet: Set = hashMap.keySet()
        keyArray: list[object] = keySet.toArray()
        size: int = len(keyArray)
        for i in range(0, size):
            name: str = keyArray[i]
            anyType: object = hashMap.get(name)
            value: str = stringUtil.getNonNull(anyType)
            node.appendChild(ModDomHelper.createTextNode(document, name, value))
        return node
# from java.util.HashMap import HashMap
# from java.util.Set import Set
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.java.anyType.clazz.ClassUtil import ClassUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


