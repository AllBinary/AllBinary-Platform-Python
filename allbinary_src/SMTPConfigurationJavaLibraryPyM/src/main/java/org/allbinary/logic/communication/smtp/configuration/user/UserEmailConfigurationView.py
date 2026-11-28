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
# package org.allbinary.logic.communication.smtp.configuration.user

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class UserEmailConfigurationView(DomNodeInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "userEmailConfigurationInterface" not in vars(self): self.userEmailConfigurationInterface: UserEmailConfigurationInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__.__jconstructor1(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "Node" for base in type(args[0]).__mro__)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)
    

    def _constructor1_1(self, node: Node) -> None:
        from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfiguration import UserEmailConfiguration
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventsConfigurationData import UserEmailEventsConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventsConfigurationView import UserEmailEventsConfigurationView
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
            self.logUtil.putF(self.commonStrings.CONSTRUCTOR, self, self.commonStrings.CONSTRUCTOR)
        self.userEmailConfigurationInterface = UserEmailConfiguration()
        childNodeList: NodeList = node.getChildNodes()
        userEmailEventsConfigurationNode: Node = DomSearchHelper.getNodeNoThrow(UserEmailEventsConfigurationData.NAME, childNodeList)
        userEmailEventsConfigurationView: UserEmailEventsConfigurationView = UserEmailEventsConfigurationView(userEmailEventsConfigurationNode)
        self.userEmailConfigurationInterface.setUserEmailEventsConfigurationInterface(userEmailEventsConfigurationView.getUserEmailEventsConfigurationInterface())
    

    def _constructor1_2(self, userEmailConfigurationInterface: UserEmailConfigurationInterface) -> None:
        __class__._init_fields(self)
        self.userEmailConfigurationInterface = userEmailConfigurationInterface
    

    def getEmailConfigurationInterface(self) -> UserEmailConfigurationInterface:
        return self.userEmailConfigurationInterface
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfigurationMapping import UserEmailConfigurationMapping
        from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfigurationData import UserEmailConfigurationData
        from java.util.HashMap import HashMap
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventsConfigurationInterface import UserEmailEventsConfigurationInterface
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventsConfigurationView import UserEmailEventsConfigurationView
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        emailConfigurationMapping: UserEmailConfigurationMapping = UserEmailConfigurationMapping(self.userEmailConfigurationInterface)
        hashMap: HashMap = emailConfigurationMapping.toHashMap()
        node: Node = ModDomHelper.createNameValueNodes(document, UserEmailConfigurationData.NAME, hashMap)
        userEmailConfigurationInterface: UserEmailConfigurationInterface = self.getEmailConfigurationInterface()
        userEmailEventsConfigurationInterface: UserEmailEventsConfigurationInterface = userEmailConfigurationInterface.getUserEmailEventsConfigurationInterface()
        userEmailEventsConfigurationView: UserEmailEventsConfigurationView = UserEmailEventsConfigurationView(userEmailEventsConfigurationInterface)
        node.appendChild(userEmailEventsConfigurationView.toXmlNode(document))
        return node
# from java.util.HashMap import HashMap
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventsConfigurationData import UserEmailEventsConfigurationData
# from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventsConfigurationInterface import UserEmailEventsConfigurationInterface
# from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventsConfigurationView import UserEmailEventsConfigurationView
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


