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
# package org.allbinary.android.input.motion.api1

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.android.input.motion.BaseGameInputMotionEventProcessor import BaseGameInputMotionEventProcessor


class GameInputMotionEventProcessorAPI1(BaseGameInputMotionEventProcessor):
    instance: object = None

    def _init_fields(self) -> None:
        from org.allbinary.input.motion.AllMotionRecognizer import AllMotionRecognizer
        from org.allbinary.input.motion.MotionRecognizer import MotionRecognizer
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.motionRecognizer: MotionRecognizer = AllMotionRecognizer()
    

    @staticmethod
    def getInstance() -> GameInputMotionEventProcessorAPI1:
        from org.allbinary.logic.NullUtil import NullUtil
        if GameInputMotionEventProcessorAPI1.instance == NullUtil.getInstance().NULL_OBJECT:
            GameInputMotionEventProcessorAPI1.instance = GameInputMotionEventProcessorAPI1()
        return GameInputMotionEventProcessorAPI1.instance
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def process(self, motionEvent: MotionEvent) -> None:
        from android.view.MotionEvent import MotionEvent
        try:
            x: int = int(motionEvent.getX())
            y: int = int(motionEvent.getY())
            action: int = motionEvent.getAction()
            if action == MotionEvent.ACTION_DOWN:
                self.motionRecognizer.processStartMotionEvent(x, y, motionEvent.getDeviceId(), 0)
            elif action == MotionEvent.ACTION_UP or action == MotionEvent.ACTION_CANCEL:
                self.motionRecognizer.processEndMotionEvent(x, y, motionEvent.getDeviceId(), 0)
            elif action == MotionEvent.ACTION_MOVE:
                self.motionRecognizer.processDraggedMotionEvent(x, y, motionEvent.getDeviceId(), 0)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.PROCESS, e)
# from android.view.MotionEvent import MotionEvent
# from org.allbinary.input.motion.AllMotionRecognizer import AllMotionRecognizer
# from org.allbinary.input.motion.MotionRecognizer import MotionRecognizer
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil


def _GameInputMotionEventProcessorAPI1_instance() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(GameInputMotionEventProcessorAPI1, "instance", _GameInputMotionEventProcessorAPI1_instance)

