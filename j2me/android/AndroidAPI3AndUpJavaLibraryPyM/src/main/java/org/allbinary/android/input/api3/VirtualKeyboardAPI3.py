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
# package org.allbinary.android.input.api3

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.android.input.VirtualKeyboard import VirtualKeyboard
from org.allbinary.input.event.VirtualKeyboardEventListenerInterface import VirtualKeyboardEventListenerInterface


@java_inherited_overloads
class VirtualKeyboardAPI3(*java_bases(VirtualKeyboard, VirtualKeyboardEventListenerInterface)):
    MAX_API: int = 2147483647
    MIN_API: int = 3
    def _java_defaults(self):
        vars(self).setdefault("virtualKeyboard", False)
        vars(self).setdefault("activity", None)
        vars(self).setdefault("showVirtualKeyboardRunnable", None)
        vars(self).setdefault("hideVirtualKeyboardRunnable", None)

    def _init_fields(self) -> None:
        if "virtualKeyboard" not in vars(self): self.virtualKeyboard: bool = False
        if "activity" not in vars(self): self.activity: Activity = None
        if "showVirtualKeyboardRunnable" not in vars(self): self.showVirtualKeyboardRunnable: object = None
        if "hideVirtualKeyboardRunnable" not in vars(self): self.hideVirtualKeyboardRunnable: object = None
    

    def __init__(self, activity: Activity) -> None:
        __class__._java_defaults(self)
        from org.allbinary.android.input.api3.ShowVirtualKeyboardRunnable import ShowVirtualKeyboardRunnable
        from org.allbinary.android.input.api3.HideVirtualKeyboardRunnable import HideVirtualKeyboardRunnable
        from android.app.Activity import Activity
        from org.allbinary.input.event.VirtualKeyboardEventHandler import VirtualKeyboardEventHandler
        super().__init__()
        __class__._init_fields(self)
        self.activity = activity
        self.showVirtualKeyboardRunnable = ShowVirtualKeyboardRunnable(self.activity)
        self.hideVirtualKeyboardRunnable = HideVirtualKeyboardRunnable(self.activity)
        virtualKeyboardEventHandler: VirtualKeyboardEventHandler = VirtualKeyboardEventHandler.getInstance()
        virtualKeyboardEventHandler.removeAllListeners()
        virtualKeyboardEventHandler.addListenerInterface(self)
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventStrings import EventStrings
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onVirtualKeyboardEvent(self, virtualKeyboardEvent: VirtualKeyboardEvent) -> None:
        from org.allbinary.input.event.VirtualKeyboardEvent import VirtualKeyboardEvent
        isShow: bool = virtualKeyboardEvent.getSource()
        if isShow:
            self.showVirtualKeyboard()
        else:
            self.hideVirtualKeyboard()
    

    def forceHide(self) -> None:
        self.hideVirtualKeyboard()
    

    def hide(self) -> None:
        if self.virtualKeyboard:
            self.forceHide()
    

    def showVirtualKeyboard(self) -> None:
        self.activity.runOnUiThread(self.showVirtualKeyboardRunnable)
        self.virtualKeyboard = True
    

    def hideVirtualKeyboard(self) -> None:
        self.activity.runOnUiThread(self.hideVirtualKeyboardRunnable)
        self.virtualKeyboard = False
# from android.app.Activity import Activity
# from org.allbinary.input.event.VirtualKeyboardEvent import VirtualKeyboardEvent
# from org.allbinary.input.event.VirtualKeyboardEventHandler import VirtualKeyboardEventHandler
# from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.logic.util.event.EventStrings import EventStrings


