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
# package org.allbinary.logic.communication.smtp.event.handler.factory

from __future__ import annotations



class UserEmailEventHandlerSingletons:
    instance: UserEmailEventHandlerSingletons = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.userEmailEventHandlerHashMap: dict = StdUtil.getInstance().createHashMap()
    

    @staticmethod
    def getInstance() -> UserEmailEventHandlerSingletons:
        return UserEmailEventHandlerSingletons.instance
    

    def __init__(self) -> None:
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, abeClientInformation: AbeClientInformationInterface, userEmailEventNameData: UserEmailEventNameData, userInterface: UserInterface) -> UserEmailEventHandler:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.GET_INSTANCE)
        userEmailEventHandler: UserEmailEventHandler = self.userEmailEventHandlerHashMap.get(userEmailEventNameData)
        if userEmailEventHandler is None:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
                self.logUtil.putF("Creating New Named UserEmailEventHandler", self, self.commonStrings.GET_INSTANCE)
            newUserEmailEventHandler: UserEmailEventHandler = UserEmailEventHandler()
            vector: BasicArrayList = EmailEventHandlerUtil.getUserEmailEventListenerVector(abeClientInformation, userEmailEventNameData, userInterface)
            newUserEmailEventHandler.addListener(vector)
            newUserEmailEventHandler.addListener(LogUserEmailEventListenerModule())
            self.userEmailEventHandlerHashMap.put(userEmailEventNameData, newUserEmailEventHandler)
            return newUserEmailEventHandler
        else:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
                self.logUtil.putF("Returning existing UserEmailEventHandler", self, self.commonStrings.GET_INSTANCE)
            return userEmailEventHandler
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.user.UserInterface import UserInterface
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
from org.allbinary.logic.communication.smtp.event.handler.EmailEventHandlerUtil import EmailEventHandlerUtil
from org.allbinary.logic.communication.smtp.event.handler.UserEmailEventHandler import UserEmailEventHandler
from org.allbinary.logic.communication.smtp.event.modules.log.LogUserEmailEventListenerModule import LogUserEmailEventListenerModule
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.string.CommonStrings import CommonStrings


UserEmailEventHandlerSingletons.instance = UserEmailEventHandlerSingletons()

