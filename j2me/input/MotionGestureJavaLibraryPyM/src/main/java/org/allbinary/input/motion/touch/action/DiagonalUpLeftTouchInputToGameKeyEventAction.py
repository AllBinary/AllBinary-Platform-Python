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

from org.allbinary.game.input.motion.action.GameKeyCompleteMotionGestureInputEvent import GameKeyCompleteMotionGestureInputEvent
from org.allbinary.logic.NullUtil import NullUtil


class DiagonalUpLeftTouchInputToGameKeyEventAction(GameKeyCompleteMotionGestureInputEvent):
    instance: object = NullUtil.getInstance().NULL_OBJECT
    

    @staticmethod
    def getInstance() -> GameKeyCompleteMotionGestureInputEvent:
        if DiagonalUpLeftTouchInputToGameKeyEventAction.instance == NullUtil.getInstance().NULL_OBJECT:
            DiagonalUpLeftTouchInputToGameKeyEventAction.instance = DiagonalUpLeftTouchInputToGameKeyEventAction()
        return DiagonalUpLeftTouchInputToGameKeyEventAction.instance
    

    def __init__(self) -> None:
        super().__init__("Diagonal Up Left Action", TouchMotionGestureFactory.getInstance().DIAGONAL_UP_LEFT, PlatformInputMappingFactory.getInstance().getPersistentInputMappingInstance().getInputMapping())
from org.allbinary.game.input.PlatformInputMappingFactory import PlatformInputMappingFactory
from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory


