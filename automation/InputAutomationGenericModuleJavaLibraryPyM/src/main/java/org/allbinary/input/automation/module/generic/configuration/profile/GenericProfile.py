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
# package org.allbinary.input.automation.module.generic.configuration.profile

from __future__ import annotations



class GenericProfile:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.name: str = None
        self.vector: BasicArrayList = None
        self.genericProfileActions: GenericProfileActions = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfileDataWorkerData import GenericProfileDataWorkerData
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfileDataWorkerType import GenericProfileDataWorkerType
        self._init_fields()
        self.setName(DomNodeHelper.getTextNodeValue(node))
        self.vector = BasicArrayListD()
        nodeList: NodeList = node.getChildNodes()
        self.logUtil.putF("Name: " + self.getName() + " Child Nodes: " + str(nodeList.getLength()), self, "Contructor")
        for index in range(0, nodeList.getLength()):
            profileNode: Node = nodeList.item(index)
            if profileNode.getNodeName().compareTo(GenericProfileDataWorkerData.NAME) == 0:
                genericProfileDataWorkerType: GenericProfileDataWorkerType = GenericProfileDataWorkerType.getInstance(profileNode)
                self.logUtil.putF("Adding GenericProfileDataWorkerType: " + str(genericProfileDataWorkerType), self, "Contructor")
                self.vector.add(genericProfileDataWorkerType)
    

    def _constructor1(self, name: str) -> None:
        self._init_fields()
        self.setName(name)
        self.vector = BasicArrayListD()
    

    def getGenericProfileDataWorkerTypeVector(self) -> BasicArrayList:
        return self.vector
    

    def add(self, genericProfileDataWorkerType: GenericProfileDataWorkerType) -> None:
        if not self.vector.contains(genericProfileDataWorkerType):
            self.vector.add(genericProfileDataWorkerType)
    

    def remove(self, genericProfileDataWorkerType: GenericProfileDataWorkerType) -> None:
        self.vector.remove(genericProfileDataWorkerType)
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfileData import GenericProfileData
        node: Node = ModDomHelper.createTextNode(document, GenericProfileData.NAME, self.name)
        size: int = self.vector.size()
        for index in range(0, size):
            genericProfileDataWorkerType: GenericProfileDataWorkerType = self.vector.get(index)
            node.appendChild(genericProfileDataWorkerType.toXmlNode(document))
        return node
    

    def getName(self) -> str:
        return self.name
    

    def setName(self, name: str) -> None:
        self.name = name
    

    def getGenericProfileActions(self) -> GenericProfileActions:
        return self.genericProfileActions
    

    def setGenericProfileActions(self, genericProfileActions: GenericProfileActions) -> None:
        self.genericProfileActions = genericProfileActions
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActions import GenericProfileActions
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


