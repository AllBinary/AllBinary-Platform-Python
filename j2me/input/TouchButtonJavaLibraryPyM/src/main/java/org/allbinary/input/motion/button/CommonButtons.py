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

from java.lang.JavaRuntimeStatic import java_divide
from java.lang.JavaRuntimeStatic import lazy_static


class CommonButtons:
    instance: CommonButtons = None

    def _init_fields(self) -> None:
        if "STANDARD_BUTTON_SIZE" not in vars(self): self.STANDARD_BUTTON_SIZE: int = 0
        if "NORMAL_BUTTON" not in vars(self): self.NORMAL_BUTTON: Rectangle = None
        if "LARGE_BUTTON" not in vars(self): self.LARGE_BUTTON: Rectangle = None
    

    @staticmethod
    def getInstance() -> CommonButtons:
        return CommonButtons.instance
    

    def __init__(self) -> None:
        from org.allbinary.graphics.PointFactory import PointFactory
        from org.allbinary.graphics.Rectangle import Rectangle
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        __class__._init_fields(self)
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        commonButtonSize: int = 128
        while commonButtonSize > 64:
            totalColumns: int = java_divide(displayInfo.getLastWidth(), commonButtonSize)
            
            totalRows: int = java_divide(displayInfo.getLastHeight(), commonButtonSize)
            
            max: int = totalColumns
            if totalRows > max:
                max = totalRows
            if max > 9:
                break
            commonButtonSize = int(commonButtonSize) >> (int(1) & 31)
        self.STANDARD_BUTTON_SIZE = commonButtonSize
        self.NORMAL_BUTTON = Rectangle(PointFactory.getInstance().ZERO_ZERO, self.STANDARD_BUTTON_SIZE, self.STANDARD_BUTTON_SIZE)
        self.LARGE_BUTTON = Rectangle(PointFactory.getInstance().ZERO_ZERO, ((((self.STANDARD_BUTTON_SIZE) << ((1) & 31)) + 0x80000000) % 0x100000000 - 0x80000000), ((((self.STANDARD_BUTTON_SIZE) << ((1) & 31)) + 0x80000000) % 0x100000000 - 0x80000000))
# from org.allbinary.graphics.PointFactory import PointFactory
# from org.allbinary.graphics.Rectangle import Rectangle
# from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton


def _CommonButtons_instance() -> object:
    return CommonButtons()

lazy_static(CommonButtons, "instance", _CommonButtons_instance)

