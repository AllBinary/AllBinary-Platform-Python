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



class DomNodeHelper:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getFirstChildElement(parentNode: Node) -> Node:
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        node: Node = parentNode.getFirstChild()
        if node is not None and node.getNodeType() != Node.ELEMENT_NODE:
            nodeList: NodeList = parentNode.getChildNodes()
            for index in range(0, nodeList.getLength()):
                node = nodeList.item(index)
                if node.getNodeType() == 1:
                    break
        return node
    

    @staticmethod
    def getTextNodeValue_j1(node: Node) -> str:
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.w3c.dom.Node import Node
        nodeTextNode: Node = node.getFirstChild()
        if nodeTextNode is not None:
            return nodeTextNode.getNodeValue()
        else:
            return StringUtil.getInstance().EMPTY_STRING
    

    # throws Exception
    @staticmethod
    def getTextNodeValue_j2(nodeName: str, nodeList: NodeList) -> str:
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        node: Node = DomSearchHelper.getNode(nodeName, nodeList)
        return DomNodeHelper.getTextNodeValue(node)

    @staticmethod
    def getTextNodeValue(*args):
        return getattr(DomNodeHelper, "getTextNodeValue_j" + str(len(args)))(*args)
    

    @staticmethod
    def getTextNodesValue(node: Node) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        stringBuffer: StringMaker = StringMaker()
        nodeList: NodeList = node.getChildNodes()
        for index in range(0, nodeList.getLength()):
            nodeTextNode: Node = nodeList.item(index)
            if nodeTextNode.getNodeType() == Node.TEXT_NODE:
                if nodeTextNode is not None:
                    stringBuffer.append(nodeTextNode.getNodeValue())
        return str(stringBuffer)
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList


