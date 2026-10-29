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
# package org.allbinary.graphics.color

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class ColorChangeEvent(AllBinaryEventObject):

    def _init_fields(self) -> None:
        self.basicColor: BasicColor = BasicColorFactory.getInstance().WHITE
    

    def __init__(self, anyType: object) -> None:
        super().__init__(anyType)
        self._init_fields()
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        self.basicColor = basicColor
    

    def getBasicColorP(self) -> BasicColor:
        return self.basicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory


