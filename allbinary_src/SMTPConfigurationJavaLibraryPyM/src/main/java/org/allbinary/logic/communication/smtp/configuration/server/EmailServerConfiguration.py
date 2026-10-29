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
# package org.allbinary.logic.communication.smtp.configuration.server

from __future__ import annotations

from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationInterface import EmailServerConfigurationInterface


class EmailServerConfiguration(EmailServerConfigurationInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.accountName: str = None
        self.password: str = None
        self.smtpServer: str = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 3:
            self._constructor3(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.START, self, commonStrings.CONSTRUCTOR)
        self.setSmtpServer(StringUtil.getInstance().EMPTY_STRING)
    

    def _constructor1(self, hashMap: dict) -> None:
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.START, self, "EmailServerConfiguration(HashMap)")
        self.setAccountName(hashMap.get(EmailServerConfigurationData.ACCOUNT))
        self.setPassword(hashMap.get(EmailServerConfigurationData.PASSWORD))
        self.setSmtpServer(hashMap.get(EmailServerConfigurationData.SERVER))
        self.log()
    

    def _constructor3(self, account: str, password: str, server: str) -> None:
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.START, self, "EmailServerConfiguration(HashMap)")
        self.setAccountName(account)
        self.setPassword(password)
        self.setSmtpServer(server)
        self.log()
    

    def setSmtpServer(self, value: str) -> None:
        self.smtpServer = value
    

    def getSmtpServer(self) -> str:
        return self.smtpServer
    

    def getAccountName(self) -> str:
        return self.accountName
    

    def setAccountName(self, accountName: str) -> None:
        self.accountName = accountName
    

    def getPassword(self) -> str:
        return self.password
    

    def setPassword(self, password: str) -> None:
        self.password = password
    

    def log(self) -> None:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            self.logUtil.putF(str(self), self, "EmailServerConfiguration")
    

    def toString(self) -> str:
        return "Email Server Configuration:\n" + "Smtp Server: \n" + str(self.getSmtpServer()) + "\nAccount Name: " + str(self.getAccountName()) + "\nPassword: " + str(self.getPassword())

    def __str__(self) -> str:
        return self.toString()
# from java.util.HashMap import HashMap
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


