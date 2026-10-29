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
# package org.allbinary.input.motion.gesture.observer

from __future__ import annotations

from org.allbinary.input.motion.gesture.observer.CompleteMotionGestureListenerInterface import CompleteMotionGestureListenerInterface


class ResolveCompleteMotionGestureListener(CompleteMotionGestureListenerInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        self.logUtil.putF("MotionGesture to CompleteMotionGesture Reciever", self, commonStrings.CONSTRUCTOR)
        CompleteMotionGestureInputEventHandler.getInstance().addListener(GameKeyFromMotionGestureEventListener())
    

    # throws Exception
    def onMotionGestureCompleted(self, list_: BasicArrayList) -> None:
        configuration: MotionGestureConfiguration = MotionGestureConfigurationFactory.getInstance()
        commandActionsList: BasicArrayList = configuration.getAssociateCommandActionsList()
        size: int = commandActionsList.size()
        for index in range(size - 1, 0 - 1, -1):
            association: MotionGestureToMotionGestureActionAssociation = commandActionsList.objectArray[index]
            if association.isMotionGestureArrayEquals(list_) == True:
                completeMotionGestureInputEvent: GameKeyCompleteMotionGestureInputEvent = association.getCommandAction()
                CompleteMotionGestureInputEventHandler.getInstance().fireEvent(completeMotionGestureInputEvent)
                break
from org.allbinary.game.input.CompleteMotionGestureInputEventHandler import CompleteMotionGestureInputEventHandler
from org.allbinary.game.input.motion.action.GameKeyCompleteMotionGestureInputEvent import GameKeyCompleteMotionGestureInputEvent
from org.allbinary.game.input.motion.action.GameKeyFromMotionGestureEventListener import GameKeyFromMotionGestureEventListener
from org.allbinary.input.motion.gesture.MotionGestureToMotionGestureActionAssociation import MotionGestureToMotionGestureActionAssociation
from org.allbinary.input.motion.gesture.configuration.MotionGestureConfiguration import MotionGestureConfiguration
from org.allbinary.input.motion.gesture.configuration.MotionGestureConfigurationFactory import MotionGestureConfigurationFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList


