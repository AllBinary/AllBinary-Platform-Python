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
# package org.allbinary.game.graphics.hud

from __future__ import annotations



class BasicHudFactory:
    instance: BasicHudFactory = None

    def _init_fields(self) -> None:
        self.DIRECTION_EXCEPTION: str = "Only Horizontal Direction is Allowed Currently"
        self.VERTICAL: int = 0
        self.HORIZONTAL: int = 1
        self.BOTTOMLEFT: int = 0
        self.BOTTOMRIGHT: int = 1
        self.TOPLEFT: int = 2
        self.TOPRIGHT: int = 3
        self.BOTTOMCENTER: int = 4
        self.TOPCENTER: int = 5
        self.ABSOLUTE: int = 6
    

    @staticmethod
    def getInstance() -> BasicHudFactory:
        return BasicHudFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()


BasicHudFactory.instance = BasicHudFactory()

