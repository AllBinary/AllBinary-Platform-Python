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
# package org.allbinary.graphics.form

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.canvas.Processor import Processor


@java_inherited_overloads
class FormPlayerGameInputProcessor(Processor):
    def _java_defaults(self):
        vars(self).setdefault("playerGameInputCompositeInterface", None)

    def _init_fields(self) -> None:
        if "playerGameInputCompositeInterface" not in vars(self): self.playerGameInputCompositeInterface: PlayerGameInputCompositeInterface = None
    

    def __init__(self, playerGameInputCompositeInterface: PlayerGameInputCompositeInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.input.PlayerGameInputCompositeInterface import PlayerGameInputCompositeInterface
        super().__init__()
        __class__._init_fields(self)
        self.playerGameInputCompositeInterface = playerGameInputCompositeInterface
    

    # throws Exception
    def process(self) -> None:
        self.playerGameInputCompositeInterface.getPlayerGameInput().update()
# from org.allbinary.game.input.PlayerGameInputCompositeInterface import PlayerGameInputCompositeInterface


