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

import threading


class UserEmailEventHandler:
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        if "emailVector" not in vars(self): self.emailVector: BasicArrayList = None
        if "emailInfo" not in vars(self): self.emailInfo: EmailInfo = None
        if "userEmailEventNameData" not in vars(self): self.userEmailEventNameData: UserEmailEventNameData = None
    

    def __init__(self) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        __class__._init_fields(self)
        self.emailVector = BasicArrayListD()
    

    # throws Exception
    def receiveEmailInfo(self, userEmailEventNameData: UserEmailEventNameData, emailInfo: EmailInfo) -> None:
        with self._lock:
            return __class__.__dict__["_receiveEmailInfo_unlocked"].__get__(self, __class__)(userEmailEventNameData, emailInfo)

    def _receiveEmailInfo_unlocked(self, userEmailEventNameData: UserEmailEventNameData, emailInfo: EmailInfo) -> None:
        from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
        from org.allbinary.logic.communication.smtp.info.EmailInfo import EmailInfo
        self.userEmailEventNameData = userEmailEventNameData
        self.emailInfo = emailInfo
        self.fireEmailEvent()
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def addListener_j1_1(self, vector: BasicArrayList) -> None:
        with self._lock:
            return __class__.__dict__["_addListener_j1_1_unlocked"].__get__(self, __class__)(vector)

    def _addListener_j1_1_unlocked(self, vector: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.communication.smtp.event.UserEmailEventListenerInterface import UserEmailEventListenerInterface
        size: int = vector.size()
        for index in range(0, size):
            userEmailEventListenerInterface: UserEmailEventListenerInterface = vector.get(index)
            self.addListener(userEmailEventListenerInterface)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def addListener_j1_2(self, emailEventListenerInterface: UserEmailEventListenerInterface) -> None:
        with self._lock:
            return __class__.__dict__["_addListener_j1_2_unlocked"].__get__(self, __class__)(emailEventListenerInterface)

    def _addListener_j1_2_unlocked(self, emailEventListenerInterface: UserEmailEventListenerInterface) -> None:
        from org.allbinary.logic.communication.smtp.event.UserEmailEventListenerInterface import UserEmailEventListenerInterface
        self.emailVector.add(emailEventListenerInterface)

    def addListener(self, *args):
        if len(args) == 1 and True and (args[0] is None or any(base.__name__ == "BasicArrayList" for base in type(args[0]).__mro__)):
            return __class__.__dict__["addListener_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["addListener_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("addListener_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().addListener(*args)
    

    def removeListener(self, emailEventListenerInterface: UserEmailEventListenerInterface) -> None:
        with self._lock:
            return __class__.__dict__["_removeListener_unlocked"].__get__(self, __class__)(emailEventListenerInterface)

    def _removeListener_unlocked(self, emailEventListenerInterface: UserEmailEventListenerInterface) -> None:
        from org.allbinary.logic.communication.smtp.event.UserEmailEventListenerInterface import UserEmailEventListenerInterface
        self.emailVector.remove(emailEventListenerInterface)
    

    # throws Exception
    def fireEmailEvent(self) -> None:
        with self._lock:
            return __class__.__dict__["_fireEmailEvent_unlocked"].__get__(self, __class__)()

    def _fireEmailEvent_unlocked(self) -> None:
        from org.allbinary.logic.communication.smtp.event.EmailEvent import EmailEvent
        from org.allbinary.logic.communication.smtp.event.UserEmailEventListenerInterface import UserEmailEventListenerInterface
        emailEvent: EmailEvent = EmailEvent(self, self.userEmailEventNameData, self.emailInfo, 0)
        size: int = self.emailVector.size()
        for index in range(0, size):
            emailEventListenerInterface: UserEmailEventListenerInterface = self.emailVector.get(index)
            emailEventListenerInterface.onEmailSendRequest(emailEvent)
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.smtp.event.EmailEvent import EmailEvent
# from org.allbinary.logic.communication.smtp.event.UserEmailEventListenerInterface import UserEmailEventListenerInterface
# from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
# from org.allbinary.logic.communication.smtp.info.EmailInfo import EmailInfo


