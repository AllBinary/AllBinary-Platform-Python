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
# package org.allbinary.input.motion.touch.action

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.input.motion.action.GameKeyCompleteMotionGestureInputEvent import GameKeyCompleteMotionGestureInputEvent


class DiagonalUpLeftTouchInputToGameKeyEventAction(GameKeyCompleteMotionGestureInputEvent):
    instance: object = None
    

    @staticmethod
    def getInstance() -> GameKeyCompleteMotionGestureInputEvent:
        from org.allbinary.logic.NullUtil import NullUtil
        if DiagonalUpLeftTouchInputToGameKeyEventAction.instance == NullUtil.getInstance().NULL_OBJECT:
            DiagonalUpLeftTouchInputToGameKeyEventAction.instance = DiagonalUpLeftTouchInputToGameKeyEventAction()
        return DiagonalUpLeftTouchInputToGameKeyEventAction.instance
    

    def __init__(self) -> None:
        from org.allbinary.game.input.PlatformInputMappingFactory import PlatformInputMappingFactory
        from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
        super().__init__("Diagonal Up Left Action", TouchMotionGestureFactory.getInstance().DIAGONAL_UP_LEFT, PlatformInputMappingFactory.getInstance().getPersistentInputMappingInstance().getInputMapping())
# from org.allbinary.game.input.PlatformInputMappingFactory import PlatformInputMappingFactory
# from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
# from org.allbinary.logic.NullUtil import NullUtil


def _DiagonalUpLeftTouchInputToGameKeyEventAction_instance() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(DiagonalUpLeftTouchInputToGameKeyEventAction, "instance", _DiagonalUpLeftTouchInputToGameKeyEventAction_instance)

