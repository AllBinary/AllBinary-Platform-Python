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
# package org.allbinary.input.automation.module.configuration

from __future__ import annotations



class InputAutomationModuleConfiguration:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.className: str = None
        self.name: str = None
        self.inputAutomationModuleInterface: InputAutomationModuleFactoryInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 3:
            self._constructor3(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
    

    def _constructor2(self, abeClientInformation: AbeClientInformationInterface, node: Node) -> None:
        self._init_fields()
        self.init(abeClientInformation, node)
    

    def _constructor3(self, abeClientInformation: AbeClientInformationInterface, name: str, className: str) -> None:
        self._init_fields()
        self.setName(name)
        self.setClassName(className)
        self.init(abeClientInformation)
    

    def _constructor1(self, inputAutomationModuleInterface: InputAutomationModuleFactoryInterface) -> None:
        self._init_fields()
        self.setInputAutomationModuleInterface(inputAutomationModuleInterface)
        self.setClassName(type(self.inputAutomationModuleInterface).__module__ + "." + type(self.inputAutomationModuleInterface).__qualname__)
    

    # throws Exception
    def init(self, abeClientInformation: AbeClientInformationInterface, node: Node) -> None:
        nodeList: NodeList = node.getChildNodes()
        if nodeList is not None:
            classNameNode: Node = DomSearchHelper.getNode(DynamicObjectData.NAME, nodeList)
            if classNameNode is not None:
                self.setClassName(DomNodeHelper.getTextNodeValue(classNameNode))
                self.init(abeClientInformation)
            else:
                self.logUtil.putF("Class Node Null", self, self.commonStrings.INIT)
        else:
            self.logUtil.putF(str(InputAutomationData.NAME) + " Node Has No Children", self, "Contructor")
    

    # Java overloaded method: Python keeps the last definition
    def init(self, abeClientInformation: AbeClientInformationInterface) -> None:
        try:
            self.logUtil.putF("Name: " + self.getName(), self, self.commonStrings.INIT)
            self.logUtil.putF("ClassName: " + self.className, self, self.commonStrings.INIT)
            self.setInputAutomationModuleInterface(AbeFactory.getInstance().getInstance().getInstance(abeClientInformation, self.getClassName()))
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.INIT, e)
            raise RuntimeError()
    

    # throws Exception
    def toDomNode(self, document: Document) -> Node:
        node: Node = document.createElement(InputAutomationModuleData.NAME)
        classNameNode: Node = ModDomHelper.createTextNode(document, DynamicObjectData.NAME, self.getClassName())
        node.appendChild(classNameNode)
        return node
    

    def getName(self) -> str:
        return self.name
    

    def setName(self, name: str) -> None:
        self.logUtil.putF("Name: " + name, self, "setName")
        self.name = name
    

    def getClassName(self) -> str:
        return self.className
    

    def setClassName(self, className: str) -> None:
        self.logUtil.putF("ClassName : " + className, self, "setClassName")
        self.className = className
    

    def getInputAutomationModuleInterface(self) -> InputAutomationModuleFactoryInterface:
        return self.inputAutomationModuleInterface
    

    def setInputAutomationModuleInterface(self, inputAutomationModuleInterface: InputAutomationModuleFactoryInterface) -> None:
        self.logUtil.putF("InputAutomationModuleFactoryInterface : " + str(inputAutomationModuleInterface), self, "setInputAutomationModuleInterface")
        self.inputAutomationModuleInterface = inputAutomationModuleInterface
        self.setName(self.inputAutomationModuleInterface.getName())
# from javax.xml.bind.annotation.XmlAccessType import XmlAccessType
# from javax.xml.bind.annotation.XmlAccessorType import XmlAccessorType
# from javax.xml.bind.annotation.XmlElement import XmlElement
# from javax.xml.bind.annotation.XmlRootElement import XmlRootElement
# from javax.xml.bind.annotation.XmlType import XmlType
from org.allbinary.business.DynamicObjectData import DynamicObjectData
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.input.automation.InputAutomationData import InputAutomationData
from org.allbinary.input.automation.module.InputAutomationModuleData import InputAutomationModuleData
from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


