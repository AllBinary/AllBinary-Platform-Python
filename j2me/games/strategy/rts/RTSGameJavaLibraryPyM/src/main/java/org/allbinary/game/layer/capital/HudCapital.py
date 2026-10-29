# 
# AllBinary Open License Version 1 
# Copyright (c) 2002 AllBinary 
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
# package org.allbinary.game.layer.capital

from __future__ import annotations

from org.allbinary.game.layer.capital.Capital import Capital


class HudCapital(Capital):

    def _init_fields(self) -> None:
        self.capitalGraphic: NumberStringHud = None
    

    def __init__(self, moneyGraphic: NumberStringHud) -> None:
        super().__init__()
        self._init_fields()
        self.capitalGraphic = moneyGraphic
    

    def removeMoney(self, points: int) -> None:
        super().removeMoney(points)
        self.capitalGraphic.reduce(points)
    

    def getTotalMoney(self) -> int:
        return self.capitalGraphic.get()
    

    def addMoney(self, points: int) -> None:
        super().addMoney(points)
        self.capitalGraphic.add(points)
from org.allbinary.game.ag.layer.hud.basic.NumberStringHud import NumberStringHud


