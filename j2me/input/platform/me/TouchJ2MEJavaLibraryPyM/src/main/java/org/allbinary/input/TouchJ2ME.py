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
# package org.allbinary.input

from __future__ import annotations



#TouchJ2ME
class TouchJ2ME:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.DEVICE_ID: int = 0
        self.motionRecognizer: AllMotionRecognizer = AllMotionRecognizer()
    

    def __init__(self) -> None:
        self._init_fields()
        motionGesturesHandler: BasicMotionGesturesHandler = self.motionRecognizer.getMotionGestureRecognizer().getMotionGesturesHandler()
        motionGesturesHandler.addListenerInterface(GameMotionGestureListener(MotionGestureReceiveInterfaceFactory.getInstance()))
    

    def pointerDragged(self, x: int, y: int) -> None:
        try:
            self.motionRecognizer.processDraggedMotionEvent(x, y, self.DEVICE_ID, 0)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, "pointerDragged", e)
    

    def pointerPressed(self, x: int, y: int) -> None:
        try:
            self.motionRecognizer.processStartMotionEvent(x, y, self.DEVICE_ID, 0)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, "pointerPressed", e)
    

    def pointerReleased(self, x: int, y: int) -> None:
        try:
            self.motionRecognizer.processEndMotionEvent(x, y, self.DEVICE_ID, 0)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, "pointerReleased", e)
from org.allbinary.input.motion.AllMotionRecognizer import AllMotionRecognizer
from org.allbinary.input.motion.gesture.observer.BasicMotionGesturesHandler import BasicMotionGesturesHandler
from org.allbinary.input.motion.gesture.observer.GameMotionGestureListener import GameMotionGestureListener
from org.allbinary.input.motion.gesture.observer.MotionGestureReceiveInterfaceFactory import MotionGestureReceiveInterfaceFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


