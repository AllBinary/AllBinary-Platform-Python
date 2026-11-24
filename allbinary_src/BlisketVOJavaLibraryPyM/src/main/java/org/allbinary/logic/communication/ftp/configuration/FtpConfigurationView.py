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
# package org.allbinary.logic.communication.ftp.configuration

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class FtpConfigurationView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.ftpConfigurationInterface: FtpConfigurationInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self.__jconstructor1(*args)

    def __jconstructor1(self, *args) -> None:
        if True and not isinstance(args[0], (str, list, int, float)):
            self._constructor1_1(*args)
        else:
            self._constructor1_2(*args)
    

    def _constructor1_1(self, node: Node) -> None:
        from org.allbinary.logic.communication.ftp.configuration.FtpConfiguration import FtpConfiguration
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        self._init_fields()
        self.setFtpConfigurationInterface(FtpConfiguration())
        chileNodeList: NodeList = node.getChildNodes()
        server: str = DomNodeHelper.getTextNodeValue(FtpConfigurationData.SERVER, chileNodeList)
        self.getFtpConfigurationInterface().setServer(server)
        userName: str = DomNodeHelper.getTextNodeValue(FtpConfigurationData.USERNAME, chileNodeList)
        self.getFtpConfigurationInterface().setUserName(userName)
        password: str = DomNodeHelper.getTextNodeValue(FtpConfigurationData.PASSWORD, chileNodeList)
        self.getFtpConfigurationInterface().setPassword(password)
        path: str = DomNodeHelper.getTextNodeValue(FtpConfigurationData.PATH, chileNodeList)
        self.getFtpConfigurationInterface().setPath(path)
    

    def _constructor1_2(self, ftpConfigurationInterface: FtpConfigurationInterface) -> None:
        self._init_fields()
        self.setFtpConfigurationInterface(ftpConfigurationInterface)
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.communication.ftp.configuration.FtpConfigurationMapping import FtpConfigurationMapping
        from java.util.HashMap import HashMap
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        ftpConfigurationMapping: FtpConfigurationMapping = FtpConfigurationMapping(self.getFtpConfigurationInterface())
        hashMap: HashMap = ftpConfigurationMapping.toHashMap()
        node: Node = ModDomHelper.createNameValueNodes(document, FtpConfigurationData.NAME, hashMap)
        return node
    

    def getFtpConfigurationInterface(self) -> FtpConfigurationInterface:
        return self.ftpConfigurationInterface
    

    def setFtpConfigurationInterface(self, ftpConfigurationInterface: FtpConfigurationInterface) -> None:
        self.ftpConfigurationInterface = ftpConfigurationInterface
# from java.util.HashMap import HashMap
# from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList


