# Generated Code Do Not Modify
# package org.allbinary.view

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.game.configuration.event.GameInitializedListenerInterface import GameInitializedListenerInterface
from org.allbinary.game.midlet.DemoGameMidletEventListener import DemoGameMidletEventListener
from org.allbinary.midlet.MidletCompositeInterface import MidletCompositeInterface
from org.allbinary.view.EmulatorViewInterface import EmulatorViewInterface


# Java interface
@java_inherited_overloads
class AllBinaryMidletViewInterface(*java_bases(MidletCompositeInterface, EmulatorViewInterface, DemoGameMidletEventListener, GameInitializedListenerInterface)):
    

    def onResume(self) -> None:
        raise NotImplementedError()
    

    def onPause(self) -> None:
        raise NotImplementedError()
    

    def onDestroy(self) -> None:
        raise NotImplementedError()


