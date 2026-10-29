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
# package org.allbinary.animation.vector

from __future__ import annotations

from org.allbinary.animation.Animation import Animation
from org.allbinary.graphics.color.ColorCompositeInterface import ColorCompositeInterface
from org.allbinary.layer.PositionInterface import PositionInterface


class LineAnimation(Animation, ColorCompositeInterface, PositionInterface):

    def _init_fields(self) -> None:
        self.newLine: list[list[int]] = [[0] * (2) for _ in range(2)]
        self.tempLine: list[list[int]] = NullUtil.getInstance().NULL_INT_ARRAY_ARRAY
        self.line: list[list[int]] = [[0] * (2) for _ in range(2)]
    

    def __init__(self, basicColor: BasicColor) -> None:
        super().__init__()
        self._init_fields()
        self.setBasicColorP(basicColor)
    

    def init(self, x: int, y: int) -> None:
        self.newLine[0][0] = x
        self.newLine[0][1] = y
        self.newLine[1][0] = x
        self.newLine[1][1] = y
        self.tempLine = self.line
        self.line = self.newLine
        self.newLine = self.tempLine
    

    def setPosition(self, x: int, y: int, z: int) -> None:
        self.newLine[0][0] = self.line[1][0]
        self.newLine[0][1] = self.line[1][1]
        self.newLine[1][0] = x
        self.newLine[1][1] = y
        self.tempLine = self.line
        self.line = self.newLine
        self.newLine = self.tempLine
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        currentLine: list[list[int]] = self.line
        self.basicSetColorUtil.setBasicColorP3(graphics, self.getBasicColorP(), self.getColor())
        graphics.drawLine(currentLine[0][0], currentLine[0][1], currentLine[1][0], currentLine[1][1])
    

    def nextFrame(self) -> None:
        pass
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.logic.NullUtil import NullUtil


