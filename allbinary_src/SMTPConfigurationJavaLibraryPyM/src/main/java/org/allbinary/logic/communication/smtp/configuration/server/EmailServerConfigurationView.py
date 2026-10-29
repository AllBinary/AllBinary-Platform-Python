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
# package org.allbinary.logic.communication.smtp.configuration.server

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class EmailServerConfigurationView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.emailServerConfigurationInterface: EmailServerConfigurationInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfiguration import EmailServerConfiguration
        self._init_fields()
        childNodeList: NodeList = node.getChildNodes()
        server: str = DomNodeHelper.getTextNodeValue(EmailServerConfigurationData.SERVER, childNodeList)
        accountName: str = DomNodeHelper.getTextNodeValue(EmailServerConfigurationData.ACCOUNT, childNodeList)
        password: str = DomNodeHelper.getTextNodeValue(EmailServerConfigurationData.PASSWORD, childNodeList)
        self.emailServerConfigurationInterface = EmailServerConfiguration(accountName, password, server)
    

    def _constructor1(self, emailServerConfigurationInterface: EmailServerConfigurationInterface) -> None:
        self._init_fields()
        self.emailServerConfigurationInterface = emailServerConfigurationInterface
    

    def getEmailConfigurationInterface(self) -> EmailServerConfigurationInterface:
        return self.emailServerConfigurationInterface
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationMapping import EmailServerConfigurationMapping
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        emailConfigurationMapping: EmailServerConfigurationMapping = EmailServerConfigurationMapping(self.emailServerConfigurationInterface)
        hashMap: dict = emailConfigurationMapping.toHashMap()
        node: Node = ModDomHelper.createNodeWithValueNodes(document, EmailServerConfigurationData.NAME, hashMap)
        return node
# from java.util.HashMap import HashMap
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


