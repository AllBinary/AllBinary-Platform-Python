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


class Email(EmailInterface):
    DEBUG: str = "mail.debug"
    SMTP_HOST: str = "mail.smtp.host"
    SMTP_PORT: str = "mail.smtp.port"
    SMTP_USER: str = "mail.smtp.user"
    SMTP_RETURN_ADDRESS: str = "mail.from"
    SMTP_LOCAL_HOST: str = "mail.smtp.localhost"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.msg: MimeMessage = None
        self.properties: Properties = None
        self.bs: ByteArrayOutputStream = None
        self.isDebug: bool = None

    def __init__(self, *args) -> None:
        if len(args) == 7:
            self._constructor7(*args)
        elif len(args) == 8:
            self._constructor8(*args)
    

    def _constructor7(self, from_: str, to: str, subject: str, server: str, textBody: str, htmlAttachment: str, contentBase: str) -> None:
        self._init_fields()
        self.isDebug = False
        self.init(from_, to, subject, server, textBody, htmlAttachment, contentBase)
    

    def _constructor8(self, from_: str, to: str, subject: str, server: str, textBody: str, htmlAttachment: str, contentBase: str, isDebug: bool) -> None:
        self._init_fields()
        self.isDebug = isDebug
        self.init(from_, to, subject, server, textBody, htmlAttachment, contentBase)
    

    # throws Exception
    def init(self, from_: str, to: str, subject: str, server: str, textBody: str, htmlAttachment: str, contentBase: str) -> None:
        try:
            stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
            mimeBodyParts: list[MimeBodyPart] = [None] * ((2 if not stringValidationUtil.isEmpty(htmlAttachment) else 1))
            mimeBodyParts[0] = MimeBodyPart()
            mimeBodyParts[0].setText(textBody)
            if not stringValidationUtil.isEmpty(htmlAttachment):
                internetHeaders: InternetHeaders = InternetHeaders()
                internetHeaders.addHeader("Content-Type", "text/html")
                if not stringValidationUtil.isEmpty(contentBase):
                    internetHeaders.addHeader("Content-Base", contentBase)
                mimeBodyParts[1] = MimeBodyPart(internetHeaders, list(htmlAttachment.encode()))
            self.init(server, None, [InternetAddress(from_)], [InternetAddress(to)], None, None, subject, mimeBodyParts)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGINGERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, "emailConstructor", e)
            raise e
    

    # throws MessagingException
    # Java overloaded method: Python keeps the last definition
    def init(self, server: str, authenticator: Authenticator, addresses_from: list[InternetAddress], addresses_to: list[InternetAddress], addresses_cc: list[InternetAddress], addresses_bcc: list[InternetAddress], subject: str, mimeBodyParts: list[MimeBodyPart]) -> None:
        self.properties = Properties()
        self.properties.put(Email.SMTP_HOST, server)
        try:
            hostName: str = StringUtil.getInstance().EMPTY_STRING
            if StringValidationUtil.getInstance().isEmpty(hostName):
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGINGERROR):
                    self.logUtil.putF("Unable to get HostName so using fake", self, "init()")
                self.properties.put(Email.SMTP_LOCAL_HOST, "FakeHostName")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGINGERROR):
                self.logUtil.put("Continuing on Exception: Unable to get HostName", self, "init()", e)
            self.properties.put(Email.SMTP_LOCAL_HOST, "FakeHostName")
        if self.isDebug:
            self.properties.put(Email.DEBUG, "true")
        session: Session = Session.getInstance(self.properties, authenticator)
        if self.isDebug:
            session.setDebug(True)
            self.bs = ByteArrayOutputStream()
            printStream: PrintStream = PrintStream(self.bs)
            session.setDebugOut(printStream)
        self.msg = MimeMessage(session)
        self.msg.addFrom(addresses_from)
        self.msg.setRecipients(Message.RecipientType.TO, addresses_to)
        self.msg.setRecipients(Message.RecipientType.CC, addresses_cc)
        self.msg.setRecipients(Message.RecipientType.BCC, addresses_bcc)
        self.msg.setSubject(subject)
        mimeMultipart: MimeMultipart = MimeMultipart()
        for i in range(0, len(mimeBodyParts)):
            mimeMultipart.addBodyPart(mimeBodyParts[i])
        self.msg.setContent(mimeMultipart)
    

    def getMimeMessage(self) -> MimeMessage:
        return self.msg
    

    def getDebugInfo(self) -> str:
        if self.isDebug:
            return "More Logging Before This To Standard Out: " + str(str(str(self.bs)))
        else:
            return "Debugging Is Off"
    

    # throws Exception
    def log(self) -> str:
        return "\nHashMap: " + str(self.toHashMap())
    

    # throws Exception
    def toHashMap(self) -> dict:
        from org.allbinary.logic.communication.smtp.EmailData import EmailData
        from org.allbinary.logic.communication.smtp.EmailData import EmailData
        from org.allbinary.logic.communication.smtp.EmailData import EmailData
        from org.allbinary.logic.communication.smtp.EmailData import EmailData
        from org.allbinary.logic.communication.smtp.EmailData import EmailData
        from org.allbinary.logic.communication.smtp.EmailData import EmailData
        from org.allbinary.logic.communication.smtp.EmailData import EmailData
        try:
            hashMap: dict = StdUtil.getInstance().createHashMap()
            hashMap.put(EmailData.SERVER, self.properties.get(Email.SMTP_HOST))
            addresses: list[Address] = self.msg.getFrom()
            if addresses is not None:
                for index in range(0, len(addresses)):
                    hashMap.put(EmailData.FROM, str(addresses[index]))
            addresses = self.msg.getRecipients(Message.RecipientType.TO)
            if addresses is not None:
                for index in range(0, len(addresses)):
                    hashMap.put(EmailData.TO, str(addresses[index]))
            addresses = self.msg.getRecipients(Message.RecipientType.CC)
            if addresses is not None:
                for index in range(0, len(addresses)):
                    hashMap.put(EmailData.CC, str(addresses[index]))
            addresses = self.msg.getRecipients(Message.RecipientType.BCC)
            if addresses is not None:
                for index in range(0, len(addresses)):
                    hashMap.put(EmailData.BCC, str(addresses[index]))
            hashMap.put(EmailData.SUBJECT, self.msg.getSubject())
            mimeMultipart: MimeMultipart = self.msg.getContent()
            if mimeMultipart is not None:
                for index in range(0, mimeMultipart.getCount()):
                    content: str = mimeMultipart.getBodyPart(index).getContent()
                    hashMap.put(EmailData.CONTENT, content)
            return hashMap
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGINGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "toHashMap()", e)
            raise e
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.communication.smtp.EmailData import EmailData
        node: Node = ModDomHelper.createNameValueNodes(document, EmailData.NAME, self.toHashMap())
        return node
    

    # throws Exception
    def toXmlDoc(self) -> Document:
        raise Exception(CommonStrings.getInstance().NOT_IMPLEMENTED)
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.PrintStream import PrintStream
# from java.util.HashMap import HashMap
# from java.util.Properties import Properties
# from javax.mail.Address import Address
# from javax.mail.Authenticator import Authenticator
# from javax.mail.Message import Message
# from javax.mail.MessagingException import MessagingException
# from javax.mail.Session import Session
# from javax.mail.internet.InternetAddress import InternetAddress
# from javax.mail.internet.InternetHeaders import InternetHeaders
# from javax.mail.internet.MimeBodyPart import MimeBodyPart
# from javax.mail.internet.MimeMessage import MimeMessage
# from javax.mail.internet.MimeMultipart import MimeMultipart
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


