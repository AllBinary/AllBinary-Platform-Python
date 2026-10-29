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
# package org.allbinary.logic.communication.smtp.event.modules.log

from __future__ import annotations

from org.allbinary.logic.communication.smtp.event.UserEmailEventListenerInterface import UserEmailEventListenerInterface


class LogUserEmailEventListenerModule(UserEmailEventListenerInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def onEmailSendRequest(self, userEmailInfoEvent: EmailEvent) -> None:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            message: str = "Logging EmailEvent - Temporary Listener for debugging.\n\n" + str(userEmailInfoEvent)
            self.logUtil.putF(message, self, "onEmailSendRequest")
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.smtp.event.EmailEvent import EmailEvent


