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

from org.allbinary.android.input.motion.MotionEventProcessor import MotionEventProcessor


class TrackballGameInputMotionEventProcessor(MotionEventProcessor):
    PROCESSOR: TrackballGameInputMotionEventProcessor = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.listener: SingleKeyPressGameKeyFromMotionGestureEventListener = SingleKeyPressGameKeyFromMotionGestureEventListener()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    @staticmethod
    def getInstance() -> TrackballGameInputMotionEventProcessor:
        return TrackballGameInputMotionEventProcessor.PROCESSOR
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def process(self, motionEvent: MotionEvent) -> None:
        try:
            x: float = motionEvent.getX()
            y: float = motionEvent.getY()
            if x < 0.0:
                self.listener.onCompleteMotionGestureInputEvent(LeftTrackballInputToGameKeyEventAction.getInstance())
            elif x > 0.0:
                self.listener.onCompleteMotionGestureInputEvent(RightTrackballInputToGameKeyEventAction.getInstance())
            if y < 0.0:
                self.listener.onCompleteMotionGestureInputEvent(UpTrackballInputToGameKeyEventAction.getInstance())
            elif y > 0.0:
                self.listener.onCompleteMotionGestureInputEvent(DownTrackballInputToGameKeyEventAction.getInstance())
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.PROCESS, e)
from android.view.MotionEvent import MotionEvent
from org.allbinary.game.input.motion.action.SingleKeyPressGameKeyFromMotionGestureEventListener import SingleKeyPressGameKeyFromMotionGestureEventListener
from org.allbinary.input.motion.trackball.action.DownTrackballInputToGameKeyEventAction import DownTrackballInputToGameKeyEventAction
from org.allbinary.input.motion.trackball.action.LeftTrackballInputToGameKeyEventAction import LeftTrackballInputToGameKeyEventAction
from org.allbinary.input.motion.trackball.action.RightTrackballInputToGameKeyEventAction import RightTrackballInputToGameKeyEventAction
from org.allbinary.input.motion.trackball.action.UpTrackballInputToGameKeyEventAction import UpTrackballInputToGameKeyEventAction
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


TrackballGameInputMotionEventProcessor.PROCESSOR = TrackballGameInputMotionEventProcessor()

