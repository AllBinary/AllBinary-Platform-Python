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
# package org.allbinary.input.motion.gesture

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil


class TouchMotionGestureFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.LEFT: MotionGestureInput = None
        self.RIGHT: MotionGestureInput = None
        self.UP: MotionGestureInput = None
        self.DOWN: MotionGestureInput = None
        self.PRESSED: MotionGestureInput = None
        self.RELEASED: MotionGestureInput = None
        self.DIAGONAL_DOWN_RIGHT: MotionGestureInput = None
        self.DIAGONAL_DOWN_LEFT: MotionGestureInput = None
        self.DIAGONAL_UP_RIGHT: MotionGestureInput = None
        self.DIAGONAL_UP_LEFT: MotionGestureInput = None
        self.SCROLL_UP: MotionGestureInput = None
        self.SCROLL_DOWN: MotionGestureInput = None
        self.NO_MOTION: MotionGestureInput = None
        self.LAST_MOTION: MotionGestureInput = None
    

    @staticmethod
    def getInstance() -> TouchMotionGestureFactory:
        if TouchMotionGestureFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            TouchMotionGestureFactory.instance = TouchMotionGestureFactory()
        return TouchMotionGestureFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        self._init_fields()
        MAX: int = InputFactory.getInstance().MAX
        self.LEFT = MotionGestureInput(MAX - 3, "Left Touch")
        self.RIGHT = MotionGestureInput(MAX - 4, "Right Touch")
        self.UP = MotionGestureInput(MAX - 5, "Up Touch")
        self.DOWN = MotionGestureInput(MAX - 6, "Down Touch")
        self.PRESSED = MotionGestureInput(MAX - 7, "Screen Press")
        self.RELEASED = MotionGestureInput(MAX - 8, "Released")
        self.DIAGONAL_DOWN_RIGHT = MotionGestureInput(MAX - 9, "Diagonal Dn R")
        self.DIAGONAL_DOWN_LEFT = MotionGestureInput(MAX - 10, "Diagonal Dn L")
        self.DIAGONAL_UP_RIGHT = MotionGestureInput(MAX - 11, "Diagonal Up R")
        self.DIAGONAL_UP_LEFT = MotionGestureInput(MAX - 12, "Diagonal Up L")
        self.SCROLL_UP = MotionGestureInput(MAX - 13, "Scroll Up")
        self.SCROLL_DOWN = MotionGestureInput(MAX - 14, "Scroll Down")
        self.NO_MOTION = MotionGestureInput(MAX - 2, "No Motion")
        self.LAST_MOTION = MotionGestureInput(MAX - 19, "Last Motion")
from org.allbinary.game.input.InputFactory import InputFactory


