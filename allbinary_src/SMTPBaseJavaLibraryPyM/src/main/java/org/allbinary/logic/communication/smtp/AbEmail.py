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

from org.allbinary.logic.communication.smtp.EmailInterface import EmailInterface


class AbEmail(EmailInterface):

    def _init_fields(self) -> None:
        self.email: Email = None
    

    def __init__(self, server: str, from_: str, to: str, subject: str, textBody: str, htmlAttachment: str, contentBase: str) -> None:
        from org.allbinary.logic.communication.smtp.Email import Email
        from org.allbinary.logic.communication.smtp.Email import Email
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGINGERROR):
            self.email = Email(from_, to, subject, server, textBody, htmlAttachment, contentBase, True)
        else:
            self.email = Email(from_, to, subject, server, textBody, htmlAttachment, contentBase)
    

    def getMimeMessage(self) -> MimeMessage:
        return self.email.getMimeMessage()
    

    def getDebugInfo(self) -> str:
        return self.email.getDebugInfo()
    

    # throws Exception
    def log(self) -> str:
        return self.email.log()
    

    # throws Exception
    def toHashMap(self) -> dict:
        return self.email.toHashMap()
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        return self.email.toXmlNode(document)
    

    def getEmail(self) -> Email:
        return self.email
    

    # throws Exception
    def toXmlDoc(self) -> Document:
        return self.email.toXmlDoc()
# from java.util.HashMap import HashMap
# from javax.mail.internet.MimeMessage import MimeMessage
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


