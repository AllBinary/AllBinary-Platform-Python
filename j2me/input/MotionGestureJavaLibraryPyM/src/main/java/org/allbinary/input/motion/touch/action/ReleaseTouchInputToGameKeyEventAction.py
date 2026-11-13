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


class ReleaseTouchInputToGameKeyEventAction(GameKeyCompleteMotionGestureInputEvent):
    instance: object = None

    def _init_fields(self) -> None:
        from org.allbinary.game.input.GameKey import GameKey
        from org.allbinary.game.input.GameKeyFactory import GameKeyFactory
        self.NONE: GameKey = GameKeyFactory.getInstance().NONE
    

    @staticmethod
    def getInstance() -> GameKeyCompleteMotionGestureInputEvent:
        from org.allbinary.logic.NullUtil import NullUtil
        if ReleaseTouchInputToGameKeyEventAction.instance == NullUtil.getInstance().NULL_OBJECT:
            ReleaseTouchInputToGameKeyEventAction.instance = ReleaseTouchInputToGameKeyEventAction()
        return ReleaseTouchInputToGameKeyEventAction.instance
    

    def __init__(self) -> None:
        from org.allbinary.game.input.PlatformInputMappingFactory import PlatformInputMappingFactory
        from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
        from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
        from org.allbinary.string.CommonStrings import CommonStrings
        super().__init__("Release Action", TouchMotionGestureFactory.getInstance().RELEASED, PlatformInputMappingFactory.getInstance().getPersistentInputMappingInstance().getInputMapping())
        self._init_fields()
        try:
            self.setGameKey(self.NONE)
            self.setGameKeyEvent(GameKeyEventFactory.getInstance().getInstanceForInput(self, self.NONE))
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.CONSTRUCTOR, e)
    

    def update(self) -> None:
        pass
# from org.allbinary.game.input.GameKey import GameKey
# from org.allbinary.game.input.GameKeyFactory import GameKeyFactory
# from org.allbinary.game.input.PlatformInputMappingFactory import PlatformInputMappingFactory
# from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
# from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.string.CommonStrings import CommonStrings


def _ReleaseTouchInputToGameKeyEventAction_instance() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(ReleaseTouchInputToGameKeyEventAction, "instance", _ReleaseTouchInputToGameKeyEventAction_instance)

