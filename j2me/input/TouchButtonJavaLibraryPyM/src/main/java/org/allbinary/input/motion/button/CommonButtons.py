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



class CommonButtons:
    instance: CommonButtons = None

    def _init_fields(self) -> None:
        self.STANDARD_BUTTON_SIZE: int = None
        self.NORMAL_BUTTON: Rectangle = None
        self.LARGE_BUTTON: Rectangle = None
    

    @staticmethod
    def getInstance() -> CommonButtons:
        return CommonButtons.instance
    

    def __init__(self) -> None:
        self._init_fields()
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        commonButtonSize: int = 128
        while commonButtonSize > 64:
            totalColumns: int = displayInfo.getLastWidth() / commonButtonSize
            totalRows: int = displayInfo.getLastHeight() / commonButtonSize
            max: int = totalColumns
            if totalRows > max:
                max = totalRows
            if max > 9:
                break
            commonButtonSize = commonButtonSize >> 1
        self.STANDARD_BUTTON_SIZE = commonButtonSize
        self.NORMAL_BUTTON = Rectangle(PointFactory.getInstance().ZERO_ZERO, self.STANDARD_BUTTON_SIZE, self.STANDARD_BUTTON_SIZE)
        self.LARGE_BUTTON = Rectangle(PointFactory.getInstance().ZERO_ZERO, self.STANDARD_BUTTON_SIZE << 1, self.STANDARD_BUTTON_SIZE << 1)
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton


CommonButtons.instance = CommonButtons()

