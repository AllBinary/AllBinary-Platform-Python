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



class InputAutomationModuleConfigurations:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.hashMap: dict = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 0:
            self._constructor0(*args)
    

    def _constructor2(self, abeClientInformation: AbeClientInformationInterface, file: File) -> None:
        from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfiguration import InputAutomationModuleConfiguration
        self._init_fields()
        self.setHashMap(dict())
        bytes: list[int] = [0] * (100000)
        idFile: FileInputStream = FileInputStream(file)
        length: int = idFile.read(bytes)
        data: str = bytes(bytes).decode()
        endIndex: int = data.rfind('>')
        document: Document = DomDocumentHelper.create(data[0:endIndex + 1])
        nodeList: NodeList = document.getElementsByTagName(NewInputAutomationModulesData.NAME)
        if nodeList.getLength() > 0:
            nameNodeList: NodeList = document.getElementsByTagName(InputAutomationModuleData.NAME)
            self.logUtil.putF("Number Of Module(s) Specified: " + str(nameNodeList.getLength()), self, "Contructor")
            for index in range(0, nameNodeList.getLength()):
                node: Node = nameNodeList.item(index)
                self.add(InputAutomationModuleConfiguration(abeClientInformation, node))
    

    def _constructor2(self, abeClientInformation: AbeClientInformationInterface, document: Document) -> None:
        from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfiguration import InputAutomationModuleConfiguration
        self._init_fields()
        self.setHashMap(dict())
        nameNodeList: NodeList = document.getElementsByTagName(InputAutomationModuleData.NAME)
        self.logUtil.putF("Number Of Module(s) Specified: " + str(nameNodeList.getLength()), self, "Contructor")
        for index in range(0, nameNodeList.getLength()):
            node: Node = nameNodeList.item(index)
            self.add(InputAutomationModuleConfiguration(abeClientInformation, node))
    

    def _constructor1(self, inputAutomationModuleConfigurationList: List[InputAutomationModuleConfiguration]) -> None:
        self._init_fields()
        self.setHashMap(dict())
        size: int = inputAutomationModuleConfigurationList.size()
        inputAutomationModuleConfiguration: InputAutomationModuleConfiguration = None
        for index in range(0, size):
            inputAutomationModuleConfiguration = inputAutomationModuleConfigurationList.get(index)
            self.add(inputAutomationModuleConfiguration)
    

    def _constructor0(self) -> None:
        self._init_fields()
        self.setHashMap(dict())
    

    def add(self, inputAutomationModuleConfiguration: InputAutomationModuleConfiguration) -> None:
        self.getHashMap().put(inputAutomationModuleConfiguration.getClassName(), inputAutomationModuleConfiguration)
    

    def remove(self, inputAutomationModuleConfiguration: InputAutomationModuleConfiguration) -> None:
        self.getHashMap().remove(inputAutomationModuleConfiguration.getClassName())
    

    def getHashMap(self) -> dict:
        return self.hashMap
    

    def setHashMap(self, hashMap: dict) -> None:
        self.hashMap = hashMap
# from java.io.File import File
# from java.io.FileInputStream import FileInputStream
# from java.util.HashMap import HashMap
# from java.util.List import List
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.input.automation.module.InputAutomationModuleData import InputAutomationModuleData
from org.allbinary.input.automation.module.NewInputAutomationModulesData import NewInputAutomationModulesData
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


