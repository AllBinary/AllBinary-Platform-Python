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
        if "userEmailConfigurationInterface" not in vars(self): self.userEmailConfigurationInterface: UserEmailConfigurationInterface = None
        if "timeCreated" not in vars(self): self.timeCreated: TimeCreated = None
        if "timeLastModified" not in vars(self): self.timeLastModified: TimeLastModified = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 1:
            __class__._constructor1(self, *args)
    

    def _constructor0(self) -> None:
        from org.allbinary.business.time.created.TimeCreated import TimeCreated
        from org.allbinary.business.time.modified.TimeLastModified import TimeLastModified
        from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfiguration import UserEmailConfiguration
        from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfigurationInterface import UserEmailConfigurationInterface
        __class__._init_fields(self)
        self.userEmailConfigurationInterface = UserEmailConfiguration()
        self.timeCreated = TimeCreated(0)
        self.timeLastModified = TimeLastModified(0)
    

    def _constructor1(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.time.created.TimeCreated import TimeCreated
        from org.allbinary.business.time.modified.TimeLastModified import TimeLastModified
        from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfiguration import UserEmailConfiguration
        from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfigurationInterface import UserEmailConfigurationInterface
        __class__._init_fields(self)
        self.userEmailConfigurationInterface = UserEmailConfiguration(hashMap)
        self.timeCreated = TimeCreated(hashMap.get(EntryData.getInstance().TIMECREATED))
        self.timeLastModified = TimeLastModified(hashMap.get(EntryData.getInstance().LASTMODIFIED))
    

    def getUserEmailConfigurationInterface(self) -> UserEmailConfigurationInterface:
        from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfigurationInterface import UserEmailConfigurationInterface
        return self.userEmailConfigurationInterface
    

    def setUserEmailConfigurationInterface(self, userEmailConfigurationInterface: UserEmailConfigurationInterface) -> None:
        from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfigurationInterface import UserEmailConfigurationInterface
        self.userEmailConfigurationInterface = userEmailConfigurationInterface
    

    def getTimeCreated(self) -> TimeCreated:
        from org.allbinary.business.time.created.TimeCreated import TimeCreated
        return self.timeCreated
    

    def getTimeLastModified(self) -> TimeLastModified:
        from org.allbinary.business.time.modified.TimeLastModified import TimeLastModified
        return self.timeLastModified
    

    def setTimeCreated(self, timeCreated: TimeCreated) -> None:
        from org.allbinary.business.time.created.TimeCreated import TimeCreated
        self.timeCreated = timeCreated
    

    def setTimeLastModified(self, timeLastModified: TimeLastModified) -> None:
        from org.allbinary.business.time.modified.TimeLastModified import TimeLastModified
        self.timeLastModified = timeLastModified
# from java.util.HashMap import HashMap
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.time.created.TimeCreated import TimeCreated
# from org.allbinary.business.time.modified.TimeLastModified import TimeLastModified
# from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfiguration import UserEmailConfiguration
# from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfigurationInterface import UserEmailConfigurationInterface


