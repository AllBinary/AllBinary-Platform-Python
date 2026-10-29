# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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
# package org.allbinary.game.layer.unit

from __future__ import annotations

from org.allbinary.game.input.GameInputProcessor import GameInputProcessor


class UnitGameInputProcessor(GameInputProcessor):

    def _init_fields(self) -> None:
        self.unitLayer: UnitLayer = None
    

    def __init__(self, unitLayer: UnitLayer) -> None:
        super().__init__()
        self._init_fields()
        self.unitLayer = unitLayer


