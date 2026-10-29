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
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.game.input.CompleteMotionGestureInputInterface import CompleteMotionGestureInputInterface


class CompleteMotionGestureInputEvent(AllBinaryEventObject, CompleteMotionGestureInputInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.name: str = StringUtil.getInstance().EMPTY_STRING
        self.motionGestureInput: MotionGestureInput = TouchMotionGestureFactory.getInstance().NO_MOTION
    

    def __init__(self, name: str, motionGestureInput: MotionGestureInput) -> None:
        super().__init__(motionGestureInput)
        self._init_fields()
        self.setName(name)
        try:
            self.setMotionGestureInput(motionGestureInput)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, "InputToGameKeyEventAction", e)
    

    def setName(self, name: str) -> None:
        self.name = name
    

    def getName(self) -> str:
        return self.name
    

    def setMotionGestureInput(self, motionGestureInput: MotionGestureInput) -> None:
        self.motionGestureInput = motionGestureInput
    

    def getMotionGestureInput(self) -> MotionGestureInput:
        return self.motionGestureInput
from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


