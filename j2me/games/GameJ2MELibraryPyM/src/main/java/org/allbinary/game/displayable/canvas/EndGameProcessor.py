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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.canvas.Processor import Processor


@java_inherited_overloads
class EndGameProcessor(Processor):
    def _java_defaults(self):
        vars(self).setdefault("gameStateFactory", None)
        vars(self).setdefault("gameCanvas", None)
        vars(self).setdefault("WAIT", 0)

    def _init_fields(self) -> None:
        from org.allbinary.game.state.GameStateFactory import GameStateFactory
        self.gameStateFactory: GameStateFactory = GameStateFactory.getInstance()
        if "gameCanvas" not in vars(self): self.gameCanvas: AllBinaryGameCanvas = None
        self.WAIT: int = 5000
    

    def __init__(self, gameCanvas: AllBinaryGameCanvas) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.gameCanvas = gameCanvas
    

    # throws Exception
    def process(self) -> None:
        from org.allbinary.game.score.HighScores import HighScores
        from org.allbinary.game.score.HighScoresHelperBase import HighScoresHelperBase
        from org.allbinary.game.score.NullHighScoresSingletonFactory import NullHighScoresSingletonFactory
        from org.allbinary.graphics.paint.NullPaintable import NullPaintable
        if java_predicate(self.gameCanvas, "isHighScoreSubmitted"):
            if self.gameCanvas.getGameStateTimeHelper().isElapsedTNT(self.WAIT):
                if self.gameCanvas.getGameState() == self.gameStateFactory.SHOW_END_RESULT_GAME_STATE:
                    highScoresBase: HighScoresHelperBase = self.gameCanvas.highScoresHelper
                    highScores: HighScores = highScoresBase.getSelectedHighScores()
                    if highScores != NullHighScoresSingletonFactory.getInstance():
                        highScoresBase.selectHighScores()
                        self.gameCanvas.getRealHighScoresPaintable().setHighScores(highScores)
                        self.gameCanvas.setGameState(self.gameStateFactory.SHOW_HIGH_SCORE_GAME_STATE)
                        self.gameCanvas.setHighScoresPaintable(self.gameCanvas.getRealHighScoresPaintable())
                elif self.gameCanvas.getGameState() == self.gameStateFactory.SHOW_HIGH_SCORE_GAME_STATE:
                    self.gameCanvas.setGameState(self.gameStateFactory.SHOW_END_RESULT_GAME_STATE)
                    self.gameCanvas.setHighScoresPaintable(NullPaintable.getInstance())
# from org.allbinary.game.score.HighScores import HighScores
# from org.allbinary.game.score.HighScoresHelperBase import HighScoresHelperBase
# from org.allbinary.game.score.NullHighScoresSingletonFactory import NullHighScoresSingletonFactory
# from org.allbinary.game.state.GameStateFactory import GameStateFactory
# from org.allbinary.graphics.paint.NullPaintable import NullPaintable


