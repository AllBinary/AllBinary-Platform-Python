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
# package org.allbinary.game.ag.layer.hud.basic.score

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.score.Scoreable import Scoreable


@java_inherited_overloads
class ScoreableAddOnlyForHud(Scoreable):
    def _java_defaults(self):
        vars(self).setdefault("scoreHudWidget", None)

    def _init_fields(self) -> None:
        if "scoreHudWidget" not in vars(self): self.scoreHudWidget: ScoreHudWidget = None
    

    def __init__(self, scoreVectorGraphic: ScoreHudWidget) -> None:
        __class__._java_defaults(self)
        super().__init__(0)
        __class__._init_fields(self)
        self.scoreHudWidget = scoreVectorGraphic
        self.getScoreHudWidget().set(0)
    

    def removePoints(self, points: int) -> None:
        pass
    

    def addPoints(self, points: int) -> None:
        java_super_call(super(), "addPoints", points)
        self.getScoreHudWidget().add(points)
    

    def getScoreHudWidget(self) -> ScoreHudWidget:
        return self.scoreHudWidget


