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
# package org.allbinary.logic.communication.smtp.configuration.user.event

from __future__ import annotations



# Java interface
class UserEmailEventsConfigurationInterface:
    

    def getEventConfigurationHashMap(self) -> dict:
        raise NotImplementedError()
    

    def addUserEmailEventConfiguration(self, userEmailEventConfigurationInterface: UserEmailEventConfigurationInterface) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def getEventListener(self, abeClientInformation: AbeClientInformationInterface, userEmailEventNameData: UserEmailEventNameData, userInterface: UserInterface) -> UserEmailEventListenerInterface:
        raise NotImplementedError()
# from java.util.HashMap import HashMap
from org.allbinary.business.user.UserInterface import UserInterface
from org.allbinary.logic.communication.smtp.event.UserEmailEventListenerInterface import UserEmailEventListenerInterface
from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface


