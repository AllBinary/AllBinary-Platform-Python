#
# AllBinary Open License Version 1
# Copyright (c) 2009 AllBinary
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
# package org.allbinary.android.input.motion

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.android.input.motion.MotionEventProcessor import MotionEventProcessor


class NoMotionEventProcessor(MotionEventProcessor):
    SINGLETON: MotionEventProcessor = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> MotionEventProcessor:
        return NoMotionEventProcessor.SINGLETON


def _NoMotionEventProcessor_SINGLETON() -> object:
    from org.allbinary.android.input.motion.MotionEventProcessor import MotionEventProcessor
    return MotionEventProcessor()

lazy_static(NoMotionEventProcessor, "SINGLETON", _NoMotionEventProcessor_SINGLETON)

