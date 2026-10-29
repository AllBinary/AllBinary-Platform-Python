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
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.logic.communication.ftp.configuration.FtpConfiguration import FtpConfiguration
        from org.allbinary.logic.communication.ftp.configuration.FtpConfigurationData import FtpConfigurationData
        from org.allbinary.logic.communication.ftp.configuration.FtpConfigurationData import FtpConfigurationData
        from org.allbinary.logic.communication.ftp.configuration.FtpConfigurationData import FtpConfigurationData
        from org.allbinary.logic.communication.ftp.configuration.FtpConfigurationData import FtpConfigurationData
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
    

    def _constructor1(self, ftpConfigurationInterface: FtpConfigurationInterface) -> None:
        self._init_fields()
        self.setFtpConfigurationInterface(ftpConfigurationInterface)
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.communication.ftp.configuration.FtpConfigurationMapping import FtpConfigurationMapping
        from org.allbinary.logic.communication.ftp.configuration.FtpConfigurationData import FtpConfigurationData
        ftpConfigurationMapping: FtpConfigurationMapping = FtpConfigurationMapping(self.getFtpConfigurationInterface())
        hashMap: dict = ftpConfigurationMapping.toHashMap()
        node: Node = ModDomHelper.createNameValueNodes(document, FtpConfigurationData.NAME, hashMap)
        return node
    

    def getFtpConfigurationInterface(self) -> FtpConfigurationInterface:
        return self.ftpConfigurationInterface
    

    def setFtpConfigurationInterface(self, ftpConfigurationInterface: FtpConfigurationInterface) -> None:
        self.ftpConfigurationInterface = ftpConfigurationInterface
# from java.util.HashMap import HashMap
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


