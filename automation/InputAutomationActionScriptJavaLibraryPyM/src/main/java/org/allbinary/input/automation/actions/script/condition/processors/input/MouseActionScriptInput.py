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

from org.allbinary.input.automation.actions.script.condition.processors.input.BasicProfileActionScriptInput import BasicProfileActionScriptInput
from org.allbinary.input.automation.actions.script.condition.processors.input.MouseActionScriptInputInterface import MouseActionScriptInputInterface


class MouseActionScriptInput(BasicProfileActionScriptInput, MouseActionScriptInputInterface):
    NAME: str = "Mouse"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.point: Point = None
        self.buttons: int = 0
        self.mouseActionScriptInputJPanel: MouseActionScriptInputJPanel = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 0:
            self._constructor0(*args)
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.input.automation.actions.script.condition.processors.input.Point import Point
        from org.allbinary.input.automation.actions.script.condition.processors.input.MouseActionScriptInputData import MouseActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.MouseActionScriptInputData import MouseActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.MouseActionScriptInputData import MouseActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.MouseActionScriptInputData import MouseActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.MouseActionScriptInputData import MouseActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.Point import Point
        from org.allbinary.input.automation.actions.script.condition.processors.input.MouseActionScriptInputJPanel import MouseActionScriptInputJPanel
        super().__init__(MouseActionScriptInput.NAME, node)
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.point = Point()
        actionNode: Node = DomSearchHelper.getNode(MouseActionScriptInputData.NAME, node.getChildNodes())
        if actionNode is not None:
            nodeList: NodeList = actionNode.getChildNodes()
            for index in range(0, nodeList.getLength()):
                childNode: Node = nodeList.item(index)
                if childNode.getNodeName().compareTo(MouseActionScriptInputData.BUTTONS) == 0:
                    buttons: str = DomNodeHelper.getTextNodeValue(childNode)
                    self.setButtonClicks(int(str(buttons)))
                elif childNode.getNodeName().compareTo(MouseActionScriptInputData.MOVE) == 0:
                    mouseXNode: Node = DomSearchHelper.getNode(MouseActionScriptInputData.MOVE_X, childNode.getChildNodes())
                    mouseXString: str = DomNodeHelper.getTextNodeValue(mouseXNode)
                    mouseXInteger: int = str(mouseXString)
                    mouseYNode: Node = DomSearchHelper.getNode(MouseActionScriptInputData.MOVE_Y, childNode.getChildNodes())
                    mouseYString: str = DomNodeHelper.getTextNodeValue(mouseYNode)
                    mouseYInteger: int = str(mouseYString)
                    newPoint: Point = Point(int(mouseXInteger), int(mouseYInteger))
                    self.setPoint(newPoint)
                else:
                    raise Exception("Action Script Input Unknown Node")
        else:
            raise Exception("Action Script Input Node Null")
        self.setAllowsChildren(False)
        self.mouseActionScriptInputJPanel = MouseActionScriptInputJPanel(self)
    

    def _constructor0(self) -> None:
        from org.allbinary.input.automation.actions.script.condition.processors.input.Point import Point
        from org.allbinary.input.automation.actions.script.condition.processors.input.MouseActionScriptInputJPanel import MouseActionScriptInputJPanel
        super().__init__(MouseActionScriptInput.NAME)
        self._init_fields()
        self.point = Point()
        self.setAllowsChildren(False)
        self.mouseActionScriptInputJPanel = MouseActionScriptInputJPanel(self)
    

    def setPoint(self, point: Point) -> None:
        self.point = point
    

    def getPoint(self) -> Point:
        return self.point
    

    def getButtonClicks(self) -> int:
        return self.buttons
    

    def setButtonClicks(self, buttons: int) -> None:
        self.buttons = buttons
    

    def showDialog(self) -> None:
        self.mouseActionScriptInputJPanel.getMouseActionJDialog().setVisible(True)
    

    def toHashMap(self) -> dict:
        from org.allbinary.input.automation.actions.script.condition.processors.input.MouseActionScriptInputData import MouseActionScriptInputData
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(MouseActionScriptInputData.BUTTONS, str(self.getButtonClicks()))
        self.logUtil.putF("HashMap: " + str(hashMap), self, "toHashMap()")
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.actions.script.condition.processors.input.MouseActionScriptInputData import MouseActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.MouseActionScriptInputData import MouseActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.MouseActionScriptInputData import MouseActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.MouseActionScriptInputData import MouseActionScriptInputData
        node: Node = super().toXmlNode(document)
        mouseNode: Node = ModDomHelper.createNodeWithValueNodes(document, MouseActionScriptInputData.NAME, self.toHashMap())
        node.appendChild(mouseNode)
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(MouseActionScriptInputData.MOVE_X, str(self.getPoint().x))
        hashMap.put(MouseActionScriptInputData.MOVE_Y, str(self.getPoint().y))
        mouseNode.appendChild(ModDomHelper.createNodeWithValueNodes(document, MouseActionScriptInputData.MOVE, hashMap))
        return node
    

    # throws Exception
    def process(self, frame: int) -> None:
        from org.allbinary.input.automation.actions.script.condition.processors.input.MouseInputAutomationProcessor import MouseInputAutomationProcessor
        MouseInputAutomationProcessor.process(self)
    

    def log(self) -> None:
        buttonStringBuffer: StringMaker = StringMaker()
        buttonStringBuffer.append("1: ")
        booleanFactory: BooleanFactory = BooleanFactory.getInstance()
        if (self.getButtonClicks() & InputEvent.BUTTON1_MASK) != 0:
            buttonStringBuffer.append(booleanFactory.TRUE_STRING)
        else:
            buttonStringBuffer.append(booleanFactory.FALSE_STRING)
        buttonStringBuffer.append(" 2: ")
        if (self.getButtonClicks() & InputEvent.BUTTON2_MASK) != 0:
            buttonStringBuffer.append(booleanFactory.TRUE_STRING)
        else:
            buttonStringBuffer.append(booleanFactory.FALSE_STRING)
        buttonStringBuffer.append(" 3: ")
        if (self.getButtonClicks() & InputEvent.BUTTON3_MASK) != 0:
            buttonStringBuffer.append(booleanFactory.TRUE_STRING)
        else:
            buttonStringBuffer.append(booleanFactory.FALSE_STRING)
        self.logUtil.putF("Input Type: " + self.getInputRobotInterface().getName() + " Point: " + str(self.getPoint()) + " Buttons Clicked: " + str(buttonStringBuffer), self, "log")
# from java.awt import *
# from java.awt.event.InputEvent import InputEvent
# from java.util.HashMap import HashMap
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


