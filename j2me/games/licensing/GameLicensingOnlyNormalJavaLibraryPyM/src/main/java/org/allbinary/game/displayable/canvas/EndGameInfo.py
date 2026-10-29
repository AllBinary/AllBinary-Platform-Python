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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations



class EndGameInfo:

    def _init_fields(self) -> None:
        self.NORMAL_GAME_OVER: str = "Game Over"
        self.NORMAL_GAME_OVER_WIN: str = "You Won"
        self.gameOverStr: str = StringUtil.getInstance().EMPTY_STRING
        self.winStr: str = self.gameOverStr
    

    def __init__(self) -> None:
        self._init_fields()
    

    def update(self, gameInfo: GameInfo, myCanvas: MyCanvas) -> None:
        self.setGameOverStr(self.NORMAL_GAME_OVER)
        self.setWinStr(self.NORMAL_GAME_OVER_WIN)
    

    def getGameOverStr(self) -> str:
        return self.gameOverStr
    

    def setGameOverStr(self, gameOverStr: str) -> None:
        self.gameOverStr = gameOverStr
    

    def getWinStr(self) -> str:
        return self.winStr
    

    def setWinStr(self, winStr: str) -> None:
        self.winStr = winStr
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
from org.allbinary.logic.string.StringUtil import StringUtil


