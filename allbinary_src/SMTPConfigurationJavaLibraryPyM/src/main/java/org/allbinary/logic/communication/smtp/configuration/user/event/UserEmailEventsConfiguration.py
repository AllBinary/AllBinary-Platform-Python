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

from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventsConfigurationInterface import UserEmailEventsConfigurationInterface


class UserEmailEventsConfiguration(UserEmailEventsConfigurationInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.emailEventHashMap: dict = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
        self.init()
    

    def _constructor1(self, hashMap: dict) -> None:
        self._init_fields()
        self.init()
    

    def init(self) -> None:
        self.emailEventHashMap = StdUtil.getInstance().createHashMap()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            self.logUtil.putF(self.commonStrings.CONSTRUCTOR, self, " Constructor")
    

    def getEventConfigurationHashMap(self) -> dict:
        return self.emailEventHashMap
    

    def addUserEmailEventConfiguration(self, userEmailEventConfigurationInterface: UserEmailEventConfigurationInterface) -> None:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            self.logUtil.putF("Adding: " + str(userEmailEventConfigurationInterface.log()), self, "addUserEmailEventConfiguration")
        self.emailEventHashMap.put(userEmailEventConfigurationInterface.getName(), userEmailEventConfigurationInterface)
    

    # throws Exception
    def getEventListener(self, abeClientInformation: AbeClientInformationInterface, userEmailEventNameData: UserEmailEventNameData, userInterface: UserInterface) -> UserEmailEventListenerInterface:
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventListenerFactory import UserEmailEventListenerFactory
        userEmailEventConfigurationInterface: UserEmailEventConfigurationInterface = self.emailEventHashMap.get(str(userEmailEventNameData))
        return UserEmailEventListenerFactory.getInstance(abeClientInformation, userEmailEventConfigurationInterface, userInterface)
# from java.util.HashMap import HashMap
from org.allbinary.business.user.UserInterface import UserInterface
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.smtp.event.UserEmailEventListenerInterface import UserEmailEventListenerInterface
from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.string.CommonStrings import CommonStrings


