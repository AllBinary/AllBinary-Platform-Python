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
# package org.allbinary.input.motion.gesture.observer

from __future__ import annotations

import threading


class MotionEventCircularPool:
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.MIN: int = TouchMotionGestureFactory.getInstance().LAST_MOTION.getId()
        self.eventPool: AllBinaryEventCircularPool = AllBinaryEventCircularPool((InputFactory.getInstance().MAX - 1) - self.MIN)
    

    @staticmethod
    def createPool(id: int) -> MotionEventCircularPool:
        return MotionEventCircularPool(id)
    

    def __init__(self, id: int) -> None:
        from org.allbinary.input.motion.gesture.observer.MotionEventFactory import MotionEventFactory
        self._init_fields()
        self.eventPool.initAllBinaryEventCircularPool(MotionEventFactory(self.eventPool, id))
    

    # throws Exception
    def getInstance(self, motionGestureInput: MotionGestureInput) -> MotionGestureEvent:
        with self._lock:
            return self._getInstance_unlocked(motionGestureInput)

    def _getInstance_unlocked(self, motionGestureInput: MotionGestureInput) -> MotionGestureEvent:
        return self.eventPool.getInstance(motionGestureInput.getId() - self.MIN)
from org.allbinary.game.input.InputFactory import InputFactory
from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
from org.allbinary.logic.util.event.AllBinaryEventCircularPool import AllBinaryEventCircularPool


