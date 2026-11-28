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
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        newValueNode: Node = document.createElement(name)
        newValueTextNode: Node = document.createTextNode(text)
        newValueNode.appendChild(newValueTextNode)
        return newValueNode
    

    # throws Exception
    @staticmethod
    def createValueNode(document: Document, text: str) -> Node:
        from org.allbinary.data.tree.dom.DomData import DomData
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return ModDomHelper.createTextNode(document, DomData.VALUE, text)
    

    # throws Exception
    @staticmethod
    def createNameNode(document: Document, text: str) -> Node:
        from org.allbinary.data.tree.dom.DomData import DomData
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return ModDomHelper.createTextNode(document, DomData.NAME, text)
    

    # throws Exception
    @staticmethod
    def createIndexNode(document: Document, index: int) -> Node:
        from org.allbinary.data.tree.dom.DomData import DomData
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return ModDomHelper.createTextNode(document, DomData.INDEX, str(int(index)))
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def createNameValueNodes_j4_1(document: Document, elementName: str, nameText: str, valueText: str) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        newNode: Node = document.createElement(elementName)
        newNode.appendChild(ModDomHelper.createNameNode(document, nameText))
        newNode.appendChild(ModDomHelper.createValueNode(document, valueText))
        return newNode
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def createNameValueNodes_j3_1(document: Document, elementNameAndNameText: str, valueText: str) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        newNode: Node = ModDomHelper.createNameValueNodes(document, elementNameAndNameText, elementNameAndNameText, valueText)
        return newNode
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def createNameValueIndexNodes_j4_1(document: Document, elementNameAndNameText: str, index: int, valueText: str) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        newNode: Node = ModDomHelper.createNameValueNodes(document, elementNameAndNameText, valueText)
        newNode.appendChild(ModDomHelper.createIndexNode(document, index))
        return newNode
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def createNameValueNodes_j3_2(document: Document, rootNode: str, hashMap: HashMap) -> Node:
        from java.util.HashMap import HashMap
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = document.createElement(rootNode)
        return ModDomHelper.createNameValueNodes(document, node, hashMap)
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def createNameValueNodes_j3_3(document: Document, node: Node, hashMap: HashMap) -> Node:
        from java.util.HashMap import HashMap
        from java.util.Set import Set
        from org.allbinary.logic.java.anyType.clazz.ClassUtil import ClassUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
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
            elif isinstance(anyType, HashMap):
                node.appendChild(ModDomHelper.createNameValueNodes(document, name, hashMap))
            else:
                raise Exception("HashMap value is the wrong instance and is: " + str(ClassUtil.viewAll(anyType, CommonSeps.getInstance().NEW_LINE)))
        return node
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def createNameValueNodes_j4_2(document: Document, rootNodeName: str, duplicateNodeName: str, valueVector: BasicArrayList) -> Node:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        stringUtil: StringUtil = StringUtil.getInstance()
        node: Node = document.createElement(rootNodeName)
        size: int = valueVector.size()
        for i in range(0, size):
            value: str = stringUtil.getNonNull(valueVector.get(i))
            node.appendChild(ModDomHelper.createNameValueNodes(document, duplicateNodeName, value))
        return node

    @staticmethod
    def createNameValueNodes(*args):
        if len(args) == 4 and True and (args[0] is None or any(base.__name__ == "Document" for base in type(args[0]).__mro__)) and (args[1] is None or isinstance(args[1], str)) and (args[2] is None or isinstance(args[2], str)) and (args[3] is None or isinstance(args[3], str)):
            return ModDomHelper.createNameValueNodes_j4_1(*args)
        if len(args) == 3 and True and (args[0] is None or any(base.__name__ == "Document" for base in type(args[0]).__mro__)) and (args[1] is None or isinstance(args[1], str)) and (args[2] is None or isinstance(args[2], str)):
            return ModDomHelper.createNameValueNodes_j3_1(*args)
        if len(args) == 3 and True and (args[0] is None or any(base.__name__ == "Document" for base in type(args[0]).__mro__)) and (args[1] is None or isinstance(args[1], str)) and not isinstance(args[2], (str, list, int, float)):
            return ModDomHelper.createNameValueNodes_j3_2(*args)
        if len(args) == 3:
            return ModDomHelper.createNameValueNodes_j3_3(*args)
        if len(args) == 4:
            return ModDomHelper.createNameValueNodes_j4_2(*args)
        return getattr(ModDomHelper, "createNameValueNodes_j" + str(len(args)))(*args)
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def createNameValueIndexNodes_j4_2(document: Document, rootNodeName: str, duplicateNodeName: str, valueVector: BasicArrayList) -> Node:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        stringUtil: StringUtil = StringUtil.getInstance()
        node: Node = document.createElement(rootNodeName)
        size: int = valueVector.size()
        for index in range(0, size):
            value: str = stringUtil.getNonNull(valueVector.get(index))
            node.appendChild(ModDomHelper.createNameValueIndexNodes(document, duplicateNodeName, index, value))
        return node

    @staticmethod
    def createNameValueIndexNodes(*args):
        if len(args) == 4 and True and (args[0] is None or any(base.__name__ == "Document" for base in type(args[0]).__mro__)) and (args[1] is None or isinstance(args[1], str)) and isinstance(args[2], int) and not isinstance(args[2], bool) and (args[3] is None or isinstance(args[3], str)):
            return ModDomHelper.createNameValueIndexNodes_j4_1(*args)
        if len(args) == 4:
            return ModDomHelper.createNameValueIndexNodes_j4_2(*args)
        return getattr(ModDomHelper, "createNameValueIndexNodes_j" + str(len(args)))(*args)
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def createNodeWithValueNodes_j3_1(document: Document, rootNode: str, hashMap: HashMap) -> Node:
        from java.util.HashMap import HashMap
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = document.createElement(rootNode)
        return ModDomHelper.createNodeWithValueNodes(document, node, hashMap)
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def createNodeWithValueNodes_j3_2(document: Document, node: Node, hashMap: HashMap) -> Node:
        from java.util.HashMap import HashMap
        from java.util.Set import Set
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
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

    @staticmethod
    def createNodeWithValueNodes(*args):
        if len(args) == 3 and True and (args[0] is None or any(base.__name__ == "Document" for base in type(args[0]).__mro__)) and (args[1] is None or isinstance(args[1], str)) and not isinstance(args[2], (str, list, int, float)):
            return ModDomHelper.createNodeWithValueNodes_j3_1(*args)
        if len(args) == 3:
            return ModDomHelper.createNodeWithValueNodes_j3_2(*args)
        return getattr(ModDomHelper, "createNodeWithValueNodes_j" + str(len(args)))(*args)
# from java.util.HashMap import HashMap
# from java.util.Set import Set
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.java.anyType.clazz.ClassUtil import ClassUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node


