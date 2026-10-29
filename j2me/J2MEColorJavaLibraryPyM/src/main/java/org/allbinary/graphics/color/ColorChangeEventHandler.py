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
# package org.allbinary.graphics.color

from __future__ import annotations

import threading
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


class ColorChangeEventHandler(BasicEventHandler):
    eventHandler: ColorChangeEventHandler = None
    _lock = threading.RLock()
    

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> ColorChangeEventHandler:
        with ColorChangeEventHandler._lock:
            return ColorChangeEventHandler._getInstance_unlocked()

    @staticmethod
    def _getInstance_unlocked() -> ColorChangeEventHandler:
        return ColorChangeEventHandler.eventHandler


ColorChangeEventHandler.eventHandler = ColorChangeEventHandler()

