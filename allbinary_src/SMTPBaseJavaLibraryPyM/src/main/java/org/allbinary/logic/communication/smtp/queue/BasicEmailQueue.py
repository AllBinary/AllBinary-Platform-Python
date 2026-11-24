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
# package org.allbinary.logic.communication.smtp.queue

from __future__ import annotations

import threading
from java.lang.JavaRuntimeStatic import lazy_static
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.util.queue.BasicQueue import BasicQueue
from org.allbinary.logic.communication.smtp.queue.EmailQueueInterface import EmailQueueInterface


class BasicEmailQueue(*java_bases(BasicQueue, EmailQueueInterface)):
    instance: BasicEmailQueue = None
    basicEmailQueue: BasicEmailQueue = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BasicEmailQueue:
        with BasicEmailQueue._lock:
            return BasicEmailQueue._getInstance_unlocked()

    @staticmethod
    def _getInstance_unlocked() -> BasicEmailQueue:
        if BasicEmailQueue.basicEmailQueue is None:
            BasicEmailQueue.basicEmailQueue = BasicEmailQueue()
        return BasicEmailQueue.basicEmailQueue
    

    # throws Exception
    def offer(self, emailInterface: EmailInterface) -> bool:
        with self._lock:
            return self._offer_unlocked(emailInterface)

    def _offer_unlocked(self, emailInterface: EmailInterface) -> bool:
        from org.allbinary.logic.communication.smtp.EmailInterface import EmailInterface
        self.offer(emailInterface)
        self.post(emailInterface)
        return True
    

    def remove_j1(self, emailInterface: EmailInterface) -> None:
        with self._lock:
            return self._remove_j1_unlocked(emailInterface)

    def _remove_j1_unlocked(self, emailInterface: EmailInterface) -> None:
        from org.allbinary.logic.communication.smtp.EmailInterface import EmailInterface
        self.remove(emailInterface)
    

    def remove_j0(self) -> EmailInterface:
        with self._lock:
            return self._remove_j0_unlocked()

    def _remove_j0_unlocked(self) -> EmailInterface:
        from org.allbinary.logic.communication.smtp.EmailInterface import EmailInterface
        return None

    def remove(self, *args):
        return getattr(self, "remove_j" + str(len(args)))(*args)
    

    # throws Exception
    def post(self, emailInterface: EmailInterface) -> None:
        with self._lock:
            return self._post_unlocked(emailInterface)

    def _post_unlocked(self, emailInterface: EmailInterface) -> None:
        from org.allbinary.logic.communication.smtp.EmailInterface import EmailInterface
        if self.send(emailInterface):
            self.remove(emailInterface)
            self.processAllUnsent()
    

    # throws Exception
    def processAllUnsent(self) -> None:
        with self._lock:
            return self._processAllUnsent_unlocked()

    def _processAllUnsent_unlocked(self) -> None:
        from org.allbinary.logic.communication.smtp.EmailInterface import EmailInterface
        size: int = self.queueVector.size()
        for index in range(0, size):
            emailInterface: EmailInterface = self.queueVector.get(index)
            if self.send(emailInterface):
                self.remove(emailInterface)
                self.processAllUnsent()
    

    def send(self, emailInterface: EmailInterface) -> bool:
        with self._lock:
            return self._send_unlocked(emailInterface)

    def _send_unlocked(self, emailInterface: EmailInterface) -> bool:
        from org.allbinary.logic.communication.smtp.EmailInterface import EmailInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
                self.logUtil.putF("Sending: " + str(emailInterface.log()), self, "send")
            Transport.send(emailInterface.getMimeMessage())
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
                self.logUtil.putF("Email Send Debug: " + str(emailInterface.getDebugInfo()), self, "send")
            return True
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
                self.logUtil.put("Failed Email Send Debug: " + str(emailInterface.getDebugInfo()), self, "send", e)
            return False
# from javax.mail.Transport import Transport
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.smtp.EmailInterface import EmailInterface
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _BasicEmailQueue_instance() -> object:
    return BasicEmailQueue()

lazy_static(BasicEmailQueue, "instance", _BasicEmailQueue_instance)

