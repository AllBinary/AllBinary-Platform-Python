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

from java.lang.JavaRuntimeStatic import lazy_static


class TrackballMotionGestureFactory:
    instance: object = None

    def _init_fields(self) -> None:
        if "LEFT" not in vars(self): self.LEFT: MotionGestureInput = None
        if "RIGHT" not in vars(self): self.RIGHT: MotionGestureInput = None
        if "UP" not in vars(self): self.UP: MotionGestureInput = None
        if "DOWN" not in vars(self): self.DOWN: MotionGestureInput = None
    

    @staticmethod
    def getInstance() -> TrackballMotionGestureFactory:
        from org.allbinary.logic.NullUtil import NullUtil
        if TrackballMotionGestureFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            TrackballMotionGestureFactory.instance = TrackballMotionGestureFactory()
        return TrackballMotionGestureFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
        from org.allbinary.game.input.InputFactory import InputFactory
        __class__._init_fields(self)
        MAX: int = InputFactory.getInstance().MAX
        self.LEFT = MotionGestureInput(MAX - 26, "L Trackball")
        self.RIGHT = MotionGestureInput(MAX - 27, "R Trackball")
        self.UP = MotionGestureInput(MAX - 28, "Up Trackball")
        self.DOWN = MotionGestureInput(MAX - 29, "D Trackball")
# from org.allbinary.game.input.InputFactory import InputFactory
# from org.allbinary.logic.NullUtil import NullUtil


def _TrackballMotionGestureFactory_instance() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(TrackballMotionGestureFactory, "instance", _TrackballMotionGestureFactory_instance)

