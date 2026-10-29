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

from org.allbinary.android.input.VirtualKeyboard import VirtualKeyboard
from org.allbinary.input.event.VirtualKeyboardEventListenerInterface import VirtualKeyboardEventListenerInterface


class VirtualKeyboardAPI3(VirtualKeyboard, VirtualKeyboardEventListenerInterface):
    MAX_API: int = 2147483647
    MIN_API: int = 3

    def _init_fields(self) -> None:
        self.virtualKeyboard: bool = False
        self.activity: Activity = None
        self.showVirtualKeyboardRunnable: object = None
        self.hideVirtualKeyboardRunnable: object = None
    

    def __init__(self, activity: Activity) -> None:
        from org.allbinary.android.input.api3.ShowVirtualKeyboardRunnable import ShowVirtualKeyboardRunnable
        from org.allbinary.android.input.api3.HideVirtualKeyboardRunnable import HideVirtualKeyboardRunnable
        super().__init__()
        self._init_fields()
        self.activity = activity
        self.showVirtualKeyboardRunnable = ShowVirtualKeyboardRunnable(self.activity)
        self.hideVirtualKeyboardRunnable = HideVirtualKeyboardRunnable(self.activity)
        virtualKeyboardEventHandler: VirtualKeyboardEventHandler = VirtualKeyboardEventHandler.getInstance()
        virtualKeyboardEventHandler.removeAllListeners()
        virtualKeyboardEventHandler.addListenerInterface(self)
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onVirtualKeyboardEvent(self, virtualKeyboardEvent: VirtualKeyboardEvent) -> None:
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
from android.app.Activity import Activity
from org.allbinary.input.event.VirtualKeyboardEvent import VirtualKeyboardEvent
from org.allbinary.input.event.VirtualKeyboardEventHandler import VirtualKeyboardEventHandler
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings


