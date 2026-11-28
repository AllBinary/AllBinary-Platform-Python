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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.canvas.Processor import Processor


@java_inherited_overloads
class GameProcessor(Processor):
    def _java_defaults(self):
        vars(self).setdefault("gameCanvas", None)

    def _init_fields(self) -> None:
        if "gameCanvas" not in vars(self): self.gameCanvas: AllBinaryGameCanvas = None
    

    def __init__(self, gameCanvas: AllBinaryGameCanvas) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.gameCanvas = gameCanvas
    

    # throws Exception
    def process(self) -> None:
        self.gameCanvas.processPlayingGame()


