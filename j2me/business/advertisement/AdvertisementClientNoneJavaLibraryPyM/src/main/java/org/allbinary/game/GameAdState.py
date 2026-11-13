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
# package org.allbinary.game

from __future__ import annotations

from org.allbinary.business.advertisement.GameAdStateBase import GameAdStateBase
from org.allbinary.input.event.VirtualKeyboardEventListenerInterface import VirtualKeyboardEventListenerInterface


class GameAdState(GameAdStateBase, VirtualKeyboardEventListenerInterface):
    

    def __init__(self, adConfiguration: AdConfiguration) -> None:
        from org.allbinary.business.advertisement.AdConfiguration import AdConfiguration
        from org.allbinary.input.event.VirtualKeyboardEventHandler import VirtualKeyboardEventHandler
        super().__init__(adConfiguration)
        VirtualKeyboardEventHandler.getInstance().addListenerInterface(self)
    

    # throws Exception
    def onVirtualKeyboardEvent(self, virtualKeyboardEvent: VirtualKeyboardEvent) -> None:
        from org.allbinary.input.event.VirtualKeyboardEvent import VirtualKeyboardEvent
        pass
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        super().onEvent(eventObject)
# from org.allbinary.business.advertisement.AdConfiguration import AdConfiguration
# from org.allbinary.input.event.VirtualKeyboardEvent import VirtualKeyboardEvent
# from org.allbinary.input.event.VirtualKeyboardEventHandler import VirtualKeyboardEventHandler
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


