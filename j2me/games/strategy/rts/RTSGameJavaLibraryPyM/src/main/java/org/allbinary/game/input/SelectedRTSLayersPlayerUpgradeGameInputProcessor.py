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

from org.allbinary.game.input.SelectedRTSLayersPlayerGameInputProcessor import SelectedRTSLayersPlayerGameInputProcessor


class SelectedRTSLayersPlayerUpgradeGameInputProcessor(SelectedRTSLayersPlayerGameInputProcessor):
    

    def __init__(self, selectedRTSLayersPlayerGameInput: SelectedRTSLayersPlayerGameInput) -> None:
        super().__init__(selectedRTSLayersPlayerGameInput)
    

    # throws Exception
    def processEvent(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        self.selectedRTSLayersPlayerGameInput.upgrade()
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


