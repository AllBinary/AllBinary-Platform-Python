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
# package org.allbinary.game.ai

from __future__ import annotations

from org.allbinary.ai.ArtificialIntelligence import ArtificialIntelligence
from org.allbinary.game.input.GameKeyEventSourceInterface import GameKeyEventSourceInterface
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory


class BasicAI(ArtificialIntelligence, GameKeyEventSourceInterface):
    AI_VISITOR: int = SmallIntegerSingletonFactory.getInstance().getAt(2)
    ID: int = SmallIntegerSingletonFactory.getInstance().getAt(1)

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.gameKeyEventFactory: GameKeyEventFactory = GameKeyEventFactory.getInstance()
        self.ownerLayerInterface: AllBinaryLayer = None
        self.gameInput: GameInput = None
        self.lastKey: int = -1
    

    def __init__(self, ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__()
        self._init_fields()
        self.ownerLayerInterface = ownerLayerInterface
        self.gameInput = gameInput
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    # throws Exception
    def processKeyAI(self, key: int) -> None:
        if key != -1:
            self.gameInput.add(self.gameKeyEventFactory.getInstanceForKey(self, key))
    

    def setLastKey(self, lastKey: int) -> None:
        self.lastKey = lastKey
    

    def getLastKey(self) -> int:
        return self.lastKey
    

    def getOwnerLayerInterface(self) -> AllBinaryLayer:
        return self.ownerLayerInterface
    

    def getGameInput(self) -> GameInput:
        return self.gameInput
    

    def getName(self) -> str:
        return type(self).__module__ + "." + type(self).__qualname__
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(CommonSeps.getInstance().NEW_LINE)
        stringBuffer.append(self.getName())
        stringBuffer.append(" LastKey: ")
        stringBuffer.append(CanvasUtil.getKeyName(self.getLastKey()))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def getSourceId(self) -> int:
        return 1
from org.allbinary.game.displayable.canvas.CanvasUtil import CanvasUtil
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings


