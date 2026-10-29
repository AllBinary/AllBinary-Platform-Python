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
# package org.allbinary.business.user.modules.configuration

from __future__ import annotations



# Java interface
class UserConfigurationInterface:
    

    def getUserEmailConfigurationInterface(self) -> UserEmailConfigurationInterface:
        raise NotImplementedError()
    

    def setUserEmailConfigurationInterface(self, userEmailConfigurationInterface: UserEmailConfigurationInterface) -> None:
        raise NotImplementedError()
    

    def getTimeCreated(self) -> TimeCreated:
        raise NotImplementedError()
    

    def getTimeLastModified(self) -> TimeLastModified:
        raise NotImplementedError()
    

    def setTimeCreated(self, timeCreated: TimeCreated) -> None:
        raise NotImplementedError()
    

    def setTimeLastModified(self, timeLastModified: TimeLastModified) -> None:
        raise NotImplementedError()
from org.allbinary.business.time.created.TimeCreated import TimeCreated
from org.allbinary.business.time.modified.TimeLastModified import TimeLastModified
from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfigurationInterface import UserEmailConfigurationInterface


