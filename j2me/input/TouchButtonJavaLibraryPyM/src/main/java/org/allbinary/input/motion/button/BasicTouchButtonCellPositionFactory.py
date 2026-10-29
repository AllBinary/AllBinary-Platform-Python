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



class BasicTouchButtonCellPositionFactory:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.TOP_RIGHT: CellPosition = None
        self.TOP_LEFT: CellPosition = None
        self.SECOND_FROM_TOP_LEFT: CellPosition = None
        self.SECOND_FROM_TOP_RIGHT: CellPosition = None
        self.TOP_SECOND_FROM_LEFT: CellPosition = None
        self.TOP_SECOND_FROM_RIGHT: CellPosition = None
        self.BOTTOM_RIGHT: CellPosition = None
        self.BOTTOM_SECOND_FROM_RIGHT: CellPosition = None
        self.SECOND_FROM_BOTTOM_RIGHT: CellPosition = None
        self.THIRD_FROM_BOTTOM_RIGHT: CellPosition = None
        self.FOURTH_FROM_BOTTOM_RIGHT: CellPosition = None
        self.SECOND_FROM_BOTTOM_SECOND_FROM_RIGHT: CellPosition = None
        self.SECOND_FROM_BOTTOM_THIRD_FROM_RIGHT: CellPosition = None
        self.SECOND_FROM_BOTTOM_FOURTH_FROM_RIGHT: CellPosition = None
        self.BOTTOM_THIRD_FROM_RIGHT: CellPosition = None
        self.BOTTOM_FOURTH_FROM_RIGHT: CellPosition = None
        self.BOTTOM_SECOND_FROM_LEFT: CellPosition = None
        self.SECOND_FROM_BOTTOM_LEFT: CellPosition = None
        self.THIRD_FROM_BOTTOM_LEFT: CellPosition = None
        self.BOTTOM_LEFT: CellPosition = None
        self.SECOND_FROM_BOTTOM_SECOND_FROM_LEFT: CellPosition = None
    

    def __init__(self) -> None:
        from org.allbinary.input.motion.button.TouchButtonLocationHelper import TouchButtonLocationHelper
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        touchButtonLocationHelper: TouchButtonLocationHelper = TouchButtonLocationHelper()
        cellPositionFactory: CellPositionFactory = CellPositionFactory.getInstance()
        cellPositionFactory.init(touchButtonLocationHelper.getTotalColumns(), touchButtonLocationHelper.getTotalRows())
        self.TOP_LEFT = cellPositionFactory.getInstanceColRow(0, 0)
        self.TOP_RIGHT = cellPositionFactory.getInstanceColRow(touchButtonLocationHelper.getTotalColumns() - 1, 0)
        self.BOTTOM_LEFT = cellPositionFactory.getInstanceColRow(0, touchButtonLocationHelper.getTotalRows() - 1)
        self.BOTTOM_RIGHT = cellPositionFactory.getInstanceColRow(touchButtonLocationHelper.getTotalColumns() - 1, touchButtonLocationHelper.getTotalRows() - 1)
        self.BOTTOM_SECOND_FROM_RIGHT = cellPositionFactory.getInstanceColRow(touchButtonLocationHelper.getTotalColumns() - 2, touchButtonLocationHelper.getTotalRows() - 1)
        self.SECOND_FROM_BOTTOM_RIGHT = cellPositionFactory.getInstanceColRow(touchButtonLocationHelper.getTotalColumns() - 1, touchButtonLocationHelper.getTotalRows() - 2)
        self.SECOND_FROM_BOTTOM_SECOND_FROM_RIGHT = cellPositionFactory.getInstanceColRow(touchButtonLocationHelper.getTotalColumns() - 2, touchButtonLocationHelper.getTotalRows() - 2)
        self.BOTTOM_SECOND_FROM_LEFT = cellPositionFactory.getInstanceColRow(1, touchButtonLocationHelper.getTotalRows() - 1)
        self.SECOND_FROM_BOTTOM_LEFT = cellPositionFactory.getInstanceColRow(0, touchButtonLocationHelper.getTotalRows() - 2)
        self.SECOND_FROM_BOTTOM_SECOND_FROM_LEFT = cellPositionFactory.getInstanceColRow(1, touchButtonLocationHelper.getTotalRows() - 2)
        if touchButtonLocationHelper.getTotalRows() > 2:
            self.SECOND_FROM_TOP_LEFT = cellPositionFactory.getInstanceColRow(0, 1)
            self.SECOND_FROM_TOP_RIGHT = cellPositionFactory.getInstanceColRow(touchButtonLocationHelper.getTotalColumns() - 1, 1)
        else:
            self.SECOND_FROM_TOP_LEFT = cellPositionFactory.NONE
            self.SECOND_FROM_TOP_RIGHT = cellPositionFactory.NONE
        if touchButtonLocationHelper.getTotalRows() >= 4:
            self.THIRD_FROM_BOTTOM_RIGHT = cellPositionFactory.getInstanceColRow(touchButtonLocationHelper.getTotalColumns() - 1, touchButtonLocationHelper.getTotalRows() - 3)
            self.FOURTH_FROM_BOTTOM_RIGHT = cellPositionFactory.getInstanceColRow(touchButtonLocationHelper.getTotalColumns() - 1, touchButtonLocationHelper.getTotalRows() - 4)
            self.THIRD_FROM_BOTTOM_LEFT = cellPositionFactory.getInstanceColRow(0, touchButtonLocationHelper.getTotalRows() - 3)
        else:
            self.THIRD_FROM_BOTTOM_RIGHT = cellPositionFactory.NONE
            self.FOURTH_FROM_BOTTOM_RIGHT = cellPositionFactory.NONE
            self.THIRD_FROM_BOTTOM_LEFT = cellPositionFactory.NONE
        if touchButtonLocationHelper.getTotalColumns() >= 4:
            self.SECOND_FROM_BOTTOM_THIRD_FROM_RIGHT = cellPositionFactory.getInstanceColRow(touchButtonLocationHelper.getTotalColumns() - 3, touchButtonLocationHelper.getTotalRows() - 2)
            self.SECOND_FROM_BOTTOM_FOURTH_FROM_RIGHT = cellPositionFactory.getInstanceColRow(touchButtonLocationHelper.getTotalColumns() - 4, touchButtonLocationHelper.getTotalRows() - 2)
            self.BOTTOM_THIRD_FROM_RIGHT = cellPositionFactory.getInstanceColRow(touchButtonLocationHelper.getTotalColumns() - 3, touchButtonLocationHelper.getTotalRows() - 1)
            self.BOTTOM_FOURTH_FROM_RIGHT = cellPositionFactory.getInstanceColRow(touchButtonLocationHelper.getTotalColumns() - 4, touchButtonLocationHelper.getTotalRows() - 1)
            self.TOP_SECOND_FROM_LEFT = cellPositionFactory.getInstanceColRow(1, 0)
            self.TOP_SECOND_FROM_RIGHT = cellPositionFactory.getInstanceColRow(touchButtonLocationHelper.getTotalColumns() - 2, 0)
        else:
            self.SECOND_FROM_BOTTOM_THIRD_FROM_RIGHT = cellPositionFactory.NONE
            self.SECOND_FROM_BOTTOM_FOURTH_FROM_RIGHT = cellPositionFactory.NONE
            self.BOTTOM_THIRD_FROM_RIGHT = cellPositionFactory.NONE
            self.BOTTOM_FOURTH_FROM_RIGHT = cellPositionFactory.NONE
            self.TOP_SECOND_FROM_LEFT = cellPositionFactory.NONE
            self.TOP_SECOND_FROM_RIGHT = cellPositionFactory.NONE
from org.allbinary.graphics.CellPosition import CellPosition
from org.allbinary.graphics.CellPositionFactory import CellPositionFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


