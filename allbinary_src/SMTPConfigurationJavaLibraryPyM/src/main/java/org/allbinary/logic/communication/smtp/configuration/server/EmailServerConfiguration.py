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
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "accountName" not in vars(self): self.accountName: str = None
        if "password" not in vars(self): self.password: str = None
        if "smtpServer" not in vars(self): self.smtpServer: str = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 3:
            __class__._constructor3(self, *args)
    

    def _constructor0(self) -> None:
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.START, self, commonStrings.CONSTRUCTOR)
        self.setSmtpServer(StringUtil.getInstance().EMPTY_STRING)
    

    def _constructor1(self, hashMap: HashMap) -> None:
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        from java.util.HashMap import HashMap
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.START, self, "EmailServerConfiguration(HashMap)")
        self.setAccountName(hashMap.get(EmailServerConfigurationData.ACCOUNT))
        self.setPassword(hashMap.get(EmailServerConfigurationData.PASSWORD))
        self.setSmtpServer(hashMap.get(EmailServerConfigurationData.SERVER))
        self.log()
    

    def _constructor3(self, account: str, password: str, server: str) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
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
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
            self.logUtil.putF(str(self), self, "EmailServerConfiguration")
    

    def toString(self) -> str:
        return "Email Server Configuration:\n" + "Smtp Server: \n" + str(self.getSmtpServer()) + "\nAccount Name: " + str(self.getAccountName()) + "\nPassword: " + str(self.getPassword())

    def __str__(self) -> str:
        return self.toString()
# from java.util.HashMap import HashMap
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


