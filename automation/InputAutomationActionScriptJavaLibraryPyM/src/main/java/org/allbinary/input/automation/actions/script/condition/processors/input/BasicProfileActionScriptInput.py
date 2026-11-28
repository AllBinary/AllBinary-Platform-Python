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
# package org.allbinary.input.automation.actions.script.condition.processors.input

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.input.automation.actions.script.condition.processors.BasicProfileActionScriptProcessor import BasicProfileActionScriptProcessor
from org.allbinary.input.automation.actions.script.condition.processors.input.ProfileActionScriptInputInterface import ProfileActionScriptInputInterface


@java_inherited_overloads
class BasicProfileActionScriptInput(*java_bases(BasicProfileActionScriptProcessor, ProfileActionScriptInputInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("inputRobotInterface", None)
        vars(self).setdefault("time", 0)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "inputRobotInterface" not in vars(self): self.inputRobotInterface: InputRobotInterface = None
        if "time" not in vars(self): self.time: int = 0

    def __init__(self, *args) -> None:
        if len(args) == 2:
            __class__._constructor2(self, *args)
        elif len(args) == 1:
            __class__._constructor1(self, *args)
    

    def _constructor2(self, label: str, node: Node) -> None:
        __class__._java_defaults(self)
        from org.allbinary.input.automation.actions.script.condition.processors.input.GenericProfileActionScriptInputData import GenericProfileActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.GenericProfileActionScriptInputData import GenericProfileActionScriptInputData
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory
        from org.w3c.dom.Node import Node
        super().__init__(label, node)
        __class__._init_fields(self)
        self.logUtil.putF(str(self.commonStrings.START) + label, self, self.commonStrings.CONSTRUCTOR)
        actionNode: Node = DomSearchHelper.getNode(GenericProfileActionScriptInputData.TYPE, node.getChildNodes())
        inputTypeString: str = DomNodeHelper.getTextNodeValue(actionNode)
        timeNode: Node = DomSearchHelper.getNodeNoThrow(GenericProfileActionScriptInputData.DELAY, node.getChildNodes())
        if timeNode is not None:
            delayString: str = DomNodeHelper.getTextNodeValue(timeNode)
            self.setTime(int(str(delayString)))
        else:
            self.setTime(0)
        self.setInputRobotInterface(InputRobotFactory.getInstance().get(inputTypeString))
    

    def _constructor1(self, label: str) -> None:
        __class__._java_defaults(self)
        from java.util.Iterator import Iterator
        from java.util.Set import Set
        from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory
        from org.allbinary.util.ABHashtable import ABHashtable
        super().__init__(label)
        __class__._init_fields(self)
        self.logUtil.putF(str(self.commonStrings.START) + label, self, self.commonStrings.CONSTRUCTOR)
        inputRobotFactory: InputRobotFactory = InputRobotFactory.getInstance()
        hashtable: ABHashtable[object, object] = inputRobotFactory.get()
        set: Set = hashtable.keySet()
        iterator: Iterator = set.iterator()
        self.setInputRobotInterface(inputRobotFactory.get(iterator.next()))
        self.setTime(0)
    

    def getTime(self) -> int:
        return self.time
    

    def setTime(self, time: int) -> None:
        self.time = time
    

    def BasicProfileActionScriptInput_toHashMap(self) -> HashMap:
        from org.allbinary.input.automation.actions.script.condition.processors.input.GenericProfileActionScriptInputData import GenericProfileActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.GenericProfileActionScriptInputData import GenericProfileActionScriptInputData
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        hashMap.put(GenericProfileActionScriptInputData.TYPE, self.getInputRobotInterface().getName())
        hashMap.put(GenericProfileActionScriptInputData.DELAY, str(self.getTime()))
        self.logUtil.putF("HashMap: " + str(hashMap), self, "toHashMap()")
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.actions.script.condition.processors.input.GenericProfileActionScriptInputData import GenericProfileActionScriptInputData
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = ModDomHelper.createNodeWithValueNodes(document, GenericProfileActionScriptInputData.NAME, self.BasicProfileActionScriptInput_toHashMap())
        return node
    

    def setInputRobotInterface(self, inputRobotInterface: InputRobotInterface) -> None:
        from org.allbinary.input.automation.robot.InputRobotInterface import InputRobotInterface
        self.inputRobotInterface = inputRobotInterface
    

    def getInputRobotInterface(self) -> InputRobotInterface:
        from org.allbinary.input.automation.robot.InputRobotInterface import InputRobotInterface
        return self.inputRobotInterface
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(java_super_call(super(), "toString"))
        stringBuffer.append(" Input Type: ")
        if self.getInputRobotInterface() is not None:
            stringBuffer.append(self.getInputRobotInterface().getName())
        else:
            stringBuffer.append(StringUtil.getInstance().NULL_STRING)
        stringBuffer.append(" Time: ")
        stringBuffer.appendlong(self.getTime())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from java.util.HashMap import HashMap
# from java.util.Iterator import Iterator
# from java.util.Set import Set
# from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory
# from org.allbinary.input.automation.robot.InputRobotInterface import InputRobotInterface
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.util.ABHashtable import ABHashtable
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node


