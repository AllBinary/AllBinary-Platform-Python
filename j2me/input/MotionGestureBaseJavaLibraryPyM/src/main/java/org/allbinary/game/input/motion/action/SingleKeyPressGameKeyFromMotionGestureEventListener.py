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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.input.CompleteMotionGestureInputEventListener import CompleteMotionGestureInputEventListener


@java_inherited_overloads
class SingleKeyPressGameKeyFromMotionGestureEventListener(CompleteMotionGestureInputEventListener):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventStrings import EventStrings
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onCompleteMotionGestureInputEvent(self, completeMotionGestureInputEvent: CompleteMotionGestureInputEvent) -> None:
        from org.allbinary.game.input.CompleteMotionGestureInputEvent import CompleteMotionGestureInputEvent
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        from org.allbinary.game.input.event.PressGameKeyEventHandler import PressGameKeyEventHandler
        from org.allbinary.string.CommonStrings import CommonStrings
        try:
            gameKeyCompleteMotionGestureInputEvent: GameKeyCompleteMotionGestureInputEvent = completeMotionGestureInputEvent
            gameKeyEvent: GameKeyEvent = gameKeyCompleteMotionGestureInputEvent.getGameKeyEvent()
            PressGameKeyEventHandler.getInstance().fireEvent(gameKeyEvent)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, "onCompleteMotionGestureInputEvent", e)
# from org.allbinary.game.input.CompleteMotionGestureInputEvent import CompleteMotionGestureInputEvent
# from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
# from org.allbinary.game.input.event.PressGameKeyEventHandler import PressGameKeyEventHandler
# from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.logic.util.event.EventStrings import EventStrings
# from org.allbinary.string.CommonStrings import CommonStrings


