# Generated Code Do Not Modify
# package org.allbinary.game

from __future__ import annotations



class BasicGameInfoFactory:
    SINGLETON: BasicGameInfoFactory = None

    def _init_fields(self) -> None:
        self.currentReleaseIndex: int = 0
        self.currentDestroyIndex: int = 0
        self.total: int = 0
    

    @staticmethod
    def getInstance() -> BasicGameInfoFactory:
        return BasicGameInfoFactory.SINGLETON
    

    def __init__(self) -> None:
        self._init_fields()
    

    def init(self, total: int) -> None:
        self.currentReleaseIndex = 0
        self.currentDestroyIndex = 0
        self.total = total
    

    def isPeaked(self) -> bool:
        if self.currentDestroyIndex >= self.total:
            return True
        else:
            return False
    

    def howManyLeft(self) -> int:
        return self.total - self.currentDestroyIndex


BasicGameInfoFactory.SINGLETON = BasicGameInfoFactory()

