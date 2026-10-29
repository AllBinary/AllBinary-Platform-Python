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
# package org.allbinary.animation

from __future__ import annotations

import threading
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


class AnimationEventHandler(BasicEventHandler):
    eventHandler: AnimationEventHandler = None
    _lock = threading.RLock()
    

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> AnimationEventHandler:
        with AnimationEventHandler._lock:
            return AnimationEventHandler._getInstance_unlocked()

    @staticmethod
    def _getInstance_unlocked() -> AnimationEventHandler:
        return AnimationEventHandler.eventHandler


AnimationEventHandler.eventHandler = AnimationEventHandler()

