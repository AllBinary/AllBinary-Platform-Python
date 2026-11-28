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
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "hashMap" not in vars(self): self.hashMap: HashMap = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            __class__.__jconstructor2(self, *args)
        elif len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 0:
            __class__._constructor0(self, *args)

    def __jconstructor2(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "AbeClientInformationInterface" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "File" for base in type(args[1]).__mro__)):
            __class__._constructor2_1(self, *args)
        else:
            __class__._constructor2_2(self, *args)
    

    def _constructor2_1(self, abeClientInformation: AbeClientInformationInterface, file: File) -> None:
        from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfiguration import InputAutomationModuleConfiguration
        from java.io.File import File
        from java.io.FileInputStream import FileInputStream
        from java.util.HashMap import HashMap
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.allbinary.input.automation.module.InputAutomationModuleData import InputAutomationModuleData
        from org.allbinary.input.automation.module.NewInputAutomationModulesData import NewInputAutomationModulesData
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        __class__._init_fields(self)
        self.setHashMap(HashMap())
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
    

    def _constructor2_2(self, abeClientInformation: AbeClientInformationInterface, document: Document) -> None:
        from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfiguration import InputAutomationModuleConfiguration
        from java.util.HashMap import HashMap
        from org.allbinary.input.automation.module.InputAutomationModuleData import InputAutomationModuleData
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        __class__._init_fields(self)
        self.setHashMap(HashMap())
        nameNodeList: NodeList = document.getElementsByTagName(InputAutomationModuleData.NAME)
        self.logUtil.putF("Number Of Module(s) Specified: " + str(nameNodeList.getLength()), self, "Contructor")
        for index in range(0, nameNodeList.getLength()):
            node: Node = nameNodeList.item(index)
            self.add(InputAutomationModuleConfiguration(abeClientInformation, node))
    

    def _constructor1(self, inputAutomationModuleConfigurationList: List[InputAutomationModuleConfiguration]) -> None:
        from java.util.HashMap import HashMap
        from java.util.List import List
        __class__._init_fields(self)
        self.setHashMap(HashMap())
        size: int = inputAutomationModuleConfigurationList.size()
        inputAutomationModuleConfiguration: InputAutomationModuleConfiguration = None
        for index in range(0, size):
            inputAutomationModuleConfiguration = inputAutomationModuleConfigurationList.get(index)
            self.add(inputAutomationModuleConfiguration)
    

    def _constructor0(self) -> None:
        from java.util.HashMap import HashMap
        __class__._init_fields(self)
        self.setHashMap(HashMap())
    

    def add(self, inputAutomationModuleConfiguration: InputAutomationModuleConfiguration) -> None:
        self.getHashMap().put(inputAutomationModuleConfiguration.getClassName(), inputAutomationModuleConfiguration)
    

    def remove(self, inputAutomationModuleConfiguration: InputAutomationModuleConfiguration) -> None:
        self.getHashMap().remove(inputAutomationModuleConfiguration.getClassName())
    

    def getHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        return self.hashMap
    

    def setHashMap(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        self.hashMap = hashMap
# from java.io.File import File
# from java.io.FileInputStream import FileInputStream
# from java.util.HashMap import HashMap
# from java.util.List import List
# from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
# from org.allbinary.input.automation.module.InputAutomationModuleData import InputAutomationModuleData
# from org.allbinary.input.automation.module.NewInputAutomationModulesData import NewInputAutomationModulesData
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList


