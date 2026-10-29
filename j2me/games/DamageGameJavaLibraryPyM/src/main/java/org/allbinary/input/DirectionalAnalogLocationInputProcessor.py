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
# package org.allbinary.input

from __future__ import annotations

from org.allbinary.android.input.motion.AnalogLocationInputProcessor import AnalogLocationInputProcessor
from org.allbinary.game.input.GameKeyEventSourceInterface import GameKeyEventSourceInterface


class DirectionalAnalogLocationInputProcessor(AnalogLocationInputProcessor, GameKeyEventSourceInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.inputProcessorArray: list[GameInputProcessor] = None
        self.gameKeyFactory: GameKeyFactory = GameKeyFactory.getInstance()
        self.leftGameKeyEvent: GameKeyEvent = GameKeyEvent.NONE
        self.rightGameKeyEvent: GameKeyEvent = GameKeyEvent.NONE
        self.upGameKeyEvent: GameKeyEvent = GameKeyEvent.NONE
        self.downGameKeyEvent: GameKeyEvent = GameKeyEvent.NONE
        self.leftTriggerGameKeyEvent: GameKeyEvent = GameKeyEvent.NONE
        self.rightTriggerGameKeyEvent: GameKeyEvent = GameKeyEvent.NONE
    

    def __init__(self, inputProcessorArray: list[GameInputProcessor]) -> None:
        super().__init__()
        self._init_fields()
        self.inputProcessorArray = inputProcessorArray
        try:
            self.leftGameKeyEvent = GameKeyEventFactory.getInstance().getInstanceForInput(self, self.gameKeyFactory.LEFT)
            self.rightGameKeyEvent = GameKeyEventFactory.getInstance().getInstanceForInput(self, self.gameKeyFactory.RIGHT)
            self.upGameKeyEvent = GameKeyEventFactory.getInstance().getInstanceForInput(self, self.gameKeyFactory.UP)
            self.downGameKeyEvent = GameKeyEventFactory.getInstance().getInstanceForInput(self, self.gameKeyFactory.DOWN)
            self.leftTriggerGameKeyEvent = GameKeyEventFactory.getInstance().getInstanceForInput(self, self.gameKeyFactory.KEY_NUM0)
            self.rightTriggerGameKeyEvent = GameKeyEventFactory.getInstance().getInstanceForInput(self, self.gameKeyFactory.KEY_NUM5)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.CONSTRUCTOR, e)
    

    def process(self, allbinaryLayerManager: AllBinaryLayerManager, analogLocationInput: AnalogLocationInput) -> None:
        try:
            customGPoint: CustomGPoint = None
            customGPoint = analogLocationInput.getCustomGPoint()
            x: int = customGPoint.getX()
            y: int = customGPoint.getY()
            leftTrigger: int = analogLocationInput.getLeftTrigger()
            rightTrigger: int = analogLocationInput.getRightTrigger()
            if x < 0:
                self.inputProcessorArray[self.leftGameKeyEvent.getKey()].processAnalog(allbinaryLayerManager, self.leftGameKeyEvent, x)
            elif x > 0:
                self.inputProcessorArray[self.rightGameKeyEvent.getKey()].processAnalog(allbinaryLayerManager, self.rightGameKeyEvent, x)
            if y < 0:
                self.inputProcessorArray[self.downGameKeyEvent.getKey()].processAnalog(allbinaryLayerManager, self.downGameKeyEvent, y)
            elif y > 0:
                self.inputProcessorArray[self.upGameKeyEvent.getKey()].processAnalog(allbinaryLayerManager, self.upGameKeyEvent, y)
            if leftTrigger > 0:
                self.inputProcessorArray[self.leftTriggerGameKeyEvent.getKey()].processAnalog(allbinaryLayerManager, self.leftTriggerGameKeyEvent, leftTrigger)
            if rightTrigger > 0:
                self.inputProcessorArray[self.rightTriggerGameKeyEvent.getKey()].processAnalog(allbinaryLayerManager, self.rightTriggerGameKeyEvent, rightTrigger)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put("Unable to process analog input", self, commonStrings.PROCESS, e)
    

    def getSourceId(self) -> int:
        return 0
from org.allbinary.game.input.GameInputProcessor import GameInputProcessor
from org.allbinary.game.input.GameKeyFactory import GameKeyFactory
from org.allbinary.game.input.analog.AnalogLocationInput import AnalogLocationInput
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
from org.allbinary.graphics.CustomGPoint import CustomGPoint
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


