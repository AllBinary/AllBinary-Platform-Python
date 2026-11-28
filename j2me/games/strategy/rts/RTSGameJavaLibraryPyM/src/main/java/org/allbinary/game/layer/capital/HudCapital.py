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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.layer.capital.Capital import Capital


@java_inherited_overloads
class HudCapital(Capital):
    def _java_defaults(self):
        vars(self).setdefault("capitalGraphic", None)

    def _init_fields(self) -> None:
        if "capitalGraphic" not in vars(self): self.capitalGraphic: NumberStringHud = None
    

    def __init__(self, moneyGraphic: NumberStringHud) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.ag.layer.hud.basic.NumberStringHud import NumberStringHud
        super().__init__()
        __class__._init_fields(self)
        self.capitalGraphic = moneyGraphic
    

    def removeMoney(self, points: int) -> None:
        java_super_call(super(), "removeMoney", points)
        self.capitalGraphic.reduce(points)
    

    def getTotalMoney(self) -> int:
        return self.capitalGraphic.get()
    

    def addMoney(self, points: int) -> None:
        java_super_call(super(), "addMoney", points)
        self.capitalGraphic.add(points)
# from org.allbinary.game.ag.layer.hud.basic.NumberStringHud import NumberStringHud


