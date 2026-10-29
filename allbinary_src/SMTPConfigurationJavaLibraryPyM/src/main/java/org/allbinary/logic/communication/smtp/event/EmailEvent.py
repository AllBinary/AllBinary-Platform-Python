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
# package org.allbinary.logic.communication.smtp.event

from __future__ import annotations

# from java.util.EventObject import EventObject


class EmailEvent(EventObject):

    def _init_fields(self) -> None:
        self.emailInfo: EmailInfo = None
        self.userEmailEventNameData: UserEmailEventNameData = None
        self.attempts: int = 0
    

    def __init__(self, emailEventHandler: object, userEmailEventNameData: UserEmailEventNameData, emailInfo: EmailInfo, attempts: int) -> None:
        super().__init__(emailEventHandler)
        self._init_fields()
        self.userEmailEventNameData = userEmailEventNameData
        self.emailInfo = emailInfo
    

    def getEmailInfo(self) -> EmailInfo:
        return self.emailInfo
    

    def getAttempts(self) -> int:
        return self.attempts
    

    def setAttempts(self, attempts: int) -> None:
        self.attempts = attempts
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("EmailEvent Log: \n")
        stringBuffer.append("Event Name: ")
        stringBuffer.append(str(self.userEmailEventNameData))
        stringBuffer.append(str(self.getEmailInfo()))
        stringBuffer.append("\nNumber of Attempts: ")
        stringBuffer.appendint(self.getAttempts())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.communication.smtp.info.EmailInfo import EmailInfo
from org.allbinary.logic.string.StringMaker import StringMaker


