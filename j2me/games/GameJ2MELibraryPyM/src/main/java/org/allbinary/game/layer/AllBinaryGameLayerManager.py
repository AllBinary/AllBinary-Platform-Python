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
# package org.allbinary.game.layer

from __future__ import annotations

from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory


class AllBinaryGameLayerManager(AllBinaryLayerManager):
    NULL_ALLBINARY_LAYER_MANAGER: object = NullUtil.getInstance().NULL_OBJECT
    ID: int = SmallIntegerSingletonFactory.getInstance().getAt(22)

    def _init_fields(self) -> None:
        self.backgroundBasicColor: BasicColor = None
        self.foregroundBasicColor: BasicColor = None
        self.gameInfo: GameInfo = None
        self.playerGameInputCompositeInterface: PlayerGameInputCompositeInterface = NullPlayerGameInputComposite.NULL_PLAYER_GAME_INPUT_COMPOSITE
    

    @staticmethod
    def getNullInstance() -> AllBinaryGameLayerManager:
        if AllBinaryGameLayerManager.NULL_ALLBINARY_LAYER_MANAGER == NullUtil.getInstance().NULL_OBJECT:
            AllBinaryGameLayerManager.NULL_ALLBINARY_LAYER_MANAGER = AllBinaryGameLayerManager(BasicColorFactory.getInstance().BLACK, BasicColorFactory.getInstance().WHITE, GameInfo.NONE)
        return AllBinaryGameLayerManager.NULL_ALLBINARY_LAYER_MANAGER
    

    def __init__(self, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor, gameInfo: GameInfo) -> None:
        super().__init__()
        self._init_fields()
        self.backgroundBasicColor = backgroundBasicColor
        self.foregroundBasicColor = foregroundBasicColor
        itemColorFactory: ItemColorFactory = ItemColorFactory.getInstance()
        itemColorFactory.INVERT_PAINT = int(self.backgroundBasicColor)
        itemColorFactory.PAINT = int(self.foregroundBasicColor)
        self.gameInfo = gameInfo
    

    def getLayerManager(self) -> AllBinaryLayerManager:
        return self
    

    def init(self) -> None:
        pass
    

    def getBackgroundBasicColor(self) -> BasicColor:
        return self.backgroundBasicColor
    

    def setBackgroundBasicColor(self, backgroundBasicColor: BasicColor) -> None:
        self.backgroundBasicColor = backgroundBasicColor
        ItemColorFactory.getInstance().INVERT_PAINT = int(self.backgroundBasicColor)
    

    def getForegroundBasicColor(self) -> BasicColor:
        return self.foregroundBasicColor
    

    def setForegroundBasicColor(self, foregroundBasicColor: BasicColor) -> None:
        self.foregroundBasicColor = foregroundBasicColor
        ItemColorFactory.getInstance().PAINT = int(self.foregroundBasicColor)
    

    def getGameInfo(self) -> GameInfo:
        return self.gameInfo
    

    def setGameInfo(self, gameInfo: GameInfo) -> None:
        self.gameInfo = gameInfo
    

    def setLayerProcessorList(self, list_: BasicArrayList) -> None:
        layerProcessorInterfaceArray: list[LayerProcessor] = [None] * (list_.size())
        size: int = len(layerProcessorInterfaceArray)
        for index in range(0, size):
            layerProcessorInterfaceArray[index] = list_.objectArray[index]
        self.setLayerProcessorArray(layerProcessorInterfaceArray)
    

    def setPlayerGameInputCompositeInterface(self, playerGameInputCompositeInterface: PlayerGameInputCompositeInterface) -> None:
        self.playerGameInputCompositeInterface = playerGameInputCompositeInterface
    

    def getPlayerGameInputCompositeInterface(self) -> PlayerGameInputCompositeInterface:
        return self.playerGameInputCompositeInterface
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.game.input.NullPlayerGameInputComposite import NullPlayerGameInputComposite
from org.allbinary.game.input.PlayerGameInputCompositeInterface import PlayerGameInputCompositeInterface
from org.allbinary.graphics.ItemColorFactory import ItemColorFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.layer.LayerProcessor import LayerProcessor
from org.allbinary.util.BasicArrayList import BasicArrayList


