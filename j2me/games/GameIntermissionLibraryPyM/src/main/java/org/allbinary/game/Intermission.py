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

from org.allbinary.game.IntermissionInterface import IntermissionInterface


class Intermission(IntermissionInterface):

    def _init_fields(self) -> None:
        self.enabled: bool = False
        self.timeElapsedHelper: TimeDelayHelper = TimeDelayHelper(0)
        self.intermissionEnableListener: IntermissionEnableListenerInterface = NullIntermissionEnableListener.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    def setListener(self, enableListener: IntermissionEnableListenerInterface) -> None:
        self.intermissionEnableListener = enableListener
    

    def getTimeDelayHelper(self) -> TimeDelayHelper:
        return self.timeElapsedHelper
    

    def setEnabled(self, enabled: bool) -> None:
        self.enabled = enabled
        if self.isEnabled():
            self.getTimeDelayHelper().setStartTimeTNT()
        self.intermissionEnableListener.notifyIntermission(enabled)
    

    def isEnabled(self) -> bool:
        return self.enabled
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.game.NullIntermissionEnableListener import NullIntermissionEnableListener


