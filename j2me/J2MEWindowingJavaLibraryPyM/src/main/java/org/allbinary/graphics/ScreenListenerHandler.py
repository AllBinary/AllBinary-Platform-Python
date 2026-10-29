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
# package org.allbinary.graphics

from __future__ import annotations



class ScreenListenerHandler:
    instance: ScreenListenerHandler = None

    def _init_fields(self) -> None:
        self.screenListenerInterface: ScreenListenerInterface = ScreenEmptyListener()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ScreenListenerHandler:
        return ScreenListenerHandler.instance
    

    def setListener(self, screenListenerInterface: ScreenListenerInterface) -> None:
        self.screenListenerInterface = screenListenerInterface
    

    def fireWithState(self, isFullScreen: bool) -> None:
        self.screenListenerInterface.onFullScreen(isFullScreen)
    

    def fire(self) -> None:
        self.screenListenerInterface.onFullScreenDisplay()
from org.allbinary.graphics.ScreenEmptyListener import ScreenEmptyListener


ScreenListenerHandler.instance = ScreenListenerHandler()

