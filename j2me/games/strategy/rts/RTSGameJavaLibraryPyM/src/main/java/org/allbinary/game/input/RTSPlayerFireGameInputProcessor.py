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

from org.allbinary.game.input.RTSPlayerGameInputProcessor import RTSPlayerGameInputProcessor


class RTSPlayerFireGameInputProcessor(RTSPlayerGameInputProcessor):
    

    def __init__(self, rtsPlayerGameInput: RTSPlayerGameInput) -> None:
        super().__init__(rtsPlayerGameInput)
    

    # throws Exception
    def processEvent(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        self.rtsPlayerGameInput.addForRemoval(gameKeyEvent)
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


