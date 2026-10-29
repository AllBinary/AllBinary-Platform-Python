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



class J2MEKeyFactory:
    instance: J2MEKeyFactory = None

    def _init_fields(self) -> None:
        self.gameKeyFactory: GameKeyFactory = GameKeyFactory.getInstance()
    

    @staticmethod
    def getInstance() -> J2MEKeyFactory:
        return J2MEKeyFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def init(self) -> None:
        from org.allbinary.game.input.InputFactory import InputFactory
        gameKeyArray: list[GameKey] = [self.gameKeyFactory.DOWN, self.gameKeyFactory.FIRE, self.gameKeyFactory.GAME_A, self.gameKeyFactory.GAME_B, self.gameKeyFactory.GAME_C, self.gameKeyFactory.GAME_D, self.gameKeyFactory.KEY_NUM0, self.gameKeyFactory.KEY_NUM1, self.gameKeyFactory.KEY_NUM2, self.gameKeyFactory.KEY_NUM3, self.gameKeyFactory.KEY_NUM4, self.gameKeyFactory.KEY_NUM5, self.gameKeyFactory.KEY_NUM6, self.gameKeyFactory.KEY_NUM7, self.gameKeyFactory.KEY_NUM8, self.gameKeyFactory.KEY_NUM9, self.gameKeyFactory.KEY_POUND, self.gameKeyFactory.KEY_STAR, self.gameKeyFactory.LEFT, self.gameKeyFactory.LEVEL_DOWN, self.gameKeyFactory.LEVEL_UP, self.gameKeyFactory.NONE, self.gameKeyFactory.RIGHT, self.gameKeyFactory.UP]
        inputFactory: InputFactory = InputFactory.getInstance()
        index = len(gameKeyArray)
        while (index := index - 1) >= 0:
            inputFactory.add(gameKeyArray[index].getId(), gameKeyArray[index])
    

    def isSubmission(self, input: Input) -> bool:
        if input == self.gameKeyFactory.FIRE:
            return True
        return False
    

    def isDelete(self, input: Input) -> bool:
        if input == self.gameKeyFactory.GAME_D:
            return True
        return False
    

    def isBackSpace(self, input: Input) -> bool:
        return False
    

    def isUp(self, input: Input) -> bool:
        if input == self.gameKeyFactory.UP:
            return True
        return False
    

    def isDown(self, input: Input) -> bool:
        if input == self.gameKeyFactory.DOWN:
            return True
        return False
    

    def isLeft(self, input: Input) -> bool:
        if input == self.gameKeyFactory.LEFT:
            return True
        return False
    

    def isRight(self, input: Input) -> bool:
        if input == self.gameKeyFactory.RIGHT:
            return True
        return False
    

    def isEnter(self, input: Input) -> bool:
        if input == self.gameKeyFactory.FIRE:
            return True
        return False
from org.allbinary.game.input.GameKeyFactory import GameKeyFactory


J2MEKeyFactory.instance = J2MEKeyFactory()

