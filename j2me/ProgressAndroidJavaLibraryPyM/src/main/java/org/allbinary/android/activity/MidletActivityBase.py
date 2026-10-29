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
# package org.allbinary.android.activity

from __future__ import annotations

from android.app.Activity import Activity
from org.allbinary.android.GenericMotionEventVerifyInterface import GenericMotionEventVerifyInterface
from org.allbinary.game.configuration.event.GameFeatureListenerInterface import GameFeatureListenerInterface
from org.allbinary.game.configuration.event.GameInitializedListenerInterface import GameInitializedListenerInterface
from org.allbinary.android.activity.SimpleProgressActivityInterface import SimpleProgressActivityInterface
from org.allbinary.android.activity.KeyInputViewCompositeInterface import KeyInputViewCompositeInterface


class MidletActivityBase(Activity, GameFeatureListenerInterface, GameInitializedListenerInterface, SimpleProgressActivityInterface, KeyInputViewCompositeInterface, GenericMotionEventVerifyInterface):

    def __init__(self) -> None:
        super().__init__()
    

    def onGameFeatureChange(self, gameFeatureEvent: GameFeatureEvent) -> None:
        pass
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        pass
    

    def onGameInitialized(self, gameInitializedEvent: GameInitializedEvent) -> None:
        pass
    

    # throws Exception
    def onSetProgress(self, value: int, text: str) -> None:
        pass
    

    # throws Exception
    def onDismissProgress(self, animationSequence: list[int]) -> None:
        pass
    

    # throws Exception
    def onShowProgress(self, indeterminate: bool, animationSequence: list[int]) -> None:
        pass
    

    def getRootView(self) -> View:
        raise RuntimeError()
    

    def getView(self) -> View:
        raise RuntimeError()
    

    def setKeyInputView(self, keyInputView: View) -> None:
        pass
    

    def onGenericMotionEvent(self, event: MotionEvent) -> bool:
        raise RuntimeError()
from android.view.MotionEvent import MotionEvent
from android.view.View import View
from org.allbinary.game.configuration.event.GameFeatureEvent import GameFeatureEvent
from org.allbinary.game.configuration.event.GameInitializedEvent import GameInitializedEvent
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


