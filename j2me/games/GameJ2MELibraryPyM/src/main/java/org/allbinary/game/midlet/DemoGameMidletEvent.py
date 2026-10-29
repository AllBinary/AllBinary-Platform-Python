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
# package org.allbinary.game.midlet

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class DemoGameMidletEvent(AllBinaryEventObject):

    def _init_fields(self) -> None:
        self.demoGameMidletState: DemoGameMidletState = None
    

    def __init__(self, anyType: object, demoGameMidletState: DemoGameMidletState) -> None:
        super().__init__(anyType)
        self._init_fields()
        self.demoGameMidletState = demoGameMidletState
    

    def init(self, anyType: object) -> None:
        self.setSource(anyType)
    

    def setDemoGameMidletState(self, demoGameMidletState: DemoGameMidletState) -> None:
        self.demoGameMidletState = demoGameMidletState
    

    def getDemoGameMidletState(self) -> DemoGameMidletState:
        return self.demoGameMidletState


