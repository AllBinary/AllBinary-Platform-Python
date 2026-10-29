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
# package admin.taghelpers

from __future__ import annotations

from admin.taghelpers.TagHelper import TagHelper


class BasicTextEmailHelper(TagHelper):

    def _init_fields(self) -> None:
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        self.hashMap: dict = None
        self.pageContext: PageContext = None
    

    def __init__(self, hashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        self.pageContext = pageContext
        self.hashMap = hashMap
    

    # throws Exception
    def send(self) -> None:
        adminEmailSubject: str = self.hashMap.get("Subject")
        adminEmailTextBody: str = self.hashMap.get("Body")
        adminBasicEmailInfo: BasicEmailInfo = AdminEmailInfo(adminEmailSubject, adminEmailTextBody)
        adminEmailInfo: EmailInfo = EmailInfo(adminBasicEmailInfo)
        adminUserEmailEventHandler: UserEmailEventHandler = AdminUserEmailEventHandlerSingletons.getInstance().getInstance(self.abeClientInformation, UserEmailEventNameData.INSTALLER)
        adminUserEmailEventHandler.receiveEmailInfo(UserEmailEventNameData.INSTALLER, adminEmailInfo)
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
from org.allbinary.logic.communication.smtp.event.handler.UserEmailEventHandler import UserEmailEventHandler
from org.allbinary.logic.communication.smtp.event.handler.factory.AdminUserEmailEventHandlerSingletons import AdminUserEmailEventHandlerSingletons
from org.allbinary.logic.communication.smtp.info.AdminEmailInfo import AdminEmailInfo
from org.allbinary.logic.communication.smtp.info.BasicEmailInfo import BasicEmailInfo
from org.allbinary.logic.communication.smtp.info.EmailInfo import EmailInfo
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory


