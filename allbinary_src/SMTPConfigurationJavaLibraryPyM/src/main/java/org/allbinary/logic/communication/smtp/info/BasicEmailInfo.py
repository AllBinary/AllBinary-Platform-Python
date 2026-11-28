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
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "subject" not in vars(self): self.subject: str = None
        if "textBody" not in vars(self): self.textBody: str = None
        if "emailServerConfigurationInterface" not in vars(self): self.emailServerConfigurationInterface: EmailServerConfigurationInterface = None
    

    def __init__(self, subject: str, textBody: str) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.START, self, commonStrings.CONSTRUCTOR)
        self.subject = subject
        self.textBody = textBody
    

    def getSubject(self) -> str:
        return self.subject
    

    def getTextBody(self) -> str:
        return self.textBody
    

    def getEmailServerConfigurationInterface(self) -> EmailServerConfigurationInterface:
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationInterface import EmailServerConfigurationInterface
        return self.emailServerConfigurationInterface
    

    def setEmailServerConfigurationInterface(self, emailServerConfigurationInterface: EmailServerConfigurationInterface) -> None:
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationInterface import EmailServerConfigurationInterface
        self.emailServerConfigurationInterface = emailServerConfigurationInterface
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
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
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationInterface import EmailServerConfigurationInterface
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


