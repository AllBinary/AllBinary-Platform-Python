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
# package org.allbinary.input.motion.button

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.game.input.CompleteMotionGestureInputEventListenerInterface import CompleteMotionGestureInputEventListenerInterface
from org.allbinary.graphics.paint.ProcessPaintable import ProcessPaintable


@java_inherited_overloads
class TouchButtonsPaintableComposite(*java_bases(ProcessPaintable, CompleteMotionGestureInputEventListenerInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("inputMappingInterface", None)
        vars(self).setdefault("touchButtonsPaintable", None)
        vars(self).setdefault("timeHelper", None)
        vars(self).setdefault("released", False)
        vars(self).setdefault("METHOD_NAME", None)
        vars(self).setdefault("RELEASE", None)
        vars(self).setdefault("FAST_REPEAT", None)
        vars(self).setdefault("IGNORE", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "inputMappingInterface" not in vars(self): self.inputMappingInterface: InputMappingInterface = None
        if "touchButtonsPaintable" not in vars(self): self.touchButtonsPaintable: TouchButtonsMappingPaintable = None
        self.timeHelper: TimeDelayHelper = TimeDelayHelper(250)
        self.released: bool = True
        self.METHOD_NAME: str = "onCompleteMotionGestureInputEvent"
        self.RELEASE: str = "Ignoring: MotionGestureInput Release"
        self.FAST_REPEAT: str = "Ignoring: MotionGestureInput Repeated To Quickly"
        self.IGNORE: str = "Ignoring: Until Released"
    

    def __init__(self, inputMappingInterface: InputMappingInterface, basicColor: BasicColor) -> None:
        __class__._java_defaults(self)
        from org.allbinary.input.motion.button.TouchButtonsMappingPaintable import TouchButtonsMappingPaintable
        from org.allbinary.game.input.CompleteMotionGestureInputEventHandler import CompleteMotionGestureInputEventHandler
        from org.allbinary.game.input.mapping.InputMappingInterface import InputMappingInterface
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__()
        __class__._init_fields(self)
        self.inputMappingInterface = inputMappingInterface
        CompleteMotionGestureInputEventHandler.getInstance().addListenerInterface(self)
        self.touchButtonsPaintable = TouchButtonsMappingPaintable(basicColor)
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventStrings import EventStrings
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onCompleteMotionGestureInputEvent(self, completeMotionGestureInputEvent: CompleteMotionGestureInputEvent) -> None:
        from org.allbinary.game.input.CompleteMotionGestureInputEvent import CompleteMotionGestureInputEvent
        from org.allbinary.game.input.GameKey import GameKey
        from org.allbinary.game.input.motion.action.GameKeyCompleteMotionGestureInputEvent import GameKeyCompleteMotionGestureInputEvent
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        try:
            self.logUtil.putF(self.commonStrings.START, self, "onCompleteMotionGestureInputEvent")
            touchMotionGestureFactory: TouchMotionGestureFactory = TouchMotionGestureFactory.getInstance()
            gameKeyCompleteMotionGestureInputEvent: GameKeyCompleteMotionGestureInputEvent = completeMotionGestureInputEvent
            gameKey: GameKey = gameKeyCompleteMotionGestureInputEvent.getGameKey()
            motionGestureInput: MotionGestureInput = completeMotionGestureInputEvent.getMotionGestureInput()
            if motionGestureInput == touchMotionGestureFactory.RELEASED:
                self.logUtil.putF(self.RELEASE, self, self.METHOD_NAME)
                self.released = True
                return
            if motionGestureInput == TouchMotionGestureFactory.getInstance().NO_MOTION and not (java_predicate(self.timeHelper, "isTimeTNT")):
                self.logUtil.putF(self.FAST_REPEAT, self, self.METHOD_NAME)
                return
            if not (self.released):
                self.logUtil.putF(self.IGNORE, self, self.METHOD_NAME)
                return
            self.released = False
            self.logUtil.putF(str(StringMaker().append("GameKey: ").append(StringUtil.getInstance().toString(gameKey)).append(" MotionGestureInput: ").append(StringUtil.getInstance().toString(motionGestureInput))), self, self.METHOD_NAME)
            self.inputMappingInterface.processInputMapping(gameKey, motionGestureInput)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.METHOD_NAME, e)
    

    def process(self) -> None:
        from org.allbinary.game.input.CompleteMotionGestureInputEventHandler import CompleteMotionGestureInputEventHandler
        CompleteMotionGestureInputEventHandler.getInstance().removeListener(self)
# from org.allbinary.game.input.CompleteMotionGestureInputEvent import CompleteMotionGestureInputEvent
# from org.allbinary.game.input.CompleteMotionGestureInputEventHandler import CompleteMotionGestureInputEventHandler
# from org.allbinary.game.input.GameKey import GameKey
# from org.allbinary.game.input.mapping.InputMappingInterface import InputMappingInterface
# from org.allbinary.game.input.motion.action.GameKeyCompleteMotionGestureInputEvent import GameKeyCompleteMotionGestureInputEvent
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
# from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
# from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.logic.util.event.EventStrings import EventStrings
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


