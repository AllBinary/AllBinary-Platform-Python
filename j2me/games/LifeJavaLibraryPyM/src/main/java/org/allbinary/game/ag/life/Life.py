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
# package org.allbinary.game.ag.life

from __future__ import annotations

from org.allbinary.game.ag.life.LifeInterface import LifeInterface


class Life(LifeInterface):
    NO_LIFE: Life = None

    def _init_fields(self) -> None:
        self.lives: int = None
        self.startLives: int = None
        self.maxlives: int = None
    

    @staticmethod
    def createLife() -> Life:
        try:
            return Life(((int(0) + 32768) % 65536 - 32768), ((int(0) + 32768) % 65536 - 32768))
        except Exception as e:
            raise RuntimeError()
    

    def __init__(self, lives: int, maxlives: int) -> None:
        self._init_fields()
        self.maxlives = maxlives
        if lives > self.maxlives:
            raise Exception("To Many Lives")
        self.lives = lives
        self.startLives = lives
    

    def get(self) -> int:
        return self.lives
    

    def set(self, lives: int) -> None:
        self.lives = lives
    

    def reset(self) -> None:
        self.lives = self.startLives
    

    def add(self, lives: int) -> None:
        if not self.reachedLimit():
            if self.lives + lives <= self.getMaxlives():
                self.lives = ((int((self.lives + lives)) + 32768) % 65536 - 32768)
            else:
                self.lives = self.getMaxlives()
    

    def isAlive(self) -> bool:
        if self.lives <= 0:
            return False
        else:
            return True
    

    def getMaxlives(self) -> int:
        return self.maxlives
    

    def reachedLimit(self) -> bool:
        if self.lives > self.maxlives or self.lives < 0:
            return True
        else:
            return False
    

    def deaths(self, lives: int) -> None:
        if not self.reachedLimit():
            if self.lives - lives >= 0:
                self.lives = ((int((self.lives - lives)) + 32768) % 65536 - 32768)
            else:
                self.lives = 0
    

    def getStartLives(self) -> int:
        return self.startLives
    

    def setStartLives(self, startLives: int) -> None:
        self.startLives = startLives


Life.NO_LIFE = Life.createLife()

