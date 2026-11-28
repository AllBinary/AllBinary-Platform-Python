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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.input.automation.actions.script.condition.BasicProfileActionScriptCondition import BasicProfileActionScriptCondition
from org.allbinary.input.automation.actions.script.condition.TimeIntervalActionScriptConditionInterface import TimeIntervalActionScriptConditionInterface


@java_inherited_overloads
class TimeIntervalActionScriptCondition(*java_bases(BasicProfileActionScriptCondition, TimeIntervalActionScriptConditionInterface)):
    NAME: str = "Time Interval"
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("timeIntervalActionScriptConditionJPanel", None)
        vars(self).setdefault("timeHelper", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "timeIntervalActionScriptConditionJPanel" not in vars(self): self.timeIntervalActionScriptConditionJPanel: TimeIntervalActionScriptConditionJPanel = None
        if "timeHelper" not in vars(self): self.timeHelper: TimeDelayHelper = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 0:
            __class__._constructor0(self, *args)
    

    def _constructor1(self, node: Node) -> None:
        __class__._java_defaults(self)
        from org.allbinary.input.automation.actions.script.condition.TimeIntervalActionScriptConditionData import TimeIntervalActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.TimeIntervalActionScriptConditionData import TimeIntervalActionScriptConditionData
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        super().__init__(TimeIntervalActionScriptCondition.NAME, node)
        __class__._init_fields(self)
        actionNode: Node = DomSearchHelper.getNode(TimeIntervalActionScriptConditionData.NAME, node.getChildNodes())
        if actionNode is not None:
            nodeList: NodeList = actionNode.getChildNodes()
            for index in range(0, nodeList.getLength()):
                childNode: Node = nodeList.item(index)
                if childNode.getNodeName().compareTo(TimeIntervalActionScriptConditionData.TIME) == 0:
                    interval: str = DomNodeHelper.getTextNodeValue(childNode)
                    self.setTimeDelayHelper(TimeDelayHelper(str(interval)))
                else:
                    raise Exception("Time Interval Action Script Condition Unknown Node")
        else:
            raise Exception("Time Interval Action Script Condition Node Null")
        self.init()
    

    def _constructor0(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        super().__init__(TimeIntervalActionScriptCondition.NAME)
        __class__._init_fields(self)
        self.setTimeDelayHelper(TimeDelayHelper(0))
        self.init()
    

    def init(self) -> None:
        from org.allbinary.input.automation.actions.script.condition.TimeIntervalActionScriptConditionJPanel import TimeIntervalActionScriptConditionJPanel
        self.timeIntervalActionScriptConditionJPanel = TimeIntervalActionScriptConditionJPanel(self)
    

    def showDialog(self) -> None:
        self.timeIntervalActionScriptConditionJPanel.getTimeIntervalActionJDialog().setVisible(True)
    

    def toHashMap(self) -> HashMap:
        from org.allbinary.input.automation.actions.script.condition.TimeIntervalActionScriptConditionData import TimeIntervalActionScriptConditionData
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        hashMap.put(TimeIntervalActionScriptConditionData.TIME, str(self.timeHelper.delay))
        self.logUtil.putF("HashMap: " + str(hashMap), self, "toHashMap()")
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.actions.script.condition.TimeIntervalActionScriptConditionData import TimeIntervalActionScriptConditionData
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = java_super_call(super(), "toXmlNode", document)
        node.appendChild(ModDomHelper.createNodeWithValueNodes(document, TimeIntervalActionScriptConditionData.NAME, self.toHashMap()))
        return node
    

    def log(self) -> None:
        self.logUtil.putF("Time Interval: " + str(self.timeHelper.delay), self, "log")
    

    def getTimeDelayHelper(self) -> TimeDelayHelper:
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        return self.timeHelper
    

    def setTimeDelayHelper(self, timeHelper: TimeDelayHelper) -> None:
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        self.timeHelper = timeHelper
    

    # throws Exception
    def shouldProcess(self, frame: int) -> bool:
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        timeHelper: TimeDelayHelper = self.getTimeDelayHelper()
        if java_predicate(timeHelper, "isTimeTNT"):
            timeHelper.setStartTimeTNT()
            return java_super_call(super(), "shouldProcess", frame)
        return False
# from java.util.HashMap import HashMap
# from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList


