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
# package org.allbinary.logic.communication.smtp.configuration.user.event

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class UserEmailEventConfigurationView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.userEmailEventConfigurationInterface: UserEmailEventConfigurationInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationData import UserEmailEventConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationData import UserEmailEventConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationData import UserEmailEventConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationData import UserEmailEventConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfiguration import UserEmailEventConfiguration
        self._init_fields()
        childNodeList: NodeList = node.getChildNodes()
        hashMap: dict = StdUtil.getInstance().createHashMap()
        name: str = DomNodeHelper.getTextNodeValue(UserEmailEventConfigurationData.NAME, childNodeList)
        hashMap.put(UserEmailEventConfigurationData.NAME, name)
        eventListenerClassPath: str = DomNodeHelper.getTextNodeValue(UserEmailEventConfigurationData.LISTENER_CLASSPATH, childNodeList)
        hashMap.put(UserEmailEventConfigurationData.LISTENER_CLASSPATH, eventListenerClassPath)
        self.setUserEmailEventConfigurationInterface(UserEmailEventConfiguration(hashMap))
    

    def _constructor1(self, userEmailEventConfigurationInterface: UserEmailEventConfigurationInterface) -> None:
        self._init_fields()
        self.setUserEmailEventConfigurationInterface(userEmailEventConfigurationInterface)
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationMapping import UserEmailEventConfigurationMapping
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationData import UserEmailEventConfigurationData
        userEmailEventConfigurationMapping: UserEmailEventConfigurationMapping = UserEmailEventConfigurationMapping(self.getUserEmailEventConfigurationInterface())
        hashMap: dict = userEmailEventConfigurationMapping.toHashMap()
        node: Node = ModDomHelper.createNameValueNodes(document, UserEmailEventConfigurationData.NAME, hashMap)
        return node
    

    def getUserEmailEventConfigurationInterface(self) -> UserEmailEventConfigurationInterface:
        return self.userEmailEventConfigurationInterface
    

    def setUserEmailEventConfigurationInterface(self, userEmailEventConfigurationInterface: UserEmailEventConfigurationInterface) -> None:
        self.userEmailEventConfigurationInterface = userEmailEventConfigurationInterface
# from java.util.HashMap import HashMap
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


