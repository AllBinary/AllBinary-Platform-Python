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
# package org.allbinary.logic.communication.smtp.event.handler

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class EmailEventHandlerUtil:
    instance: EmailEventHandlerUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> EmailEventHandlerUtil:
        return EmailEventHandlerUtil.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws Exception
    def getEventHandler(self, abeClientInformation: AbeClientInformationInterface, userEmailEventNameData: UserEmailEventNameData, userVector: BasicArrayList) -> UserEmailEventHandler:
        from org.allbinary.logic.communication.smtp.event.handler.UserEmailEventHandler import UserEmailEventHandler
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.business.user.UserInterface import UserInterface
        from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
        from org.allbinary.logic.communication.smtp.event.modules.log.LogUserEmailEventListenerModule import LogUserEmailEventListenerModule
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Returning UserEmailEventHandler for ")
            stringBuffer.appendint(userVector.size())
            stringBuffer.append(" users.")
            self.logUtil.putF(str(stringBuffer), self, "getEventHandler")
        userEmailEventHandler: UserEmailEventHandler = UserEmailEventHandler()
        userEmailEventHandler.addListener(LogUserEmailEventListenerModule())
        size: int = userVector.size()
        for index in range(0, size):
            userInterface: UserInterface = userVector.get(index)
            vector: BasicArrayList = EmailEventHandlerUtil.getUserEmailEventListenerVector(abeClientInformation, userEmailEventNameData, userInterface)
            userEmailEventHandler.addListener(vector)
        return userEmailEventHandler
    

    # throws Exception
    @staticmethod
    def getUserEmailEventListenerVector(abeClientInformation: AbeClientInformationInterface, userEmailEventNameData: UserEmailEventNameData, userInterface: UserInterface) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.user.UserInterface import UserInterface
        from org.allbinary.business.user.modules.configuration.UserConfigurationInterface import UserConfigurationInterface
        from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfigurationInterface import UserEmailConfigurationInterface
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventsConfigurationInterface import UserEmailEventsConfigurationInterface
        from org.allbinary.logic.communication.smtp.event.UserEmailEventListenerInterface import UserEmailEventListenerInterface
        from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        userConfigurationInterface: UserConfigurationInterface = userInterface.getUserConfigurationInterface()
        userEmailConfigurationInterface: UserEmailConfigurationInterface = userConfigurationInterface.getUserEmailConfigurationInterface()
        userEmailEventsConfigurationInterface: UserEmailEventsConfigurationInterface = userEmailConfigurationInterface.getUserEmailEventsConfigurationInterface()
        userEmailEventListenerInterface: UserEmailEventListenerInterface = userEmailEventsConfigurationInterface.getEventListener(abeClientInformation, userEmailEventNameData, userInterface)
        vector: BasicArrayList = BasicArrayListD()
        vector.add(userEmailEventListenerInterface)
        return vector
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.user.UserInterface import UserInterface
# from org.allbinary.business.user.modules.configuration.UserConfigurationInterface import UserConfigurationInterface
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.smtp.configuration.user.UserEmailConfigurationInterface import UserEmailConfigurationInterface
# from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventsConfigurationInterface import UserEmailEventsConfigurationInterface
# from org.allbinary.logic.communication.smtp.event.UserEmailEventListenerInterface import UserEmailEventListenerInterface
# from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
# from org.allbinary.logic.communication.smtp.event.modules.log.LogUserEmailEventListenerModule import LogUserEmailEventListenerModule
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _EmailEventHandlerUtil_instance() -> object:
    return EmailEventHandlerUtil()

lazy_static(EmailEventHandlerUtil, "instance", _EmailEventHandlerUtil_instance)

