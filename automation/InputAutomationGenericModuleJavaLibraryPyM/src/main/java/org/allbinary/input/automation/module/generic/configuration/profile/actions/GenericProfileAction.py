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
# package org.allbinary.input.automation.module.generic.configuration.profile.actions

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class GenericProfileAction(DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.name: str = None
        self.genericProfileActionScript: GenericProfileActionScript = None
        self.genericProfileActionJPanel: GenericProfileActionJPanel = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor2(self, genericProfileActionJPanel: GenericProfileActionJPanel, node: Node) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionData import GenericProfileActionData
        self._init_fields()
        actionNameNode: Node = DomSearchHelper.getNode(GenericProfileActionData.NAME, node.getChildNodes())
        if actionNameNode is not None:
            self.name = DomNodeHelper.getTextNodeValue(actionNameNode)
        else:
            raise Exception("Profile Action Name Node Null")
        self.setGenericProfileActionScript(GenericProfileActionScript(self.genericProfileActionJPanel, node))
    

    def _constructor1(self, name: str) -> None:
        self._init_fields()
        self.name = name
        self.setGenericProfileActionScript(GenericProfileActionScript(self.genericProfileActionJPanel))
    

    def getName(self) -> str:
        return self.name
    

    def setName(self, name: str) -> None:
        self.name = name
    

    def toHashMap(self) -> dict:
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionData import GenericProfileActionData
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(GenericProfileActionData.NAME, self.name)
        self.logUtil.putF("HashMap: " + str(hashMap), self, "toHashMap()")
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionData import GenericProfileActionData
        node: Node = ModDomHelper.createNodeWithValueNodes(document, GenericProfileActionData.NAME, self.toHashMap())
        node.appendChild(self.getGenericProfileActionScript().toXmlNode(document))
        return node
    

    def getGenericProfileActionScript(self) -> GenericProfileActionScript:
        return self.genericProfileActionScript
    

    def setGenericProfileActionScript(self, genericProfileActionScript: GenericProfileActionScript) -> None:
        self.genericProfileActionScript = genericProfileActionScript
# from java.util.HashMap import HashMap
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.GenericProfileActionScript import GenericProfileActionScript
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


