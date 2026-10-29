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
# package org.allbinary.logic.communication.smtp

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class EmailsNotUsed(DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.emailInfoVector: BasicArrayList = None
    

    def __init__(self) -> None:
        self._init_fields()
        self.emailInfoVector = BasicArrayListD()
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.communication.smtp.EmailData import EmailData
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PAYMENT):
                self.logUtil.putF(self.commonStrings.START, self, "toXmlNode")
            node: Node = document.createElement(EmailData.NAME)
            size: int = self.emailInfoVector.size()
            for index in range(0, size):
                email: Email = self.emailInfoVector.get(index)
                emailNode: Node = email.toXmlNode(document)
                if emailNode is not None:
                    node.appendChild(emailNode)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PAYMENT):
                self.logUtil.putF(self.commonStrings.END, self, "toXmlNode()")
            return node
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGINGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "toXmlNode()", e)
            error: str = "Error Processing Order.  Please contact us if error persists.<p/>"
            return BasicErrorNodeUtil.get(document, error)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.data.tree.dom.BasicErrorNodeUtil import BasicErrorNodeUtil
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


