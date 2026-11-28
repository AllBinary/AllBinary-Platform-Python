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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.input.motion.MotionRecognizer import MotionRecognizer


@java_inherited_overloads
class OnlyTouchButtonRecognizer(MotionRecognizer):
    def _java_defaults(self):
        vars(self).setdefault("touchButtonRecognizer", None)
        vars(self).setdefault("touchButtonProcessing", False)

    def _init_fields(self) -> None:
        if "touchButtonRecognizer" not in vars(self): self.touchButtonRecognizer: TouchButtonRecognizer = None
        self.touchButtonProcessing: bool = False
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.input.motion.button.TouchButtonRecognizer import TouchButtonRecognizer
        super().__init__()
        __class__._init_fields(self)
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
# from org.allbinary.input.motion.button.TouchButtonRecognizer import TouchButtonRecognizer


