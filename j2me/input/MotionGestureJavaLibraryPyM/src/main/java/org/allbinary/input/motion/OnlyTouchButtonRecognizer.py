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

from org.allbinary.input.motion.MotionRecognizer import MotionRecognizer


class OnlyTouchButtonRecognizer(MotionRecognizer):

    def _init_fields(self) -> None:
        self.touchButtonRecognizer: TouchButtonRecognizer = None
        self.touchButtonProcessing: bool = False
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.touchButtonRecognizer = TouchButtonRecognizer()
    

    # throws Exception
    def processStartMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        if self.touchButtonRecognizer.pressTouchButtonInput(x, y, deviceId):
            self.touchButtonProcessing = True
    

    # throws Exception
    def processEndMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        if self.touchButtonProcessing:
            self.touchButtonProcessing = False
        if self.touchButtonRecognizer.releaseTouchButtonInput(x, y, deviceId):
            return
    

    # throws Exception
    def processDraggedMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        if self.touchButtonProcessing:
            self.touchButtonRecognizer.pressTouchButtonInput(x, y, deviceId)
from org.allbinary.input.motion.button.TouchButtonRecognizer import TouchButtonRecognizer


