# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

from org.allbinary.game.displayable.canvas.DemoGameBehavior import DemoGameBehavior


class BaseGameBehavior(DemoGameBehavior):
    instanceC: BaseGameBehavior = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> DemoGameBehavior:
        return BaseGameBehavior.instanceC
    

    # throws Exception
    def init(self) -> None:
        gameAdState: GameAdState = GameAdStateFactory.getInstance().getCurrentInstance()
        gameAdState.playingAdState()
    

    def pause(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        features: Features = Features.getInstance()
        if features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL_AS_GAME_THREAD):
            currentDisplayableFactory: CurrentDisplayableFactory = CurrentDisplayableFactory.getInstance()
            currentDisplayableFactory.setRunnable(allBinaryGameCanvas.gamePauseRunnable)
    

    def unPause(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        if Features.getInstance().isDefault(OpenGLFeatureFactory.getInstance().OPENGL_AS_GAME_THREAD):
            currentDisplayableFactory: CurrentDisplayableFactory = CurrentDisplayableFactory.getInstance()
            currentDisplayableFactory.setRunnable(allBinaryGameCanvas.gameRunnable)
            currentDisplayableFactory.setDisplayable(allBinaryGameCanvas)
    

    # throws Exception
    def updateTouch(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        allBinaryGameCanvas.updateTouch2()
    

    # throws Exception
    def updateScreenButtonPaintable(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        allBinaryGameCanvas.updateScreenButtonPaintable2()
    

    # throws Exception
    def setGameState(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        allBinaryGameCanvas.updateGameState()
    

    def removeAllGameKeyInputListeners(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        allBinaryGameCanvas.removeAllGameKeyInputListeners2()
    

    # throws Exception
    def updateEndGameProcessor(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        allBinaryGameCanvas.updateEndGameProcessor2()
    

    # throws Exception
    def buildGame(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        allBinaryGameCanvas.buildGame2()
    

    # throws Exception
    def run(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        allBinaryGameCanvas.run2()
    

    # throws Exception
    def setHighScore(self, abeClientInformation: AbeClientInformationInterface, allBinaryGameCanvas: AllBinaryGameCanvas, name: str, score: int, autoSubmit: bool, isLast: bool) -> None:
        allBinaryGameCanvas.setHighScore2(abeClientInformation, name, score, autoSubmit, isLast)
from org.allbinary.business.advertisement.GameAdStateFactory import GameAdStateFactory
from org.allbinary.game.GameAdState import GameAdState
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.graphics.opengles.CurrentDisplayableFactory import CurrentDisplayableFactory
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface


BaseGameBehavior.instanceC = BaseGameBehavior()

