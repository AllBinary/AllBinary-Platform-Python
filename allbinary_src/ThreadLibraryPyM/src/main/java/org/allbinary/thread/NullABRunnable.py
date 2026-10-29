# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
from org.allbinary.thread.ABRunnable import ABRunnable


class NullABRunnable(ABRunnable):
    instance: NullABRunnable = None
    _lock = threading.RLock()

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> NullABRunnable:
        return NullABRunnable.instance
    

    def isRunning(self) -> bool:
        with self._lock:
            return self._isRunning_unlocked()

    def _isRunning_unlocked(self) -> bool:
        return False


NullABRunnable.instance = NullABRunnable()

