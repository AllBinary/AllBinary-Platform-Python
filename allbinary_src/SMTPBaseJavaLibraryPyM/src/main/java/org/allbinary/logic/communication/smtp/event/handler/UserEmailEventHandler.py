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
        self.emailVector: BasicArrayList = None
        self.emailInfo: EmailInfo = None
        self.userEmailEventNameData: UserEmailEventNameData = None
    

    def __init__(self) -> None:
        self._init_fields()
        self.emailVector = BasicArrayListD()
    

    # throws Exception
    def receiveEmailInfo(self, userEmailEventNameData: UserEmailEventNameData, emailInfo: EmailInfo) -> None:
        with self._lock:
            return self._receiveEmailInfo_unlocked(userEmailEventNameData, emailInfo)

    def _receiveEmailInfo_unlocked(self, userEmailEventNameData: UserEmailEventNameData, emailInfo: EmailInfo) -> None:
        self.userEmailEventNameData = userEmailEventNameData
        self.emailInfo = emailInfo
        self.fireEmailEvent()
    

    def addListener(self, vector: BasicArrayList) -> None:
        with self._lock:
            return self._addListener_unlocked(vector)

    def _addListener_unlocked(self, vector: BasicArrayList) -> None:
        size: int = vector.size()
        for index in range(0, size):
            userEmailEventListenerInterface: UserEmailEventListenerInterface = vector.get(index)
            self.addListener(userEmailEventListenerInterface)
    

    # Java overloaded method: Python keeps the last definition
    def addListener(self, emailEventListenerInterface: UserEmailEventListenerInterface) -> None:
        with self._lock:
            return self._addListener_unlocked(emailEventListenerInterface)

    def _addListener_unlocked(self, emailEventListenerInterface: UserEmailEventListenerInterface) -> None:
        self.emailVector.add(emailEventListenerInterface)
    

    def removeListener(self, emailEventListenerInterface: UserEmailEventListenerInterface) -> None:
        with self._lock:
            return self._removeListener_unlocked(emailEventListenerInterface)

    def _removeListener_unlocked(self, emailEventListenerInterface: UserEmailEventListenerInterface) -> None:
        self.emailVector.remove(emailEventListenerInterface)
    

    # throws Exception
    def fireEmailEvent(self) -> None:
        with self._lock:
            return self._fireEmailEvent_unlocked()

    def _fireEmailEvent_unlocked(self) -> None:
        emailEvent: EmailEvent = EmailEvent(self, self.userEmailEventNameData, self.emailInfo, 0)
        size: int = self.emailVector.size()
        for index in range(0, size):
            emailEventListenerInterface: UserEmailEventListenerInterface = self.emailVector.get(index)
            emailEventListenerInterface.onEmailSendRequest(emailEvent)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.smtp.event.EmailEvent import EmailEvent
from org.allbinary.logic.communication.smtp.event.UserEmailEventListenerInterface import UserEmailEventListenerInterface
from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
from org.allbinary.logic.communication.smtp.info.EmailInfo import EmailInfo


