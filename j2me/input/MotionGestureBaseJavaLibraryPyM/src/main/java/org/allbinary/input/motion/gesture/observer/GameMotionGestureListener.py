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

from org.allbinary.input.motion.gesture.observer.MotionGestureEventListener import MotionGestureEventListener


class GameMotionGestureListener(MotionGestureEventListener):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.motionGestureCollection: BasicArrayList = BasicArrayListD()
        self.touchGestureCollection: BasicArrayList = BasicArrayListD()
        self.signed: CompleteMotionGestureListenerInterface = None
    

    def __init__(self, signed: CompleteMotionGestureListenerInterface) -> None:
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.signed = signed
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(self.commonStrings.NOT_IMPLEMENTED, self)
    

    def onUpMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        self.onMotionGestureEvent(ev)
    

    def onDownMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        self.onMotionGestureEvent(ev)
    

    def onLeftMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        self.onMotionGestureEvent(ev)
    

    def onRightMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        self.onMotionGestureEvent(ev)
    

    def onDiagonalDownRightMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        self.onMotionGestureEvent(ev)
    

    def onDiagonalDownLeftMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        self.onMotionGestureEvent(ev)
    

    def onDiagonalUpRightMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        self.onMotionGestureEvent(ev)
    

    def onDiagonalUpLeftMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        self.onMotionGestureEvent(ev)
    

    def onPressedMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        self.touchGestureCollection.add(ev.getMotionGesture())
    

    def released(self, ev: MotionGestureEvent) -> None:
        try:
            self.touchGestureCollection.add(ev.getMotionGesture())
            self.signed.onMotionGestureCompleted(self.touchGestureCollection)
            self.touchGestureCollection.clear()
        except Exception as e:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.commonStrings.EXCEPTION_LABEL)
            stringBuffer.append(StringUtil.getInstance().toString(ev.getMotionGesture()))
            self.logUtil.put(str(stringBuffer), self, "release", e)
    

    def onScrolledMotionGestureEvent(self, motionGestureEvent: MotionGestureEvent) -> None:
        pass
    

    def onMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        try:
            motionGestureInput: MotionGestureInput = ev.getMotionGesture()
            if motionGestureInput == TouchMotionGestureFactory.getInstance().PRESSED:
                self.onPressedMotionGestureEvent(ev)
            elif motionGestureInput == TouchMotionGestureFactory.getInstance().RELEASED:
                self.released(ev)
            else:
                self.motionGestureCollection.add(motionGestureInput)
                self.signed.onMotionGestureCompleted(self.motionGestureCollection)
                self.motionGestureCollection.clear()
                self.touchGestureCollection.clear()
        except Exception as e:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.commonStrings.EXCEPTION_LABEL)
            stringBuffer.append(StringUtil.getInstance().toString(ev.getMotionGesture()))
            self.logUtil.put(str(stringBuffer), self, "onMotionGestureEvent", e)
from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


