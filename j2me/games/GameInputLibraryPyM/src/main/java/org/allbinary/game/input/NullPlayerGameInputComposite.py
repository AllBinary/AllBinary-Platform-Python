# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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

from org.allbinary.game.input.PlayerGameInputCompositeInterface import PlayerGameInputCompositeInterface


class NullPlayerGameInputComposite(PlayerGameInputCompositeInterface):
    NULL_PLAYER_GAME_INPUT_COMPOSITE: NullPlayerGameInputComposite = None
    

    def getName(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    # throws Exception
    def processInput(self, layerManager: AllBinaryLayerManager) -> None:
        pass
    

    def initInputProcessors(self) -> None:
        pass
    

    def getPlayerGameInput(self) -> PlayerGameInput:
        from org.allbinary.game.input.NoPlayerGameInput import NoPlayerGameInput
        return NoPlayerGameInput.getInstance()
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.string.StringUtil import StringUtil


NullPlayerGameInputComposite.NULL_PLAYER_GAME_INPUT_COMPOSITE = NullPlayerGameInputComposite()

