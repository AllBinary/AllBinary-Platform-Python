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



class DemoGameMidletStateFactory:
    STATE: DemoGameMidletStateFactory = None

    def _init_fields(self) -> None:
        self.NONE: DemoGameMidletState = DemoGameMidletState()
        self.START_DEMO: DemoGameMidletState = DemoGameMidletState()
        self.START_GAME: DemoGameMidletState = DemoGameMidletState()
        self.START_INPUT_MAPPING: DemoGameMidletState = DemoGameMidletState()
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> DemoGameMidletStateFactory:
        return DemoGameMidletStateFactory.STATE
from org.allbinary.game.midlet.DemoGameMidletState import DemoGameMidletState


DemoGameMidletStateFactory.STATE = DemoGameMidletStateFactory()

