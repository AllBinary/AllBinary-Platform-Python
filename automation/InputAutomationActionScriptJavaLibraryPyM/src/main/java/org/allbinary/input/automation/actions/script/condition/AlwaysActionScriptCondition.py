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
# package org.allbinary.input.automation.actions.script.condition

from __future__ import annotations

from org.allbinary.input.automation.actions.script.condition.BasicProfileActionScriptCondition import BasicProfileActionScriptCondition
from org.allbinary.input.automation.actions.script.condition.AlwaysActionScriptConditionInterface import AlwaysActionScriptConditionInterface


class AlwaysActionScriptCondition(BasicProfileActionScriptCondition, AlwaysActionScriptConditionInterface):
    NAME: str = "Always On/Off"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.alwaysActionScriptConditionJPanel: AlwaysActionScriptConditionJPanel = None
        self.isOn: bool = False

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 0:
            self._constructor0(*args)
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.input.automation.actions.script.condition.AlwaysActionScriptConditionData import AlwaysActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.AlwaysActionScriptConditionData import AlwaysActionScriptConditionData
        super().__init__(AlwaysActionScriptCondition.NAME, node)
        self._init_fields()
        actionNode: Node = DomSearchHelper.getNode(AlwaysActionScriptConditionData.NAME, node.getChildNodes())
        if actionNode is not None:
            nodeList: NodeList = actionNode.getChildNodes()
            for index in range(0, nodeList.getLength()):
                childNode: Node = nodeList.item(index)
                if childNode.getNodeName().compareTo(AlwaysActionScriptConditionData.IS_ON) == 0:
                    booleanString: str = DomNodeHelper.getTextNodeValue(childNode)
                    self.setIsOn(booleanString)
                else:
                    raise Exception("Action Script Condition Unknown Node")
        else:
            raise Exception("Action Script Condition Node Null")
        self.init()
    

    def _constructor0(self) -> None:
        super().__init__(AlwaysActionScriptCondition.NAME)
        self._init_fields()
        self.init()
    

    def init(self) -> None:
        from org.allbinary.input.automation.actions.script.condition.AlwaysActionScriptConditionJPanel import AlwaysActionScriptConditionJPanel
        self.alwaysActionScriptConditionJPanel = AlwaysActionScriptConditionJPanel(self)
    

    def isIsOn(self) -> bool:
        return self.isOn
    

    def setIsOn(self, isOn: bool) -> None:
        self.isOn = isOn
    

    def showDialog(self) -> None:
        self.alwaysActionScriptConditionJPanel.getAlwaysActionJDialog().setVisible(True)
    

    def toHashMap(self) -> dict:
        from org.allbinary.input.automation.actions.script.condition.AlwaysActionScriptConditionData import AlwaysActionScriptConditionData
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(AlwaysActionScriptConditionData.IS_ON, str(self.isIsOn()))
        self.logUtil.putF("HashMap: " + str(hashMap), self, "toHashMap()")
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.actions.script.condition.AlwaysActionScriptConditionData import AlwaysActionScriptConditionData
        node: Node = super().toXmlNode(document)
        node.appendChild(ModDomHelper.createNodeWithValueNodes(document, AlwaysActionScriptConditionData.NAME, self.toHashMap()))
        return node
    

    # throws Exception
    def shouldProcess(self, frame: int) -> bool:
        if self.isIsOn():
            return super().shouldProcess(frame)
        return False
    

    def log(self) -> None:
        self.logUtil.putF("Is On: " + str(self.isIsOn()), self, "log")
# from java.util.HashMap import HashMap
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


