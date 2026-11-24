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
# package org.allbinary.android.input.api1

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.android.input.VirtualKeyboard import VirtualKeyboard
from org.allbinary.input.event.VirtualKeyboardEventListenerInterface import VirtualKeyboardEventListenerInterface


class VirtualKeyboardAPI1(*java_bases(VirtualKeyboard, VirtualKeyboardEventListenerInterface)):
    MIN_API: int = 1
    MAX_API: int = 2
    

    def __init__(self, activity: Activity) -> None:
        from android.app.Activity import Activity
        super().__init__()
    

    def onVirtualKeyboardEvent(self, virtualKeyboardEvent: VirtualKeyboardEvent) -> None:
        from org.allbinary.input.event.VirtualKeyboardEvent import VirtualKeyboardEvent
        super().onVirtualKeyboardEvent(virtualKeyboardEvent)
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        super().onEvent(eventObject)
# from android.app.Activity import Activity
# from org.allbinary.input.event.VirtualKeyboardEvent import VirtualKeyboardEvent
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


