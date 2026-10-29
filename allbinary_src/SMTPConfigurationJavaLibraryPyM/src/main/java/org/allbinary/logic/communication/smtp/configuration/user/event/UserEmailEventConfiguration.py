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

from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationInterface import UserEmailEventConfigurationInterface


class UserEmailEventConfiguration(UserEmailEventConfigurationInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.name: str = None
        self.eventListenerClassPath: str = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
        self.setName(StringUtil.getInstance().EMPTY_STRING)
        self.setEventListenerClassPath(StringUtil.getInstance().EMPTY_STRING)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            self.logUtil.putF("New", self, " Constructor")
    

    def _constructor1(self, hashMap: dict) -> None:
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationData import UserEmailEventConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventConfigurationData import UserEmailEventConfigurationData
        self._init_fields()
        self.setName(hashMap.get(UserEmailEventConfigurationData.NAME))
        self.setEventListenerClassPath(hashMap.get(UserEmailEventConfigurationData.LISTENER_CLASSPATH))
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            self.logUtil.putF("Log: " + str(self.log()), self, " Constructor")
    

    def getName(self) -> str:
        return self.name
    

    def setName(self, name: str) -> None:
        self.name = name
    

    def getEventListenerClassPath(self) -> str:
        return self.eventListenerClassPath
    

    def setEventListenerClassPath(self, eventListenerClassPath: str) -> None:
        self.eventListenerClassPath = eventListenerClassPath
    

    def log(self) -> str:
        return "\nUser Email Event Log Info:" + "\nName: " + self.getName() + "\nEventListenerClassPath: " + str(self.getEventListenerClassPath())
# from java.util.HashMap import HashMap
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil


