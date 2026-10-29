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
# package org.allbinary.input.motion.button

from __future__ import annotations

from org.allbinary.graphics.paint.Paintable import Paintable


class TouchButtonsMappingPaintable(Paintable):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.foregroundColor: int = None
        self.paintableTable: list[list[Paintable]] = [[None] * (0) for _ in range(0)]
        self.touchButtonLocationHelper: TouchButtonLocationHelper = TouchButtonLocationHelper()
    

    def __init__(self, basicColor: BasicColor) -> None:
        super().__init__()
        self._init_fields()
        self.foregroundColor = int(basicColor)
        self.init()
    

    def init(self) -> None:
        try:
            self.paintableTable = self.createPaintableTable()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, "updateRectangle", e)
    

    # throws Exception
    def createPaintableTable(self) -> list[list[Paintable]]:
        from org.allbinary.input.motion.button.CommonButtons import CommonButtons
        from org.allbinary.input.motion.button.TouchButton import TouchButton
        from org.allbinary.input.motion.button.BasicTouchInputFactory import BasicTouchInputFactory
        from org.allbinary.input.motion.button.TouchButtonBlankResource import TouchButtonBlankResource
        totalColumns: int = self.touchButtonLocationHelper.getTotalColumns()
        totalRows: int = self.touchButtonLocationHelper.getTotalRows()
        paintableTable: list[list[Paintable]] = [[None] * (totalRows) for _ in range(totalColumns)]
        cellPositionFactory: CellPositionFactory = CellPositionFactory.getInstance()
        commonButtons: CommonButtons = CommonButtons.getInstance()
        for index in range(totalColumns - 1, 0 - 1, -1):
            for rowIndex in range(totalRows - 1, 0 - 1, -1):
                self.paintableTable[index][rowIndex] = TouchButton.createButton(BasicTouchInputFactory.getInstance().NONE, TouchButtonBlankResource.getInstance(), commonButtons.NORMAL_BUTTON, cellPositionFactory.getInstanceColRow(index, rowIndex), self.touchButtonLocationHelper.getColumnsRemainderHalf(), self.touchButtonLocationHelper.getRowsRemainderHalf())
        return paintableTable
    

    def paint(self, graphics: Graphics) -> None:
        totalColumns: int = self.touchButtonLocationHelper.getTotalColumns()
        totalRows: int = self.touchButtonLocationHelper.getTotalRows()
        for index in range(totalColumns - 1, 0 - 1, -1):
            for rowIndex in range(totalRows - 1, 0 - 1, -1):
                self.paintableTable[index][rowIndex].paint(graphics)
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.CellPositionFactory import CellPositionFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.input.motion.button.TouchButtonLocationHelper import TouchButtonLocationHelper


