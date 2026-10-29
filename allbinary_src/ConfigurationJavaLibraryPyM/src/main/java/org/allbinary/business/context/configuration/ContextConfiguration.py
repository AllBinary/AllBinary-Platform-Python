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
# package org.allbinary.business.context.configuration

from __future__ import annotations

from org.allbinary.business.context.configuration.ContextConfigurationInterface import ContextConfigurationInterface


class ContextConfiguration(ContextConfigurationInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.emailServerConfigurationInterface: EmailServerConfigurationInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, "ContextConfiguration")
        self.setEmailServerConfigurationInterface(EmailServerConfiguration())
    

    def _constructor1(self, hashMap: dict) -> None:
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, "ContextConfiguration(HashMap)")
        self.setEmailServerConfigurationInterface(EmailServerConfiguration(hashMap))
    

    def getEmailServerConfigurationInterface(self) -> EmailServerConfigurationInterface:
        return self.emailServerConfigurationInterface
    

    def setEmailServerConfigurationInterface(self, emailServerConfigurationInterface: EmailServerConfigurationInterface) -> None:
        self.emailServerConfigurationInterface = emailServerConfigurationInterface
# from java.util.HashMap import HashMap
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfiguration import EmailServerConfiguration
from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationInterface import EmailServerConfigurationInterface
from org.allbinary.string.CommonStrings import CommonStrings


