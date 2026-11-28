#
# AllBinary Open License Version 1
# Copyright (c) 2009 AllBinary
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
# package org.allbinary.android.input.motion

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.android.input.motion.MotionEventProcessor import MotionEventProcessor


@java_inherited_overloads
class BaseGameInputMotionEventProcessor(MotionEventProcessor):
    def _java_defaults(self):
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("gameMotionGestureListener", None)

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "gameMotionGestureListener" not in vars(self): self.gameMotionGestureListener: GameMotionGestureListener = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.input.motion.gesture.observer.GameMotionGestureListener import GameMotionGestureListener
        from org.allbinary.input.motion.gesture.observer.MotionGestureReceiveInterfaceFactory import MotionGestureReceiveInterfaceFactory
        super().__init__()
        __class__._init_fields(self)
        self.gameMotionGestureListener = GameMotionGestureListener(MotionGestureReceiveInterfaceFactory.getInstance())
        self.addListener()
    

    def process(self, motionEvent: MotionEvent) -> None:
        from android.view.MotionEvent import MotionEvent
        pass
    

    def addListener(self) -> None:
        from org.allbinary.input.motion.gesture.observer.BasicMotionGesturesHandler import BasicMotionGesturesHandler
        motionGesturesHandler: BasicMotionGesturesHandler = BasicMotionGesturesHandler.getInstance()
        motionGesturesHandler.addListenerInterface(self.gameMotionGestureListener)
# from android.view.MotionEvent import MotionEvent
# from org.allbinary.input.motion.gesture.observer.BasicMotionGesturesHandler import BasicMotionGesturesHandler
# from org.allbinary.input.motion.gesture.observer.GameMotionGestureListener import GameMotionGestureListener
# from org.allbinary.input.motion.gesture.observer.MotionGestureReceiveInterfaceFactory import MotionGestureReceiveInterfaceFactory
# from org.allbinary.string.CommonStrings import CommonStrings


