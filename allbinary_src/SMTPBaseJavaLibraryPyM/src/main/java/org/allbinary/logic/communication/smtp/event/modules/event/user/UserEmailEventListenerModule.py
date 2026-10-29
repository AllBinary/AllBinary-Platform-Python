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
# package org.allbinary.logic.communication.smtp.event.modules.event.user

from __future__ import annotations

from org.allbinary.logic.communication.smtp.event.UserEmailEventListenerInterface import UserEmailEventListenerInterface


class UserEmailEventListenerModule(UserEmailEventListenerInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.userInterface: UserInterface = None
    

    def __init__(self, userInterface: UserInterface) -> None:
        self._init_fields()
        self.userInterface = userInterface
    

    # throws Exception
    def onEmailSendFailure(self, emailEvent: EmailEvent) -> None:
        to: str = self.userInterface.getSecondaryEmail()
        email: BasicEmail = BasicEmail(emailEvent.getEmailInfo(), to)
        EmailQueueFactory.getInstance().offer(email.getEmail())
    

    # throws Exception
    def onEmailSendRequest(self, emailEvent: EmailEvent) -> None:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            self.logUtil.putF("Add Email To Que For Sending: " + str(emailEvent), self, "onEmailSendRequest")
        to: str = self.userInterface.getMainEmail()
        email: BasicEmail = BasicEmail(emailEvent.getEmailInfo(), to)
        EmailQueueFactory.getInstance().offer(email.getEmail())
from org.allbinary.business.user.UserInterface import UserInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.smtp.BasicEmail import BasicEmail
from org.allbinary.logic.communication.smtp.EmailInterface import EmailInterface
from org.allbinary.logic.communication.smtp.event.EmailEvent import EmailEvent
from org.allbinary.logic.communication.smtp.queue.EmailQueueFactory import EmailQueueFactory


