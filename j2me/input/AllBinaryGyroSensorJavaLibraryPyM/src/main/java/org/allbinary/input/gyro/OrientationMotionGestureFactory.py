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
# package org.allbinary.input.gyro

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil


class OrientationMotionGestureFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.LEFT: MotionGestureInput = None
        self.RIGHT: MotionGestureInput = None
        self.UP: MotionGestureInput = None
        self.DOWN: MotionGestureInput = None
        self.ROLL_LEFT: MotionGestureInput = None
        self.ROLL_RIGHT: MotionGestureInput = None
    

    @staticmethod
    def getInstance() -> OrientationMotionGestureFactory:
        if OrientationMotionGestureFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            OrientationMotionGestureFactory.instance = OrientationMotionGestureFactory()
        return OrientationMotionGestureFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
        MAX: int = InputFactory.getInstance().MAX
        self.LEFT = MotionGestureInput(MAX - 20, "Left Orient")
        self.RIGHT = MotionGestureInput(MAX - 21, "Right Orient")
        self.UP = MotionGestureInput(MAX - 22, "Up Orient")
        self.DOWN = MotionGestureInput(MAX - 23, "Down Orient")
        self.ROLL_LEFT = MotionGestureInput(MAX - 24, "Roll Left")
        self.ROLL_RIGHT = MotionGestureInput(MAX - 25, "Roll Right")
from org.allbinary.game.input.InputFactory import InputFactory
from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput


