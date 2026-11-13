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

from java.lang.JavaRuntimeStatic import lazy_static


class GameInputProcessor:
    instance: GameInputProcessor = None
    

    @staticmethod
    def getInstance() -> GameInputProcessor:
        return GameInputProcessor.instance
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def processEvent(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        pass
    

    # throws Exception
    def processReleasedEvent(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        pass
    

    # throws Exception
    def processAnalog(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent, analogValue: int) -> None:
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        pass
    

    # throws Exception
    def process(self, allbinaryLayerManager: AllBinaryLayerManager, keyAsInteger: int) -> None:
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        pass
    

    # throws Exception
    def processReleased(self, allbinaryLayerManager: AllBinaryLayerManager, keyAsInteger: int) -> None:
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        pass
# from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
# from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


def _GameInputProcessor_instance() -> object:
    return GameInputProcessor()

lazy_static(GameInputProcessor, "instance", _GameInputProcessor_instance)

