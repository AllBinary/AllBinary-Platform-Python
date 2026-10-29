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
# package org.allbinary.game

from __future__ import annotations



class GameStrings:
    instance: GameStrings = None

    def _init_fields(self) -> None:
        self.PROCESS_TICK: str = "processTick"
        self.ON_GAME_INITIALIZED: str = "onGameInitialized"
        self.UPDATESURFACE: str = "updateSurface"
        self.ON_SET_DISPLAYABLE: str = "onSetDisplayable"
        self.UNPAUSE: str = "unPause"
        self.TOGGLE_MENU: str = "toggleMenu"
        self.SET_GAME_OVER: str = "setGameOver"
        self.GAME_STATE: str = "Game State: "
        self.SET_GAME_STATE: str = "setGameState"
        self.STOP_GAME_CANVAS_RUNNABLE_INTERFACE: str = "stopGameCanvasRunnableInterface"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GameStrings:
        return GameStrings.instance


GameStrings.instance = GameStrings()

