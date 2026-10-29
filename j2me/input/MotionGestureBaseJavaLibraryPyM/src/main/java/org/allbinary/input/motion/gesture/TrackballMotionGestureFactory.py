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


class TrackballMotionGestureFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.LEFT: MotionGestureInput = None
        self.RIGHT: MotionGestureInput = None
        self.UP: MotionGestureInput = None
        self.DOWN: MotionGestureInput = None
    

    @staticmethod
    def getInstance() -> TrackballMotionGestureFactory:
        if TrackballMotionGestureFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            TrackballMotionGestureFactory.instance = TrackballMotionGestureFactory()
        return TrackballMotionGestureFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        self._init_fields()
        MAX: int = InputFactory.getInstance().MAX
        self.LEFT = MotionGestureInput(MAX - 26, "L Trackball")
        self.RIGHT = MotionGestureInput(MAX - 27, "R Trackball")
        self.UP = MotionGestureInput(MAX - 28, "Up Trackball")
        self.DOWN = MotionGestureInput(MAX - 29, "D Trackball")
from org.allbinary.game.input.InputFactory import InputFactory


