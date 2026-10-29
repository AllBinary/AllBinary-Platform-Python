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
# package org.allbinary.input.automation.module.generic.configuration.profile

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.data.tree.dom.document.mapping.DomDocumentMappingInterface import DomDocumentMappingInterface


class GenericProfiles(DomNodeInterface, DomDocumentMappingInterface):
    DEFAULT_PROFILES_PATH: str = "./modules/configs/profiles/"
    DEFAULT_PROFILE_ACTIONS_PATH: str = None
    DEFAULT_FILE: str = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.hashMap: dict = None
        self.profilesDefaultListModelHelper: DefaultListModelHelper = None
        self.fileName: str = None
    

    def __init__(self, fileName: str) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfilesData import GenericProfilesData
        self._init_fields()
        self.fileName = fileName
        self.profilesDefaultListModelHelper = DefaultListModelHelper()
        self.hashMap = StdUtil.getInstance().createHashMap()
        if File(fileName).isFile():
            bytes: list[int] = [0] * (100000)
            idFile: FileInputStream = FileInputStream(fileName)
            length: int = idFile.read(bytes)
            data: str = bytes(bytes).decode()
            endIndex: int = data.rfind('>')
            document: Document = DomDocumentHelper.create(data[0:endIndex + 1])
            nodeList: NodeList = document.getElementsByTagName(GenericProfilesData.NAME)
            self.logUtil.putF("Number Of Profiles Specified: " + str(nodeList.getLength()), self, "Contructor")
            if nodeList is not None:
                self.initProfiles(nodeList.item(0))
            else:
                raise Exception(str(GenericProfileActionData.NAME) + " Name Node Node Children")
            self.logUtil.putF("Loaded: " + str(self.hashMap.size()) + " Configuration Profile Actions", self, "Contructor")
        else:
            self.logUtil.putF("No Generic Profile: " + fileName, self, "Contructor")
        self.getDefaultListModelHelper().initDefaultModelList()
    

    # throws Exception
    def initProfiles(self, node: Node) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfileData import GenericProfileData
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfile import GenericProfile
        nodeList: NodeList = node.getChildNodes()
        for index in range(0, nodeList.getLength()):
            profileNameNode: Node = nodeList.item(index)
            if profileNameNode.getNodeName().compareTo(GenericProfileData.NAME) == 0:
                genericProfile: GenericProfile = GenericProfile(profileNameNode)
                self.hashMap.put(genericProfile.getName(), genericProfile)
                self.getDefaultListModelHelper().add(genericProfile.getName())
    

    def getDefaultListModelHelper(self) -> DefaultListModelHelper:
        return self.profilesDefaultListModelHelper
    

    # throws Exception
    def get(self, name: str) -> GenericProfile:
        genericProfile: GenericProfile = self.hashMap.get(name)
        if genericProfile is None:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF("No Generic Profile Named: " + name + " availability was: " + str(self.hashMap), self, commonStrings.GET)
        return genericProfile
    

    # throws Exception
    def add(self, name: str) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfile import GenericProfile
        self.hashMap.put(name, GenericProfile(name))
        self.getDefaultListModelHelper().add(name)
        self.getDefaultListModelHelper().initDefaultModelList()
        self.save()
    

    # throws Exception
    def remove(self, name: str) -> None:
        self.hashMap.remove(name)
        self.getDefaultListModelHelper().remove(name)
        self.getDefaultListModelHelper().initDefaultModelList()
        self.save()
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfilesData import GenericProfilesData
        node: Node = document.createElement(GenericProfilesData.NAME)
        set: Set = self.hashMap.keySet()
        nameArray: list[object] = set.toArray()
        size: int = len(nameArray)
        for index in range(0, size):
            genericProfile: GenericProfile = self.hashMap.get(nameArray[index])
            node.appendChild(genericProfile.toXmlNode(document))
        return node
    

    # throws Exception
    def toXmlDoc(self) -> Document:
        document: Document = DomDocumentHelper.create()
        node: Node = self.toXmlNode(document)
        document.appendChild(node)
        return document
    

    # throws Exception
    def save(self) -> None:
        idFile: FileOutputStream = FileOutputStream(self.fileName)
        idOutData: DataOutputStream = DataOutputStream(idFile)
        documentString: str = XmlDocumentHelper.toString(self.toXmlDoc())
        idOutData.writeBytes(documentString)
# from java.io.DataOutputStream import DataOutputStream
# from java.io.File import File
# from java.io.FileInputStream import FileInputStream
# from java.io.FileOutputStream import FileOutputStream
# from java.util.HashMap import HashMap
# from java.util.Set import Set
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.input.automation.module.DefaultListModelHelper import DefaultListModelHelper
from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionData import GenericProfileActionData
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


GenericProfiles.DEFAULT_PROFILE_ACTIONS_PATH = str(GenericProfiles.DEFAULT_PROFILES_PATH) + "actions/"

GenericProfiles.DEFAULT_FILE = str(GenericProfiles.DEFAULT_PROFILES_PATH) + "profiles.xml"

