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
# package org.allbinary.business.user.modules.configuration

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class UserConfigurationView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.userConfigurationInterface: UserConfigurationInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.business.user.modules.configuration.UserConfiguration import UserConfiguration
        self._init_fields()
        self.userConfigurationInterface = UserConfiguration()
        childNodeList: NodeList = node.getChildNodes()
        emailConfigurationNode: Node = DomSearchHelper.getNode(UserEmailConfigurationData.NAME, childNodeList)
        userEmailConfigurationView: UserEmailConfigurationView = UserEmailConfigurationView(emailConfigurationNode)
        userEmailConfigurationInterface: UserEmailConfigurationInterface = userEmailConfigurationView.getEmailConfigurationInterface()
        self.userConfigurationInterface.setUserEmailConfigurationInterface(userEmailConfigurationInterface)
        timeCreatedNode: Node = DomSearchHelper.getNode(EntryData.getInstance().TIMECREATED, childNodeList)
        timeCreatedView: TimeCreatedView = TimeCreatedView(timeCreatedNode)
        self.userConfigurationInterface.setTimeCreated(timeCreatedView.getTimeCreated())
        timeLastModifiedNode: Node = DomSearchHelper.getNode(EntryData.getInstance().LASTMODIFIED, childNodeList)
        timeLastModifiedView: TimeLastModifiedView = TimeLastModifiedView(timeLastModifiedNode)
        self.userConfigurationInterface.setTimeLastModified(timeLastModifiedView.getTimeLastModified())
    

    def _constructor1(self, userConfigurationInterface: UserConfigurationInterface) -> None:
        self._init_fields()
        self.userConfigurationInterface = userConfigurationInterface
    

    def getUserConfigurationInterface(self) -> UserConfigurationInterface:
        return self.userConfigurationInterface
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.user.modules.configuration.UserConfigurationData import UserConfigurationData
        node: Node = document.createElement(UserConfigurationData.NAME)
        userEmailConfigurationView: UserEmailConfigurationView = UserEmailConfigurationView(self.userConfigurationInterface.getUserEmailConfigurationInterface())
        node.appendChild(userEmailConfigurationView.toXmlNode(document))
        timeCreatedView: TimeCreatedView = TimeCreatedView(self.userConfigurationInterface.getTimeCreated())
        node.appendChild(timeCreatedView.toXmlNode(document))
        timeLastModifiedView: TimeLastModifiedView = TimeLastModifiedView(self.userConfigurationInterface.getTimeLastModified())
        node.appendChild(timeLastModifiedView.toXmlNode(document))
        return node
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.time.created.TimeCreatedView import TimeCreatedView
from org.allbinary.business.time.modified.TimeLastModifiedView import TimeLastModifiedView
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfigurationData import UserEmailConfigurationData
from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfigurationInterface import UserEmailConfigurationInterface
from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfigurationView import UserEmailConfigurationView
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


