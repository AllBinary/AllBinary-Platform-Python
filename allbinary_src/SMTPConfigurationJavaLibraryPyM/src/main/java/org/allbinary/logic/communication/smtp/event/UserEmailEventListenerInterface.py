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
# package org.allbinary.logic.communication.smtp.event

from __future__ import annotations

# from java.util.EventListener import EventListener


# Java interface
class UserEmailEventListenerInterface(EventListener):
    

    # throws Exception
    def onEmailSendRequest(self, userEmailInfoEvent: EmailEvent) -> None:
        raise NotImplementedError()


