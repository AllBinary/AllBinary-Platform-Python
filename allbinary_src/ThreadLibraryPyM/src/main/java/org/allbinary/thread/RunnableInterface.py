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
# package org.allbinary.thread

from __future__ import annotations

import threading


# Java interface
class RunnableInterface(object):
    

    def isRunning(self) -> bool:
        raise NotImplementedError()
    

    def setRunning(self, isRunning: bool) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def setThread(self, thread: threading.Thread) -> None:
        raise NotImplementedError()


