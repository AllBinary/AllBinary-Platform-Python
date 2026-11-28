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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


@java_inherited_overloads
class PointsLayer(AllBinaryLayer):
    def _java_defaults(self):
        vars(self).setdefault("points", 0)

    def _init_fields(self) -> None:
        if "points" not in vars(self): self.points: int = 0
    

    def __init__(self, points: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.PointFactory import PointFactory
        from org.allbinary.graphics.Rectangle import Rectangle
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.view.ViewPosition import ViewPosition
        super().__init__(StringUtil.getInstance().EMPTY_STRING, Rectangle(PointFactory.getInstance().ZERO_ZERO, 0, 0), ViewPosition.getInstanceD())
        __class__._init_fields(self)
        self.points = points
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
    

    def visit(self, scoreableInterface: ScoreableInterface) -> None:
        from org.allbinary.game.score.ScoreableInterface import ScoreableInterface
        scoreableInterface.addPoints(self.points)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.game.score.ScoreableInterface import ScoreableInterface
# from org.allbinary.graphics.PointFactory import PointFactory
# from org.allbinary.graphics.Rectangle import Rectangle
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.view.ViewPosition import ViewPosition


