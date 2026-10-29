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
# package org.allbinary.logic.communication.smtp.email

from __future__ import annotations



class NewPasswordEmail:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = None
        self.userInterface: UserInterface = None
        self.newPassword: str = None
    

    def __init__(self, abeClientInformation: AbeClientInformationInterface, userInterface: UserInterface, newPassword: str) -> None:
        self._init_fields()
        self.abeClientInformation = abeClientInformation
        self.userInterface = userInterface
        self.newPassword = newPassword
    

    # throws Exception
    def process(self) -> None:
        self.notifyStoreAdmin()
        self.notifyUser()
    

    # throws Exception
    def notifyStoreAdmin(self) -> None:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
                self.logUtil.putF("notifyStoreAdmin", self, "notifyStoreAdmin")
            emailSubject: str = "New Password For User: " + str(self.userInterface.getUserName())
            emailBody: str = "New Password: " + self.newPassword
            basicEmailInfo: BasicEmailInfo = AdminEmailInfo(emailSubject, emailBody)
            emailInfo: EmailInfo = EmailInfo(basicEmailInfo)
            adminUserEmailEventHandler: UserEmailEventHandler = AdminUserEmailEventHandlerSingletons.getInstance().getInstance(self.abeClientInformation, UserEmailEventNameData.NEWPASSWORD)
            adminUserEmailEventHandler.receiveEmailInfo(UserEmailEventNameData.NEWPASSWORD, emailInfo)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGINGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "emailAdmin", e)
    

    # throws Exception
    def notifyUser(self) -> None:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
                self.logUtil.putF("Email User", self, "notifyUser()")
            subject: str = "New Password"
            body: str = "New Password: " + self.newPassword
            basicEmailInfo: BasicEmailInfo = AdminEmailInfo(subject, body)
            emailInfo: EmailInfo = EmailInfo(basicEmailInfo)
            userEmailEventHandler: UserEmailEventHandler = UserEmailEventHandlerSingletons.getInstance().getInstance(self.abeClientInformation, UserEmailEventNameData.NEWPASSWORD, self.userInterface)
            userEmailEventHandler.receiveEmailInfo(UserEmailEventNameData.NEWPASSWORD, emailInfo)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGINGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "notifyUser", e)
            raise e
from org.allbinary.business.user.UserInterface import UserInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
from org.allbinary.logic.communication.smtp.event.handler.UserEmailEventHandler import UserEmailEventHandler
from org.allbinary.logic.communication.smtp.event.handler.factory.AdminUserEmailEventHandlerSingletons import AdminUserEmailEventHandlerSingletons
from org.allbinary.logic.communication.smtp.event.handler.factory.UserEmailEventHandlerSingletons import UserEmailEventHandlerSingletons
from org.allbinary.logic.communication.smtp.info.AdminEmailInfo import AdminEmailInfo
from org.allbinary.logic.communication.smtp.info.BasicEmailInfo import BasicEmailInfo
from org.allbinary.logic.communication.smtp.info.EmailInfo import EmailInfo
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.string.CommonStrings import CommonStrings


