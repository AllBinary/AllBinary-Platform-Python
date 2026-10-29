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

from org.allbinary.game.ag.layer.hud.basic.NumberStringHud import NumberStringHud


class ScoreHudWidget(NumberStringHud):
    

    # throws Exception
    @staticmethod
    def getInstance(maxscore: int, location: int, direction: int) -> ScoreHudWidget:
        return ScoreHudWidget(maxscore, location, direction, 2, BasicColorFactory.getInstance().GREY)
    

    def __init__(self, maxscore: int, location: int, direction: int, bufferZone: int, basicColor: BasicColor) -> None:
        super().__init__("Pts ", maxscore, location, direction, bufferZone, basicColor)
        self.updateMaxHeight = 14
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.updateMaxWidth = font.getSize() * 5
        super().updateMeasurement(graphics)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory


