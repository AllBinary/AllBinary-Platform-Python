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
# package org.allbinary.graphics.paint

from __future__ import annotations

from org.allbinary.graphics.paint.LocationPaintable import LocationPaintable


class StringLocationPaintable(LocationPaintable):

    def _init_fields(self) -> None:
        self.value: str = None
    

    def __init__(self, value: str) -> None:
        super().__init__()
        self._init_fields()
        self.value = value
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        graphics.drawString(self.value, x, y, 0)
# from javax.microedition.lcdui.Graphics import Graphics


