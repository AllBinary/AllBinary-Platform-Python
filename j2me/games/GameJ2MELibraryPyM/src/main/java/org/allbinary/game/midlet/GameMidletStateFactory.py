# Generated Code Do Not Modify
# package org.allbinary.game.midlet

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class GameMidletStateFactory:
    INSTANCE: GameMidletStateFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.game.state.GameState import GameState
        from org.allbinary.game.state.GameStateFactory import GameStateFactory
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.currentGameState: GameState = GameStateFactory.getInstance().NO_GAME_STATE
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GameMidletStateFactory:
        return GameMidletStateFactory.INSTANCE
    

    def getCurrentGameState(self) -> GameState:
        from org.allbinary.game.state.GameState import GameState
        return self.currentGameState
    

    def setCurrentGameState(self, currentGameState: GameState) -> None:
        from org.allbinary.game.state.GameState import GameState
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.string.CommonLabels import CommonLabels
        self.logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().CURRENT).append(" GameState: ").append(StringUtil.getInstance().toString(currentGameState))), self, "setCurrentGameState")
        self.currentGameState = currentGameState
# from org.allbinary.game.state.GameState import GameState
# from org.allbinary.game.state.GameStateFactory import GameStateFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonLabels import CommonLabels


def _GameMidletStateFactory_INSTANCE() -> object:
    return GameMidletStateFactory()

lazy_static(GameMidletStateFactory, "INSTANCE", _GameMidletStateFactory_INSTANCE)

