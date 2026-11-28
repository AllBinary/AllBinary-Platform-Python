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
        if "userEmailEventConfigurationInterface" not in vars(self): self.userEmailEventConfigurationInterface: UserEmailEventConfigurationInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__.__jconstructor1(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "Node" for base in type(args[0]).__mro__)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)
    

    def _constructor1_1(self, node: Node) -> None:
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationData import UserEmailEventConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationData import UserEmailEventConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationData import UserEmailEventConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationData import UserEmailEventConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfiguration import UserEmailEventConfiguration
        from java.util.HashMap import HashMap
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.allbinary.logic.StdUtil import StdUtil
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        __class__._init_fields(self)
        childNodeList: NodeList = node.getChildNodes()
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        name: str = DomNodeHelper.getTextNodeValue(UserEmailEventConfigurationData.NAME, childNodeList)
        hashMap.put(UserEmailEventConfigurationData.NAME, name)
        eventListenerClassPath: str = DomNodeHelper.getTextNodeValue(UserEmailEventConfigurationData.LISTENER_CLASSPATH, childNodeList)
        hashMap.put(UserEmailEventConfigurationData.LISTENER_CLASSPATH, eventListenerClassPath)
        self.setUserEmailEventConfigurationInterface(UserEmailEventConfiguration(hashMap))
    

    def _constructor1_2(self, userEmailEventConfigurationInterface: UserEmailEventConfigurationInterface) -> None:
        __class__._init_fields(self)
        self.setUserEmailEventConfigurationInterface(userEmailEventConfigurationInterface)
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationMapping import UserEmailEventConfigurationMapping
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationData import UserEmailEventConfigurationData
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


