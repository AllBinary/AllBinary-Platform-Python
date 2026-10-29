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
# package org.allbinary.game.input.motion.action

from __future__ import annotations



class GameKeyCompleteMotionGestureInputEventFactory:
    SINGLETON: GameKeyCompleteMotionGestureInputEventFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.eventList: BasicArrayList = BasicArrayListD()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GameKeyCompleteMotionGestureInputEventFactory:
        return GameKeyCompleteMotionGestureInputEventFactory.SINGLETON
    

    def add(self, gameKeyCompleteMotionGestureInputEvent: GameKeyCompleteMotionGestureInputEvent) -> None:
        self.eventList.add(gameKeyCompleteMotionGestureInputEvent)
    

    def updateAll(self) -> None:
        self.logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().START_LABEL).appendint(self.eventList.size())), self, "updateAll")
        for index in range(self.eventList.size() - 1, 0 - 1, -1):
            gameKeyCompleteMotionGestureInputEvent: GameKeyCompleteMotionGestureInputEvent = self.eventList.objectArray[index]
            gameKeyCompleteMotionGestureInputEvent.update()
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


GameKeyCompleteMotionGestureInputEventFactory.SINGLETON = GameKeyCompleteMotionGestureInputEventFactory()

