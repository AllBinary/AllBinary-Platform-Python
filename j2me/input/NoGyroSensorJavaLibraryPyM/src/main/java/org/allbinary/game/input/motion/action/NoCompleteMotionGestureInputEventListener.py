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
# package org.allbinary.game.input.motion.action

from __future__ import annotations

from org.allbinary.game.input.CompleteMotionGestureInputEventListenerInterface import CompleteMotionGestureInputEventListenerInterface


class NoCompleteMotionGestureInputEventListener(CompleteMotionGestureInputEventListenerInterface):
    instance: NoCompleteMotionGestureInputEventListener = None
    

    def __init__(self) -> None:
        pass
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onCompleteMotionGestureInputEvent(self, completeMotionGestureInputEvent: CompleteMotionGestureInputEvent) -> None:
        pass
    

    @staticmethod
    def getInstance() -> NoCompleteMotionGestureInputEventListener:
        return NoCompleteMotionGestureInputEventListener.instance
from org.allbinary.game.input.CompleteMotionGestureInputEvent import CompleteMotionGestureInputEvent
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings


NoCompleteMotionGestureInputEventListener.instance = NoCompleteMotionGestureInputEventListener()

