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

from org.allbinary.android.input.motion.MotionEventProcessor import MotionEventProcessor


class BaseGameInputMotionEventProcessor(MotionEventProcessor):

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.gameMotionGestureListener: GameMotionGestureListener = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.gameMotionGestureListener = GameMotionGestureListener(MotionGestureReceiveInterfaceFactory.getInstance())
        self.addListener()
    

    def process(self, motionEvent: MotionEvent) -> None:
        pass
    

    def addListener(self) -> None:
        motionGesturesHandler: BasicMotionGesturesHandler = BasicMotionGesturesHandler.getInstance()
        motionGesturesHandler.addListenerInterface(self.gameMotionGestureListener)
from android.view.MotionEvent import MotionEvent
from org.allbinary.input.motion.gesture.observer.BasicMotionGesturesHandler import BasicMotionGesturesHandler
from org.allbinary.input.motion.gesture.observer.GameMotionGestureListener import GameMotionGestureListener
from org.allbinary.input.motion.gesture.observer.MotionGestureReceiveInterfaceFactory import MotionGestureReceiveInterfaceFactory
from org.allbinary.string.CommonStrings import CommonStrings


