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
# package org.allbinary.game.ag.ai.tactical

from __future__ import annotations

from org.allbinary.game.ai.BasicAI import BasicAI


class BasicRandomAI(BasicAI):

    def _init_fields(self) -> None:
        self.i_random: int = 0
        self.inputProbability: InputProbability = None
        self.visitor: Visitor = None
        self.keyArray: list[int] = [Canvas.UP, Canvas.DOWN, Canvas.LEFT, Canvas.RIGHT, Canvas.KEY_NUM1, Canvas.KEY_NUM7, Canvas.KEY_NUM9]
        self.myRandomFactory: MyRandomFactory = MyRandomFactory.getInstance()
    

    def __init__(self, ownerLayerInterface: AllBinaryLayer, gameInput: GameInput, inputProbability: InputProbability, visitor: Visitor) -> None:
        super().__init__(ownerLayerInterface, gameInput)
        self._init_fields()
        self.inputProbability = inputProbability
        self.visitor = visitor
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        if self.inputProbability.getTimeDelayHelper().isTime(GameTickTimeDelayHelperFactory.getInstance().startTime):
            self.i_random = self.myRandomFactory.getAbsoluteNextInt(self.inputProbability.getMax())
            repeat: bool = False
            repeatLikelyhoodIntegerArray: list[int] = self.inputProbability.getRepeatLikelyhoodIntegerArray()
            if self.getLastKey() != -1 and int(repeatLikelyhoodIntegerArray[self.getLastKey()]) >= self.i_random:
                repeat = True
            if not repeat:
                likelyhoodIntegerArray: list[list[int]] = self.inputProbability.getLikelyhoodIntegerArray()
                self.i_random = self.myRandomFactory.getAbsoluteNextInt(self.inputProbability.getMax())
                size: int = len(self.keyArray)
                likelyhoodIntegerKeyArray: list[int] = None
                for index in range(0, size):
                    key: int = self.keyArray[index]
                    likelyhoodIntegerKeyArray = likelyhoodIntegerArray[key]
                    if len(likelyhoodIntegerArray) >= key and likelyhoodIntegerKeyArray[0] is not None:
                        if self.i_random >= int(likelyhoodIntegerKeyArray[0]) and self.i_random < int(likelyhoodIntegerKeyArray[1]):
                            self.setLastKey(key)
                            break
            self.visitor.visit(self)
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.game.ag.ai.InputProbability import InputProbability
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.game.rand.MyRandomFactory import MyRandomFactory
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.util.visitor.Visitor import Visitor
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory


