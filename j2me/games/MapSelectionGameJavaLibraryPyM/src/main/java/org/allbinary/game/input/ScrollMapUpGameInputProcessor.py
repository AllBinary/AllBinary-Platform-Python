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
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.game.input.ScrollMapGameInputProcessor import ScrollMapGameInputProcessor


class ScrollMapUpGameInputProcessor(ScrollMapGameInputProcessor):
    

    def __init__(self, scrollMapPlayerGameInput: ScrollMapPlayerGameInput) -> None:
        super().__init__(scrollMapPlayerGameInput)
    

    # throws Exception
    def processEvent(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        self.scrollMapPlayerGameInput.up()
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


