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

from org.allbinary.game.input.motion.action.GameKeyCompleteMotionGestureInputEvent import GameKeyCompleteMotionGestureInputEvent
from org.allbinary.logic.NullUtil import NullUtil


class DownOrientationInputToGameKeyEventAction(GameKeyCompleteMotionGestureInputEvent):
    instance: object = NullUtil.getInstance().NULL_OBJECT
    

    @staticmethod
    def getInstance() -> GameKeyCompleteMotionGestureInputEvent:
        if DownOrientationInputToGameKeyEventAction.instance == NullUtil.getInstance().NULL_OBJECT:
            DownOrientationInputToGameKeyEventAction.instance = DownOrientationInputToGameKeyEventAction()
        return DownOrientationInputToGameKeyEventAction.instance
    

    def __init__(self) -> None:
        super().__init__("Down Action", OrientationMotionGestureFactory.getInstance().DOWN, PlatformInputMappingFactory.getInstance().getPersistentInputMappingInstance().getInputMapping())
from org.allbinary.game.input.PlatformInputMappingFactory import PlatformInputMappingFactory
from org.allbinary.input.gyro.OrientationMotionGestureFactory import OrientationMotionGestureFactory


