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
# package org.allbinary.game.layer.special

from __future__ import annotations

from org.allbinary.game.layer.special.SpecialGameInputInterface import SpecialGameInputInterface


class SpecialGameInput(SpecialGameInputInterface):
    

    # throws Exception
    def up(self) -> None:
        pass
    

    # throws Exception
    def down(self) -> None:
        pass
    

    # throws Exception
    def right(self) -> None:
        pass
    

    # throws Exception
    def left(self) -> None:
        pass
    

    # throws Exception
    def strafeLeft(self) -> None:
        pass
    

    # throws Exception
    def strafeRight(self) -> None:
        pass
    

    # throws Exception
    def fire(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        pass
    

    # throws Exception
    def special1(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        pass
    

    # throws Exception
    def special2(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        pass
    

    # throws Exception
    def special3(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        pass
    

    # throws Exception
    def special4(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        pass
    

    # throws Exception
    def special5(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        pass
    

    def paint(self, graphics: Graphics) -> None:
        pass
    

    def paintThreed(self, graphics: Graphics) -> None:
        pass
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


