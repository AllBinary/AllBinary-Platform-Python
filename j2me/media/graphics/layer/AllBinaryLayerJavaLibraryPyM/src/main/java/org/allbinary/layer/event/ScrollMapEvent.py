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
# package org.allbinary.layer.event

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class ScrollMapEvent(AllBinaryEventObject):

    def _init_fields(self) -> None:
        self.dx: int = 0
        self.dy: int = 0
    

    def __init__(self, anyType: object) -> None:
        super().__init__(anyType)
        self._init_fields()
    

    def setDx(self, dx: int) -> None:
        self.dx = dx
    

    def getDx(self) -> int:
        return self.dx
    

    def setDy(self, dy: int) -> None:
        self.dy = dy
    

    def getDy(self) -> int:
        return self.dy
    

    def setDxDy(self, dx: int, dy: int) -> None:
        self.dx = dx
        self.dy = dy


