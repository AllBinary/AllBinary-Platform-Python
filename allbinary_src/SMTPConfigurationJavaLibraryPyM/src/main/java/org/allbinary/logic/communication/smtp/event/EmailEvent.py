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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.util.EventObject import EventObject


@java_inherited_overloads
class EmailEvent(EventObject):
    def _java_defaults(self):
        vars(self).setdefault("emailInfo", None)
        vars(self).setdefault("userEmailEventNameData", None)
        vars(self).setdefault("attempts", 0)

    def _init_fields(self) -> None:
        if "emailInfo" not in vars(self): self.emailInfo: EmailInfo = None
        if "userEmailEventNameData" not in vars(self): self.userEmailEventNameData: UserEmailEventNameData = None
        if "attempts" not in vars(self): self.attempts: int = 0
    

    def __init__(self, emailEventHandler: object, userEmailEventNameData: UserEmailEventNameData, emailInfo: EmailInfo, attempts: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.communication.smtp.info.EmailInfo import EmailInfo
        super().__init__(emailEventHandler)
        __class__._init_fields(self)
        self.userEmailEventNameData = userEmailEventNameData
        self.emailInfo = emailInfo
    

    def getEmailInfo(self) -> EmailInfo:
        from org.allbinary.logic.communication.smtp.info.EmailInfo import EmailInfo
        return self.emailInfo
    

    def getAttempts(self) -> int:
        return self.attempts
    

    def setAttempts(self, attempts: int) -> None:
        self.attempts = attempts
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
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
# from org.allbinary.logic.communication.smtp.info.EmailInfo import EmailInfo
# from org.allbinary.logic.string.StringMaker import StringMaker


