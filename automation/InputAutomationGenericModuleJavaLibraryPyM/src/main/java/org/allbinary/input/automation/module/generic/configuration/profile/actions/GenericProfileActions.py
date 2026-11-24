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

from java.lang.JavaRuntimeStatic import lazy_static
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.data.tree.dom.document.mapping.DomDocumentMappingInterface import DomDocumentMappingInterface


class GenericProfileActions(*java_bases(DomNodeInterface, DomDocumentMappingInterface)):
    DEFAULT_PROFILE_ACTIONS_PATH: str = None

    def _init_fields(self) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.input.automation.module.DefaultListModelHelper import DefaultListModelHelper
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.io.file.CommonDataFileStrings import CommonDataFileStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonFileStrings: CommonDataFileStrings = CommonDataFileStrings.getInstance()
        self.name: str = None
        self.genericProfileActionsJPanel: GenericProfileActionsJPanel = None
        self.actionsDefaultListModelHelper: DefaultListModelHelper = None
        self.hashMap: HashMap = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 3:
            self.__jconstructor3(*args)

    def __jconstructor3(self, *args) -> None:
        if True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)) and (args[2] is None or isinstance(args[2], str)):
            self._constructor3_1(*args)
        else:
            self._constructor3_2(*args)
    

    def _constructor2(self, genericProfileActionsJPanel: GenericProfileActionsJPanel, name: str) -> None:
        self._init_fields()
        self.setName(name)
        self.init(genericProfileActionsJPanel)
        self.load()
    

    def _constructor3_1(self, genericProfileActionsJPanel: GenericProfileActionsJPanel, abPath: AbPath, name: str) -> None:
        from org.allbinary.logic.io.path.AbPath import AbPath
        self._init_fields()
        self.setName(name)
        self.init(genericProfileActionsJPanel)
        self.load()
    

    def _constructor3_2(self, genericProfileActionsJPanel: GenericProfileActionsJPanel, fileInputStream: FileInputStream, name: str) -> None:
        from java.io.FileInputStream import FileInputStream
        self._init_fields()
        self.setName(name)
        self.init(genericProfileActionsJPanel)
        self.fileInit(fileInputStream)
    

    # throws Exception
    def init(self, genericProfileActionsJPanel: GenericProfileActionsJPanel) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.input.automation.module.DefaultListModelHelper import DefaultListModelHelper
        self.setGenericProfileActionsJPanel(genericProfileActionsJPanel)
        self.actionsDefaultListModelHelper = DefaultListModelHelper()
        self.setHashMap(HashMap())
    

    # throws Exception
    def save(self) -> None:
        from java.io.DataOutputStream import DataOutputStream
        from java.io.FileOutputStream import FileOutputStream
        from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
        idFile: FileOutputStream = FileOutputStream(str(GenericProfileActions.DEFAULT_PROFILE_ACTIONS_PATH) + self.getName() + str(self.commonFileStrings._XML))
        idOutData: DataOutputStream = DataOutputStream(idFile)
        idOutData.writeBytes(XmlDocumentHelper.toString(self.toXmlDoc()))
    

    def getFile(self, name: str) -> File:
        fileName: str = GenericProfileActions.DEFAULT_PROFILE_ACTIONS_PATH + name + str(self.commonFileStrings._XML)
        return File(fileName)
    

    # throws Exception
    def load(self) -> None:
        from java.io.FileInputStream import FileInputStream
        file: File = self.getFile(self.getName())
        if file.isFile():
            idFile: FileInputStream = FileInputStream(file)
            self.fileInit(idFile)
        else:
            self.logUtil.putF("No Profile: " + str(file.getAbsolutePath()), self, "Contructor")
    

    # throws Exception
    def fileInit(self, fileInputStream: FileInputStream) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionsData import GenericProfileActionsData
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionData import GenericProfileActionData
        from java.io.FileInputStream import FileInputStream
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        bytes: list[int] = [0] * (100000)
        length: int = fileInputStream.read(bytes)
        data: str = bytes(bytes).decode()
        endIndex: int = data.rfind('>')
        document: Document = DomDocumentHelper.create(data[0:endIndex + 1])
        nameNodeList: NodeList = document.getElementsByTagName(GenericProfileActionsData.NAME)
        self.logUtil.putF("Number Of Profiles Specified: " + str(nameNodeList.getLength()), self, "Contructor")
        for index in range(0, nameNodeList.getLength()):
            node: Node = nameNodeList.item(index)
            nodeList: NodeList = node.getChildNodes()
            if nodeList is not None:
                self.initActions(nodeList)
            else:
                raise Exception(str(GenericProfileActionData.NAME) + " Name Node Node Children")
        self.logUtil.putF("Loaded: " + str(self.getHashMap().size()) + " Configuration Profile Action(s)", self, "Contructor")
        self.getDefaultListModelHelper().initDefaultModelList()
    

    # throws Exception
    def initActions(self, nodeList: NodeList) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionData import GenericProfileActionData
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileAction import GenericProfileAction
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        for index in range(0, nodeList.getLength()):
            actionNode: Node = nodeList.item(index)
            if actionNode is not None:
                genericConfigurationProfileAction: GenericProfileAction = GenericProfileAction(self.getGenericProfileActionsJPanel().getGenericProfileActionJPanel(), actionNode)
                self.getHashMap().put(genericConfigurationProfileAction.getName(), genericConfigurationProfileAction)
                self.getDefaultListModelHelper().add(genericConfigurationProfileAction.getName())
            else:
                raise Exception(str(GenericProfileActionData.NAME) + " Node Null")
    

    def getDefaultListModelHelper(self) -> DefaultListModelHelper:
        from org.allbinary.input.automation.module.DefaultListModelHelper import DefaultListModelHelper
        return self.actionsDefaultListModelHelper
    

    def getAction(self, string: str) -> GenericProfileAction:
        return self.getHashMap().get(string)
    

    # throws Exception
    def add(self, name: str) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileAction import GenericProfileAction
        genericProfileAction: GenericProfileAction = GenericProfileAction(name)
        self.getHashMap().put(genericProfileAction.getName(), genericProfileAction)
        self.getDefaultListModelHelper().add(genericProfileAction.getName())
        self.getDefaultListModelHelper().initDefaultModelList()
        self.save()
    

    # throws Exception
    def remove(self, name: str) -> None:
        self.getHashMap().remove(name)
        self.getDefaultListModelHelper().remove(name)
        self.getDefaultListModelHelper().initDefaultModelList()
        self.save()
    

    def toHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        self.logUtil.putF("HashMap: " + str(hashMap), self, "toHashMap()")
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionsData import GenericProfileActionsData
        from java.util.Set import Set
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = document.createElement(GenericProfileActionsData.NAME)
        set: Set = self.getHashMap().keySet()
        actionNameArray: list[object] = set.toArray()
        size: int = len(actionNameArray)
        for index in range(0, size):
            nextActionName: str = actionNameArray[index]
            nextGenericProfileAction: GenericProfileAction = self.getAction(nextActionName)
            node.appendChild(nextGenericProfileAction.toXmlNode(document))
        return node
    

    # throws Exception
    def toXmlDoc(self) -> Document:
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        document: Document = DomDocumentHelper.create()
        node: Node = self.toXmlNode(document)
        document.appendChild(node)
        return document
    

    def getGenericProfileActionsJPanel(self) -> GenericProfileActionsJPanel:
        return self.genericProfileActionsJPanel
    

    def setGenericProfileActionsJPanel(self, genericProfileActionsJPanel: GenericProfileActionsJPanel) -> None:
        self.genericProfileActionsJPanel = genericProfileActionsJPanel
    

    def getHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        return self.hashMap
    

    def setHashMap(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        self.hashMap = hashMap
    

    def getName(self) -> str:
        return self.name
    

    def setName(self, name: str) -> None:
        self.name = name
# from java.io.DataOutputStream import DataOutputStream
# from java.io.File import File
# from java.io.FileInputStream import FileInputStream
# from java.io.FileOutputStream import FileOutputStream
# from java.util.HashMap import HashMap
# from java.util.Set import Set
# from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
# from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
# from org.allbinary.input.automation.module.DefaultListModelHelper import DefaultListModelHelper
# from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfiles import GenericProfiles
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.file.CommonDataFileStrings import CommonDataFileStrings
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList


def _GenericProfileActions_DEFAULT_PROFILE_ACTIONS_PATH() -> object:
    from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfiles import GenericProfiles
    return str(GenericProfiles.DEFAULT_PROFILES_PATH) + "actions/"

lazy_static(GenericProfileActions, "DEFAULT_PROFILE_ACTIONS_PATH", _GenericProfileActions_DEFAULT_PROFILE_ACTIONS_PATH)

