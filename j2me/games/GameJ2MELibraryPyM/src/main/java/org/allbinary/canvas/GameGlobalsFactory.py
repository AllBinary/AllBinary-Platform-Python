# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.canvas

from __future__ import annotations



class GameGlobalsFactory:
    instance: GameGlobalsFactory = None

    def _init_fields(self) -> None:
        self.newCanvas: bool = True
        self.newDisplaybleTime: int = int(-2147483648)
        self.point: GPoint = PointFactory.getInstance().ZERO_ZERO

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GameGlobalsFactory:
        return GameGlobalsFactory.instance
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory


GameGlobalsFactory.instance = GameGlobalsFactory()

