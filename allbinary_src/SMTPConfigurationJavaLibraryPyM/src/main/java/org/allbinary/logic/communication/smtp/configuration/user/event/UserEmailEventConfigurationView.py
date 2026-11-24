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
            self.__jconstructor1(*args)

    def __jconstructor1(self, *args) -> None:
        if True and not isinstance(args[0], (str, list, int, float)):
            self._constructor1_1(*args)
        else:
            self._constructor1_2(*args)
    

    def _constructor1_1(self, node: Node) -> None:
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfiguration import UserEmailEventConfiguration
        from java.util.HashMap import HashMap
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.allbinary.logic.StdUtil import StdUtil
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        self._init_fields()
        childNodeList: NodeList = node.getChildNodes()
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        name: str = DomNodeHelper.getTextNodeValue(UserEmailEventConfigurationData.NAME, childNodeList)
        hashMap.put(UserEmailEventConfigurationData.NAME, name)
        eventListenerClassPath: str = DomNodeHelper.getTextNodeValue(UserEmailEventConfigurationData.LISTENER_CLASSPATH, childNodeList)
        hashMap.put(UserEmailEventConfigurationData.LISTENER_CLASSPATH, eventListenerClassPath)
        self.setUserEmailEventConfigurationInterface(UserEmailEventConfiguration(hashMap))
    

    def _constructor1_2(self, userEmailEventConfigurationInterface: UserEmailEventConfigurationInterface) -> None:
        self._init_fields()
        self.setUserEmailEventConfigurationInterface(userEmailEventConfigurationInterface)
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationMapping import UserEmailEventConfigurationMapping
        from java.util.HashMap import HashMap
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        userEmailEventConfigurationMapping: UserEmailEventConfigurationMapping = UserEmailEventConfigurationMapping(self.getUserEmailEventConfigurationInterface())
        hashMap: HashMap = userEmailEventConfigurationMapping.toHashMap()
        node: Node = ModDomHelper.createNameValueNodes(document, UserEmailEventConfigurationData.NAME, hashMap)
        return node
    

    def getUserEmailEventConfigurationInterface(self) -> UserEmailEventConfigurationInterface:
        return self.userEmailEventConfigurationInterface
    

    def setUserEmailEventConfigurationInterface(self, userEmailEventConfigurationInterface: UserEmailEventConfigurationInterface) -> None:
        self.userEmailEventConfigurationInterface = userEmailEventConfigurationInterface
# from java.util.HashMap import HashMap
# from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.logic.StdUtil import StdUtil
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList


