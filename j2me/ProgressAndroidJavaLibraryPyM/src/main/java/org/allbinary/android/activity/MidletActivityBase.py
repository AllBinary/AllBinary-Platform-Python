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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from android.app.Activity import Activity
from org.allbinary.android.GenericMotionEventVerifyInterface import GenericMotionEventVerifyInterface
from org.allbinary.game.configuration.event.GameFeatureListenerInterface import GameFeatureListenerInterface
from org.allbinary.game.configuration.event.GameInitializedListenerInterface import GameInitializedListenerInterface
from org.allbinary.android.activity.SimpleProgressActivityInterface import SimpleProgressActivityInterface
from org.allbinary.android.activity.KeyInputViewCompositeInterface import KeyInputViewCompositeInterface


@java_inherited_overloads
class MidletActivityBase(*java_bases(Activity, GameFeatureListenerInterface, GameInitializedListenerInterface, SimpleProgressActivityInterface, KeyInputViewCompositeInterface, GenericMotionEventVerifyInterface)):

    def __init__(self) -> None:
        super().__init__()
    

    def onGameFeatureChange(self, gameFeatureEvent: GameFeatureEvent) -> None:
        from org.allbinary.game.configuration.event.GameFeatureEvent import GameFeatureEvent
        pass
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        pass
    

    def onGameInitialized(self, gameInitializedEvent: GameInitializedEvent) -> None:
        from org.allbinary.game.configuration.event.GameInitializedEvent import GameInitializedEvent
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
        from android.view.View import View
        raise RuntimeError()
    

    def getView(self) -> View:
        from android.view.View import View
        raise RuntimeError()
    

    def setKeyInputView(self, keyInputView: View) -> None:
        from android.view.View import View
        pass
    

    def onGenericMotionEvent(self, event: MotionEvent) -> bool:
        from android.view.MotionEvent import MotionEvent
        raise RuntimeError()
# from android.view.MotionEvent import MotionEvent
# from android.view.View import View
# from org.allbinary.game.configuration.event.GameFeatureEvent import GameFeatureEvent
# from org.allbinary.game.configuration.event.GameInitializedEvent import GameInitializedEvent
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


