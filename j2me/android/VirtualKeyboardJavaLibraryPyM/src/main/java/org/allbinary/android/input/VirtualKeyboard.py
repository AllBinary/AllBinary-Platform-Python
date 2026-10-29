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
# package org.allbinary.android.input

from __future__ import annotations



class VirtualKeyboard:
    NULL_VIRTUAL_KEYBOARD: VirtualKeyboard = None
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onVirtualKeyboardEvent(self, virtualKeyboardEvent: VirtualKeyboardEvent) -> None:
        pass
    

    def forceHide(self) -> None:
        pass
    

    def hide(self) -> None:
        pass
from org.allbinary.input.event.VirtualKeyboardEvent import VirtualKeyboardEvent
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings


VirtualKeyboard.NULL_VIRTUAL_KEYBOARD = VirtualKeyboard()

