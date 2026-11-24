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

from java.lang.JavaRuntimeStatic import lazy_static


class AdminUserEmailEventHandlerSingletons:
    instance: AdminUserEmailEventHandlerSingletons = None

    def _init_fields(self) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.userEmailEventHandlerHashMap: HashMap = StdUtil.getInstance().createHashMap()
    

    @staticmethod
    def getInstance_j0() -> AdminUserEmailEventHandlerSingletons:
        return AdminUserEmailEventHandlerSingletons.instance
    

    def __init__(self) -> None:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        self._init_fields()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
    

    # throws Exception
    def getInstance_j2(self, abeClientInformation: AbeClientInformationInterface, userEmailEventNameData: UserEmailEventNameData) -> UserEmailEventHandler:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
        from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
        from org.allbinary.logic.communication.smtp.event.handler.EmailEventHandlerUtil import EmailEventHandlerUtil
        from org.allbinary.logic.communication.smtp.event.handler.UserEmailEventHandler import UserEmailEventHandler
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.GET_INSTANCE)
        userEmailEventHandler: UserEmailEventHandler = self.userEmailEventHandlerHashMap.get(userEmailEventNameData)
        if userEmailEventHandler is None:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
                self.logUtil.putF("Creating New Named UserEmailEventHandler", self, self.commonStrings.GET_INSTANCE)
            userVector: BasicArrayList = UserEntityFactory.getInstance().getAdministrators()
            newUserEmailEventHandler: UserEmailEventHandler = EmailEventHandlerUtil.getInstance().getEventHandler(abeClientInformation, userEmailEventNameData, userVector)
            self.userEmailEventHandlerHashMap.put(userEmailEventNameData, newUserEmailEventHandler)
            return newUserEmailEventHandler
        else:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
                self.logUtil.putF("Returning existing UserEmailEventHandler", self, self.commonStrings.GET_INSTANCE)
            return userEmailEventHandler

    def getInstance(self, *args):
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
# from org.allbinary.logic.communication.smtp.event.handler.EmailEventHandlerUtil import EmailEventHandlerUtil
# from org.allbinary.logic.communication.smtp.event.handler.UserEmailEventHandler import UserEmailEventHandler
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _AdminUserEmailEventHandlerSingletons_instance() -> object:
    return AdminUserEmailEventHandlerSingletons()

lazy_static(AdminUserEmailEventHandlerSingletons, "instance", _AdminUserEmailEventHandlerSingletons_instance)

