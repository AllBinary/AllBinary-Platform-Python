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
# package org.allbinary.game.ag.layer.pickup.points

from __future__ import annotations

from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


class PointsLayer(AllBinaryLayer):

    def _init_fields(self) -> None:
        self.points: int = None
    

    def __init__(self, points: int) -> None:
        super().__init__(StringUtil.getInstance().EMPTY_STRING, Rectangle(PointFactory.getInstance().ZERO_ZERO, 0, 0), ViewPosition.getInstanceD())
        self._init_fields()
        self.points = points
    

    def paint(self, graphics: Graphics) -> None:
        pass
    

    def visit(self, scoreableInterface: ScoreableInterface) -> None:
        scoreableInterface.addPoints(self.points)
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.score.ScoreableInterface import ScoreableInterface
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.view.ViewPosition import ViewPosition


