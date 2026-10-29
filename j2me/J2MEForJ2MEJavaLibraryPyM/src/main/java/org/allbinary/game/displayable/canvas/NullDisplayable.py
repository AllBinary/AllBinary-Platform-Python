# Generated Code Do Not Modify
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

# from javax.microedition.lcdui.Canvas import Canvas


#J2MEForJ2ME
class NullDisplayable(Canvas):
    SINGLETON: NullDisplayable = None

    def _init_fields(self) -> None:
        self.baseGameStatistics: BaseGameStatistics = GameStatisticsFactory.getInstance()
    

    @staticmethod
    def getInstance() -> NullDisplayable:
        return NullDisplayable.SINGLETON
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def paint(self, graphics: Graphics) -> None:
        self.baseGameStatistics.nextRefresh()
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.canvas.BaseGameStatistics import BaseGameStatistics
from org.allbinary.canvas.GameStatisticsFactory import GameStatisticsFactory


NullDisplayable.SINGLETON = NullDisplayable()

