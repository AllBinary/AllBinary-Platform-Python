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


class UserEmailEventsConfigurationView(DomNodeInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.userEmailEventsConfigurationInterface: UserEmailEventsConfigurationInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self.__jconstructor1(*args)

    def __jconstructor1(self, *args) -> None:
        if True and not isinstance(args[0], (str, list, int, float)):
            self._constructor1_1(*args)
        else:
            self._constructor1_2(*args)
    

    def _constructor1_1(self, node: Node) -> None:
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventsConfiguration import UserEmailEventsConfiguration
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationView import UserEmailEventConfigurationView
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        self._init_fields()
        self.userEmailEventsConfigurationInterface = UserEmailEventsConfiguration()
        childNodeList: NodeList = node.getChildNodes()
        emailEventConfigurationNodeVector: BasicArrayList = DomSearchHelper.getAllNodesNoThrow(UserEmailEventConfigurationData.NAME, childNodeList)
        size: int = emailEventConfigurationNodeVector.size()
        for index in range(0, size):
            userEmailConfigurationNode: Node = emailEventConfigurationNodeVector.get(index)
            userEmailEventConfigurationView: UserEmailEventConfigurationView = UserEmailEventConfigurationView(userEmailConfigurationNode)
            self.userEmailEventsConfigurationInterface.addUserEmailEventConfiguration(userEmailEventConfigurationView.getUserEmailEventConfigurationInterface())
    

    def _constructor1_2(self, userEmailEventsConfigurationInterface: UserEmailEventsConfigurationInterface) -> None:
        self._init_fields()
        self.userEmailEventsConfigurationInterface = userEmailEventsConfigurationInterface
    

    def getUserEmailEventsConfigurationInterface(self) -> UserEmailEventsConfigurationInterface:
        return self.userEmailEventsConfigurationInterface
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventsConfigurationMapping import UserEmailEventsConfigurationMapping
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationView import UserEmailEventConfigurationView
        from java.util.HashMap import HashMap
        from java.util.Set import Set
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        userEmailConfigurationMapping: UserEmailEventsConfigurationMapping = UserEmailEventsConfigurationMapping(self.userEmailEventsConfigurationInterface)
        node: Node = document.createElement(UserEmailEventsConfigurationData.NAME)
        emailEventHashMap: HashMap = self.getUserEmailEventsConfigurationInterface().getEventConfigurationHashMap()
        set: Set = emailEventHashMap.keySet()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
            self.logUtil.putF("Number Of Email Events Specified in file: " + str(set.size()), self, self.commonStrings.CONSTRUCTOR)
        eventNameArray: list[object] = set.toArray()
        size: int = len(eventNameArray)
        for index in range(0, size):
            eventName: str = eventNameArray[index]
            userEmailEventsConfigurationInterface: UserEmailEventConfigurationInterface = emailEventHashMap.get(eventName)
            userEmailEventConfigurationView: UserEmailEventConfigurationView = UserEmailEventConfigurationView(userEmailEventsConfigurationInterface)
            node.appendChild(userEmailEventConfigurationView.toXmlNode(document))
        return node
# from java.util.HashMap import HashMap
# from java.util.Set import Set
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


