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
# package org.allbinary.game.layer

from __future__ import annotations

from org.allbinary.game.layer.RTSPlayerLayerInterface import RTSPlayerLayerInterface


# Java interface
class AdvancedRTSPlayerLayerInterface(RTSPlayerLayerInterface):
    

    def getAdvancedPlayerOwnedRTSLayers(self) -> AdvancedPlayerOwnedRTSLayers:
        raise NotImplementedError()
    

    def isLocalPlayer(self) -> bool:
        raise NotImplementedError()
    

    def getGameType(self) -> GameType:
        raise NotImplementedError()
    

    def getDecalBasicColor(self) -> BasicColor:
        raise NotImplementedError()
from org.allbinary.game.GameType import GameType
from org.allbinary.graphics.color.BasicColor import BasicColor


