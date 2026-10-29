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
# package org.allbinary.game.combat.canvas

from __future__ import annotations

from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas
from org.allbinary.layer.BasicLayerProcessor import BasicLayerProcessor


class CombatGameCanvas(AllBinaryGameCanvas):
    basicLayerProcessor: list[BasicLayerProcessor] = [None] * (0)
    

    def __init__(self, cmdListener: CommandListener, gameLayerManager: AllBinaryGameLayerManager, highScoresFactoryInterface: HighScoresFactoryInterface, gameInitializationInterfaceFactoryInterface: BasicBuildGameInitializerFactory, buffered: bool) -> None:
        super().__init__(cmdListener, gameLayerManager, highScoresFactoryInterface, gameInitializationInterfaceFactoryInterface, buffered)
    

    def CombatGameCanvas_init(self) -> None:
        DestroyEventCircularStaticPool.getInstance().init(self)
        ProgressCanvasFactory.getInstance().addNormalPortion(50, "Destroy Events")
    

    # throws Exception
    def initApp(self, abeClientInformation: AbeClientInformationInterface) -> None:
        self.CombatGameCanvas_init()
        super().initApp(abeClientInformation)
    

    def initConfigurablePortion(self, portion: int) -> None:
        DestroyedLayerProcessor.init()
        ProgressCanvasFactory.getInstance().addNormalPortion(portion, "Basic Processors")
        features: Features = Features.getInstance()
        gameFeatureFactory: GameFeatureFactory = GameFeatureFactory.getInstance()
        if features.isFeature(gameFeatureFactory.DROPPED_ITEMS) and features.isFeature(gameFeatureFactory.DROPPED_ITEMS_FROM_DEATH):
            CombatGameCanvas.basicLayerProcessor = [None] * (2)
            CombatGameCanvas.basicLayerProcessor[0] = DestroyedLayerProcessor.getInstance()
            CombatGameCanvas.basicLayerProcessor[1] = DropLayerProcessor.getInstance()
        else:
            CombatGameCanvas.basicLayerProcessor = [None] * (1)
            CombatGameCanvas.basicLayerProcessor[0] = DestroyedLayerProcessor.getInstance()
    

    # throws Exception
    def processPlayingGame(self) -> None:
        super().processPlayingGame()
        index = len(CombatGameCanvas.basicLayerProcessor)
        while (index := index - 1) >= 0:
            CombatGameCanvas.basicLayerProcessor[index].process(self.gameLayerManager)
    

    # throws Exception
    def cleanupGame(self) -> None:
        super().cleanupGame()
        index = len(CombatGameCanvas.basicLayerProcessor)
        while (index := index - 1) >= 0:
            CombatGameCanvas.basicLayerProcessor[index].getList().clear()
        GroupLayerManagerListener.getInstance().clear()
        GroupLayerManagerListener.getInstance().log()
        DestroyedEventHandler.getInstance().removeAllListeners()
        self.cleanupManager()
    

    # throws Exception
    def cleanupManager(self) -> None:
        self.gameLayerManager.cleanup()
# from javax.microedition.lcdui.CommandListener import CommandListener
from org.allbinary.game.combat.destroy.DestroyedLayerProcessor import DestroyedLayerProcessor
from org.allbinary.game.combat.destroy.event.DestroyEventCircularStaticPool import DestroyEventCircularStaticPool
from org.allbinary.game.combat.destroy.event.DestroyedEventHandler import DestroyedEventHandler
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.GameFeatureFactory import GameFeatureFactory
from org.allbinary.game.init.BasicBuildGameInitializerFactory import BasicBuildGameInitializerFactory
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.drop.DropLayerProcessor import DropLayerProcessor
from org.allbinary.game.layer.identification.GroupLayerManagerListener import GroupLayerManagerListener
from org.allbinary.game.score.HighScoresFactoryInterface import HighScoresFactoryInterface
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface


