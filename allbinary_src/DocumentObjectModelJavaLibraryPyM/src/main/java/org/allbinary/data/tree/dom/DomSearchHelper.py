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



class DomSearchHelper:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getNodeNoThrow(nodeName: str, nodeList: NodeList) -> Node:
        numberOfNodes: int = nodeList.getLength()
        for index in range(0, numberOfNodes):
            node: Node = nodeList.item(index)
            if node.getNodeName().compareTo(nodeName) == 0:
                return node
        return None
    

    # throws Exception
    @staticmethod
    def getNode(nodeName: str, nodeList: NodeList) -> Node:
        node: Node = DomSearchHelper.getNodeNoThrow(nodeName, nodeList)
        if node is not None:
            return node
        else:
            raise Exception(nodeName + " Node Not Found in search")
    

    # throws Exception
    @staticmethod
    def getChildNodeList(nodeName: str, nodeList: NodeList) -> NodeList:
        node: Node = DomSearchHelper.getNode(nodeName, nodeList)
        return node.getChildNodes()
    

    # throws Exception
    @staticmethod
    def getAllNodes(nodeName: str, nodeList: NodeList) -> BasicArrayList:
        vector: BasicArrayList = DomSearchHelper.getAllNodesNoThrow(nodeName, nodeList)
        if vector is None:
            raise Exception(nodeName + " Node Not Found in search")
        else:
            return vector
    

    @staticmethod
    def getAllNodesNoThrow(nodeName: str, nodeList: NodeList) -> BasicArrayList:
        nodeVector: BasicArrayList = BasicArrayListD()
        numberOfNodes: int = nodeList.getLength()
        for index in range(0, numberOfNodes):
            node: Node = nodeList.item(index)
            if node.getNodeName().compareTo(nodeName) == 0:
                nodeVector.add(node)
        return nodeVector
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


