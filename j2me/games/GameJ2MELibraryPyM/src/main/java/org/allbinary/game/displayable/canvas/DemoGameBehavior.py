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



class DemoGameBehavior:
    instance: DemoGameBehavior = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> DemoGameBehavior:
        return DemoGameBehavior.instance
    

    # throws Exception
    def init(self) -> None:
        pass
    

    def pause(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        pass
    

    def unPause(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        pass
    

    # throws Exception
    def updateTouch(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        pass
    

    # throws Exception
    def updateScreenButtonPaintable(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        allBinaryGameCanvas.setTouchPaintableP(NullPaintable.getInstance())
    

    # throws Exception
    def setGameState(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        pass
    

    def removeAllGameKeyInputListeners(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        pass
    

    # throws Exception
    def updateEndGameProcessor(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        pass
    

    # throws Exception
    def buildGame(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        pass
    

    # throws Exception
    def run(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        self.logUtil.putF(str(GameTypeFactory.getInstance().BOT), self, commonStrings.RUN)
    

    # throws Exception
    def setHighScore(self, abeClientInformation: AbeClientInformationInterface, allBinaryGameCanvas: AllBinaryGameCanvas, name: str, score: int, autoSubmit: bool, isLast: bool) -> None:
        pass
from org.allbinary.game.GameTypeFactory import GameTypeFactory
from org.allbinary.graphics.paint.NullPaintable import NullPaintable
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.string.CommonStrings import CommonStrings


DemoGameBehavior.instance = DemoGameBehavior()

