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
# package org.allbinary.input.motion.gyro.action

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.input.motion.action.GameKeyCompleteMotionGestureInputEvent import GameKeyCompleteMotionGestureInputEvent


class UpOrientationInputToGameKeyEventAction(GameKeyCompleteMotionGestureInputEvent):
    instance: object = None
    

    @staticmethod
    def getInstance() -> GameKeyCompleteMotionGestureInputEvent:
        from org.allbinary.logic.NullUtil import NullUtil
        if UpOrientationInputToGameKeyEventAction.instance == NullUtil.getInstance().NULL_OBJECT:
            UpOrientationInputToGameKeyEventAction.instance = UpOrientationInputToGameKeyEventAction()
        return UpOrientationInputToGameKeyEventAction.instance
    

    def __init__(self) -> None:
        from org.allbinary.game.input.PlatformInputMappingFactory import PlatformInputMappingFactory
        from org.allbinary.input.gyro.OrientationMotionGestureFactory import OrientationMotionGestureFactory
        super().__init__("Up Action", OrientationMotionGestureFactory.getInstance().UP, PlatformInputMappingFactory.getInstance().getPersistentInputMappingInstance().getInputMapping())
# from org.allbinary.game.input.PlatformInputMappingFactory import PlatformInputMappingFactory
# from org.allbinary.input.gyro.OrientationMotionGestureFactory import OrientationMotionGestureFactory
# from org.allbinary.logic.NullUtil import NullUtil


def _UpOrientationInputToGameKeyEventAction_instance() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(UpOrientationInputToGameKeyEventAction, "instance", _UpOrientationInputToGameKeyEventAction_instance)

