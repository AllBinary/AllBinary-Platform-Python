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
        if "emailServerConfigurationInterface" not in vars(self): self.emailServerConfigurationInterface: EmailServerConfigurationInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__.__jconstructor1(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "Node" for base in type(args[0]).__mro__)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)
    

    def _constructor1_1(self, node: Node) -> None:
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfiguration import EmailServerConfiguration
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        __class__._init_fields(self)
        childNodeList: NodeList = node.getChildNodes()
        server: str = DomNodeHelper.getTextNodeValue(EmailServerConfigurationData.SERVER, childNodeList)
        accountName: str = DomNodeHelper.getTextNodeValue(EmailServerConfigurationData.ACCOUNT, childNodeList)
        password: str = DomNodeHelper.getTextNodeValue(EmailServerConfigurationData.PASSWORD, childNodeList)
        self.emailServerConfigurationInterface = EmailServerConfiguration(accountName, password, server)
    

    def _constructor1_2(self, emailServerConfigurationInterface: EmailServerConfigurationInterface) -> None:
        __class__._init_fields(self)
        self.emailServerConfigurationInterface = emailServerConfigurationInterface
    

    def getEmailConfigurationInterface(self) -> EmailServerConfigurationInterface:
        return self.emailServerConfigurationInterface
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationMapping import EmailServerConfigurationMapping
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        from java.util.HashMap import HashMap
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        emailConfigurationMapping: EmailServerConfigurationMapping = EmailServerConfigurationMapping(self.emailServerConfigurationInterface)
        hashMap: HashMap = emailConfigurationMapping.toHashMap()
        node: Node = ModDomHelper.createNodeWithValueNodes(document, EmailServerConfigurationData.NAME, hashMap)
        return node
# from java.util.HashMap import HashMap
# from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList


