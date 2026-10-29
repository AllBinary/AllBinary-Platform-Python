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
# package org.allbinary.input.motion

from __future__ import annotations



class CompleteMotionGestureInputToGameMotionGestureInput:
    instance: CompleteMotionGestureInputToGameMotionGestureInput = None

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CompleteMotionGestureInputToGameMotionGestureInput:
        return CompleteMotionGestureInputToGameMotionGestureInput.instance
    

    def init(self) -> None:
        PreLogUtil.put("No Touch Button = No Compound Motion Gestures", self, self.commonStrings.INIT)
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.string.CommonStrings import CommonStrings


CompleteMotionGestureInputToGameMotionGestureInput.instance = CompleteMotionGestureInputToGameMotionGestureInput()

