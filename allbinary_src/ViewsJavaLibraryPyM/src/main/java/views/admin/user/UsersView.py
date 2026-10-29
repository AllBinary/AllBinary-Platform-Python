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
# package views.admin.user

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from views.business.context.HttpContextView import HttpContextView


class UsersView(HttpContextView, DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.userVector: BasicArrayList = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
    

    def toXmlNode(self, document: Document) -> Node:
        try:
            usersNode: Node = document.createElement(UsersData.NAME)
            size: int = self.userVector.size()
            for index in range(0, size):
                userInterface: User = self.userVector.get(index)
                if userInterface is not None:
                    node: Node = UserDomNode(userInterface).toXmlNode(document)
                    usersNode.appendChild(node)
                else:
                    self.logUtil.putF("UserHelper", self, "toXmlNode")
            return usersNode
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().XSLLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "toXmlNode", e)
            return None
    

    def addDomNodeInterfaces(self) -> None:
        self.addDomNodeInterface(self)
    

    # throws Exception
    def view(self) -> str:
        try:
            self.addDomNodeInterfaces()
            return super().view()
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.user.UserDomNode import UserDomNode
from org.allbinary.business.user.UsersData import UsersData
from org.allbinary.business.user.modules.User import User
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


