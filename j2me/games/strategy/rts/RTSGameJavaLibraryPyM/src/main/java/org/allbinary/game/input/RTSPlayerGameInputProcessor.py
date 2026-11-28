# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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
# package org.allbinary.game.input

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.input.GameInputProcessor import GameInputProcessor


@java_inherited_overloads
class RTSPlayerGameInputProcessor(GameInputProcessor):
    def _java_defaults(self):
        vars(self).setdefault("rtsPlayerGameInput", None)

    def _init_fields(self) -> None:
        if "rtsPlayerGameInput" not in vars(self): self.rtsPlayerGameInput: RTSPlayerGameInput = None
    

    def __init__(self, rtsPlayerGameInput: RTSPlayerGameInput) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.rtsPlayerGameInput = rtsPlayerGameInput


