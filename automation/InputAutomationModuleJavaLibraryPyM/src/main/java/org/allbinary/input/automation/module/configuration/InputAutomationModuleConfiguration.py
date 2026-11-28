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
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "className" not in vars(self): self.className: str = None
        if "name" not in vars(self): self.name: str = None
        if "inputAutomationModuleInterface" not in vars(self): self.inputAutomationModuleInterface: InputAutomationModuleFactoryInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 2:
            __class__._constructor2(self, *args)
        elif len(args) == 3:
            __class__._constructor3(self, *args)
        elif len(args) == 1:
            __class__._constructor1(self, *args)
    

    def _constructor0(self) -> None:
        __class__._init_fields(self)
    

    def _constructor2(self, abeClientInformation: AbeClientInformationInterface, node: Node) -> None:
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.w3c.dom.Node import Node
        __class__._init_fields(self)
        self.init(abeClientInformation, node)
    

    def _constructor3(self, abeClientInformation: AbeClientInformationInterface, name: str, className: str) -> None:
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        __class__._init_fields(self)
        self.setName(name)
        self.setClassName(className)
        self.init(abeClientInformation)
    

    def _constructor1(self, inputAutomationModuleInterface: InputAutomationModuleFactoryInterface) -> None:
        from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
        __class__._init_fields(self)
        self.setInputAutomationModuleInterface(inputAutomationModuleInterface)
        self.setClassName(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(self.inputAutomationModuleInterface)))
    

    # throws Exception
    def init_j2(self, abeClientInformation: AbeClientInformationInterface, node: Node) -> None:
        from org.allbinary.business.DynamicObjectData import DynamicObjectData
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.allbinary.input.automation.InputAutomationData import InputAutomationData
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
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
    

    def init_j1(self, abeClientInformation: AbeClientInformationInterface) -> None:
        from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
        from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        try:
            self.logUtil.putF("Name: " + self.getName(), self, self.commonStrings.INIT)
            self.logUtil.putF("ClassName: " + self.className, self, self.commonStrings.INIT)
            self.setInputAutomationModuleInterface(AbeFactory.getInstance().getInstance().getInstance(abeClientInformation, self.getClassName()))
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.INIT, e)
            raise RuntimeError()

    def init(self, *args):
        implementation = __class__.__dict__.get("init_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().init(*args)
    

    # throws Exception
    def toDomNode(self, document: Document) -> Node:
        from org.allbinary.business.DynamicObjectData import DynamicObjectData
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.allbinary.input.automation.module.InputAutomationModuleData import InputAutomationModuleData
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
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
        from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
        return self.inputAutomationModuleInterface
    

    def setInputAutomationModuleInterface(self, inputAutomationModuleInterface: InputAutomationModuleFactoryInterface) -> None:
        from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
        self.logUtil.putF("InputAutomationModuleFactoryInterface : " + str(inputAutomationModuleInterface), self, "setInputAutomationModuleInterface")
        self.inputAutomationModuleInterface = inputAutomationModuleInterface
        self.setName(self.inputAutomationModuleInterface.getName())
# from javax.xml.bind.annotation.XmlAccessType import XmlAccessType
# from javax.xml.bind.annotation.XmlAccessorType import XmlAccessorType
# from javax.xml.bind.annotation.XmlElement import XmlElement
# from javax.xml.bind.annotation.XmlRootElement import XmlRootElement
# from javax.xml.bind.annotation.XmlType import XmlType
# from org.allbinary.business.DynamicObjectData import DynamicObjectData
# from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.input.automation.InputAutomationData import InputAutomationData
# from org.allbinary.input.automation.module.InputAutomationModuleData import InputAutomationModuleData
# from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList


