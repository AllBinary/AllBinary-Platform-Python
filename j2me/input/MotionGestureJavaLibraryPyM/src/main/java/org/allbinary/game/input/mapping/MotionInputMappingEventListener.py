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
# package org.allbinary.game.input.mapping

from __future__ import annotations

from org.allbinary.game.input.mapping.event.InputMappingEventListenerInterface import InputMappingEventListenerInterface


class MotionInputMappingEventListener(InputMappingEventListenerInterface):
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    # throws Exception
    def onInputMappingEvent(self, inputMappingEvent: InputMappingEvent) -> None:
        GameKeyCompleteMotionGestureInputEventFactory.getInstance().updateAll()
        BasicTouchInputFactory.getInstance().updateAll(inputMappingEvent.getInputToGameKeyMapping())
from org.allbinary.game.input.mapping.event.InputMappingEvent import InputMappingEvent
from org.allbinary.game.input.motion.action.GameKeyCompleteMotionGestureInputEventFactory import GameKeyCompleteMotionGestureInputEventFactory
from org.allbinary.input.motion.button.BasicTouchInputFactory import BasicTouchInputFactory
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings


