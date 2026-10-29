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

from org.allbinary.business.user.modules.configuration.UserConfigurationInterface import UserConfigurationInterface


class UserConfiguration(UserConfigurationInterface):

    def _init_fields(self) -> None:
        self.userEmailConfigurationInterface: UserEmailConfigurationInterface = None
        self.timeCreated: TimeCreated = None
        self.timeLastModified: TimeLastModified = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
        self.userEmailConfigurationInterface = UserEmailConfiguration()
        self.timeCreated = TimeCreated(0)
        self.timeLastModified = TimeLastModified(0)
    

    def _constructor1(self, hashMap: dict) -> None:
        self._init_fields()
        self.userEmailConfigurationInterface = UserEmailConfiguration(hashMap)
        self.timeCreated = TimeCreated(hashMap.get(EntryData.getInstance().TIMECREATED))
        self.timeLastModified = TimeLastModified(hashMap.get(EntryData.getInstance().LASTMODIFIED))
    

    def getUserEmailConfigurationInterface(self) -> UserEmailConfigurationInterface:
        return self.userEmailConfigurationInterface
    

    def setUserEmailConfigurationInterface(self, userEmailConfigurationInterface: UserEmailConfigurationInterface) -> None:
        self.userEmailConfigurationInterface = userEmailConfigurationInterface
    

    def getTimeCreated(self) -> TimeCreated:
        return self.timeCreated
    

    def getTimeLastModified(self) -> TimeLastModified:
        return self.timeLastModified
    

    def setTimeCreated(self, timeCreated: TimeCreated) -> None:
        self.timeCreated = timeCreated
    

    def setTimeLastModified(self, timeLastModified: TimeLastModified) -> None:
        self.timeLastModified = timeLastModified
# from java.util.HashMap import HashMap
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.time.created.TimeCreated import TimeCreated
from org.allbinary.business.time.modified.TimeLastModified import TimeLastModified
from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfiguration import UserEmailConfiguration
from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfigurationInterface import UserEmailConfigurationInterface


