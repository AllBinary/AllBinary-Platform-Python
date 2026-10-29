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
# package org.allbinary.logic.communication.smtp.configuration.user

from __future__ import annotations

from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfigurationInterface import UserEmailConfigurationInterface


class UserEmailConfiguration(UserEmailConfigurationInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.userEmailEventsConfigurationInterface: UserEmailEventsConfigurationInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            self.logUtil.putF(self.commonStrings.CONSTRUCTOR, self, self.commonStrings.CONSTRUCTOR)
        self.setUserEmailEventsConfigurationInterface(UserEmailEventsConfiguration())
    

    def _constructor1(self, hashMap: dict) -> None:
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            self.logUtil.putF(self.commonStrings.CONSTRUCTOR, self, self.commonStrings.CONSTRUCTOR)
        self.setUserEmailEventsConfigurationInterface(UserEmailEventsConfiguration(hashMap))
    

    def getUserEmailEventsConfigurationInterface(self) -> UserEmailEventsConfigurationInterface:
        return self.userEmailEventsConfigurationInterface
    

    def setUserEmailEventsConfigurationInterface(self, userEmailEventsConfigurationInterface: UserEmailEventsConfigurationInterface) -> None:
        self.userEmailEventsConfigurationInterface = userEmailEventsConfigurationInterface
# from java.util.HashMap import HashMap
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventsConfiguration import UserEmailEventsConfiguration
from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventsConfigurationInterface import UserEmailEventsConfigurationInterface
from org.allbinary.string.CommonStrings import CommonStrings


