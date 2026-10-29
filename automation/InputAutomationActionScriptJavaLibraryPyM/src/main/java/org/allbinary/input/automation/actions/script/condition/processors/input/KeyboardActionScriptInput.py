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
from org.allbinary.input.automation.actions.script.condition.processors.input.KeyboardActionScriptInputInterface import KeyboardActionScriptInputInterface


class KeyboardActionScriptInput(BasicProfileActionScriptInput, KeyboardActionScriptInputInterface):
    NAME: str = "Keyboard"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.keyArray: list[int] = [KeySingletonFactory.getInstance(KeyEvent.VK_0)]
        self.keyboardActionScriptInputJPanel: KeyboardActionScriptInputJPanel = None
        self.press: bool = False
        self.release: bool = False
        self.delayBetweenKeys: int = 0

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 0:
            self._constructor0(*args)
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyboardActionScriptInputData import KeyboardActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyboardActionScriptInputData import KeyboardActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyboardActionScriptInputData import KeyboardActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyboardActionScriptInputData import KeyboardActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyboardActionScriptInputData import KeyboardActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyboardActionScriptInputJPanel import KeyboardActionScriptInputJPanel
        super().__init__(KeyboardActionScriptInput.NAME, node)
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        actionNode: Node = DomSearchHelper.getNode(KeyboardActionScriptInputData.NAME, node.getChildNodes())
        if actionNode is not None:
            nodeList: NodeList = actionNode.getChildNodes()
            vector: BasicArrayList = BasicArrayListD()
            for index in range(0, nodeList.getLength()):
                childNode: Node = nodeList.item(index)
                if childNode.getNodeName().startsWith(KeyboardActionScriptInputData.KEY):
                    keyString: str = DomNodeHelper.getTextNodeValue(childNode)
                    vector.add(str(keyString))
                elif childNode.getNodeName().compareTo(KeyboardActionScriptInputData.DELAY_BETWEEN_KEYS) == 0:
                    time: str = DomNodeHelper.getTextNodeValue(childNode)
                    self.setDelayBetweenKeys(int(str(time)))
                elif childNode.getNodeName().compareTo(KeyboardActionScriptInputData.PRESS) == 0:
                    value: str = DomNodeHelper.getTextNodeValue(childNode)
                    self.setPress(str(value))
                elif childNode.getNodeName().compareTo(KeyboardActionScriptInputData.RELEASE) == 0:
                    value: str = DomNodeHelper.getTextNodeValue(childNode)
                    self.setRelease(str(value))
                else:
                    raise Exception("Action Script Input Unknown Node")
            self.setKeyArray(vector.toArrayType([None] * (vector.size())))
        else:
            raise Exception("Action Script Input Node Null")
        self.setAllowsChildren(False)
        if not self.isPress() and not self.isRelease():
            self.setNormal()
        self.keyboardActionScriptInputJPanel = KeyboardActionScriptInputJPanel(self)
    

    def _constructor0(self) -> None:
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyboardActionScriptInputJPanel import KeyboardActionScriptInputJPanel
        super().__init__(KeyboardActionScriptInput.NAME)
        self._init_fields()
        if not self.isPress() and not self.isRelease():
            self.setNormal()
        self.setAllowsChildren(False)
        self.setTime(120)
        self.keyboardActionScriptInputJPanel = KeyboardActionScriptInputJPanel(self)
    

    def getDelayBetweenKeys(self) -> int:
        return self.delayBetweenKeys
    

    def setDelayBetweenKeys(self, delayBetweenKeys: int) -> None:
        self.delayBetweenKeys = delayBetweenKeys
    

    def isPress(self) -> bool:
        return self.press
    

    def setPress(self, press: bool) -> None:
        self.press = press
    

    def isRelease(self) -> bool:
        return self.release
    

    def setRelease(self, release: bool) -> None:
        self.release = release
    

    def isNormal(self) -> bool:
        return self.isRelease() and self.isPress()
    

    def setNormal(self) -> None:
        self.setPress(True)
        self.setRelease(True)
    

    def getKeyArray(self) -> list[int]:
        return self.keyArray
    

    def setKeyArray(self, keyArray: list[int]) -> None:
        if keyArray is not None:
            self.logUtil.putF(CommonLabels.getInstance().START + len(keyArray), self, "setKeyArray")
        self.keyArray = keyArray
    

    def showDialog(self) -> None:
        self.keyboardActionScriptInputJPanel.getKeyActionJDialog().setVisible(True)
    

    def getText(self) -> str:
        return self.getText(self.getKeyArray())
    

    def setText(self, text: str) -> None:
        self.logUtil.putF(str(CommonLabels.getInstance().START) + text, self, "setText")
        integerArray: list[int] = self.integerArrayValue(text)
        self.setKeyArray(integerArray)
    

    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def getText(integerArray: list[int]) -> str:
        index: int = 0
        stringBuffer: StringMaker = StringMaker()
        while index < len(integerArray):
            nextInteger: int = integerArray[index]
            if KeyUtil.isNormallyDisplayed(nextInteger):
                stringBuffer.append(KeyEvent.getKeyText(nextInteger))
            else:
                stringBuffer.append("&#" + str(nextInteger) + ";")
            index += 1
        return str(stringBuffer)
    

    def integerArrayValue(self, text: str) -> list[int]:
        self.logUtil.putF(str(CommonLabels.getInstance().START) + text, self, "integerArrayValue")
        vector: BasicArrayList = BasicArrayListD()
        index: int = 0
        while index < len(text):
            aChar: str = text[index]
            if aChar == '&':
                if text[index + 1] == '#':
                    endIndex: int = text.find(';', index + 1)
                    if endIndex != -1:
                        nextCharString: str = text[index + 2:endIndex]
                        self.logUtil.putF(str(CommonLabels.getInstance().NEXT) + " Char String: " + nextCharString, self, "integerArrayValue")
                        vector.add(str(nextCharString[index:len(nextCharString)]))
                        index = index + len(nextCharString) + 3
                        continue
            vector.add(KeySingletonFactory.getHashtable().get(str(aChar)))
            index += 1
        integerArray: list[int] = vector.toArrayType([None] * (vector.size()))
        return integerArray
    

    def toHashMap(self) -> dict:
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyboardActionScriptInputData import KeyboardActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyboardActionScriptInputData import KeyboardActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyboardActionScriptInputData import KeyboardActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyboardActionScriptInputData import KeyboardActionScriptInputData
        hashMap: dict = StdUtil.getInstance().createHashMap()
        for index in range(0, len(self.getKeyArray())):
            hashMap.put(KeyboardActionScriptInputData.KEY + index, str(self.getKeyArray()[index]))
        hashMap.put(KeyboardActionScriptInputData.DELAY_BETWEEN_KEYS, str(self.getDelayBetweenKeys()))
        hashMap.put(KeyboardActionScriptInputData.PRESS, str(self.isPress()))
        hashMap.put(KeyboardActionScriptInputData.RELEASE, str(self.isRelease()))
        self.logUtil.putF("HashMap: " + str(hashMap), self, "toHashMap()")
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyboardActionScriptInputData import KeyboardActionScriptInputData
        node: Node = super().toXmlNode(document)
        node.appendChild(ModDomHelper.createNodeWithValueNodes(document, KeyboardActionScriptInputData.NAME, self.toHashMap()))
        return node
    

    # throws Exception
    def process(self, frame: int) -> None:
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyboardInputAutomationProcessor import KeyboardInputAutomationProcessor
        KeyboardInputAutomationProcessor.process(self)
    

    def log(self) -> None:
        self.logUtil.putF(str(self), self, "log")
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(str(super()))
        stringBuffer.append(" Text: ")
        stringBuffer.append(self.getText())
        stringBuffer.append(" isPress: ")
        stringBuffer.appendboolean(self.isPress())
        stringBuffer.append(" isRelease: ")
        stringBuffer.appendboolean(self.isRelease())
        stringBuffer.append(" Between Key Delay: ")
        stringBuffer.appendint(self.getDelayBetweenKeys())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from java.awt.event.KeyEvent import KeyEvent
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.input.KeySingletonFactory import KeySingletonFactory
from org.allbinary.input.KeyUtil import KeyUtil
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


