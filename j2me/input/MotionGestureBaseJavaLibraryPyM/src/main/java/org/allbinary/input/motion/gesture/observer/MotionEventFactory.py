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

from org.allbinary.logic.util.event.AllBinaryEventObjectFactoryInterface import AllBinaryEventObjectFactoryInterface


class MotionEventFactory(AllBinaryEventObjectFactoryInterface):
    index: int = 0

    def _init_fields(self) -> None:
        self.source: object = None
        self.id: int = None
    

    def __init__(self, source: object, id: int) -> None:
        self._init_fields()
        self.source = source
        self.id = id
        MotionEventFactory.index = TouchMotionGestureFactory.getInstance().LAST_MOTION.getId()
    

    def getInstance(self) -> AllBinaryEventObject:
        from org.allbinary.input.motion.gesture.observer.MotionGestureEvent import MotionGestureEvent
        from org.allbinary.input.motion.gesture.observer.MotionGestureEvent import MotionGestureEvent
        inputFactory: InputFactory = InputFactory.getInstance()
        input: Input = inputFactory.getInstanceById(((setattr(MotionEventFactory, "index", MotionEventFactory.index + 1) or MotionEventFactory.index) - 1))
        if input == inputFactory.NO_INPUT:
            return MotionGestureEvent(self.source, self.id, TouchMotionGestureFactory.getInstance().NO_MOTION)
        else:
            return MotionGestureEvent(self.source, self.id, input)
from org.allbinary.game.input.Input import Input
from org.allbinary.game.input.InputFactory import InputFactory
from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


