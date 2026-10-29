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
# package org.allbinary.input.media.image.capture

from __future__ import annotations

import threading


class ProcessingFrameIndexFactory:
    currentFrame: int = 0
    _lock = threading.RLock()
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def next() -> int:
        with ProcessingFrameIndexFactory._lock:
            return ProcessingFrameIndexFactory._next_unlocked()

    @staticmethod
    def _next_unlocked() -> int:
        return ((setattr(ProcessingFrameIndexFactory, "currentFrame", ProcessingFrameIndexFactory.currentFrame + 1) or ProcessingFrameIndexFactory.currentFrame) - 1)


