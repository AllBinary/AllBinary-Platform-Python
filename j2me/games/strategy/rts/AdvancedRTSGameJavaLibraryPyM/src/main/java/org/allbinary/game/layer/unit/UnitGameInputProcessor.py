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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.input.GameInputProcessor import GameInputProcessor


@java_inherited_overloads
class UnitGameInputProcessor(GameInputProcessor):
    def _java_defaults(self):
        vars(self).setdefault("unitLayer", None)

    def _init_fields(self) -> None:
        if "unitLayer" not in vars(self): self.unitLayer: UnitLayer = None
    

    def __init__(self, unitLayer: UnitLayer) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.unitLayer = unitLayer


