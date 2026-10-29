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
# package org.allbinary.business.context.configuration

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class ContextConfigurationView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.contextConfigurationInterface: ContextConfigurationInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.business.context.configuration.ContextConfiguration import ContextConfiguration
        self._init_fields()
        childNodeList: NodeList = node.getChildNodes()
        self.contextConfigurationInterface = ContextConfiguration()
        emailConfigurationNode: Node = DomSearchHelper.getNode(EmailServerConfigurationData.NAME, childNodeList)
        emailServerConfigurationView: EmailServerConfigurationView = EmailServerConfigurationView(emailConfigurationNode)
        self.contextConfigurationInterface.setEmailServerConfigurationInterface(emailServerConfigurationView.getEmailConfigurationInterface())
    

    def _constructor1(self, contextConfigurationInterface: ContextConfigurationInterface) -> None:
        self._init_fields()
        self.contextConfigurationInterface = contextConfigurationInterface
    

    def getContextConfigurationInterface(self) -> ContextConfigurationInterface:
        return self.contextConfigurationInterface
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.context.configuration.ContextConfigurationData import ContextConfigurationData
        node: Node = document.createElement(ContextConfigurationData.getInstance().NAME)
        emailServerConfigurationView: EmailServerConfigurationView = EmailServerConfigurationView(self.getContextConfigurationInterface().getEmailServerConfigurationInterface())
        node.appendChild(emailServerConfigurationView.toXmlNode(document))
        return node
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationInterface import EmailServerConfigurationInterface
from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationView import EmailServerConfigurationView
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


