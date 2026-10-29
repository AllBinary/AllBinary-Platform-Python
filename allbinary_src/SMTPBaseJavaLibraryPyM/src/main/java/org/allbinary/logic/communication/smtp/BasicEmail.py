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


class BasicEmail(EmailInterface):

    def _init_fields(self) -> None:
        self.email: AbEmail = None
    

    def __init__(self, emailInfo: EmailInfo, to: str) -> None:
        from org.allbinary.logic.communication.smtp.AbEmail import AbEmail
        self._init_fields()
        basicEmailInfo: BasicEmailInfo = emailInfo.getBasicEmailInfo()
        self.email = AbEmail(basicEmailInfo.getEmailServerConfigurationInterface().getSmtpServer(), basicEmailInfo.getEmailServerConfigurationInterface().getAccountName(), to, basicEmailInfo.getSubject(), basicEmailInfo.getTextBody(), emailInfo.getHtmlAttachment(), emailInfo.getContentBase())
    

    def getEmail(self) -> Email:
        return self.email.getEmail()
    

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
    

    # throws Exception
    def toXmlDoc(self) -> Document:
        return self.email.toXmlDoc()
# from java.util.HashMap import HashMap
# from javax.mail.internet.MimeMessage import MimeMessage
from org.allbinary.logic.communication.smtp.info.BasicEmailInfo import BasicEmailInfo
from org.allbinary.logic.communication.smtp.info.EmailInfo import EmailInfo
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


