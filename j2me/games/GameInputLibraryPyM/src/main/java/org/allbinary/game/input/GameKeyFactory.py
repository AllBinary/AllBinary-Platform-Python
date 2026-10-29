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

from org.allbinary.logic.NullUtil import NullUtil


class GameKeyFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.NONE: GameKey = GameKey(InputFactory.getInstance().MAX - 1, "None")
        self.UP: GameKey = GameKey(Canvas.UP, CommonPhoneStrings.getInstance().UP)
        self.DOWN: GameKey = GameKey(Canvas.DOWN, CommonPhoneStrings.getInstance().DOWN)
        self.LEFT: GameKey = GameKey(Canvas.LEFT, CommonPhoneStrings.getInstance().LEFT)
        self.RIGHT: GameKey = GameKey(Canvas.RIGHT, CommonPhoneStrings.getInstance().RIGHT)
        self.KEY_POUND: GameKey = GameKey(Canvas.KEY_POUND, "POUND")
        self.KEY_STAR: GameKey = GameKey(Canvas.KEY_STAR, "STAR")
        self.KEY_NUM0: GameKey = GameKey(Canvas.KEY_NUM0, CommonPhoneStrings.getInstance().ZERO)
        self.KEY_NUM1: GameKey = GameKey(Canvas.KEY_NUM1, CommonPhoneStrings.getInstance().ONE)
        self.KEY_NUM2: GameKey = GameKey(Canvas.KEY_NUM2, CommonPhoneStrings.getInstance().TWO)
        self.KEY_NUM3: GameKey = GameKey(Canvas.KEY_NUM3, CommonPhoneStrings.getInstance().THREE)
        self.KEY_NUM4: GameKey = GameKey(Canvas.KEY_NUM4, CommonPhoneStrings.getInstance().FOUR)
        self.KEY_NUM5: GameKey = GameKey(Canvas.KEY_NUM5, CommonPhoneStrings.getInstance().FIVE)
        self.KEY_NUM6: GameKey = GameKey(Canvas.KEY_NUM6, CommonPhoneStrings.getInstance().SIX)
        self.KEY_NUM7: GameKey = GameKey(Canvas.KEY_NUM7, CommonPhoneStrings.getInstance().SEVEN)
        self.KEY_NUM8: GameKey = GameKey(Canvas.KEY_NUM8, CommonPhoneStrings.getInstance().EIGHT)
        self.KEY_NUM9: GameKey = GameKey(Canvas.KEY_NUM9, CommonPhoneStrings.getInstance().NINE)
        self.GAME_A: GameKey = GameKey(Canvas.GAME_A, "Game A")
        self.GAME_B: GameKey = GameKey(Canvas.GAME_B, "Game B")
        self.GAME_C: GameKey = GameKey(Canvas.GAME_C, "Game C")
        self.GAME_D: GameKey = GameKey(Canvas.GAME_D, "Game D")
        self.FIRE: GameKey = GameKey(Canvas.FIRE, CommonPhoneStrings.getInstance().FIRE)
        self.LEVEL_DOWN: GameKey = GameKey(Canvas.KEY_NUM9 + 1, "Cheat Level Up")
        self.LEVEL_UP: GameKey = GameKey(Canvas.KEY_NUM9 + 2, "Cheat Level Down")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GameKeyFactory:
        if GameKeyFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            GameKeyFactory.instance = GameKeyFactory()
        return GameKeyFactory.instance
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
from org.allbinary.game.input.GameKey import GameKey
from org.allbinary.game.input.InputFactory import InputFactory


