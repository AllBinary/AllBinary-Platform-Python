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



class UserEmailEventListenerFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getInstance(abeClientInformation: AbeClientInformationInterface, userEmailEventConfigurationInterface: UserEmailEventConfigurationInterface, userInterface: UserInterface) -> UserEmailEventListenerInterface:
        params: list[object] = [None] * (1)
        classes: list[type] = [None] * (1)
        classes[0] = UserInterface
        params[0] = userInterface
        return AbeFactory.getInstance().getInstance(abeClientInformation, userEmailEventConfigurationInterface.getEventListenerClassPath(), classes, params)
from org.allbinary.business.user.UserInterface import UserInterface
from org.allbinary.logic.communication.smtp.event.UserEmailEventListenerInterface import UserEmailEventListenerInterface
from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface


