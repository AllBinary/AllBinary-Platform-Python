# Generated Code Do Not Modify
# package org.allbinary.view

from __future__ import annotations

from org.allbinary.game.configuration.event.GameInitializedListenerInterface import GameInitializedListenerInterface
from org.allbinary.game.midlet.DemoGameMidletEventListener import DemoGameMidletEventListener
from org.allbinary.midlet.MidletCompositeInterface import MidletCompositeInterface
from org.allbinary.view.EmulatorViewInterface import EmulatorViewInterface


# Java interface
class AllBinaryMidletViewInterface(MidletCompositeInterface, EmulatorViewInterface, DemoGameMidletEventListener, GameInitializedListenerInterface):
    

    def onResume(self) -> None:
        raise NotImplementedError()
    

    def onPause(self) -> None:
        raise NotImplementedError()
    

    def onDestroy(self) -> None:
        raise NotImplementedError()


