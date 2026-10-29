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

from org.allbinary.game.score.Scoreable import Scoreable


class ScoreableAddOnlyForHud(Scoreable):

    def _init_fields(self) -> None:
        self.scoreHudWidget: ScoreHudWidget = None
    

    def __init__(self, scoreVectorGraphic: ScoreHudWidget) -> None:
        super().__init__(0)
        self._init_fields()
        self.scoreHudWidget = scoreVectorGraphic
        self.getScoreHudWidget().set(0)
    

    def removePoints(self, points: int) -> None:
        pass
    

    def addPoints(self, points: int) -> None:
        super().addPoints(points)
        self.getScoreHudWidget().add(points)
    

    def getScoreHudWidget(self) -> ScoreHudWidget:
        return self.scoreHudWidget


