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
# package org.allbinary.game.layer

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer
from org.allbinary.game.layer.RTSPlayerLayerInterface import RTSPlayerLayerInterface


@java_inherited_overloads
class NullRTSLayer(*java_bases(NullPathFindingLayer, RTSPlayerLayerInterface)):
    NULL_RTS_LAYER: NullRTSLayer = None

    def __init__(self) -> None:
        super().__init__()
    

    def getName(self) -> str:
        raise RuntimeError()
    

    # throws Exception
    def processInput(self, layerManager: AllBinaryLayerManager) -> None:
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        raise RuntimeError()
    

    def initInputProcessors(self) -> None:
        raise RuntimeError()
    

    def getGameNotificationHud(self) -> GameNotificationHud:
        from org.allbinary.game.ag.layer.hud.basic.notification.GameNotificationHud import GameNotificationHud
        raise RuntimeError()
    

    def getCurrentScrollSelectionForm(self) -> ScrollSelectionForm:
        from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
        raise RuntimeError()
    

    def setCurrentScrollSelectionForm(self, currentScrollSelectionForm: ScrollSelectionForm) -> None:
        from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
        raise RuntimeError()
    

    def getBuildingScrollSelectionForm(self) -> ScrollSelectionForm:
        from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
        raise RuntimeError()
    

    def getPlayerGameInput(self) -> PlayerGameInput:
        from org.allbinary.game.input.PlayerGameInput import PlayerGameInput
        raise RuntimeError()
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        raise RuntimeError()
    

    # throws Exception
    def onDestroyed(self, destroyedEvent: DestroyedEvent) -> None:
        from org.allbinary.game.combat.destroy.event.DestroyedEvent import DestroyedEvent
        raise RuntimeError()
    

    # throws Exception
    def processTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        raise RuntimeError()
    

    def getCapital(self) -> Capital:
        from org.allbinary.game.layer.capital.Capital import Capital
        raise RuntimeError()
    

    def getRTSFormInput(self) -> RTSFormInput:
        from org.allbinary.game.input.form.NullRTSFormInputFactory import NullRTSFormInputFactory
        from org.allbinary.game.input.form.RTSFormInput import RTSFormInput
        return NullRTSFormInputFactory.getInstance()
    

    def add(self, sound: Sound) -> None:
        from org.allbinary.media.audio.Sound import Sound
        raise RuntimeError()
    

    def getPlayerOwnedRTSLayers(self) -> PlayerOwnedRTSLayers:
        raise RuntimeError()
    

    def implmentsArtificialIntelligenceCompositeInterface(self) -> bool:
        raise RuntimeError()
# from org.allbinary.game.ag.layer.hud.basic.notification.GameNotificationHud import GameNotificationHud
# from org.allbinary.game.combat.destroy.event.DestroyedEvent import DestroyedEvent
# from org.allbinary.game.input.PlayerGameInput import PlayerGameInput
# from org.allbinary.game.input.form.NullRTSFormInputFactory import NullRTSFormInputFactory
# from org.allbinary.game.input.form.RTSFormInput import RTSFormInput
# from org.allbinary.game.layer.capital.Capital import Capital
# from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
# from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.media.audio.Sound import Sound


def _NullRTSLayer_NULL_RTS_LAYER() -> object:
    return NullRTSLayer()

lazy_static(NullRTSLayer, "NULL_RTS_LAYER", _NullRTSLayer_NULL_RTS_LAYER)

