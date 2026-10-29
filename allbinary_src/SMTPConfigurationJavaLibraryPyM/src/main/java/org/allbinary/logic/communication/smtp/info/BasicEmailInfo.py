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
# package org.allbinary.logic.communication.smtp.info

from __future__ import annotations



class BasicEmailInfo:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.subject: str = None
        self.textBody: str = None
        self.emailServerConfigurationInterface: EmailServerConfigurationInterface = None
    

    def __init__(self, subject: str, textBody: str) -> None:
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.START, self, commonStrings.CONSTRUCTOR)
        self.subject = subject
        self.textBody = textBody
    

    def getSubject(self) -> str:
        return self.subject
    

    def getTextBody(self) -> str:
        return self.textBody
    

    def getEmailServerConfigurationInterface(self) -> EmailServerConfigurationInterface:
        return self.emailServerConfigurationInterface
    

    def setEmailServerConfigurationInterface(self, emailServerConfigurationInterface: EmailServerConfigurationInterface) -> None:
        self.emailServerConfigurationInterface = emailServerConfigurationInterface
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(str(self.getEmailServerConfigurationInterface()))
        stringBuffer.append(CommonSeps.getInstance().NEW_LINE)
        stringBuffer.append("Subject: \n")
        stringBuffer.append(self.getSubject())
        stringBuffer.append("\nText Body: \n")
        stringBuffer.append(self.getTextBody())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    # throws Exception
    def init(self) -> None:
        raise RuntimeError()
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationInterface import EmailServerConfigurationInterface
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings


