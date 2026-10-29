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

from org.allbinary.game.input.CompleteMotionGestureInputEventListener import CompleteMotionGestureInputEventListener


class SingleKeyPressGameKeyFromMotionGestureEventListener(CompleteMotionGestureInputEventListener):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onCompleteMotionGestureInputEvent(self, completeMotionGestureInputEvent: CompleteMotionGestureInputEvent) -> None:
        try:
            gameKeyCompleteMotionGestureInputEvent: GameKeyCompleteMotionGestureInputEvent = completeMotionGestureInputEvent
            gameKeyEvent: GameKeyEvent = gameKeyCompleteMotionGestureInputEvent.getGameKeyEvent()
            PressGameKeyEventHandler.getInstance().fireEvent(gameKeyEvent)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, "onCompleteMotionGestureInputEvent", e)
from org.allbinary.game.input.CompleteMotionGestureInputEvent import CompleteMotionGestureInputEvent
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.game.input.event.PressGameKeyEventHandler import PressGameKeyEventHandler
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.string.CommonStrings import CommonStrings


