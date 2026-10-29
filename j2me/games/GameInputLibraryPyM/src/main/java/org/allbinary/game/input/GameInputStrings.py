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
# package org.allbinary.game.input

from __future__ import annotations



class GameInputStrings:
    instance: GameInputStrings = None

    def _init_fields(self) -> None:
        self.PROCESS_INPUT: str = "processInput"
        self.KEY_PRESSED: str = "keyPressed"
        self.KEY_RELEASED: str = "keyReleased"
        self.KEY_REPEATED: str = "keyRepeated"
        self.ON_PRESS_GAME_KEY: str = "onPressGameKeyEvent"
        self.ON_DOWN_GAME_KEY: str = "onDownGameKeyEvent"
        self.ON_UP_GAME_KEY: str = "onUpGameKeyEvent"
        self.NO_KEY: str = "Key Code Not Mapped For Game: "
        self.ADD_KEY_EVENT: str = "addGameKeyEvent"
        self.REMOVE_KEY_EVENT: str = "removeGameKeyEvent"
        self.STRAFE_LEFT: str = "strafeLeft"
        self.STRAFE_RIGHT: str = "strafeRight"
        self.PROCESS_MOTION_INPUT: str = "processMotionInput"
        self.UDPATE_CURRENT_TOUCH_INPUT_FACTORY: str = "updateCurrentTouchInputFactory"
        self.ENABLE_PLAYER_GAME_INPUTS: str = "Enabling PlayerGameInputs: "
        self.ENABLE_PLAYER_GAME_INPUT: str = "Enabling PlayerGameInput: "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GameInputStrings:
        return GameInputStrings.instance


GameInputStrings.instance = GameInputStrings()

