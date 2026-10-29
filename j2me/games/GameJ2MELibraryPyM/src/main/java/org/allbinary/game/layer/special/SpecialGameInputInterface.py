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
# package org.allbinary.game.layer.special

from __future__ import annotations

from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface


# Java interface
class SpecialGameInputInterface(PaintableInterface):
    

    # throws Exception
    def up(self) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def down(self) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def right(self) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def left(self) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def strafeLeft(self) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def strafeRight(self) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def fire(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def special1(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def special2(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def special3(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def special4(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def special5(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        raise NotImplementedError()
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


