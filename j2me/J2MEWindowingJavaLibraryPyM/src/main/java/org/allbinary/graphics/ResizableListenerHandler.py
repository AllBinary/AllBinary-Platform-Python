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
# package org.allbinary.graphics

from __future__ import annotations

import threading


class ResizableListenerHandler:
    instance: ResizableListenerHandler = None
    _lock = threading.RLock()
    

    @staticmethod
    def getInstance() -> ResizableListenerHandler:
        return ResizableListenerHandler.instance
    

    def setListener(self, resizableListenerInterface: ResizableListenerInterface) -> None:
        pass
    

    def fire(self, isFullScreen: bool) -> None:
        pass
    

    # throws Exception
    def fireEvent(self, value: bool) -> None:
        with self._lock:
            return self._fireEvent_unlocked(value)

    def _fireEvent_unlocked(self, value: bool) -> None:
        pass


ResizableListenerHandler.instance = ResizableListenerHandler()

