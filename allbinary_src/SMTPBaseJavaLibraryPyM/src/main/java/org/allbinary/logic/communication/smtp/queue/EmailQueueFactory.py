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

from java.lang.JavaRuntimeStatic import lazy_static


class EmailQueueFactory:
    emailQueueInterface: EmailQueueInterface = None
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance() -> EmailQueueInterface:
        return EmailQueueFactory.emailQueueInterface


def _EmailQueueFactory_emailQueueInterface() -> object:
    from org.allbinary.logic.communication.smtp.queue.BasicEmailQueue import BasicEmailQueue
    return BasicEmailQueue.getInstance()

lazy_static(EmailQueueFactory, "emailQueueInterface", _EmailQueueFactory_emailQueueInterface)

